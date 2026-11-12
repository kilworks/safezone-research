# Piety(경건) 시길

## 요약

Piety(경건) 시길을 언급하는 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

Piety는 "포션 비축가" 계열이라고 생각하면 됩니다. 모든 참가자는 시길, 곧 일종의 직업을 하나 고르는데, Piety는 체력 포션과 그것을 바꿔 얻을 수 있는 블러드 토큰을 중심으로 만들어져 있습니다. 기본 수치는 기본값보다 조금 좋아서 최대 HP 110과 인벤토리 슬롯 3개이며 ([M-0500](../rules/sigil.md#m-0500)), Upgrade 사다리로 이 최대치를 200 대신 220까지 올릴 수 있습니다 ([M-0333](../rules/economy.md#m-0333)).

핵심 흐름은 단순합니다. 포션은 15% 더 회복시키며 소수점은 내림 처리되고 ([M-0505](../rules/healing.md#m-0505)), 모든 포션이 슬롯 하나를 함께 쓰며 최대 6개까지 쌓입니다 ([M-0506](../rules/items.md#m-0506)). 상자와 보급 상자도 이 방향으로 치우쳐 있습니다. 획득한 아이템 상자마다, 그리고 가져가는 크레이트마다 안에 든 아이템 대신 무작위 체력 포션을 1개 얻습니다 ([M-0503](../rules/items.md#m-0503)). 상인의 보급 상자는 바뀌지 않습니다 ([M-0503](../rules/items.md#m-0503)).

Piety에게는 돈 버는 면도 있습니다. 부활을 제외한 모든 출처에서 HP를 5 회복할 때마다 블러드 토큰 1개를 얻습니다 ([M-0501](../rules/economy.md#m-0501)). 또는 포션을 마시는 대신 토큰으로 바꿀 수 있습니다. 작은, 중간, 큰, 거대한 포션은 각각 토큰 1, 2, 3, 4개이며, 바꾼 포션은 회복으로 계산되지 않습니다 ([M-0502](../rules/economy.md#m-0502)).

특정한 골칫거리 하나로부터도 보호받습니다. Greed 플레이어는 당신에게서 훔칠 수 없습니다 ([M-0507](../rules/sigil.md#m-0507)). 주의할 점은 가짜 상자의 함정은 여전히 당신에게 작동하며, 그 상자에서는 포션을 얻지 못한다는 것입니다 ([M-0504](../rules/items.md#m-0504)).

규칙상 가장 강한 점은 6개 중첩 ([M-0506](../rules/items.md#m-0506)), 절도 면역 ([M-0507](../rules/sigil.md#m-0507)), 그리고 포션과 토큰 중 고를 수 있는 유연성 ([M-0502](../rules/economy.md#m-0502))입니다.

가장 약하거나 가장 불확실한 점은 상자 관련 규칙이 조건부일 뿐이라는 것인데, 상자 규칙 자체가 빠져 있기 때문입니다 ([U-0015](../unknowns.md#u-0015)). 얻는 포션의 크기가 어떻게 정해지는지 ([U-0504](../unknowns.md#u-0504)), 다른 보급 상자도 전환되는지 ([U-0505](../unknowns.md#u-0505)), 이미 중첩이 가득 찼을 때 어떻게 되는지 ([U-0506](../unknowns.md#u-0506))는 미해결입니다.

일부 수치는 아직 확정되지 않은 표현에도 좌우됩니다. 토큰 계산기가 회복 사이에 남은 HP를 이어서 계산하면, 회복마다 따로 내림하는 경우보다 더 많이 얻게 됩니다. 이는 미해결입니다 ([U-0500](../unknowns.md#u-0500)). Campfire와 회복 서클(healing circle)이 토큰에 포함되는지는 미해결입니다 ([U-0502](../unknowns.md#u-0502)). 15% 보너스가 토큰을 계산할 때 반영되는지 ([U-0501](../unknowns.md#u-0501)), 그리고 정확히 무엇이 내림되는지 ([U-0503](../unknowns.md#u-0503))도 미해결입니다. 마지막으로, Ingenuity 방식의 추가 요금을 고려할 때 Piety 플레이어의 Max HP 업그레이드 가격이 얼마인지 불분명하며 ([U-0322](../unknowns.md#u-0322)), 구매가 HP도 10 회복시키는지는 미해결입니다 ([U-0331](../unknowns.md#u-0331)).

이 페이지는 규칙 10개(6 `DOCUMENTED`, 4 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0202"></a>

### M-0202: Piety 체력 포션 6개 중첩

라벨: `DOCUMENTED`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0202](../rules/items.md#m-0202) `wiki-items-003`: "Piety contestants stack up to 6 health potions in one slot." ([출처](https://iceposeidon.com/safezone/wiki/items#inventory))
  - 번역: Piety 참가자는 체력 포션을 한 칸에 최대 6개까지 중첩합니다.

**형식 모델:**

- [M-0202](../rules/items.md#m-0202) 해석 A: `Piety 참가자의 모든 체력 포션이 한 칸을 공유하며, 개수 <= 6`
- [M-0202](../rules/items.md#m-0202) 정의역: 포션 개수 0..6

**상호작용:** [M-0207](../rules/healing.md#m-0207)

메모 ([M-0202](../rules/items.md#m-0202)): Piety 페이지와 같습니다(모든 체력 포션이 인벤토리 한 칸을 공유하며 최대 6개). 다른 참가자의 포션 중첩에 대해서는 아이템 페이지에 언급이 없습니다([U-0200](../unknowns.md#u-0200) 참조).

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

**따름 결과:** [T-0300](../theorems/T-0300.md), [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

**미해결 질문:**

- [U-0329](../unknowns.md#u-0329) (높음): Inventory slot과 +10 maximum HP의 'for each one you already bought' 카운터는 별개입니까, 공유됩니까?
- [U-0330](../unknowns.md#u-0330) (보통): Max HP upgrade: HP 상한(200, Piety는 220) 외에 구매 한도가 있습니까? 시길별로 각 상한에 도달하려면 몇 번을 구매해야 합니까?
- [U-0331](../unknowns.md#u-0331) (보통): '+10 maximum HP'는 현재 HP도 10 올립니까?
- [U-0322](../unknowns.md#u-0322) (높음): Ingenuity의 'pay 10% more, rounded up'은 40 + 10k 업그레이드 사다리에 어떻게 적용됩니까?
- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?

메모 ([M-0333](../rules/economy.md#m-0333)): 기본 최대 HP: Greed 90, Piety 110, 나머지 100 (시길 페이지). 상한이 명시된 유일한 제한입니다.

<a id="m-0500"></a>

### M-0500: Piety의 기본 최대 HP와 인벤토리 슬롯

라벨: `DOCUMENTED`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-002`: "Max HP" ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety))
  - 번역: 최대 HP
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-003`: "110 HP" ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety))
  - 번역: 110 HP
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-004`: "Slots" ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety))
  - 번역: 슬롯
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-005`: "3" ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety))
  - 번역: 3
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-006`: "Your max HP is 10 HP higher." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 최대 HP가 10 HP 더 높습니다.

**형식 모델:**

- [M-0500](../rules/sigil.md#m-0500) 해석 A: `maxHP_piety = 110; slots_piety = 3; maxHP = base + 10, 여기서 base = 100 (Ingenuity와 Trolling 라벨은 100을 제시함)`
- [M-0500](../rules/sigil.md#m-0500) 정의역: 이벤트 시작 시점의 HP와 슬롯 수(정수)
- [M-0500](../rules/sigil.md#m-0500) 매개변수 `max_hp`: 110
- [M-0500](../rules/sigil.md#m-0500) 매개변수 `slots`: 3
- [M-0500](../rules/sigil.md#m-0500) 매개변수 `max_hp_delta_vs_base`: +10

**따름 결과:** [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

**상호작용:** [M-0506](../rules/items.md#m-0506)

메모 ([M-0500](../rules/sigil.md#m-0500)): 능력치 라벨은 쌍으로 읽습니다 (라벨 'Max HP' 다음에 '110 HP'; 라벨 'Slots' 다음에 '3'). 'Your max HP is 10 HP higher'라는 문장은 기준값 100에 대해 110과 일치합니다. 상인 페이지는 Piety의 최대 HP 상한을 220으로 올립니다. 그것은 상인 형식화 담당의 기록입니다. 시작 HP가 최대 HP와 같다는 것은 이 페이지에 명시되어 있지 않습니다.

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

**따름 결과:** [T-0302](../theorems/T-0302.md)

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

<a id="m-0503"></a>

### M-0503: Piety의 상자와 크레이트가 무작위 체력 포션으로 바뀜

라벨: `CONDITIONAL`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0503](../rules/items.md#m-0503) `wiki-sigils-piety-010`: "Every item chest you claim and every crate you take gives you a random health potion instead of the item inside." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 당신이 획득하는 모든 아이템 상자와 당신이 집는 모든 크레이트는 안에 든 아이템 대신 무작위 체력 포션 하나를 줍니다.
- [M-0503](../rules/items.md#m-0503) `wiki-sigils-piety-012`: "Merchant care packages are not changed." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 상인의 보급 상자는 바뀌지 않습니다.

**형식 모델:**

- [M-0503](../rules/items.md#m-0503) 해석 A: `claim(item chest) 또는 take(crate) -> 무작위 등급의 체력 포션 하나가 인벤토리에 추가됨; 안에 든 아이템은 주어지지 않음; 상인의 보급 상자는 그대로; 다른 보급 상자도 그대로`
- [M-0503](../rules/items.md#m-0503) 해석 B: `A와 같지만 상인이 아닌 보급 상자(에어드롭, 시청자, 관리자)도 변환됨`
- [M-0503](../rules/items.md#m-0503) 정의역: 아이템 상자를 획득하는 행동 또는 크레이트를 집는 행동마다
- [M-0503](../rules/items.md#m-0503) 매개변수 `potion_tier_weights`: UNKNOWN, [U-0504](../unknowns.md#u-0504) 참조
- [M-0503](../rules/items.md#m-0503) 매개변수 `scope`: UNKNOWN, [U-0505](../unknowns.md#u-0505) 참조
- [M-0503](../rules/items.md#m-0503) 매개변수 `overflow`: UNKNOWN, [U-0506](../unknowns.md#u-0506) 참조

**상호작용:** [M-0502](../rules/economy.md#m-0502), [M-0504](../rules/items.md#m-0504), [M-0506](../rules/items.md#m-0506)

**미해결 질문:**

- [U-0504](../unknowns.md#u-0504) (높음): Piety 참가자가 상자나 크레이트에서 얻는 "random health potion"의 크기 분포는 어떠합니까?
- [U-0505](../unknowns.md#u-0505) (보통): Piety 상자 변환 범위: "item chests"와 크레이트만 변환됩니까, 아니면 다른 보급 상자(에어드롭, 관리자, 시청자, Endurance)도 포션으로 바뀝니까?
- [U-0506](../unknowns.md#u-0506) (낮음): 포션 중첩이 이미 6개이거나(또는 인벤토리가 포션을 받을 수 없을 때) Piety가 상자나 크레이트를 획득하면 어떻게 됩니까?
- [U-0015](../unknowns.md#u-0015) (높음): 상자 규칙(종류, 획득 범위, 생성 빈도, 내용물)은 무엇입니까? 상자 페이지는 삭제되었습니다(RE-0004).

메모 ([M-0503](../rules/items.md#m-0503)): 상자가 무엇인지에 대한 모든 내용은 삭제된 상자 페이지에서 나온 것입니다. [U-0015](../unknowns.md#u-0015)를 참조하십시오. 가짜 상자는 아이템 상자가 아닙니다. 다음 메커니즘을 참조하십시오. Piety의 아이템 루팅에는 안에 든 아이템이 결코 포함되지 않습니다 (상자에서 무기도 방어구도 나오지 않음). Greed 참가자는 상자에서 자신만의 보너스를 굴립니다 (별도의 시길).

<a id="m-0504"></a>

### M-0504: 가짜 상자는 Piety에게도 함정을 작동시킴

라벨: `DOCUMENTED`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0504](../rules/items.md#m-0504) `wiki-sigils-piety-011`: "A fake chest still springs its trap." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 가짜 상자는 여전히 함정을 작동시킵니다.

**형식 모델:**

- [M-0504](../rules/items.md#m-0504) 해석 A: `Piety 참가자가 claim(fake chest) -> 함정 효과가 다른 참가자와 똑같이 적용됨; 체력 포션은 주어지지 않음`
- [M-0504](../rules/items.md#m-0504) 정의역: Piety 참가자가 가짜 상자를 획득하는 행동

**상호작용:** [M-0503](../rules/items.md#m-0503), [M-0533](../rules/damage.md#m-0533)

메모 ([M-0504](../rules/items.md#m-0504)): 함정 효과 자체는 Trolling 페이지에 있으며 (5 HP 피해와 상자 잠금) [M-0533](../rules/damage.md#m-0533)에서 모델링됩니다. Piety 참가자가 가짜 상자와 진짜 상자를 구별할 수 있는지는 명시되어 있지 않습니다 (Ingenuity만 가짜를 알아봄).

<a id="m-0505"></a>

### M-0505: Piety의 체력 포션 15% 보너스

라벨: `CONDITIONAL`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0505](../rules/healing.md#m-0505) `wiki-sigils-piety-013`: "Health potions heal you 15% more, rounded down." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 체력 포션의 회복량이 15% 더 많으며, 소수점 이하는 내림합니다.

**형식 모델:**

- [M-0505](../rules/healing.md#m-0505) 해석 A: `heal(h) = floor(1.15 * h): 등급 5, 10, 20, 40은 각각 5, 11, 23, 46이 됨`
- [M-0505](../rules/healing.md#m-0505) 해석 B: `heal(h) = h + floor(0.15 * h): 모든 정수 h에서 A와 같은 값`
- [M-0505](../rules/healing.md#m-0505) 해석 C: `heal = floor(1.15 * min(h, missing HP)): 보너스가 실제 회복량에 적용됨`
- [M-0505](../rules/healing.md#m-0505) 정의역: h in {5, 10, 20, 40}; binary64의 1.15*h는 5.75, 11.5, 23.0, 46.0을 주므로 floor는 정확한 값과 같음
- [M-0505](../rules/healing.md#m-0505) 매개변수 `bonus`: 15%

**상호작용:** [M-0501](../rules/economy.md#m-0501), [M-0525](../rules/healing.md#m-0525)

**미해결 질문:**

- [U-0503](../unknowns.md#u-0503) (보통): Piety의 "heal you 15% more, rounded down": 무엇이 내림되며, 최대 HP 상한 적용과 비교해 어느 단계에서 내림됩니까?
- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?

메모 ([M-0505](../rules/healing.md#m-0505)): 'Health potions'만 명시되어 있습니다. Campfire 풀과 Everything potion은 별개의 효과입니다. Ingenuity 페이지는 Piety와 Protection의 포션 변경이 Campfire에는 적용되지 않는다고 적고 있습니다. Protection 시길은 포션에서 50% 덜 회복합니다 (다른 페이지).

<a id="m-0506"></a>

### M-0506: Piety의 체력 포션을 슬롯 하나에 6개까지 중첩

라벨: `DOCUMENTED`. 시길: piety.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0506](../rules/items.md#m-0506) `wiki-sigils-piety-014`: "All your health potions share one inventory slot, up to 6 potions." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: 모든 체력 포션이 인벤토리 슬롯 하나를 공유하며, 최대 6개까지입니다.
- [M-0506](../rules/items.md#m-0506) `wiki-items-003`: "Piety contestants stack up to 6 health potions in one slot." ([출처](https://iceposeidon.com/safezone/wiki/items#inventory))
  - 번역: Piety 참가자는 체력 포션을 슬롯 하나에 최대 6개까지 중첩합니다.

**형식 모델:**

- [M-0506](../rules/items.md#m-0506) 해석 A: `모든 등급의 체력 포션이 인벤토리 슬롯 하나를 차지하며 중첩 상한은 6; 슬롯 용량은 3 ([M-0500](../rules/sigil.md#m-0500))`
- [M-0506](../rules/items.md#m-0506) 정의역: 포션 수량 0..6
- [M-0506](../rules/items.md#m-0506) 매개변수 `stack_cap`: 6
- [M-0506](../rules/items.md#m-0506) 매개변수 `slots_for_potions`: 1

**따름 결과:** [T-0302](../theorems/T-0302.md), [T-0407](../theorems/T-0407.md)

**상호작용:** [M-0500](../rules/sigil.md#m-0500), [M-0503](../rules/items.md#m-0503)

메모 ([M-0506](../rules/items.md#m-0506)): 두 페이지가 일치합니다: 슬롯 하나, 최대 6개. 등급이 섞인 포션이 슬롯을 공유하는지는 'All your health potions'에서 읽어낸 것입니다. 좀비는 10%의 확률로 체력 포션 하나를 부수는데 (좀비 페이지), 이는 Piety에게 가장 중요합니다.

<a id="m-0507"></a>

### M-0507: Piety는 Greed의 절도에 면역

라벨: `DOCUMENTED`. 시길: piety, greed.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0507](../rules/sigil.md#m-0507) `wiki-sigils-piety-015`: "You are immune to having your items stolen by Greed players." ([출처](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
  - 번역: Greed 플레이어에게 아이템을 도둑맞는 것에 면역입니다.
- [M-0507](../rules/sigil.md#m-0507) `wiki-sigils-greed-017`: "You cannot steal from Piety players." ([출처](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
  - 번역: Piety 플레이어에게서는 훔칠 수 없습니다.

**형식 모델:**

- [M-0507](../rules/sigil.md#m-0507) 해석 A: `피해자가 Piety 시길을 가지고 있으면 steal(thief, victim)은 거부됨`
- [M-0507](../rules/sigil.md#m-0507) 정의역: Greed 시길을 가진 모든 도둑, Piety 시길을 가진 모든 피해자

**상호작용:** [M-0509](../rules/sigil.md#m-0509)

메모 ([M-0507](../rules/sigil.md#m-0507)): 두 페이지는 양쪽에서 같은 말을 하고 있습니다. Piety 참가자가 다른 경로로 아이템을 잃는 것(좀비의 파손, 방어 아이템의 언세이프 서클 손실)은 막아 주지 않습니다.

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0300](../theorems/T-0300.md), [T-0302](../theorems/T-0302.md), [T-0400](../theorems/T-0400.md), [T-0407](../theorems/T-0407.md), [T-0703](../theorems/T-0703.md)

## 미해결 질문

[U-0006](../unknowns.md#u-0006), [U-0015](../unknowns.md#u-0015), [U-0322](../unknowns.md#u-0322), [U-0329](../unknowns.md#u-0329), [U-0330](../unknowns.md#u-0330), [U-0331](../unknowns.md#u-0331), [U-0500](../unknowns.md#u-0500), [U-0501](../unknowns.md#u-0501), [U-0502](../unknowns.md#u-0502), [U-0503](../unknowns.md#u-0503), [U-0504](../unknowns.md#u-0504), [U-0505](../unknowns.md#u-0505), [U-0506](../unknowns.md#u-0506)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
