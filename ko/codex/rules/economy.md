# 규칙: 경제(economy)

## 요약

`economy` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

경제 계열은 게임의 유일한 화폐인 블러드 토큰에 관한 것입니다. 상인은 아이템, 업그레이드, 인챈트를 블러드 토큰으로 판매하며, 모든 시길이 상인에게서 구매할 수 있고, 각 시길은 저마다 다른 방식으로 토큰을 얻습니다 ([M-0320](../rules/economy.md#m-0320)).

토큰 획득: 최종 처치는 25 블러드 토큰을 주며, 처치자 또는 피해자가 blood crown을 가지고 있었다면 50을 줍니다 ([M-0110](../rules/economy.md#m-0110)). 그 외에는 시길마다 고유한 수입이 있습니다. Piety는 회복과 포션 전환으로 얻습니다 ([M-0501](../rules/economy.md#m-0501), [M-0502](../rules/economy.md#m-0502)). Greed는 훔치기와 money bag으로 얻습니다 ([M-0510](../rules/economy.md#m-0510), [M-0514](../rules/economy.md#m-0514)). Ingenuity는 조합, 해킹, 그 밖의 몇 가지 행동으로 얻습니다 ([M-0521](../rules/economy.md#m-0521)). Trolling은 가한 피해와 파괴한 크레이트로 얻습니다 ([M-0531](../rules/economy.md#m-0531)). Death는 약탈한 묘비와 다른 죽음으로 얻습니다 ([M-0610](../rules/economy.md#m-0610)). Endurance는 자신의 보급 상자와 아이템 사용으로 얻습니다 ([M-0622](../rules/economy.md#m-0622), [M-0623](../rules/economy.md#m-0623)). Necromancy는 자신의 좀비와 그들이 흡수한 양으로 얻습니다 ([M-0630](../rules/economy.md#m-0630)). Protection은 면역이 타격을 막을 때 얻습니다 ([M-0642](../rules/economy.md#m-0642)). Healing은 회복과 부활로 얻습니다 ([M-0650](../rules/economy.md#m-0650)).

지출: 지도에는 최대 한 명의 상인이 있으며, 관리자가 배치하거나 세이프 존에 무작위로 나타나고, 무작위 상인은 15분 동안 머무릅니다 ([M-0321](../rules/economy.md#m-0321)). 10 m (33 ft) 이내에서 구매할 수 있으며, 아이템은 빈 인벤토리 칸이 필요합니다 ([M-0322](../rules/economy.md#m-0322)). 기본 가격 목록에는 보급 상자 10 블러드 토큰, Anti poison 12, Dual Wield 50이 포함됩니다 ([M-0324](../rules/economy.md#m-0324)). 상인의 보급 상자는 무작위 아이템 하나를 인벤토리에 바로 넣어 줍니다 ([M-0325](../rules/economy.md#m-0325)). 업그레이드는 단계식입니다. 인벤토리 칸은 40 블러드 토큰에서 시작하며 하나를 살 때마다 10씩 더 비싸지고 ([M-0332](../rules/economy.md#m-0332)), 최대 HP +10에도 같은 구조가 적용됩니다 ([M-0333](../rules/economy.md#m-0333)). Ingenuity는 10%를 더 내며 올림 처리됩니다 ([M-0323](../rules/economy.md#m-0323)).

플레이어가 느끼는 점: 획득과 구매 사이의 꾸준한 경쟁이며, 시길이 획득 방식을 결정합니다. 기재된 바에 따른 가장 강한 점은 처치 보상 같은 큰 일회성 지급입니다 ([M-0110](../rules/economy.md#m-0110)). 가장 약한 점은 많은 수입 규칙이 미해결인 문구에 의존한다는 것입니다.

알 수 없는 것: 추가 요금이 단계식 가격과 어떻게 맞물리는지 ([U-0322](../unknowns.md#u-0322)), 가격 계산이 정확한 연산인지 부동소수점 연산인지 ([U-0006](../unknowns.md#u-0006)), 칸 카운터와 HP 카운터가 공유되는지 ([U-0329](../unknowns.md#u-0329))입니다. 누가 crown을 보유한 것으로 치는지 ([U-0125](../unknowns.md#u-0125))와 "최종" 처치가 무엇인지 ([U-0104](../unknowns.md#u-0104))는 미해결입니다. 첫 상인이 언제 나타나는지 ([U-0319](../unknowns.md#u-0319))와 얼마나 오래 자리를 비우는지 ([U-0320](../unknowns.md#u-0320))도 미해결입니다. 상인의 보급 상자가 무엇을 주는지 ([U-0323](../unknowns.md#u-0323))와 최대 HP를 더 사면 회복도 되는지 ([U-0331](../unknowns.md#u-0331))도 미해결입니다.

이 페이지는 규칙 23개(4 `DOCUMENTED`, 19 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0110"></a>

### M-0110: 최종 처치는 블러드 토큰 25개를 지급하며, 블러드 크라운이 관련되면 50개

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0110](../rules/economy.md#m-0110) `wiki-013`: "A final kill pays 25 blood tokens, or 50 if the killer or victim held the blood crown." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 최종 처치는 블러드 토큰 25개를 지급하며, 처치자 또는 피처치자가 블러드 크라운(blood crown)을 가지고 있었다면 50개를 지급합니다.

**형식 모델:**

- [M-0110](../rules/economy.md#m-0110) 해석 A: `pay(kill) = crown(killer) 또는 crown(victim)이면 50, 아니면 25, 결정타 시점에 처치자에게 지급`
- [M-0110](../rules/economy.md#m-0110) 해석 B: `같은 금액을 부활 창이 끝날 때 지급`
- [M-0110](../rules/economy.md#m-0110) 해석 C: `50 = 기본 25 + 크라운 보너스 25를 당사자들이 나눔`
- [M-0110](../rules/economy.md#m-0110) 정의역: pay의 단위는 블러드 토큰
- [M-0110](../rules/economy.md#m-0110) 매개변수 `base_tokens`: 25
- [M-0110](../rules/economy.md#m-0110) 매개변수 `crown_tokens`: 50

**미해결 질문:**

- [U-0104](../unknowns.md#u-0104) (높음): 'A final kill pays 25 blood tokens, or 50 if the killer or victim held the blood crown': 누가 지급받으며, 무엇이 처치를 'final'로 만들고, 지급은 언제 이루어집니까?
- [U-0125](../unknowns.md#u-0125) (높음): Blood crown: 처치 시점에 누가 이를 'held'했습니까(처치 이전인지, 같은 처치로 이전된 이후인지), 그리고 어떻게 얻고 잃습니까?

메모 ([M-0110](../rules/economy.md#m-0110)): Death 시길 페이지에는 다른 참가자가 죽을 때마다 토큰 1개를 얻는다는 내용도 있습니다. 다른 메커니즘이므로 합치지 않았습니다.

<a id="m-0320"></a>

### M-0320: 상인 개요와 화폐

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0320](../rules/economy.md#m-0320) `wiki-merchant-001`: "The merchant sells items, upgrades and enchantments for blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant))
  - 번역: 상인은 블러드 토큰을 받고 아이템, 업그레이드, 인챈트를 판매합니다.
- [M-0320](../rules/economy.md#m-0320) `wiki-merchant-002`: "Every sigil can buy from it." ([출처](https://iceposeidon.com/safezone/wiki/merchant))
  - 번역: 모든 시길이 상인에게서 구매할 수 있습니다.
- [M-0320](../rules/economy.md#m-0320) `wiki-merchant-009`: "You pay with blood tokens only." ([출처](https://iceposeidon.com/safezone/wiki/merchant#paying))
  - 번역: 블러드 토큰으로만 지불합니다.
- [M-0320](../rules/economy.md#m-0320) `wiki-merchant-010`: "Each sigil earns them in its own way." ([출처](https://iceposeidon.com/safezone/wiki/merchant#paying))
  - 번역: 각 시길은 저마다의 방식으로 블러드 토큰을 얻습니다.

**형식 모델:**

- [M-0320](../rules/economy.md#m-0320) 해석 A: `상인은 아이템, 업그레이드, 인챈트를 판매함. 모든 시길이 구매할 수 있음. 지불은 블러드 토큰으로만 함. 각 시길은 저마다의 방식으로 토큰을 얻음`
- [M-0320](../rules/economy.md#m-0320) 정의역: 블러드 토큰(정수)

메모 ([M-0320](../rules/economy.md#m-0320)): 획득 규칙은 각 시길 페이지에 있습니다.

<a id="m-0321"></a>

### M-0321: 상인 등장과 체류 주기

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0321](../rules/economy.md#m-0321) `wiki-merchant-003`: "There is at most one merchant on the map." ([출처](https://iceposeidon.com/safezone/wiki/merchant#spawning))
  - 번역: 지도에 상인은 최대 한 명만 있습니다.
- [M-0321](../rules/economy.md#m-0321) `wiki-merchant-004`: "Admins place it, or let it appear at random inside the safe zones or inside an area they pick." ([출처](https://iceposeidon.com/safezone/wiki/merchant#spawning))
  - 번역: 관리자가 직접 배치하거나, 세이프 존 안 또는 관리자가 고른 구역 안에 무작위로 나타나게 합니다.
- [M-0321](../rules/economy.md#m-0321) `wiki-merchant-005`: "A random merchant stays for 15min." ([출처](https://iceposeidon.com/safezone/wiki/merchant#spawning))
  - 번역: 무작위 상인은 15min 동안 머뭅니다.
- [M-0321](../rules/economy.md#m-0321) `wiki-merchant-006`: "Then it leaves and comes back at a new random spot after 30min to 1h." ([출처](https://iceposeidon.com/safezone/wiki/merchant#spawning))
  - 번역: 그 뒤 떠났다가 30min에서 1h 후에 새로운 무작위 지점에 돌아옵니다.

**형식 모델:**

- [M-0321](../rules/economy.md#m-0321) 해석 A: `지도에 상인은 최대 한 명. 관리자가 직접 배치하거나 세이프 존 안 또는 관리자가 고른 구역 안에 무작위로 나타나게 함. 무작위 상인은 15 min 동안 머문 뒤 떠났다가, 떠난 시점부터 측정한 [30, 60] min 범위의 지연 후에 새로운 무작위 지점에 돌아옴`
- [M-0321](../rules/economy.md#m-0321) 해석 B: `지연이 떠난 시점이 아니라 도착한 시점부터 측정됨`
- [M-0321](../rules/economy.md#m-0321) 정의역: 분
- [M-0321](../rules/economy.md#m-0321) 매개변수 `merchant_stay_min`: 15
- [M-0321](../rules/economy.md#m-0321) 매개변수 `merchant_return_delay_min`: 30에서 60
- [M-0321](../rules/economy.md#m-0321) 매개변수 `merchant_first_spawn_min`: UNKNOWN, [U-0319](../unknowns.md#u-0319) 참조

**미해결 질문:**

- [U-0319](../unknowns.md#u-0319) (보통): 이벤트 시작 후 첫 무작위 상인은 언제 나타납니까?
- [U-0320](../unknowns.md#u-0320) (높음): 상인 복귀 지연: 'after 30min to 1h'는 떠난 시점부터 측정합니까, 도착한 시점부터 측정합니까? 그 범위 안에서의 분포는 어떻습니까?

메모 ([M-0321](../rules/economy.md#m-0321)): 관리자가 배치한 상인의 체류 시간은 명시되어 있지 않으며, '무작위 상인'만 15 min 동안 머뭅니다.

<a id="m-0322"></a>

### M-0322: 상인 구매 거리와 슬롯 요건

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0322](../rules/economy.md#m-0322) `wiki-merchant-007`: "Buy from within 10m (33ft) of it." ([출처](https://iceposeidon.com/safezone/wiki/merchant#spawning))
  - 번역: 상인으로부터 10m (33ft) 이내에서 구매합니다.
- [M-0322](../rules/economy.md#m-0322) `wiki-merchant-008`: "Items need a free inventory slot." ([출처](https://iceposeidon.com/safezone/wiki/merchant#spawning))
  - 번역: 아이템에는 빈 인벤토리 슬롯이 필요합니다.

**형식 모델:**

- [M-0322](../rules/economy.md#m-0322) 해석 A: `상인으로부터 거리 10 m 이하에서만 구매할 수 있음. 아이템 구매에는 빈 인벤토리 슬롯이 필요함`
- [M-0322](../rules/economy.md#m-0322) 정의역: 미터
- [M-0322](../rules/economy.md#m-0322) 매개변수 `merchant_range_m`: 10

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0321](../unknowns.md#u-0321) (보통): 어떤 상인 구매에 빈 인벤토리 슬롯이 필요합니까('Items need a free inventory slot')?

<a id="m-0323"></a>

### M-0323: Ingenuity 상인 추가 요금

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0323](../rules/economy.md#m-0323) `wiki-merchant-011`: "Ingenuity contestants pay 10% more, rounded up." ([출처](https://iceposeidon.com/safezone/wiki/merchant#paying))
  - 번역: Ingenuity 참가자는 10%를 더 내며, 금액은 올림합니다.

**형식 모델:**

- [M-0323](../rules/economy.md#m-0323) 해석 A: `가격 p는 ceil(11*p/10)이 됨(정확한 산술)`
- [M-0323](../rules/economy.md#m-0323) 해석 B: `가격 p는 binary64에서 ceil(p*1.1)이 됨`
- [M-0323](../rules/economy.md#m-0323) 정의역: 정수 p >= 1

**미해결 질문:**

- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?
- [U-0322](../unknowns.md#u-0322) (높음): Ingenuity의 'pay 10% more, rounded up'은 40 + 10k 업그레이드 사다리에 어떻게 적용됩니까?

메모 ([M-0323](../rules/economy.md#m-0323)): 같은 문장이 Ingenuity 페이지에도 있습니다('Merchant prices are 10% higher, rounded up', 상인 가격이 10% 높으며 올림한다는 뜻). 모순은 없습니다. 해석 A와 B는 기본 가격 50, 90, 100, 110에서 토큰 1개 차이가 납니다([U-0006](../unknowns.md#u-0006)). 추가 요금이 단계별 가격표에 어떻게 적용되는지는 [U-0322](../unknowns.md#u-0322)입니다.

<a id="m-0324"></a>

### M-0324: 상인 기본 가격 목록

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-012`: "Care package: 10 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Care package(보급 상자): 블러드 토큰 10개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-014`: "Anti poison: 12 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Anti poison: 블러드 토큰 12개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-015`: "Vulnerability Dart: 25 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Vulnerability Dart: 블러드 토큰 25개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-020`: "Sleeping Bag: 30 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag: 블러드 토큰 30개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-030`: "Missile: 10 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Missile: 블러드 토큰 10개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-038`: "Dual Wield: 50 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Dual Wield: 블러드 토큰 50개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-042`: "Deep Cut: 20 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Deep Cut: 블러드 토큰 20개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-046`: "Weapon enchantment: 15 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Weapon enchantment: 블러드 토큰 15개.
- [M-0324](../rules/economy.md#m-0324) `wiki-merchant-057`: "Armor enchantment: 30 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Armor enchantment: 블러드 토큰 30개.

**형식 모델:**

- [M-0324](../rules/economy.md#m-0324) 해석 A: `Ingenuity 추가 요금 이전의, 블러드 토큰 단위의 고정 기본 가격`
- [M-0324](../rules/economy.md#m-0324) 정의역: 블러드 토큰
- [M-0324](../rules/economy.md#m-0324) 매개변수 `care_package`: 10
- [M-0324](../rules/economy.md#m-0324) 매개변수 `anti_poison`: 12
- [M-0324](../rules/economy.md#m-0324) 매개변수 `vulnerability_dart`: 25
- [M-0324](../rules/economy.md#m-0324) 매개변수 `sleeping_bag`: 30
- [M-0324](../rules/economy.md#m-0324) 매개변수 `missile`: 10
- [M-0324](../rules/economy.md#m-0324) 매개변수 `dual_wield`: 50
- [M-0324](../rules/economy.md#m-0324) 매개변수 `deep_cut`: 20
- [M-0324](../rules/economy.md#m-0324) 매개변수 `weapon_enchantment`: 15
- [M-0324](../rules/economy.md#m-0324) 매개변수 `armor_enchantment`: 30

메모 ([M-0324](../rules/economy.md#m-0324)): 단계별 가격(슬롯, 최대 HP)은 [M-0332](../rules/economy.md#m-0332)와 [M-0333](../rules/economy.md#m-0333)입니다. Ingenuity 참가자는 더 많이 냅니다. [M-0323](../rules/economy.md#m-0323)을 참조하십시오.

<a id="m-0325"></a>

### M-0325: 상인 Care package(보급 상자) 내용물

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0325](../rules/economy.md#m-0325) `wiki-merchant-013`: "One random item, straight into your inventory." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 무작위 아이템 하나가 인벤토리에 곧바로 들어옵니다.

**형식 모델:**

- [M-0325](../rules/economy.md#m-0325) 해석 A: `무작위 아이템 하나가 인벤토리에 곧바로 들어옴`

**미해결 질문:**

- [U-0323](../unknowns.md#u-0323) (보통): 상인의 보급 상자는 어떤 아이템을 줍니까: 'One random item'의 분포는?
- [U-0321](../unknowns.md#u-0321) (보통): 어떤 상인 구매에 빈 인벤토리 슬롯이 필요합니까('Items need a free inventory slot')?

메모 ([M-0325](../rules/economy.md#m-0325)): Piety: 'Merchant care packages are not changed'(상인 보급 상자는 바뀌지 않는다는 뜻, Piety 페이지). Endurance 자체의 보급 상자에는 포션이나 Drone이 들어 있지 않지만, 상인의 것에 대해서는 그런 언급이 없습니다.

<a id="m-0332"></a>

### M-0332: 인벤토리 슬롯 업그레이드 단계

라벨: `CONDITIONAL`. 시길: all, endurance, ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0332](../rules/economy.md#m-0332) `wiki-merchant-033`: "Inventory slot: starts at 40 blood tokens and costs 10 more for each one you already bought." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Inventory slot: 블러드 토큰 40개에서 시작하며, 이미 구매한 개수마다 10개씩 더 듭니다.
- [M-0332](../rules/economy.md#m-0332) `wiki-merchant-034`: "Buy up to 10 slots, to at most 13 slots, or 20 for Endurance." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 최대 10개의 슬롯을 구매할 수 있어 최대 13슬롯이 되며, Endurance는 20슬롯입니다.
- [M-0332](../rules/economy.md#m-0332) `wiki-merchant-035`: "Ingenuity tops out at 12." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Ingenuity는 12슬롯에서 멈춥니다.

**형식 모델:**

- [M-0332](../rules/economy.md#m-0332) 해석 A: `k번째 구매(k = 0, 1, ...)의 가격은 40 + 10*k 토큰. 구매는 최대 10회. 슬롯 = 기본 + 구매 횟수이므로 최대 13(기본 3), Endurance는 20(기본 10), Ingenuity는 12(기본 2)`
- [M-0332](../rules/economy.md#m-0332) 정의역: k는 정수, 0 <= k <= 9
- [M-0332](../rules/economy.md#m-0332) 매개변수 `slot_ladder_start`: 40
- [M-0332](../rules/economy.md#m-0332) 매개변수 `slot_ladder_step`: 10
- [M-0332](../rules/economy.md#m-0332) 매개변수 `slot_purchase_max`: 10
- [M-0332](../rules/economy.md#m-0332) 매개변수 `slot_cap_default`: 13
- [M-0332](../rules/economy.md#m-0332) 매개변수 `slot_cap_endurance`: 20
- [M-0332](../rules/economy.md#m-0332) 매개변수 `slot_cap_ingenuity`: 12

**미해결 질문:**

- [U-0329](../unknowns.md#u-0329) (높음): Inventory slot과 +10 maximum HP의 'for each one you already bought' 카운터는 별개입니까, 공유됩니까?
- [U-0322](../unknowns.md#u-0322) (높음): Ingenuity의 'pay 10% more, rounded up'은 40 + 10k 업그레이드 사다리에 어떻게 적용됩니까?
- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?

메모 ([M-0332](../rules/economy.md#m-0332)): 시길 페이지와 교차 확인: Ingenuity는 2슬롯으로 시작(2+10=12), Endurance는 10(10+10=20), 나머지는 3(3+10=13)이며 일치하고 모순은 없습니다.

<a id="m-0333"></a>

### M-0333: 최대 HP 업그레이드 단계

라벨: `CONDITIONAL`. 시길: all, piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0333](../rules/economy.md#m-0333) `wiki-merchant-036`: "+10 maximum HP: starts at 40 blood tokens and costs 10 more for each one you already bought." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: +10 maximum HP: 블러드 토큰 40개에서 시작하며, 이미 구매한 개수마다 10개씩 더 듭니다.
- [M-0333](../rules/economy.md#m-0333) `wiki-merchant-037`: "Maximum HP goes up to 200, or 220 for Piety." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 최대 HP는 200까지 올라가며, Piety는 220까지 올라갑니다.

**형식 모델:**

- [M-0333](../rules/economy.md#m-0333) 해석 A: `k번째 구매의 가격은 40 + 10*k 토큰이며 최대 HP를 10 늘림. 최대 HP의 상한은 200, Piety는 220`
- [M-0333](../rules/economy.md#m-0333) 정의역: k는 0 이상의 정수
- [M-0333](../rules/economy.md#m-0333) 매개변수 `hp_ladder_start`: 40
- [M-0333](../rules/economy.md#m-0333) 매개변수 `hp_ladder_step`: 10
- [M-0333](../rules/economy.md#m-0333) 매개변수 `hp_per_purchase`: 10
- [M-0333](../rules/economy.md#m-0333) 매개변수 `hp_cap_default`: 200
- [M-0333](../rules/economy.md#m-0333) 매개변수 `hp_cap_piety`: 220
- [M-0333](../rules/economy.md#m-0333) 매개변수 `hp_purchase_limit`: UNKNOWN, [U-0330](../unknowns.md#u-0330) 참조

**미해결 질문:**

- [U-0329](../unknowns.md#u-0329) (높음): Inventory slot과 +10 maximum HP의 'for each one you already bought' 카운터는 별개입니까, 공유됩니까?
- [U-0330](../unknowns.md#u-0330) (보통): Max HP upgrade: HP 상한(200, Piety는 220) 외에 구매 한도가 있습니까? 시길별로 각 상한에 도달하려면 몇 번을 구매해야 합니까?
- [U-0331](../unknowns.md#u-0331) (보통): '+10 maximum HP'는 현재 HP도 10 올립니까?
- [U-0322](../unknowns.md#u-0322) (높음): Ingenuity의 'pay 10% more, rounded up'은 40 + 10k 업그레이드 사다리에 어떻게 적용됩니까?
- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?

메모 ([M-0333](../rules/economy.md#m-0333)): 기본 최대 HP: Greed 90, Piety 110, 나머지 100 (시길 페이지). 상한이 명시된 유일한 제한입니다.

<a id="m-0334"></a>

### M-0334: Dual Wield

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0334](../rules/economy.md#m-0334) `wiki-merchant-038`: "Dual Wield: 50 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Dual Wield: 블러드 토큰 50개.
- [M-0334](../rules/economy.md#m-0334) `wiki-merchant-039`: "Unlocks a second weapon slot and a second enchanted weapon." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 두 번째 무기 슬롯과 두 번째 인챈트된 무기를 해금합니다.
- [M-0334](../rules/economy.md#m-0334) `wiki-merchant-040`: "Weapon and worn equipment slots do not use inventory space." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 무기 슬롯과 착용 장비 슬롯은 인벤토리 공간을 사용하지 않습니다.

**형식 모델:**

- [M-0334](../rules/economy.md#m-0334) 해석 A: `토큰 50개. 두 번째 무기 슬롯과 두 번째 인챈트된 무기를 해금. 무기 슬롯과 착용 장비 슬롯은 인벤토리 공간을 사용하지 않음`
- [M-0334](../rules/economy.md#m-0334) 매개변수 `dual_wield_cost_tokens`: 50

메모 ([M-0334](../rules/economy.md#m-0334)): 첫 번째 무기 슬롯은 'a second weapon slot'이라는 문구에서 암시됩니다. 기본 가격 50은 binary64 문제([U-0006](../unknowns.md#u-0006), Ingenuity)에 걸리는 가격입니다.

<a id="m-0501"></a>

### M-0501: Piety의 회복으로 얻는 블러드 토큰

라벨: `CONDITIONAL`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0501](../rules/economy.md#m-0501) `wiki-sigils-piety-007`: "Earn one blood token per 5 HP healed from any source except revives, Campfires and healing circles included." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 부활을 제외한 모든 출처에서 5 HP 회복할 때마다 블러드 토큰 하나를 얻습니다. Campfire와 회복 서클도 포함됩니다.

**형식 모델:**

- [M-0501](../rules/economy.md#m-0501) 해석 A: `tokens += floor(H_total / 5), 자격이 되는 누적 HP 기준; 부활을 제외한 모든 회복이 산입되며 Campfire와 회복 서클도 포함됨`
- [M-0501](../rules/economy.md#m-0501) 해석 B: `tokens += floor(h / 5), 이벤트마다 적용하고 나머지는 버림, 같은 제외 목록`
- [M-0501](../rules/economy.md#m-0501) 해석 C: `Campfire, 회복 서클, 부활은 모두 집계에서 제외됨`
- [M-0501](../rules/economy.md#m-0501) 정의역: 회복 이벤트마다 정수 h >= 0; H_total은 누적값
- [M-0501](../rules/economy.md#m-0501) 매개변수 `hp_per_token`: 5
- [M-0501](../rules/economy.md#m-0501) 매개변수 `tokens_per_step`: 1
- [M-0501](../rules/economy.md#m-0501) 매개변수 `hp_basis`: UNKNOWN, [U-0501](../unknowns.md#u-0501) 참조

**상호작용:** [M-0502](../rules/economy.md#m-0502), [M-0505](../rules/healing.md#m-0505)

**미해결 질문:**

- [U-0500](../unknowns.md#u-0500) (높음): Piety 'one blood token per 5 HP healed': 나머지는 회복 사건 사이에 이월됩니까(누적 카운터), 아니면 사건마다 내림됩니까?
- [U-0501](../unknowns.md#u-0501) (높음): Piety 토큰 카운터: 'HP healed'는 포션의 명목상 수치를 뜻합니까, 실제로 회복된 HP를 뜻합니까, 그리고 +15% 보너스가 포함됩니까?
- [U-0502](../unknowns.md#u-0502) (높음): Piety 'from any source except revives, Campfires and healing circles included': Campfire와 healing circle은 집계됩니까(부활만 제외), 아니면 부활과 함께 제외됩니까?

메모 ([M-0501](../rules/economy.md#m-0501)): 명시된 출처: 부활을 제외한 모든 회복. 포션, 붕대, Healing 시길의 회복, Campfire가 후보 출처입니다. 변환된 포션은 결코 회복하지 않습니다. 변환 메커니즘을 참조하십시오. +15% 포션 보너스는 포션이 회복하는 HP를 바꾸므로, 명목값과 보너스가 적용된 값 중 어느 쪽이 산입되는지는 [U-0501](../unknowns.md#u-0501)에 있습니다.

<a id="m-0502"></a>

### M-0502: Piety의 포션을 블러드 토큰으로 변환

라벨: `DOCUMENTED`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0502](../rules/economy.md#m-0502) `wiki-sigils-piety-008`: "Convert small, medium, large or gigantic potions into 1, 2, 3 or 4 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: small, medium, large 또는 gigantic 포션을 각각 블러드 토큰 1, 2, 3 또는 4개로 변환합니다.
- [M-0502](../rules/economy.md#m-0502) `wiki-sigils-piety-009`: "Converted potions do not count as healing." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 변환된 포션은 회복으로 치지 않습니다.

**형식 모델:**

- [M-0502](../rules/economy.md#m-0502) 해석 A: `변환한 포션 하나당 tokens(small)=1, tokens(medium)=2, tokens(large)=3, tokens(gigantic)=4; 변환된 포션은 아무것도 회복하지 않으며 회복 토큰 적립도 발생시키지 않음`
- [M-0502](../rules/economy.md#m-0502) 정의역: 포션 등급 in {small, medium, large, gigantic}; 중첩된 수량 0..6
- [M-0502](../rules/economy.md#m-0502) 매개변수 `small`: 1
- [M-0502](../rules/economy.md#m-0502) 매개변수 `medium`: 2
- [M-0502](../rules/economy.md#m-0502) 매개변수 `large`: 3
- [M-0502](../rules/economy.md#m-0502) 매개변수 `gigantic`: 4

**상호작용:** [M-0501](../rules/economy.md#m-0501), [M-0503](../rules/items.md#m-0503)

메모 ([M-0502](../rules/economy.md#m-0502)): 이 페이지는 변환 행동의 쿨다운이나 장소를 알려 주지 않습니다. 변환된 포션은 회복이 아니므로, 회복으로 얻는 Piety 토큰([M-0501](../rules/economy.md#m-0501))은 변환된 포션에는 적립되지 않습니다. 포션 회복량은 아이템 페이지에 있습니다: Small 5, Medium 10, Large 20, Gigantic 40 HP (다른 계열의 조항이므로 여기에서는 인용하지 않음).

<a id="m-0510"></a>

### M-0510: Greed 훔치기 보상과 쿨다운

라벨: `CONDITIONAL`. 시길: greed.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0510](../rules/economy.md#m-0510) `wiki-sigils-greed-007`: "A successful steal earns five blood tokens, once per victim every 24 hours." ([출처](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
  - 번역: 훔치기에 성공하면 블러드 토큰 5개를 얻으며, 피해자 한 명당 24시간에 한 번만 가능합니다.
- [M-0510](../rules/economy.md#m-0510) `wiki-sigils-greed-014`: "Cooldown 30min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
  - 번역: 쿨다운 30min.

**형식 모델:**

- [M-0510](../rules/economy.md#m-0510) 해석 A: `성공한 훔치기마다 블러드 토큰 5개를 보상으로 받으며, 피해자 한 명당 최대 24 h의 롤링 구간에 한 번이고, 훔치기는 30 min마다 가능함`
- [M-0510](../rules/economy.md#m-0510) 해석 B: `특정 피해자는 도둑에게 24 h당 최대 한 번만 성공적으로 털릴 수 있음`
- [M-0510](../rules/economy.md#m-0510) 해석 C: `쿨다운 30 min은 어떤 사용에서든 시작되거나, 성공한 뒤에만 시작됨`
- [M-0510](../rules/economy.md#m-0510) 정의역: 초 단위 시간: 쿨다운 1800 s, 구간 86400 s
- [M-0510](../rules/economy.md#m-0510) 매개변수 `reward_tokens`: 5
- [M-0510](../rules/economy.md#m-0510) 매개변수 `per_victim_window_s`: 86400
- [M-0510](../rules/economy.md#m-0510) 매개변수 `cooldown_s`: 1800

**상호작용:** [M-0509](../rules/sigil.md#m-0509)

**미해결 질문:**

- [U-0507](../unknowns.md#u-0507) (높음): Greed의 "A successful steal earns five blood tokens, once per victim every 24 hours": 24 h 제한은 토큰 지급만 제한합니까, 아니면 훔치기 자체를 제한합니까?
- [U-0508](../unknowns.md#u-0508) (보통): Greed 타이머: 30 min 쿨다운은 모든 훔치기 시도에서 시작됩니까, 아니면 성공한 훔치기에서만 시작됩니까? 그리고 피해자별 24 h 구간은 마지막 지급 시점을 기준(롤링)으로 합니까, 아니면 일일 시계를 기준으로 합니까?

메모 ([M-0510](../rules/economy.md#m-0510)): 'Cooldown 30min'은 같은 목록에서 Steal 문장 바로 뒤에 있으므로 훔치기 쿨다운으로 인용했습니다. 서로 다른 피해자는 30 min마다 털 수 있습니다.

<a id="m-0514"></a>

### M-0514: Greed 돈주머니 수입

라벨: `CONDITIONAL`. 시길: greed.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0514](../rules/economy.md#m-0514) `wiki-sigils-greed-012`: "Each real chest you claim and each crate you take adds a blood token to your money bag." ([출처](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
  - 번역: 획득하는 진짜 상자마다, 그리고 가져오는 crate마다 돈주머니에 블러드 토큰 하나가 추가됩니다.

**형식 모델:**

- [M-0514](../rules/economy.md#m-0514) 해석 A: `claim(real chest) 또는 take(crate) -> money_bag += 블러드 토큰 1, 돈주머니 = 일반 잔액`
- [M-0514](../rules/economy.md#m-0514) 해석 B: `돈주머니는 명시되지 않은 시점에 지급되는 별도의 저장소임`
- [M-0514](../rules/economy.md#m-0514) 정의역: 진짜 상자 획득 1회당, 그리고 crate를 가져올 때마다
- [M-0514](../rules/economy.md#m-0514) 매개변수 `tokens_per_claim`: 1
- [M-0514](../rules/economy.md#m-0514) 매개변수 `money_bag_semantics`: UNKNOWN, see [U-0512](../unknowns.md#u-0512)

**상호작용:** [M-0510](../rules/economy.md#m-0510)

**미해결 질문:**

- [U-0512](../unknowns.md#u-0512) (높음): Greed의 "adds a blood token to your money bag": money bag은 일반 블러드 토큰 잔액입니까, 아니면 나중에 지급되는 별도의 저장소입니까?
- [U-0015](../unknowns.md#u-0015) (높음): 상자 규칙(종류, 획득 범위, 생성 빈도, 내용물)은 무엇입니까? 상자 페이지는 삭제되었습니다(RE-0004).

메모 ([M-0514](../rules/economy.md#m-0514)): Greed의 다른 수입은 훔치기 보상입니다 ([M-0510](../rules/economy.md#m-0510)). 가짜 상자는 아무것도 주지 않습니다.

<a id="m-0516"></a>

### M-0516: Ingenuity 상인 가격 10 퍼센트 인상, 올림

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0516](../rules/economy.md#m-0516) `wiki-sigils-ingenuity-007`: "Merchant prices are 10% higher, rounded up." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 상인 가격은 10% 높으며, 올림합니다.
- [M-0516](../rules/economy.md#m-0516) `wiki-merchant-011`: "Ingenuity contestants pay 10% more, rounded up." ([출처](https://iceposeidon.com/safezone/wiki/merchant#paying))
  - 번역: Ingenuity 참가자는 10% 더 지불하며, 올림합니다.

**형식 모델:**

- [M-0516](../rules/economy.md#m-0516) 해석 A: `price_I(p) = ceil(11 * p / 10), 정확한 정수`
- [M-0516](../rules/economy.md#m-0516) 해석 B: `IEEE 754 binary64에서 price_I(p) = ceil(p * 1.1): p=50이면 56, p=90이면 100, p=100이면 111, p=110이면 122 (이 기준 가격에서 A보다 토큰 하나 더 많음)`
- [M-0516](../rules/economy.md#m-0516) 정의역: p는 블러드 토큰 단위의 양의 정수 기본 가격, 예: 10, 12, 15, 20, 25, 30, 40, 50 및 단계적으로 오르는 40+10k 업그레이드
- [M-0516](../rules/economy.md#m-0516) 매개변수 `markup`: 10%
- [M-0516](../rules/economy.md#m-0516) 매개변수 `rounding`: 올림

**미해결 질문:**

- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?

메모 ([M-0516](../rules/economy.md#m-0516)): 이 기록은 Ingenuity 쪽 진술이며, 상인 페이지가 같은 문장을 반복합니다 (같은 의미, 불일치 없음). 기본 가격: Care package 10, Anti poison 12, Vulnerability Dart 25, Sleeping Bag 30, Missile 10, Dual Wield 50, Deep Cut 20, 무기 인챈트 15, 방어구 인챈트 30, 슬롯과 HP 업그레이드는 40부터 (상인 페이지). 인상이 업그레이드에도 적용되는지는 'Merchant prices'라는 표현으로 정해집니다.

<a id="m-0521"></a>

### M-0521: Ingenuity 블러드 토큰 수입

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0521](../rules/economy.md#m-0521) `wiki-sigils-ingenuity-013`: "Earn one blood token per craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 조합, 해킹, Black Hole로 파괴한 상자, Campfire가 누구에게든 회복시킨 HP, 처치한 좀비마다 블러드 토큰 하나를 얻습니다.

**형식 모델:**

- [M-0521](../rules/economy.md#m-0521) 해석 A: `조합마다 +1 토큰. 해킹마다 +1. Black Hole로 파괴한 진짜 아이템 상자마다 +1. 참가자의 Campfire가 누구에게든 회복시킨 HP마다 +1. Zombie killer로 처치한 좀비마다 +1`
- [M-0521](../rules/economy.md#m-0521) 해석 B: `Black Hole로 파괴한 상자에는 crate, 보급 상자, 에어드롭, 가짜 상자가 포함됨. 좀비는 수단에 관계없이 처치한 것으로 셈`
- [M-0521](../rules/economy.md#m-0521) 정의역: 이벤트를 발생 건수마다 셈. 상한은 명시되어 있지 않음
- [M-0521](../rules/economy.md#m-0521) 매개변수 `per_craft`: 1
- [M-0521](../rules/economy.md#m-0521) 매개변수 `per_hack`: 1
- [M-0521](../rules/economy.md#m-0521) 매개변수 `per_chest_black_hole`: 1
- [M-0521](../rules/economy.md#m-0521) 매개변수 `per_campfire_hp`: 1
- [M-0521](../rules/economy.md#m-0521) 매개변수 `per_zombie_killed`: 1

**상호작용:** [M-0517](../rules/sigil.md#m-0517), [M-0522](../rules/items.md#m-0522), [M-0525](../rules/healing.md#m-0525), [M-0527](../rules/zombies.md#m-0527), [M-0528](../rules/items.md#m-0528)

**미해결 질문:**

- [U-0519](../unknowns.md#u-0519) (보통): Ingenuity 수입: "craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed"에 무엇이 포함됩니까?

메모 ([M-0521](../rules/economy.md#m-0521)): Campfire 항목은 Piety, Trolling과 달리 5 HP당이 아니라 HP당 지급됩니다.

<a id="m-0531"></a>

### M-0531: Trolling 블러드 토큰 수입

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0531](../rules/economy.md#m-0531) `wiki-sigils-trolling-006`: "Earn one blood token per 5 HP dealt to other players and per crate destroyed, whoever spawned it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 다른 플레이어에게 준 피해 5 HP마다, 그리고 누가 생성했든 파괴한 crate마다 블러드 토큰 하나를 얻습니다.

**형식 모델:**

- [M-0531](../rules/economy.md#m-0531) 해석 A: `tokens += floor(D_total / 5) (참가자 때문에 다른 플레이어가 잃은 누적 HP 기준), 더하기 누가 생성했든 파괴한 crate당 1`
- [M-0531](../rules/economy.md#m-0531) 해석 B: `tokens += 타격당 floor(d / 5), 나머지는 버림`
- [M-0531](../rules/economy.md#m-0531) 해석 C: `D는 방어구, fortress, Kick 감소 이전의 명목 타격을 셈`
- [M-0531](../rules/economy.md#m-0531) 해석 D: `참가자의 함정이 주는 주기적 피해가 셈에 포함되는지는 [U-0529](../unknowns.md#u-0529)에 따름`
- [M-0531](../rules/economy.md#m-0531) 정의역: d는 타격당 정수 HP. crate 개수는 정수
- [M-0531](../rules/economy.md#m-0531) 매개변수 `hp_per_token`: 5
- [M-0531](../rules/economy.md#m-0531) 매개변수 `tokens_per_crate`: 1
- [M-0531](../rules/economy.md#m-0531) 매개변수 `hp_basis`: UNKNOWN, see [U-0528](../unknowns.md#u-0528)
- [M-0531](../rules/economy.md#m-0531) 매개변수 `source_scope`: UNKNOWN, see [U-0529](../unknowns.md#u-0529)

**상호작용:** [M-0528](../rules/items.md#m-0528), [M-0533](../rules/damage.md#m-0533), [M-0536](../rules/damage.md#m-0536)

**미해결 질문:**

- [U-0528](../unknowns.md#u-0528) (높음): Trolling의 "다른 플레이어에게 가한 5 HP당 블러드 토큰 1개": 나머지는 이월됩니까, 그리고 "가한"은 명목상의 타격입니까 실제로 통과한 HP(방어구, fortress, Kick 감소 적용 후)입니까?
- [U-0529](../unknowns.md#u-0529) (높음): Trolling 수입 범위: 어떤 피해가 "다른 플레이어에게 가한 HP"로 인정됩니까(무기, 가짜 상자, 언세이프 서클 틱, fake gravestone의 독, 반사된 타격), 그리고 어떤 크레이트가 "누가 소환했든 파괴된 크레이트"로 인정됩니까?
- [U-0001](../unknowns.md#u-0001) (치명적): 방어자의 Kick 라이브 10% 감소는 결과를 내림하는 것입니까(A), 아니면 제거되는 10%를 내림하는 것입니까(B)?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, robot, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?

메모 ([M-0531](../rules/economy.md#m-0531)): 'other players'에는 Trolling 참가자와 좀비가 제외됩니다. 가짜 상자를 획득하면 5 HP 피해를 주고, Kick 라이브 중인 방어자는 [U-0001](../unknowns.md#u-0001)에 따라 4 또는 5를 받으므로, 해석에 따라 획득 한 번이 토큰 0개 또는 1개를 지급할 수 있습니다.

<a id="m-0610"></a>

### M-0610: Death 블러드 토큰 수입

라벨: `CONDITIONAL`. 시길: death.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0610](../rules/economy.md#m-0610) `wiki-sigils-death-006`: "Earn ten blood tokens per gravestone robbed and one whenever another contestant dies." ([출처](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
  - 번역: 묘비를 약탈할 때마다 블러드 토큰 10개를, 다른 참가자가 죽을 때마다 1개를 얻습니다.

**형식 모델:**

- [M-0610](../rules/economy.md#m-0610) 해석 A: `tokens += 묘비 약탈 1회당 10. tokens += 다른 참가자의 죽음 1회당 1(위치 무관)`
- [M-0610](../rules/economy.md#m-0610) 해석 B: `동일하되, 토큰 1개를 받으려면 50m 이내에서 죽어야 함`
- [M-0610](../rules/economy.md#m-0610) 정의역: 정수 토큰 수
- [M-0610](../rules/economy.md#m-0610) 매개변수 `death_token_range_m`: UNKNOWN, [U-0605](../unknowns.md#u-0605) 참조

**미해결 질문:**

- [U-0605](../unknowns.md#u-0605) (보통): Death 시길 "다른 참가자가 죽을 때마다 블러드 토큰 1개": 거리 제한이 있습니까(회복은 50m 기준), 그리고 부활이나 두 번째 사망도 다시 보상을 줍니까?
- [U-0606](../unknowns.md#u-0606) (높음): Death "약탈": 아이템이나 블러드 토큰을 처음 루팅하는 것이 "묘비 약탈" 행동과 같은 5% 회복과 10 토큰을 줍니까, 그리고 부활을 위해 잠겨 있는 동안 블러드 토큰을 루팅할 수 있습니까?

메모 ([M-0610](../rules/economy.md#m-0610)): 약탈 범위 10m와 회복 범위 50m는 다른 줄에 명시되어 있으며, 토큰 줄에는 범위가 없습니다.

<a id="m-0622"></a>

### M-0622: 자신의 보급 상자를 수령할 때의 Endurance 토큰

라벨: `CONDITIONAL`. 시길: endurance.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0622](../rules/economy.md#m-0622) `wiki-sigils-endurance-006`: "Claiming one of your own care packages, which fall every 2h 30min, earns six blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 2h 30min마다 떨어지는 자신의 보급 상자를 수령하면 블러드 토큰 6개를 얻습니다.

**형식 모델:**

- [M-0622](../rules/economy.md#m-0622) 해석 A: `수령자가 그 상자가 떨어진 대상인 참가자 본인일 때 tokens += 6`
- [M-0622](../rules/economy.md#m-0622) 해석 B: `다른 사람이 먼저 루팅했더라도, 수령자가 소유한 상자를 수령하면 tokens += 6`
- [M-0622](../rules/economy.md#m-0622) 매개변수 `tokens_per_claim`: 6

**상호작용:** [M-0621](../rules/items.md#m-0621)

**미해결 질문:**

- [U-0607](../unknowns.md#u-0607) (높음): Endurance 보급 상자 "2h 30min마다": 첫 투하는 이벤트 시작 2h30 후입니까, 시길 선택 후입니까, 이전 수령 후입니까, 그리고 어떤 상자가 "자신의 것"입니까?

메모 ([M-0622](../rules/economy.md#m-0622)): 누구나 수령할 수 있으므로 경쟁자가 먼저 가져갈 수 있습니다. 그 경우 소유자가 토큰을 받는지는 명시되어 있지 않습니다.

<a id="m-0623"></a>

### M-0623: 아이템 5회 사용마다 Endurance 보너스 토큰

라벨: `CONDITIONAL`. 시길: endurance.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0623](../rules/economy.md#m-0623) `wiki-sigils-endurance-007`: "Earn one more for every five item uses." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 아이템을 5회 사용할 때마다 1개를 더 얻습니다.

**형식 모델:**

- [M-0623](../rules/economy.md#m-0623) 해석 A: `누적 아이템 사용 횟수가 5의 배수에 도달할 때마다 tokens += 1`
- [M-0623](../rules/economy.md#m-0623) 해석 B: `수령 보상 = 6 + floor(마지막 수령 이후 사용 횟수 / 5)`
- [M-0623](../rules/economy.md#m-0623) 해석 C: `수령 보상 = 5회 사용이 이루어지면 6 + 1`
- [M-0623](../rules/economy.md#m-0623) 정의역: 정수 카운터

**미해결 질문:**

- [U-0608](../unknowns.md#u-0608) (보통): Endurance의 "Earn one more for every five item uses": 추가 토큰은 언제 지급됩니까?
- [U-0609](../unknowns.md#u-0609) (보통): Endurance 아이템 사용 보너스: 어떤 행동이 "아이템 사용"입니까(무기 발사, 붕대, Safety bubble, 조합, 상인 업그레이드, 계속 활성 상태인 효과)?

메모 ([M-0623](../rules/economy.md#m-0623)): 아이템 페이지와 비교하십시오. 일부 효과(Safety Bubbles, smoke bombs, bandages, 조합 아이템, 상인 업그레이드)는 '활성 아이템 효과'에서 제외되며, 여기에 그것이 적용되는지는 명시되어 있지 않습니다.

<a id="m-0630"></a>

### M-0630: Necromancy 블러드 토큰 수입

라벨: `CONDITIONAL`. 시길: necromancy.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0630](../rules/economy.md#m-0630) `wiki-sigils-necromancy-008`: "Earn one blood token for each zombie of yours that appears, guards and horde bonuses included, and one per HP your zombies drain." ([출처](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
  - 번역: 가드와 호드 보너스를 포함해 자신의 좀비가 등장할 때마다 블러드 토큰 1개를, 좀비가 빼앗는 HP 1마다 1개를 얻습니다.

**형식 모델:**

- [M-0630](../rules/economy.md#m-0630) 해석 A: `소유한 좀비가 등장할 때마다 tokens += 1(소환, 죽음, 호드 보너스, 가드). 소유한 좀비가 빼앗은 HP 1마다 tokens += 1`
- [M-0630](../rules/economy.md#m-0630) 해석 B: `A와 같으나, 빼앗은 HP는 피해자가 방어구와 상한을 거친 뒤 실제로 잃은 HP`

**미해결 질문:**

- [U-0613](../unknowns.md#u-0613) (높음): Necromancy의 "The HP goes to you": 얻는 HP는 피해자가 실제로 잃은 HP입니까, 소유자의 최대 HP로 제한됩니까, 그리고 막히거나 방어구가 받아낸 흡수(drain)도 HP와 토큰을 줍니까?
- [U-0614](../unknowns.md#u-0614) (보통): 가드 좀비와 호드 보너스 좀비도 Necromancy 소유자에게 HP를 흡수해 주며 "one per HP your zombies drain"에 포함됩니까?

메모 ([M-0630](../rules/economy.md#m-0630)): 호드 보너스는 좀비 5마리를 주므로 토큰도 5개입니다.

<a id="m-0642"></a>

### M-0642: Protection의 면역 차단으로 얻는 블러드 토큰

라벨: `CONDITIONAL`. 시길: protection.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0642](../rules/economy.md#m-0642) `wiki-sigils-protection-010`: "A drone, missile, C4 or landmine hit earns one blood token, and an airstrike or gunship hit earns 1, but only when your own immunity blocks it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: drone, 미사일, C4 또는 landmine 타격은 블러드 토큰 한 개를, 공습 또는 건십 타격은 1개를 얻게 하지만, 당신 자신의 면역이 막았을 때만 해당합니다.
- [M-0642](../rules/economy.md#m-0642) `wiki-sigils-protection-011`: "A nuke hit earns twenty when your damage cut applies." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 핵폭탄(nuke) 타격은 자신의 피해 감소가 적용될 때 스무 개를 얻게 합니다.
- [M-0642](../rules/economy.md#m-0642) `wiki-sigils-protection-012`: "A hit already blocked by something else earns nothing." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 이미 다른 수단으로 막힌 타격은 아무것도 얻지 못합니다.

**형식 모델:**

- [M-0642](../rules/economy.md#m-0642) 해석 A: `막아 낸 {drone, missile, C4, landmine, airstrike, gunship} 타격 1회당 tokens += 1, 50% 감소에 도달한 nuke 타격 1회당 += 20, 다른 차단 수단이 이미 타격을 막았다면 += 0`
- [M-0642](../rules/economy.md#m-0642) 해석 B: `A에 더해 airstrike fire 틱도 지급함`
- [M-0642](../rules/economy.md#m-0642) 매개변수 `tokens_per_block`: 1
- [M-0642](../rules/economy.md#m-0642) 매개변수 `tokens_per_nuke`: 20

**상호작용:** [M-0640](../rules/sigil.md#m-0640), [M-0643](../rules/damage.md#m-0643)

**미해결 질문:**

- [U-0620](../unknowns.md#u-0620) (보통): 막은 타격으로 얻는 Protection 블러드 토큰: 공습의 화염 틱, 자신의 landmine, 나열되지 않은 면역(함정 선물, 독, 보복)도 토큰을 지급합니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, robot, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?

메모 ([M-0642](../rules/economy.md#m-0642)): 독, 함정 선물, Protection 응징은 면역 목록에는 있으나 토큰 목록에는 없습니다. 핵폭탄 보너스는 토큰 20개입니다. 자신이 시길 능력으로 설치한 landmine의 타격도 토큰을 지급하는지는 명시되어 있지 않습니다.

<a id="m-0650"></a>

### M-0650: Healing 블러드 토큰: 회복 1회당 1개, 부활 1회당 20개

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0650](../rules/economy.md#m-0650) `wiki-sigils-healing-006`: "Earn one blood token per heal and twenty per revive." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 회복 1회당 블러드 토큰 한 개, 부활 1회당 스무 개를 얻습니다.

**형식 모델:**

- [M-0650](../rules/economy.md#m-0650) 해석 A: `회복 능력을 1회 사용할 때마다 tokens += 1, 부활을 1회 완료할 때마다 += 20`
- [M-0650](../rules/economy.md#m-0650) 매개변수 `tokens_per_heal`: 1
- [M-0650](../rules/economy.md#m-0650) 매개변수 `tokens_per_revive`: 20

**미해결 질문:**

- [U-0623](../unknowns.md#u-0623) (보통): Healing 능력: 회복자 자신, 이미 HP가 가득 찬 대상, 중독되지 않은 대상을 대상으로 삼을 수 있습니까? 쿨다운과 토큰은 그래도 소모됩니까?

메모 ([M-0650](../rules/economy.md#m-0650)): HP가 가득 찬 대상에게 회복해도 지급되는지는 [U-0623](../unknowns.md#u-0623)입니다.

## 시뮬레이션 검증

아직 이 페이지를 다루는 정리나 시뮬레이션이 없습니다.

## 미해결 질문

[U-0001](../unknowns.md#u-0001), [U-0002](../unknowns.md#u-0002), [U-0006](../unknowns.md#u-0006), [U-0015](../unknowns.md#u-0015), [U-0104](../unknowns.md#u-0104), [U-0125](../unknowns.md#u-0125), [U-0300](../unknowns.md#u-0300), [U-0319](../unknowns.md#u-0319), [U-0320](../unknowns.md#u-0320), [U-0321](../unknowns.md#u-0321), [U-0322](../unknowns.md#u-0322), [U-0323](../unknowns.md#u-0323), [U-0329](../unknowns.md#u-0329), [U-0330](../unknowns.md#u-0330), [U-0331](../unknowns.md#u-0331), [U-0500](../unknowns.md#u-0500), [U-0501](../unknowns.md#u-0501), [U-0502](../unknowns.md#u-0502), [U-0507](../unknowns.md#u-0507), [U-0508](../unknowns.md#u-0508), [U-0512](../unknowns.md#u-0512), [U-0519](../unknowns.md#u-0519), [U-0528](../unknowns.md#u-0528), [U-0529](../unknowns.md#u-0529), [U-0605](../unknowns.md#u-0605), [U-0606](../unknowns.md#u-0606), [U-0607](../unknowns.md#u-0607), [U-0608](../unknowns.md#u-0608), [U-0609](../unknowns.md#u-0609), [U-0613](../unknowns.md#u-0613), [U-0614](../unknowns.md#u-0614), [U-0620](../unknowns.md#u-0620), [U-0623](../unknowns.md#u-0623)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
