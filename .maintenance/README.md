# GitBook maintenance

Run `python3 .maintenance/verify_book.py` from this repository before syncing.
It checks navigation completeness, local links, image integrity and alt text,
hint blocks, excluded commands, and fish/crop tables against the recorded snapshot
(including fish rarity labels, water/time/weather conditions and crop yields).
It does not certify gameplay, external URLs, live permissions or GitBook rendering.

- `sources.json` records the reviewed source paths/hashes, selected live configuration hashes, public catalog data and editorial limits as of 2026-09-22. Source paths are relative to the Eartopia coordination workspace; live paths are relative to the active server's plugins directory.
- `assets.json` records each original Eartopia image, its provenance and hash. Native captures, model renders and panel previews are distinguished in both metadata and player captions. No reference-wiki assets were copied.
- `SUMMARY.md` is the public page allowlist. This maintenance directory and `AGENT_WORKLOG.md` must never be added to that navigation. The worklog must never be staged.

When gameplay changes, review the relevant command implementation, permission
defaults, UI text and active configuration together. Refresh the affected public
instructions and snapshot; do not merely update the recorded hashes. Recheck the
GitBook commit status and rendered desktop/mobile pages after pushing.

This is a documentation repository. Plugin builds, live reloads, server restarts
and Discord deployment notifications are not part of this publication.
