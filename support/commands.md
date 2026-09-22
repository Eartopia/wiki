---
description: 자주 쓰는 명령어를 찾고, 필요한 설명으로 바로 이동해요.
---

# ⌨️ 명령어 모음

**채팅창을 열고 `/`부터 입력**하면 돼요. `<닉네임>`처럼 꺾쇠 안에 적힌 부분은 실제 값으로 바꿔 주세요. 꺾쇠는 입력하지 않아요.

처음에는 모든 명령어를 외울 필요 없어요. **웅크리기 + 손 바꾸기 키**로 [메인 메뉴](../start/main-menu.md)를 열면 자주 쓰는 기능을 찾을 수 있어요. 기본 키는 `Shift + F`예요.

## 이동과 설정

| 명령어 | 하는 일 |
| --- | --- |
| `/spawn` 또는 `/스폰` | [스폰](../systems/spawn.md)으로 돌아가기 |
| `/emainmenu` | [메인 메뉴](../start/main-menu.md) 열기 |
| `/language` | [언어 설정](../start/language.md) 열기 |
| `/language current` | 현재 언어 확인하기 |
| `/language list` | 지원하는 언어 확인하기 |
| `/language set ko_KR` | 한국어로 설정하기 |
| `/language auto` | 마인크래프트 언어를 따라가도록 설정하기 |
| `/resourcepacks update` | 적용을 기다리는 [리소스팩](../start/resource-packs.md) 업데이트 받기 |
| `/panels calibrate` | [패널 커서 위치](panel-cursor-calibration.md) 보정하기 |
| `/panels calibrate cancel` | 진행 중인 보정 닫기 |
| `/panels calibrate reset` | 저장된 보정값 초기화하기 |

## 마을과 국가

땅을 넓히거나 주민을 초대하는 명령어는 **시장이나 해당 권한을 가진 주민**만 사용할 수 있어요. 비용과 역할은 [마을 안내](../systems/towny.md)에서 먼저 확인해 주세요.

| 명령어 | 하는 일 |
| --- | --- |
| `/town` | 내 마을 정보 보기 |
| `/town list` | 마을 목록 보기 |
| `/town <마을이름>` | 해당 마을 정보 보기 |
| `/town spawn` | 내 마을 스폰으로 이동하기 |
| `/town new <마을이름>` | 현재 위치에 마을 만들기 |
| `/town set spawn` | 마을 스폰 위치 정하기 · 권한 필요 |
| `/town claim` | 현재 청크를 마을 영토로 편입하기 · 권한과 비용 필요 |
| `/town unclaim` | 현재 청크의 마을 소유권 해제하기 · 권한 필요 |
| `/towny map` | 주변 청크 소유 상태 보기 |
| `/town reslist` | 마을 주민 보기 |
| `/town add <닉네임>` | 주민 초대하기 · 권한 필요 |
| `/invite accept <마을이름>` | 받은 마을 초대 수락하기 |
| `/town leave` | 마을 떠나기 · 시장은 별도 정리 필요 |
| `/town deposit <금액>` | 개인 지갑에서 마을 금고로 입금하기 |
| `/town withdraw <금액>` | 마을 금고에서 출금하기 · 권한 필요 |
| `/plot forsale <가격>` | 개인 땅으로 판매하기 · 권한 필요 |
| `/plot claim` | 판매 중인 개인 땅 구매하기 |
| `/plot notforsale` | 땅의 판매 설정 해제하기 · 권한 필요 |
| `/nation list` | 국가 목록 보기 |
| `/nation new <국가이름>` | 국가 만들기 · 시장 권한과 비용 필요 |
| `/nation townlist` | 국가에 속한 마을 보기 |

{% hint style="warning" %}
`/town unclaim`은 영토의 소유권을 해제해요. 실행 전에 위치를 확인해 주세요. 마을을 떠나거나 세금이 부족해졌을 때의 영향도 [금고와 세금](../systems/towny/bank.md)에서 읽어 주세요.
{% endhint %}

## 낚시·농사·요리

| 명령어 | 하는 일 |
| --- | --- |
| `/fish` | [낚시 메뉴](../life/fishing.md) 열기 |
| `/fish classic` | 인벤토리 방식으로 낚시 메뉴 열기 |
| `/fish gear` | 낚시 장비 관리하기 |
| `/fish shop` | 낚시 상점 열기 |
| `/fish index` | 물고기 도감 보기 |
| `/fish stats` | 내 낚시 기록 보기 |
| `/fish sell` | [판매 화면](../life/fishing/selling.md)에서 물고기를 골라 팔기 |
| `/fish sell hand` | 손에 든 물고기 즉시 판매하기 |
| `/fish sell all` | 인벤토리의 판매 가능한 물고기 즉시 판매하기 |
| `/cooking index` | [요리 도감](../life/cooking.md) 보기 |
| `/cooking claim` | 받을 수 있는 완성 요리 수령하기 |
| `/eskills` | [스킬 수첩](../systems/skills.md) 열기 |

[농사](../life/farming.md)는 씨앗을 심고 뼛가루를 쓰고 수확하는 행동으로 진행해요.

{% hint style="warning" %}
`/fish sell hand`와 `/fish sell all`은 별도 선택 화면 없이 바로 판매해요. 요리나 수집에 쓸 물고기가 있다면 `/fish sell`에서 판매할 것만 골라 주세요.
{% endhint %}

## 특산물과 교역

| 명령어 | 하는 일 |
| --- | --- |
| `/trade` | [교역 메뉴](../systems/trade.md) 열기 |
| `/trade codex` | 특산물과 생산 지역 보기 |
| `/trade home` | 정착 지역 확인하기 |
| `/trade home confirm` | 안내받은 정착 지역 확정하기 |
| `/trade contracts` | 오늘의 계약 보기 |
| `/trade processing` | 가공 메뉴 열기 |
| `/trade research` | 국가 연구 보기 |
| `/trade deliveries` | 배송 보관함의 물품 받기 |
| `/trade market` | 물물교환 주문판 열기 |
| `/trade market mine` | 내 교환 주문 확인·취소하기 |
| `/trade charter` | 조건을 채운 뒤 개척 허가서 받기 |
| `/trade foundnation <국가이름>` | 창립 지원 조건에 맞는 국가 세우기 |

정착 지역은 확정 후 바로 다시 바꿀 수 없어요. [정착과 계약](../systems/trade/contracts-research.md), [개척자 창립 지원](../systems/trade/founding.md)의 조건부터 읽어 주세요. 교환 주문 등록법은 [물물교환](../systems/trade/market.md)에 있어요.

## 탐사·그림·꾸미기

| 명령어 | 하는 일 |
| --- | --- |
| `/wildlife` | [탐사 수첩](../life/wildlife.md) 열기 |
| `/art` 또는 `/art help` | [그림 도구와 제작법](../life/art.md) 보기 |
| `/art save <제목>` | 작업 중인 그림 저장하기 · 그리기 권한 필요 |
| `/art search <제목>` | 작품 찾기 |
| `/art search --mine <제목>` | 내 작품 찾기 |
| `/art preview <제목>` | 빈손으로 작품 미리 보기 |
| `/cosmetics` | [의상실](../life/cosmetics.md) 열기 |
| `/cosmetics exit` | 의상실에서 나오기 |
| `/skins` | 아이템 스킨 보기 |
| `/particles` | 파티클 꾸미기 보기 |
| `/trails` | 발자국 효과 보기 |

## 사진·악기·마차

| 명령어 | 하는 일 |
| --- | --- |
| `/camera shoot` | [카메라](../life/camera.md)로 촬영하기 |
| `/camera album` | 내 앨범 열기 |
| `/camera close` | 앨범 닫기 |
| `/camera print <사진번호>` | 내 사진을 지도 아이템으로 인화하기 |
| `/camera profile <사진번호>` | 프로필 사진 정하기 |
| `/camera profile clear` | 프로필 사진 해제하기 |
| `/camera tripod place` | 삼각대 설치하기 |
| `/camera tripod shoot` | 내 삼각대로 촬영하기 |
| `/camera tripod remove` | 내 삼각대 회수하기 |
| `/einstruments recordings` | [내 녹음 목록](../life/instruments.md) 열기 |
| `/transport` | [마차](../life/transport.md) 사용법 보기 |
| `/transport status` | 마차 연결 상태 확인하기 |
| `/transport detach` | 마차 분리 준비하기 · 이후 말을 클릭 |
| `/transport cancel` | 마차 분리 취소하기 |

## 친구와 엽서

| 명령어 | 하는 일 |
| --- | --- |
| `/friends` | [친구 목록](../social/friends.md) 열기 |
| `/friends add <닉네임>` | 친구 요청 보내기 |
| `/friends accept <닉네임>` | 친구 요청 수락하기 |
| `/friends deny <닉네임>` | 친구 요청 거절하기 |
| `/friends remove <닉네임>` | 친구 관계 해제하기 |
| `/friends block <닉네임>` | 해당 플레이어의 친구 요청 차단하기 |
| `/friends unblock <닉네임>` | 친구 요청 차단 풀기 |
| `/friends me` | 내 프로필 꾸미기 |
| `/friends profile <닉네임>` | 프로필 보기 |
| `/friends postcards` | [엽서함](../social/postcards.md) 열기 |

명령어가 거절되면 표시된 안내부터 확인해 주세요. 준비물·잔액·마을 역할에 따라 사용할 수 있는 기능이 달라요. 도움이 필요하면 [문제 해결](troubleshooting.md)을 확인해 주세요.
