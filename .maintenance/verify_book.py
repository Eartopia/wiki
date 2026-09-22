#!/usr/bin/env python3
"""Validate the public GitBook and its source-backed asset/catalog snapshot."""

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import sys
from urllib.parse import unquote, urlsplit


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            values = dict(attrs)
            self.images.append((values.get("src", ""), values.get("alt", "")))


def verify(root):
    errors = []
    links = 0
    referenced_images = set()
    summary = (root / "SUMMARY.md").read_text(encoding="utf-8")
    pages = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", summary)
    if len(pages) != len(set(pages)):
        errors.append("SUMMARY.md: duplicate page")
    discovered = {"README.md"}
    for folder in ("info", "start", "systems", "life", "social", "support"):
        discovered.update(str(p.relative_to(root)) for p in (root / folder).rglob("*.md"))
    if set(pages) != discovered:
        errors.append(f"Navigation mismatch: {sorted(set(pages) ^ discovered)}")

    def local_target(page, target, is_image=False):
        nonlocal links
        links += 1
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            if parsed.scheme != "https":
                errors.append(f"{page}: unsupported external URL {target}")
            return
        if parsed.fragment:
            errors.append(f"{page}: fragment link needs explicit anchor validation: {target}")
        candidate = (root / page).parent / unquote(parsed.path)
        candidate = candidate.resolve()
        if not candidate.is_relative_to(root) or not candidate.is_file():
            errors.append(f"{page}: broken or escaping local link {target}")
            return
        relative = str(candidate.relative_to(root))
        if is_image:
            referenced_images.add(relative)
        elif candidate.suffix == ".md" and relative not in pages:
            errors.append(f"{page}: links to an unpublished page {relative}")

    texts = {}
    for page in pages:
        path = (root / page).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            errors.append(f"SUMMARY.md: missing or escaping page {page}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[page] = text
        if not re.match(r"\A---\ndescription: \S[^\n]*\n---\n", text):
            errors.append(f"{page}: missing description front matter")
        if len(re.findall(r"^# .+$", text, re.M)) != 1:
            errors.append(f"{page}: expected exactly one H1")
        if re.search(r"TODO|TBD|작성\s*중|준비\s*중|추후\s*작성", text):
            errors.append(f"{page}: unfinished content marker")
        if re.search(r"/home/ubuntu|127\.0\.0\.1|localhost|AGENT_WORKLOG|PlugMan|sha256|TMP_DISCORD", text, re.I):
            errors.append(f"{page}: operational detail leaked into player copy")
        if re.search(r"`/(?:resourcepacks (?:status|list|gui)|camera admin|fishadmin|wildlifeadmin|eartopiafarming|wars)(?:\s|`)", text):
            errors.append(f"{page}: excluded admin or unverified command")
        hint_depth = 0
        for token in re.findall(r"{%\s*(hint\b[^%]*|endhint)\s*%}", text):
            hint_depth += -1 if token.strip() == "endhint" else 1
            if hint_depth not in (0, 1):
                errors.append(f"{page}: invalid hint nesting")
        if hint_depth:
            errors.append(f"{page}: unclosed hint")
        for match in re.finditer(r"(!?)\[([^\]]*)\]\(([^)]+)\)", text):
            is_image, alt, target = match.groups()
            if is_image and not alt.strip():
                errors.append(f"{page}: image without alt text")
            local_target(page, target, bool(is_image))
        parser = Images()
        parser.feed(text)
        for src, alt in parser.images:
            if not src or not alt.strip():
                errors.append(f"{page}: image missing source or alt text")
            if src:
                local_target(page, src, True)

    manifest = json.loads((root / ".maintenance/assets.json").read_text())
    assets = manifest["assets"]
    paths = [item["asset"] for item in assets]
    if len(paths) != len(set(paths)):
        errors.append("Asset manifest contains duplicates")
    if set(paths) != referenced_images:
        errors.append(f"Image references/manifest mismatch: {sorted(set(paths) ^ referenced_images)}")
    actual_assets = {str(p.relative_to(root)) for p in (root / ".gitbook/assets").rglob("*") if p.is_file()}
    if actual_assets != set(paths):
        errors.append(f"Unlisted/missing asset files: {sorted(actual_assets ^ set(paths))}")
    asset_bytes = 0
    for item in assets:
        path = (root / item["asset"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            errors.append(f"Missing or escaping manifest asset: {item['asset']}")
            continue
        data = path.read_bytes()
        asset_bytes += len(data)
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            errors.append(f"Asset changed from recorded source: {item['asset']}")
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
            errors.append(f"Invalid PNG: {item['asset']}")
        elif not all(struct.unpack(">II", data[16:24])):
            errors.append(f"Empty PNG dimensions: {item['asset']}")

    sources = json.loads((root / ".maintenance/sources.json").read_text())
    catalog = sources["catalog_snapshot"]
    fish_text = texts.get("life/fishing/catalog.md", "")
    fish_ids = re.findall(r'assets/fish/([^/"\s]+)\.png', fish_text)
    expected_fish = {item["id"] for item in catalog["fish"]}
    if set(fish_ids) != expected_fish or len(fish_ids) != len(expected_fish):
        errors.append("Fish catalog entries differ from the recorded live catalog")
    if f"**{len(expected_fish)}항목**" not in fish_text:
        errors.append("Fish total is inconsistent")
    for fish in catalog["fish"]:
        if f"| {fish['name']} |" not in fish_text:
            errors.append(f"Missing localized fish name: {fish['id']}")
    crop_text = texts.get("life/farming/crops.md", "")
    for crop in catalog["crops"]:
        hours, minutes = divmod(crop["growth_seconds"] // 60, 60)
        duration = " ".join(x for x in (f"{hours}시간" if hours else "", f"{minutes}분" if minutes else "") if x)
        if f"| {crop['name']} | {duration} |" not in crop_text:
            errors.append(f"Crop name/growth duration mismatch: {crop['id']}")
        if crop["kind"] == "custom" and f"| {crop['name']} | {duration} | {crop['drop_min']}~{crop['drop_max']}개 |" not in crop_text:
            errors.append(f"Crop yield mismatch: {crop['id']}")
    return {"ok": not errors, "pages": len(pages), "links_checked": links,
            "assets": len(assets), "asset_bytes": asset_bytes,
            "fish_entries": len(expected_fish), "crop_entries": len(catalog["crops"]), "errors": errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    try:
        report = verify(args.root.resolve())
    except (OSError, ValueError, KeyError) as error:
        report = {"ok": False, "errors": [str(error)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report["ok"] else 1)
