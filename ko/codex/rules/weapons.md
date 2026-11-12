# 규칙: 무기(weapons)

## 요약

`weapons` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

무기 계열은 참가자가 다른 참가자를 직접 해치는 데 쓸 수 있는 모든 것입니다. 참가자는 상자, 보급 상자, 크레이트에서 무기를 찾습니다 ([M-0300](../rules/weapons.md#m-0300)). 근접 무기, 활, 지팡이, Poison Dart는 무기 칸에 들어가며, 무기 칸은 인벤토리 공간을 쓰지 않습니다 ([M-0301](../rules/weapons.md#m-0301)).

근접 및 원거리 도구는 저마다 특성이 있습니다. Bow는 20 m 이내에서 5 HP로 타격하고 쿨다운이 5초이며, 발사마다 화살 한 발을 쓰고 부서지지 않습니다 ([M-0311](../rules/weapons.md#m-0311)). Assassin's knife는 10 m 이내에서 5 HP로 찌르며 2회 사용할 수 있습니다 ([M-0316](../rules/weapons.md#m-0316)). Long sword는 10 m 이내에서 10 HP로 타격하며 3회 사용할 수 있고 쿨다운은 10초입니다 ([M-0319](../rules/weapons.md#m-0319)). Zarok's axe는 체력이 가득할 때 5 HP로 타격하고 체력이 떨어질수록 최대 25 HP까지 올라가며 일회용입니다 ([M-0317](../rules/weapons.md#m-0317)). Huge machete는 10 HP로 타격하고 10회 사용할 수 있으며 관리자만 지급할 수 있습니다 ([M-0318](../rules/weapons.md#m-0318)). Wizard staff는 자신으로부터 50 m 이내에 5초 동안 지속되는 피해 구역을 만들어 총 10 HP의 피해를 주고 ([M-0313](../rules/weapons.md#m-0313)), 사용당 블러드 토큰 2개가 들며, 쿨다운은 20분입니다 ([M-0314](../rules/weapons.md#m-0314)). Poison Dart는 근처 참가자를 30분에 걸쳐 20 HP만큼 중독시킵니다 ([M-0315](../rules/weapons.md#m-0315)).

그다음은 폭발물과 Drone입니다. C4는 서 있는 곳에 설치하고 나중에 기폭하며, 자신을 포함해 10 m 이내에 20 HP의 피해를 줍니다 ([M-0302](../rules/weapons.md#m-0302)). Landmine은 다른 참가자나 좀비가 10 m 이내에 들어오면 작동하여 자신을 포함한 범위 내 모든 사람에게 15 HP의 피해를 줍니다 ([M-0307](../rules/weapons.md#m-0307)). 둘 다 한 칸에 최대 5개까지 중첩됩니다 ([M-0305](../rules/weapons.md#m-0305), [M-0310](../rules/weapons.md#m-0310)). Drone은 보이는 어떤 참가자든 거리와 관계없이 30초 뒤 10 HP로 공격합니다 ([M-0306](../rules/weapons.md#m-0306)). Ingenuity는 Robot도 만들 수 있습니다 ([M-0523](../rules/weapons.md#m-0523)).

효과적인 대상: Drone은 보이는 누구에게든 닿고 ([M-0306](../rules/weapons.md#m-0306)), C4와 Landmine은 군중을 응징합니다 ([M-0302](../rules/weapons.md#m-0302), [M-0307](../rules/weapons.md#m-0307)).

기재된 바에 따른 가장 약한 점: 일회용 및 제한 횟수 무기 ([M-0317](../rules/weapons.md#m-0317), [M-0316](../rules/weapons.md#m-0316))와 자신의 폭발물에 의한 자해 피해입니다 ([M-0302](../rules/weapons.md#m-0302), [M-0307](../rules/weapons.md#m-0307)).

알 수 없는 것: Drone, C4, Landmine, Dart의 사용 횟수가 몇 번인지 ([U-0304](../unknowns.md#u-0304)), Dart, axe, machete에서 "근처"가 무엇을 뜻하는지 ([U-0309](../unknowns.md#u-0309)), axe의 피해 곡선이 어떻게 오르는지 ([U-0310](../unknowns.md#u-0310)), 차단되거나 반사된 공격이 사용 횟수를 소모하는지 ([U-0308](../unknowns.md#u-0308)), 쿨다운이 언제 시작되는지 ([U-0307](../unknowns.md#u-0307))입니다. staff의 10 m가 반지름인지 지름인지는 미해결입니다 ([U-0312](../unknowns.md#u-0312)).

이 페이지는 규칙 24개(2 `DOCUMENTED`, 22 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0300"></a>

### M-0300: 무기 입수처

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0300](../rules/weapons.md#m-0300) `wiki-weapons-002`: "Contestants find them in chests, care packages and crates." ([출처](https://iceposeidon.com/safezone/wiki/weapons))
  - 번역: 참가자는 상자, 보급 상자, 크레이트에서 이를 찾습니다.

**형식 모델:**

- [M-0300](../rules/weapons.md#m-0300) 해석 A: `무기 아이템은 상자, 보급 상자, 크레이트를 통해서만 게임에 들어옴 (다른 곳에 명시된 거래와 상인 보급 상자 포함)`
- [M-0300](../rules/weapons.md#m-0300) 정의역: 아이템 획득

**미해결 질문:**

- [U-0015](../unknowns.md#u-0015) (높음): 상자 규칙(종류, 획득 범위, 생성 빈도, 내용물)은 무엇입니까? 상자 페이지는 삭제되었습니다(RE-0004).

메모 ([M-0300](../rules/weapons.md#m-0300)): 상자, 보급 상자, 크레이트 규칙은 이 페이지에 없습니다 ([U-0015](../unknowns.md#u-0015)). 거래와 상인 보급 상자는 다른 페이지에 명시되어 있습니다.

<a id="m-0301"></a>

### M-0301: 무기 슬롯 소속

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0301](../rules/weapons.md#m-0301) `wiki-weapons-003`: "Melee weapons, bows, staffs and Poison Darts fit a weapon slot." ([출처](https://iceposeidon.com/safezone/wiki/weapons))
  - 번역: 근접 무기, 활, 지팡이, Poison Dart는 무기 슬롯에 들어갑니다.
- [M-0301](../rules/weapons.md#m-0301) `wiki-merchant-040`: "Weapon and worn equipment slots do not use inventory space." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 무기 슬롯과 착용 장비 슬롯은 인벤토리 공간을 사용하지 않습니다.

**형식 모델:**

- [M-0301](../rules/weapons.md#m-0301) 해석 A: `근접 무기, 활, 지팡이, Poison Dart는 무기 슬롯에 들어가며, 무기 슬롯과 착용 장비는 인벤토리 공간을 사용하지 않음`
- [M-0301](../rules/weapons.md#m-0301) 정의역: 아이템 배치

메모 ([M-0301](../rules/weapons.md#m-0301)): C4, Landmine, Drone, 화살은 무기 슬롯 아이템으로 나열되어 있지 않으며 인벤토리 슬롯을 사용합니다. 두 번째 무기 슬롯은 [M-0334](../rules/economy.md#m-0334)를 참조하십시오.

<a id="m-0302"></a>

### M-0302: C4 설치와 폭발

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0302](../rules/weapons.md#m-0302) `wiki-weapons-004`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 사용 가능
- [M-0302](../rules/weapons.md#m-0302) `wiki-weapons-005`: "Place it where you stand, then detonate it at any time." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 서 있는 자리에 설치한 뒤 언제든지 기폭할 수 있습니다.
- [M-0302](../rules/weapons.md#m-0302) `wiki-weapons-006`: "It deals 20 HP to everyone within 10m (33ft), you included." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 10m (33ft) 이내의 모든 사람에게 20 HP의 피해를 주며, 본인도 포함됩니다.

**형식 모델:**

- [M-0302](../rules/weapons.md#m-0302) 해석 A: `자신의 위치에 설치하고 이후 아무 때나 기폭함. C4로부터의 거리가 10 m 이하인 모든 참가자(설치자 포함)가 20 HP의 피해를 받음`
- [M-0302](../rules/weapons.md#m-0302) 정의역: 거리(미터), 피해(HP)
- [M-0302](../rules/weapons.md#m-0302) 매개변수 `c4_damage_hp`: 20
- [M-0302](../rules/weapons.md#m-0302) 매개변수 `c4_radius_m`: 10

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0304](../unknowns.md#u-0304) (보통): 인챈트되지 않았을 때 drone, C4, landmine, Poison Dart는 각각 몇 번 사용할 수 있습니까?

메모 ([M-0302](../rules/weapons.md#m-0302)): 좀비는 C4를 작동시키지 않습니다(다른 페이지). 폭발은 범위 안의 좀비를 죽입니다(좀비 페이지).

<a id="m-0303"></a>

### M-0303: C4 함정 선물 (Ingenuity 부착)

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-007`: "With the Ingenuity sigil you can attach one C4 to another item you hold, once every 16h." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: Ingenuity 시길이 있으면 16h마다 한 번, 들고 있는 다른 아이템에 C4 하나를 부착할 수 있습니다.
- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-009`: "Detonate it while another contestant holds that item." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 다른 참가자가 그 아이템을 들고 있을 때 기폭합니다.
- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-010`: "Only that contestant takes 23 HP." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 그 참가자만 23 HP의 피해를 받습니다.
- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-011`: "It does not hurt you while you hold the item." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 아이템을 들고 있는 동안에는 본인에게 피해가 없습니다.

**형식 모델:**

- [M-0303](../rules/weapons.md#m-0303) 해석 A: `들고 있는 다른 아이템에 C4 하나를 부착하며 16h당 최대 한 번. 다른 참가자가 그것을 들고 있을 때 기폭하면 그 참가자만 23 HP의 피해를 받고, 소유자는 들고 있는 동안 피해를 받지 않음`
- [M-0303](../rules/weapons.md#m-0303) 정의역: HP, 시간
- [M-0303](../rules/weapons.md#m-0303) 매개변수 `trapped_gift_c4_damage_hp`: 23
- [M-0303](../rules/weapons.md#m-0303) 매개변수 `attach_cooldown_h`: 16

**미해결 질문:**

- [U-0301](../unknowns.md#u-0301) (보통): Ingenuity 함정 부착의 'once every 16h' 제한은 C4와 landmine이 공유하는 하나의 타이머입니까, 종류별 타이머입니까? 그리고 부착 시점에 시작됩니까, 폭발 시점에 시작됩니까?

메모 ([M-0303](../rules/weapons.md#m-0303)): 23 HP는 도출 없이 명시된 그대로 기록했습니다. 함정 선물은 다른 페이지의 차단 표(Shield, Sleeping Bag, Protection, Mirror)와 Kick 보너스 목록에도 나옵니다.

<a id="m-0304"></a>

### M-0304: C4 가시성

라벨: `CONDITIONAL`. 시길: all, ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0304](../rules/weapons.md#m-0304) `wiki-weapons-008`: "Only you can see the trap." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 함정은 본인만 볼 수 있습니다.
- [M-0304](../rules/weapons.md#m-0304) `wiki-weapons-014`: "Only you and Sigil of Ingenuity contestants can see it." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 본인과 Sigil of Ingenuity 참가자만 볼 수 있습니다.

**형식 모델:**

- [M-0304](../rules/weapons.md#m-0304) 해석 A: `설치된 C4는 소유자와 Sigil of Ingenuity 참가자만 볼 수 있으며, 함정 선물은 소유자만 볼 수 있음`
- [M-0304](../rules/weapons.md#m-0304) 해석 B: `'함정은 본인만 볼 수 있습니다'는 설치된 C4를 가리킴(뒤의 문장이 Ingenuity를 더해 같은 내용을 반복함)`

**미해결 질문:**

- [U-0302](../unknowns.md#u-0302) (낮음): 'Only you can see the trap.' (C4 섹션)은 함정 선물(C4가 부착된 아이템)을 가리킵니까, 설치된 C4를 가리킵니까?

메모 ([M-0304](../rules/weapons.md#m-0304)): Landmine과 달리 C4에는 다른 참가자의 근접 가시성도, 시청자 가시성도 명시되어 있지 않습니다.

<a id="m-0305"></a>

### M-0305: C4 중첩과 슬롯

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0305](../rules/weapons.md#m-0305) `wiki-weapons-012`: "Landmines and C4 stack: up to 5 of each share one inventory slot, and you can carry at most 5 of each." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: Landmine과 C4는 중첩됩니다. 각각 최대 5개가 인벤토리 슬롯 하나를 공유하며, 각각 최대 5개까지만 소지할 수 있습니다.
- [M-0305](../rules/weapons.md#m-0305) `wiki-weapons-013`: "An enchanted one uses its own slot." ([출처](https://iceposeidon.com/safezone/wiki/weapons#c4))
  - 번역: 인챈트된 것은 자체 슬롯을 사용합니다.

**형식 모델:**

- [M-0305](../rules/weapons.md#m-0305) 해석 A: `C4는 인벤토리 슬롯 하나에 최대 5개. 최대 5개까지 소지. 인챈트된 C4는 자체 슬롯을 차지함`
- [M-0305](../rules/weapons.md#m-0305) 정의역: 정수 개수
- [M-0305](../rules/weapons.md#m-0305) 매개변수 `c4_stack`: 5
- [M-0305](../rules/weapons.md#m-0305) 매개변수 `c4_carry_max`: 5

**미해결 질문:**

- [U-0303](../unknowns.md#u-0303) (보통): '각각 최대 5개가 한 슬롯을 공유한다 / 각각 최대 5개를 소지한다'라는 상한은 'An enchanted one uses its own slot'과 어떻게 맞물립니까?

메모 ([M-0305](../rules/weapons.md#m-0305)): 같은 문장이 아이템 페이지에도 있습니다(문구 동일, 모순 없음).

<a id="m-0306"></a>

### M-0306: Drone 공격

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0306](../rules/weapons.md#m-0306) `wiki-weapons-015`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#drone))
  - 번역: 사용 가능
- [M-0306](../rules/weapons.md#m-0306) `wiki-weapons-016`: "Strike any contestant you can see, at any distance." ([출처](https://iceposeidon.com/safezone/wiki/weapons#drone))
  - 번역: 보이는 참가자를 거리에 상관없이 공격합니다.
- [M-0306](../rules/weapons.md#m-0306) `wiki-weapons-017`: "It hits for 10 HP after 30s." ([출처](https://iceposeidon.com/safezone/wiki/weapons#drone))
  - 번역: 30s 후에 10 HP의 타격을 줍니다.

**형식 모델:**

- [M-0306](../rules/weapons.md#m-0306) 해석 A: `보이는 참가자를 거리에 상관없이 공격하며, 10 HP의 타격은 사용 30 s 후에 적중함`
- [M-0306](../rules/weapons.md#m-0306) 정의역: HP, 초
- [M-0306](../rules/weapons.md#m-0306) 매개변수 `drone_damage_hp`: 10
- [M-0306](../rules/weapons.md#m-0306) 매개변수 `drone_delay_s`: 30
- [M-0306](../rules/weapons.md#m-0306) 매개변수 `drone_uses`: UNKNOWN, [U-0304](../unknowns.md#u-0304) 참조

**미해결 질문:**

- [U-0304](../unknowns.md#u-0304) (보통): 인챈트되지 않았을 때 drone, C4, landmine, Poison Dart는 각각 몇 번 사용할 수 있습니까?
- [U-0305](../unknowns.md#u-0305) (높음): Drone: 사용 후 대상은 발사 시점에 고정되어 무슨 일이 있어도 30s 뒤에 타격받습니까, 아니면 drone이 대상이 계속 보이거나 살아 있어야 합니까?

메모 ([M-0306](../rules/weapons.md#m-0306)): '사용 가능' 라벨만 있습니다. 피해 표(다른 페이지)에 따르면 Drone은 Shield, Safety Bubble, Sleeping Bag, Protection, Mirror, Body Armor에 막힙니다.

<a id="m-0307"></a>

### M-0307: Landmine 설치, 발동, 폭발

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0307](../rules/weapons.md#m-0307) `wiki-weapons-018`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 사용 가능
- [M-0307](../rules/weapons.md#m-0307) `wiki-weapons-019`: "Place it where you stand." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 서 있는 자리에 설치합니다.
- [M-0307](../rules/weapons.md#m-0307) `wiki-weapons-020`: "It triggers when another contestant or a zombie comes within 10m (33ft)." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 다른 참가자나 좀비가 10m (33ft) 이내로 들어오면 발동합니다.
- [M-0307](../rules/weapons.md#m-0307) `wiki-weapons-021`: "It deals 15 HP to everyone in range, you included, and kills every zombie in range." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 범위 안의 모든 사람에게 15 HP의 피해를 주며, 본인도 포함되고, 범위 안의 모든 좀비를 죽입니다.

**형식 모델:**

- [M-0307](../rules/weapons.md#m-0307) 해석 A: `자신의 위치에 설치하며, 다른 참가자나 좀비가 거리 10 m 이하에 있을 때 발동함. 범위 안의 모든 사람(설치자 포함)에게 15 HP의 피해를 주고 범위 안의 모든 좀비를 죽임`
- [M-0307](../rules/weapons.md#m-0307) 정의역: 거리(미터), 피해(HP)
- [M-0307](../rules/weapons.md#m-0307) 매개변수 `landmine_damage_hp`: 15
- [M-0307](../rules/weapons.md#m-0307) 매개변수 `landmine_radius_m`: 10

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0304](../unknowns.md#u-0304) (보통): 인챈트되지 않았을 때 drone, C4, landmine, Poison Dart는 각각 몇 번 사용할 수 있습니까?

메모 ([M-0307](../rules/weapons.md#m-0307)): Landmine에 면역인 참가자(Protection)가 발동시켜도 여전히 폭발하는지는 명시되어 있지 않습니다.

<a id="m-0308"></a>

### M-0308: Landmine 함정 선물 (Ingenuity 부착)

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0308](../rules/weapons.md#m-0308) `wiki-weapons-022`: "With the Ingenuity sigil you can attach one landmine to an item you use on yourself, once every 16h." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: Ingenuity 시길이 있으면 16h마다 한 번, 자신에게 사용하는 아이템에 Landmine 하나를 부착할 수 있습니다.
- [M-0308](../rules/weapons.md#m-0308) `wiki-weapons-024`: "It fires when another contestant uses that item, the item is used up and its effect does not apply." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 다른 참가자가 그 아이템을 사용하면 발동하고, 아이템은 소모되며 그 효과는 적용되지 않습니다.
- [M-0308](../rules/weapons.md#m-0308) `wiki-weapons-025`: "Only that contestant takes 11 HP." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 그 참가자만 11 HP의 피해를 받습니다.

**형식 모델:**

- [M-0308](../rules/weapons.md#m-0308) 해석 A: `자신에게 사용하는 아이템에 Landmine 하나를 부착하며 16h당 최대 한 번. 다른 참가자가 그 아이템을 사용하면 발동함: 아이템은 소모되고 효과는 적용되지 않으며, 그 참가자만 11 HP의 피해를 받음`
- [M-0308](../rules/weapons.md#m-0308) 정의역: HP, 시간
- [M-0308](../rules/weapons.md#m-0308) 매개변수 `trapped_gift_landmine_damage_hp`: 11
- [M-0308](../rules/weapons.md#m-0308) 매개변수 `attach_cooldown_h`: 16

**미해결 질문:**

- [U-0301](../unknowns.md#u-0301) (보통): Ingenuity 함정 부착의 'once every 16h' 제한은 C4와 landmine이 공유하는 하나의 타이머입니까, 종류별 타이머입니까? 그리고 부착 시점에 시작됩니까, 폭발 시점에 시작됩니까?
- [U-0306](../unknowns.md#u-0306) (보통): Ingenuity landmine 부착의 '자신에게 사용하는 아이템'에는 어떤 아이템이 해당합니까?

메모 ([M-0308](../rules/weapons.md#m-0308)): 11 HP는 도출 없이 명시된 그대로 기록했습니다.

<a id="m-0309"></a>

### M-0309: Landmine 가시성

라벨: `CONDITIONAL`. 시길: all, ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-023`: "Only you can see the trap." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 함정은 본인만 볼 수 있습니다.
- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-026`: "Other contestants see it only within 20m (66ft) of it." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 다른 참가자는 20m (66ft) 이내에서만 볼 수 있습니다.
- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-027`: "A Sigil of Ingenuity always sees it." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: Sigil of Ingenuity는 항상 볼 수 있습니다.
- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-028`: "Viewers always see it." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 시청자는 항상 볼 수 있습니다.

**형식 모델:**

- [M-0309](../rules/weapons.md#m-0309) 해석 A: `소유자는 볼 수 있음. 다른 참가자는 20 m 이내에서만 볼 수 있음. Sigil of Ingenuity 참가자는 항상 볼 수 있음. 시청자는 항상 볼 수 있음`
- [M-0309](../rules/weapons.md#m-0309) 정의역: 거리(미터)
- [M-0309](../rules/weapons.md#m-0309) 매개변수 `other_see_radius_m`: 20

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?

메모 ([M-0309](../rules/weapons.md#m-0309)): '함정은 본인만 볼 수 있습니다'는 부착 문장 뒤에 오므로 위치상 함정 선물(아이템)을 가리킵니다. 설치된 Landmine의 규칙은 그다음 문장들입니다.

<a id="m-0310"></a>

### M-0310: Landmine 중첩과 슬롯

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0310](../rules/weapons.md#m-0310) `wiki-weapons-029`: "Landmines and C4 stack: up to 5 of each share one inventory slot, and you can carry at most 5 of each." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: Landmine과 C4는 중첩됩니다. 각각 최대 5개가 인벤토리 슬롯 하나를 공유하며, 각각 최대 5개까지만 소지할 수 있습니다.
- [M-0310](../rules/weapons.md#m-0310) `wiki-weapons-030`: "An enchanted one uses its own slot." ([출처](https://iceposeidon.com/safezone/wiki/weapons#landmine))
  - 번역: 인챈트된 것은 자체 슬롯을 사용합니다.

**형식 모델:**

- [M-0310](../rules/weapons.md#m-0310) 해석 A: `Landmine은 인벤토리 슬롯 하나에 최대 5개. 최대 5개까지 소지. 인챈트된 Landmine은 자체 슬롯을 차지함`
- [M-0310](../rules/weapons.md#m-0310) 정의역: 정수 개수
- [M-0310](../rules/weapons.md#m-0310) 매개변수 `landmine_stack`: 5
- [M-0310](../rules/weapons.md#m-0310) 매개변수 `landmine_carry_max`: 5

**미해결 질문:**

- [U-0303](../unknowns.md#u-0303) (보통): '각각 최대 5개가 한 슬롯을 공유한다 / 각각 최대 5개를 소지한다'라는 상한은 'An enchanted one uses its own slot'과 어떻게 맞물립니까?

<a id="m-0311"></a>

### M-0311: 활

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0311](../rules/weapons.md#m-0311) `wiki-weapons-031`: "Equippable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#bow))
  - 번역: 장착 가능
- [M-0311](../rules/weapons.md#m-0311) `wiki-weapons-032`: "Hits for 5 HP within 20m (66ft), cooldown 5s." ([출처](https://iceposeidon.com/safezone/wiki/weapons#bow))
  - 번역: 20m (66ft) 이내에 5 HP의 타격을 주며, 쿨다운은 5s입니다.
- [M-0311](../rules/weapons.md#m-0311) `wiki-weapons-033`: "Each shot uses one arrow." ([출처](https://iceposeidon.com/safezone/wiki/weapons#bow))
  - 번역: 한 발마다 화살 하나를 사용합니다.
- [M-0311](../rules/weapons.md#m-0311) `wiki-weapons-034`: "You cannot shoot without arrows." ([출처](https://iceposeidon.com/safezone/wiki/weapons#bow))
  - 번역: 화살이 없으면 쏠 수 없습니다.
- [M-0311](../rules/weapons.md#m-0311) `wiki-weapons-035`: "The bow has unlimited uses and never breaks." ([출처](https://iceposeidon.com/safezone/wiki/weapons#bow))
  - 번역: 활은 사용 횟수에 제한이 없고 부서지지 않습니다.

**형식 모델:**

- [M-0311](../rules/weapons.md#m-0311) 해석 A: `거리 20 m 이하에 5 HP의 타격. 쿨다운 5 s. 한 발마다 화살 하나를 사용. 화살이 없으면 쏠 수 없음. 사용 횟수 무제한이며 부서지지 않음`
- [M-0311](../rules/weapons.md#m-0311) 정의역: HP, 미터, 초
- [M-0311](../rules/weapons.md#m-0311) 매개변수 `bow_damage_hp`: 5
- [M-0311](../rules/weapons.md#m-0311) 매개변수 `bow_range_m`: 20
- [M-0311](../rules/weapons.md#m-0311) 매개변수 `bow_cooldown_s`: 5

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0307](../unknowns.md#u-0307) (높음): 쿨다운 의미(bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): 시도 시점에 시작됩니까, 타격 시점에 시작됩니까? 그리고 무기 아이템별입니까, 참가자별입니까(Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (높음): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까?

메모 ([M-0311](../rules/weapons.md#m-0311)): 활은 다른 페이지의 Kick 보너스 목록과 Mirror 목록에 나옵니다.

<a id="m-0312"></a>

### M-0312: 화살과 중첩

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0312](../rules/weapons.md#m-0312) `wiki-weapons-036`: "Ammo for the bow." ([출처](https://iceposeidon.com/safezone/wiki/weapons#arrow))
  - 번역: 활의 탄약입니다.
- [M-0312](../rules/weapons.md#m-0312) `wiki-weapons-037`: "A chest drop holds 10." ([출처](https://iceposeidon.com/safezone/wiki/weapons#arrow))
  - 번역: 상자 드롭에는 10개가 들어 있습니다.
- [M-0312](../rules/weapons.md#m-0312) `wiki-weapons-038`: "Arrows stack: new arrows join the stack you already carry, up to 10 per stack, so they need no extra slot." ([출처](https://iceposeidon.com/safezone/wiki/weapons#arrow))
  - 번역: 화살은 중첩됩니다. 새 화살은 이미 소지한 묶음에 합쳐지며 묶음당 최대 10개이므로 추가 슬롯이 필요하지 않습니다.
- [M-0312](../rules/weapons.md#m-0312) `wiki-weapons-039`: "Arrows above that start a new stack, which uses a slot." ([출처](https://iceposeidon.com/safezone/wiki/weapons#arrow))
  - 번역: 그 이상의 화살은 새 묶음을 시작하며 슬롯을 사용합니다.

**형식 모델:**

- [M-0312](../rules/weapons.md#m-0312) 해석 A: `상자 드롭에는 화살 10개가 들어 있음. 화살은 소지한 묶음에 묶음당 최대 10개까지 합쳐짐. 그 이상은 슬롯을 차지하는 새 묶음을 시작함`
- [M-0312](../rules/weapons.md#m-0312) 정의역: 정수 개수
- [M-0312](../rules/weapons.md#m-0312) 매개변수 `chest_drop_arrows`: 10
- [M-0312](../rules/weapons.md#m-0312) 매개변수 `arrow_stack`: 10

메모 ([M-0312](../rules/weapons.md#m-0312)): 새 묶음은 인벤토리 슬롯을 사용합니다(기본 3개, 아이템 페이지). 상자 규칙은 [U-0015](../unknowns.md#u-0015)입니다.

<a id="m-0313"></a>

### M-0313: Wizard staff 범위

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0313](../rules/weapons.md#m-0313) `wiki-weapons-040`: "Equippable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
  - 번역: 장착 가능
- [M-0313](../rules/weapons.md#m-0313) `wiki-weapons-041`: "Pick a spot on the map within 50m (164ft) of you to place a 10m (33ft) damage area, on top of contestants too." ([출처](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
  - 번역: 자신으로부터 50m (164ft) 이내의 지도상 지점을 골라 10m (33ft)의 피해 구역을 설치하며, 참가자 위에도 설치할 수 있습니다.
- [M-0313](../rules/weapons.md#m-0313) `wiki-weapons-042`: "It lasts 5s and deals 10 HP in total to everyone inside, you included." ([출처](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
  - 번역: 5s 동안 지속되며 안에 있는 모든 사람에게 총 10 HP의 피해를 주고, 본인도 포함됩니다.

**형식 모델:**

- [M-0313](../rules/weapons.md#m-0313) 해석 A: `사용자로부터 거리 50 m 이하의 지점을 고르면, 10 m 구역(반지름 또는 지름, [U-0312](../unknowns.md#u-0312) 참조)이 5 s 동안 지속되며 안에 있는 모든 사람(사용자 포함)에게 총 10 HP의 피해를 줌`
- [M-0313](../rules/weapons.md#m-0313) 정의역: HP, 미터, 초
- [M-0313](../rules/weapons.md#m-0313) 매개변수 `staff_placement_range_m`: 50
- [M-0313](../rules/weapons.md#m-0313) 매개변수 `staff_area_m`: 10
- [M-0313](../rules/weapons.md#m-0313) 매개변수 `staff_duration_s`: 5
- [M-0313](../rules/weapons.md#m-0313) 매개변수 `staff_total_damage_hp`: 10

**미해결 질문:**

- [U-0010](../unknowns.md#u-0010) (보통): Wizard staff의 '5 s 동안 총 10 HP': 한 번의 타격입니까, 여러 번의 틱입니까?
- [U-0312](../unknowns.md#u-0312) (보통): Wizard staff: '10m damage area'는 반지름입니까, 지름입니까?
- [U-0313](../unknowns.md#u-0313) (보통): Wizard staff: 5s 중 일부 시간만 범위 안에 있던 참가자는 10 HP 전체를 받습니까, 일부만 받습니까? 설치 후에 들어온 참가자도 피해를 받습니까?
- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?

메모 ([M-0313](../rules/weapons.md#m-0313)): 지점은 참가자 위일 수 있습니다. 'Wizard Staff area'는 다른 페이지의 피해 표에 있는 행입니다.

<a id="m-0314"></a>

### M-0314: Wizard staff 비용, 쿨다운, 내구도

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0314](../rules/weapons.md#m-0314) `wiki-weapons-043`: "Each use costs 2 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
  - 번역: 한 번 사용할 때마다 블러드 토큰 2개가 듭니다.
- [M-0314](../rules/weapons.md#m-0314) `wiki-weapons-044`: "Cooldown 20min." ([출처](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
  - 번역: 쿨다운 20min.
- [M-0314](../rules/weapons.md#m-0314) `wiki-weapons-045`: "The staff never breaks." ([출처](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
  - 번역: 지팡이는 부서지지 않습니다.

**형식 모델:**

- [M-0314](../rules/weapons.md#m-0314) 해석 A: `한 번 사용할 때마다 블러드 토큰 2개가 듦. 쿨다운 20 min. 부서지지 않음(사용 횟수 무제한)`
- [M-0314](../rules/weapons.md#m-0314) 정의역: 블러드 토큰, 분
- [M-0314](../rules/weapons.md#m-0314) 매개변수 `staff_cost_tokens`: 2
- [M-0314](../rules/weapons.md#m-0314) 매개변수 `staff_cooldown_min`: 20

**미해결 질문:**

- [U-0314](../unknowns.md#u-0314) (낮음): Wizard staff 'Each use costs 2 blood tokens': Ingenuity의 10% 할증이 여기에 적용됩니까? 토큰이 2개 미만이면 어떻게 됩니까?
- [U-0307](../unknowns.md#u-0307) (높음): 쿨다운 의미(bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): 시도 시점에 시작됩니까, 타격 시점에 시작됩니까? 그리고 무기 아이템별입니까, 참가자별입니까(Dual Wield)?

<a id="m-0315"></a>

### M-0315: Poison Dart

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0315](../rules/weapons.md#m-0315) `wiki-weapons-046`: "EquippableUsable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#poison_dart))
  - 번역: 장착 가능, 사용 가능
- [M-0315](../rules/weapons.md#m-0315) `wiki-weapons-047`: "Poison a nearby contestant for 20 HP over 30min." ([출처](https://iceposeidon.com/safezone/wiki/weapons#poison_dart))
  - 번역: 가까운 참가자를 30min 동안 20 HP만큼 중독시킵니다.

**형식 모델:**

- [M-0315](../rules/weapons.md#m-0315) 해석 A: `가까운 참가자를 30 min 동안 20 HP만큼 중독시킴(독 페이지는 1min 30s마다 1 HP의 피해를 준다고 하며, 이는 30 min 동안 20틱임)`
- [M-0315](../rules/weapons.md#m-0315) 정의역: HP, 분
- [M-0315](../rules/weapons.md#m-0315) 매개변수 `dart_total_hp`: 20
- [M-0315](../rules/weapons.md#m-0315) 매개변수 `dart_duration_min`: 30
- [M-0315](../rules/weapons.md#m-0315) 매개변수 `dart_range_m`: UNKNOWN, [U-0309](../unknowns.md#u-0309) 참조
- [M-0315](../rules/weapons.md#m-0315) 매개변수 `dart_uses`: UNKNOWN, [U-0304](../unknowns.md#u-0304) 참조

**미해결 질문:**

- [U-0309](../unknowns.md#u-0309) (높음): Poison Dart, Zarok's axe, Huge machete의 '근처(nearby)'의 범위는 얼마입니까?
- [U-0315](../unknowns.md#u-0315) (보통): Poison Dart: 이미 중독된 참가자가 다시 다트를 맞으면(또는 Fake gravestone에 맞으면) 새 독이 20 HP 전체 일정을 다시 시작합니까, 남은 분량을 대체합니까, 더해집니까?
- [U-0316](../unknowns.md#u-0316) (낮음): Poison Dart: '20 HP over 30min'과 독 페이지의 1min 30s마다 1 HP를 함께 보면, 첫 틱은 1min 30s에 옵니까, 즉시 옵니까?
- [U-0304](../unknowns.md#u-0304) (보통): 인챈트되지 않았을 때 drone, C4, landmine, Poison Dart는 각각 몇 번 사용할 수 있습니까?
- [U-0318](../unknowns.md#u-0318) (보통): 둘 다 붙어 있는 Poison Dart와 Zarok's axe에서 Equippable과 Usable 라벨은 무엇을 뜻합니까?

메모 ([M-0315](../rules/weapons.md#m-0315)): 독 페이지와 교차 확인: 30 min / 90 s = 1 HP짜리 20틱 = 20 HP로 일치하며 모순은 없습니다. Dart는 피해 페이지의 Kick 보너스 목록에 없습니다. 다시 중독시키면 타이머가 초기화되며 중첩되지 않습니다(독 페이지).

<a id="m-0316"></a>

### M-0316: Assassin's knife

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0316](../rules/weapons.md#m-0316) `wiki-weapons-048`: "Equippable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#assassins_knife))
  - 번역: 장착 가능
- [M-0316](../rules/weapons.md#m-0316) `wiki-weapons-049`: "Stabs a contestant within 10m (33ft) for 5 HP." ([출처](https://iceposeidon.com/safezone/wiki/weapons#assassins_knife))
  - 번역: 10m (33ft) 이내의 참가자를 찔러 5 HP의 피해를 줍니다.
- [M-0316](../rules/weapons.md#m-0316) `wiki-weapons-050`: "2 uses, cooldown 5s." ([출처](https://iceposeidon.com/safezone/wiki/weapons#assassins_knife))
  - 번역: 2회 사용, 쿨다운 5s.

**형식 모델:**

- [M-0316](../rules/weapons.md#m-0316) 해석 A: `거리 10 m 이하의 참가자를 찔러 5 HP의 피해를 줌. 2회 사용. 쿨다운 5 s`
- [M-0316](../rules/weapons.md#m-0316) 정의역: HP, 미터, 초
- [M-0316](../rules/weapons.md#m-0316) 매개변수 `knife_damage_hp`: 5
- [M-0316](../rules/weapons.md#m-0316) 매개변수 `knife_range_m`: 10
- [M-0316](../rules/weapons.md#m-0316) 매개변수 `knife_uses`: 2
- [M-0316](../rules/weapons.md#m-0316) 매개변수 `knife_cooldown_s`: 5

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0307](../unknowns.md#u-0307) (높음): 쿨다운 의미(bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): 시도 시점에 시작됩니까, 타격 시점에 시작됩니까? 그리고 무기 아이템별입니까, 참가자별입니까(Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (높음): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까?

<a id="m-0317"></a>

### M-0317: Zarok's axe

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0317](../rules/weapons.md#m-0317) `wiki-weapons-051`: "EquippableUsable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#zaroks_axe))
  - 번역: 장착 가능, 사용 가능
- [M-0317](../rules/weapons.md#m-0317) `wiki-weapons-052`: "Hits a nearby contestant for 5 HP at full health, rising to 25 HP as your health drops." ([출처](https://iceposeidon.com/safezone/wiki/weapons#zaroks_axe))
  - 번역: 가까운 참가자에게 체력이 가득할 때 5 HP의 타격을 주며, 자신의 체력이 떨어질수록 최대 25 HP까지 올라갑니다.
- [M-0317](../rules/weapons.md#m-0317) `wiki-weapons-053`: "Single use." ([출처](https://iceposeidon.com/safezone/wiki/weapons#zaroks_axe))
  - 번역: 1회용.

**형식 모델:**

- [M-0317](../rules/weapons.md#m-0317) 해석 A: `가까운 참가자를 타격함. 피해는 체력이 가득할 때 5 HP이고 사용자의 체력이 떨어질수록 25 HP까지 올라감(곡선은 [U-0310](../unknowns.md#u-0310)). 1회용`
- [M-0317](../rules/weapons.md#m-0317) 해석 B: `피해가 사용자가 아니라 대상의 체력에 따라 달라짐`
- [M-0317](../rules/weapons.md#m-0317) 정의역: HP 정수, 1 <= h <= 최대 HP
- [M-0317](../rules/weapons.md#m-0317) 매개변수 `axe_min_damage_hp`: 5
- [M-0317](../rules/weapons.md#m-0317) 매개변수 `axe_max_damage_hp`: 25
- [M-0317](../rules/weapons.md#m-0317) 매개변수 `axe_range_m`: UNKNOWN, [U-0309](../unknowns.md#u-0309) 참조
- [M-0317](../rules/weapons.md#m-0317) 매개변수 `axe_uses`: 1

**미해결 질문:**

- [U-0309](../unknowns.md#u-0309) (높음): Poison Dart, Zarok's axe, Huge machete의 '근처(nearby)'의 범위는 얼마입니까?
- [U-0310](../unknowns.md#u-0310) (높음): Zarok's axe: 사용자의 체력이 떨어질수록 피해가 최대 체력일 때 5 HP에서 25 HP로 어떻게 올라갑니까(선형인지, 단계적인지, 최대 HP에 대한 비율인지, 25는 어디에서 도달하는지)?
- [U-0311](../unknowns.md#u-0311) (보통): Zarok's axe: 정수가 아닌 피해 값은 어떤 방식으로 정수로 처리됩니까?
- [U-0318](../unknowns.md#u-0318) (보통): 둘 다 붙어 있는 Poison Dart와 Zarok's axe에서 Equippable과 Usable 라벨은 무엇을 뜻합니까?

메모 ([M-0317](../rules/weapons.md#m-0317)): '자신의 체력'은 사용자의 체력으로 해석합니다. 해당 문장이 '가까운 참가자에게 타격을 줍니다' 뒤에 오므로 해석 B도 유지합니다.

<a id="m-0318"></a>

### M-0318: Huge machete

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0318](../rules/weapons.md#m-0318) `wiki-weapons-054`: "Equippable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
  - 번역: 장착 가능
- [M-0318](../rules/weapons.md#m-0318) `wiki-weapons-055`: "Only admins can give it out." ([출처](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
  - 번역: 관리자만 지급할 수 있습니다.
- [M-0318](../rules/weapons.md#m-0318) `wiki-weapons-056`: "Hits a nearby contestant for 10 HP." ([출처](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
  - 번역: 가까운 참가자에게 10 HP의 타격을 줍니다.
- [M-0318](../rules/weapons.md#m-0318) `wiki-weapons-057`: "10 uses, cooldown 5s." ([출처](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
  - 번역: 10회 사용, 쿨다운 5s.

**형식 모델:**

- [M-0318](../rules/weapons.md#m-0318) 해석 A: `관리자만 지급할 수 있음. 가까운 참가자에게 10 HP의 타격을 줌. 10회 사용. 쿨다운 5 s`
- [M-0318](../rules/weapons.md#m-0318) 정의역: HP, 초
- [M-0318](../rules/weapons.md#m-0318) 매개변수 `machete_damage_hp`: 10
- [M-0318](../rules/weapons.md#m-0318) 매개변수 `machete_range_m`: UNKNOWN, [U-0309](../unknowns.md#u-0309) 참조
- [M-0318](../rules/weapons.md#m-0318) 매개변수 `machete_uses`: 10
- [M-0318](../rules/weapons.md#m-0318) 매개변수 `machete_cooldown_s`: 5

**미해결 질문:**

- [U-0309](../unknowns.md#u-0309) (높음): Poison Dart, Zarok's axe, Huge machete의 '근처(nearby)'의 범위는 얼마입니까?
- [U-0307](../unknowns.md#u-0307) (높음): 쿨다운 의미(bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): 시도 시점에 시작됩니까, 타격 시점에 시작됩니까? 그리고 무기 아이템별입니까, 참가자별입니까(Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (높음): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까?

메모 ([M-0318](../rules/weapons.md#m-0318)): 상인 페이지의 인챈트 설명과 Deep Cut 목록에 나오는 'machete'는 Huge machete로 해석합니다.

<a id="m-0319"></a>

### M-0319: Long sword

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0319](../rules/weapons.md#m-0319) `wiki-weapons-058`: "Equippable" ([출처](https://iceposeidon.com/safezone/wiki/weapons#long_sword))
  - 번역: 장착 가능
- [M-0319](../rules/weapons.md#m-0319) `wiki-weapons-059`: "Hits a contestant within 10m (33ft) for 10 HP." ([출처](https://iceposeidon.com/safezone/wiki/weapons#long_sword))
  - 번역: 10m (33ft) 이내의 참가자에게 10 HP의 타격을 줍니다.
- [M-0319](../rules/weapons.md#m-0319) `wiki-weapons-060`: "3 uses, cooldown 10s." ([출처](https://iceposeidon.com/safezone/wiki/weapons#long_sword))
  - 번역: 3회 사용, 쿨다운 10s.

**형식 모델:**

- [M-0319](../rules/weapons.md#m-0319) 해석 A: `거리 10 m 이하의 참가자에게 10 HP의 타격을 줌. 3회 사용. 쿨다운 10 s`
- [M-0319](../rules/weapons.md#m-0319) 정의역: HP, 미터, 초
- [M-0319](../rules/weapons.md#m-0319) 매개변수 `sword_damage_hp`: 10
- [M-0319](../rules/weapons.md#m-0319) 매개변수 `sword_range_m`: 10
- [M-0319](../rules/weapons.md#m-0319) 매개변수 `sword_uses`: 3
- [M-0319](../rules/weapons.md#m-0319) 매개변수 `sword_cooldown_s`: 10

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0307](../unknowns.md#u-0307) (높음): 쿨다운 의미(bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): 시도 시점에 시작됩니까, 타격 시점에 시작됩니까? 그리고 무기 아이템별입니까, 참가자별입니까(Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (높음): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까?

<a id="m-0336"></a>

### M-0336: Deep Cut 출혈

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0336](../rules/weapons.md#m-0336) `wiki-merchant-042`: "Deep Cut: 20 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Deep Cut: 블러드 토큰 20개.
- [M-0336](../rules/weapons.md#m-0336) `wiki-merchant-043`: "Your next bow, knife, long sword, axe, machete or drone hit, or Poison Dart, causes bleeding: 1 HP every five minutes until a bandage or a Healing contestant cures it." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 다음 활, 칼, 장검, 도끼, 마체테 또는 Drone 타격, 혹은 Poison Dart가 출혈을 일으키며, 붕대나 Healing 참가자가 치료할 때까지 5분마다 1 HP를 잃습니다.
- [M-0336](../rules/weapons.md#m-0336) `wiki-merchant-044`: "One charge." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 충전 1회.
- [M-0336](../rules/weapons.md#m-0336) `wiki-merchant-045`: "Bleeding does not stack." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 출혈은 중첩되지 않습니다.

**형식 모델:**

- [M-0336](../rules/weapons.md#m-0336) 해석 A: `충전 1회. 다음 활, 칼, 장검, 도끼, 마체테 또는 Drone 타격, 혹은 다음 Poison Dart가 출혈을 일으켜 붕대나 Healing 참가자가 치료할 때까지 5 min마다 1 HP를 잃음. 출혈은 중첩되지 않음`
- [M-0336](../rules/weapons.md#m-0336) 정의역: HP, 분
- [M-0336](../rules/weapons.md#m-0336) 매개변수 `deep_cut_cost_tokens`: 20
- [M-0336](../rules/weapons.md#m-0336) 매개변수 `bleed_hp`: 1
- [M-0336](../rules/weapons.md#m-0336) 매개변수 `bleed_interval_min`: 5

**따름 결과:** [T-0305](../theorems/T-0305.md)

**미해결 질문:**

- [U-0332](../unknowns.md#u-0332) (보통): Deep Cut: 첫 출혈 틱은 언제이며, 출혈 중에 새 타격을 받으면 타이머가 초기화되고, 사용하지 않은 충전은 얼마나 오래 유지되며, 출혈 틱은 타격으로 계산됩니까?
- [U-0308](../unknowns.md#u-0308) (높음): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, robot, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?

메모 ([M-0336](../rules/weapons.md#m-0336)): Staff, C4, landmine은 목록에 없습니다. 붕대와 Healing의 치료는 Bandage 페이지와 Healing 페이지에 명시되어 있습니다.

<a id="m-0337"></a>

### M-0337: 무기 인챈트 (일반 규칙)

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0337](../rules/weapons.md#m-0337) `wiki-merchant-046`: "Weapon enchantment: 15 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Weapon enchantment: 블러드 토큰 15개.
- [M-0337](../rules/weapons.md#m-0337) `wiki-merchant-047`: "Twice the uses and +10 damage for two hours." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 사용 횟수가 2배가 되고 2시간 동안 피해가 +10 됩니다.
- [M-0337](../rules/weapons.md#m-0337) `wiki-merchant-048`: "After two hours the weapon loses the bonus damage and keeps the uses it had before or the uses it has left, whichever is lower." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 2시간이 지나면 무기는 추가 피해를 잃고, 인챈트 전의 사용 횟수와 남은 사용 횟수 중 낮은 쪽을 유지합니다.
- [M-0337](../rules/weapons.md#m-0337) `wiki-merchant-049`: "If you use up the enchanted uses first, a knife, machete or long sword goes back with one use left; a single-use weapon is used up." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 인챈트된 사용 횟수를 먼저 다 쓰면, 칼, 마체테, 장검은 사용 횟수 1회가 남은 상태로 돌아오고, 1회용 무기는 소모됩니다.
- [M-0337](../rules/weapons.md#m-0337) `wiki-merchant-055`: "For every other weapon, if two hours pass first, the bonus ends and the item stays as a normal item." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 그 밖의 모든 무기는 2시간이 먼저 지나면 추가 효과가 끝나고 아이템은 일반 아이템으로 남습니다.
- [M-0337](../rules/weapons.md#m-0337) `wiki-merchant-056`: "You can have one enchanted weapon, or two with Dual Wield." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 인챈트된 무기는 하나만 가질 수 있으며, Dual Wield가 있으면 둘까지 가질 수 있습니다.

**형식 모델:**

- [M-0337](../rules/weapons.md#m-0337) 해석 A: `토큰 15개. 사용 횟수 2배와 2 h 동안 피해 +10. 2 h 후 무기는 추가 효과를 잃고 min(이전 사용 횟수, 남은 사용 횟수)를 유지. 인챈트된 사용 횟수가 먼저 소진되면 칼, 마체테, 장검은 사용 횟수 1회가 남은 상태로 돌아오고 1회용 무기는 소모됨. 그 밖의 모든 무기는 2 h가 먼저 지나면 추가 효과가 끝나고 일반 아이템이 됨. 인챈트된 무기는 하나, Dual Wield가 있으면 둘`
- [M-0337](../rules/weapons.md#m-0337) 정의역: HP, 시간, 정수 사용 횟수
- [M-0337](../rules/weapons.md#m-0337) 매개변수 `weapon_enchant_cost_tokens`: 15
- [M-0337](../rules/weapons.md#m-0337) 매개변수 `weapon_enchant_bonus_hp`: 10
- [M-0337](../rules/weapons.md#m-0337) 매개변수 `weapon_enchant_duration_h`: 2

**미해결 질문:**

- [U-0333](../unknowns.md#u-0333) (높음): 무기 인챈트 'Twice the uses ... keeps the uses it had before or the uses it has left, whichever is lower': 무엇의 두 배이며, 'the uses it had before'는 무엇입니까?
- [U-0334](../unknowns.md#u-0334) (보통): 인챈트 시계: 2시간은 구매 시점에 시작합니까, 무기에 적용하는 시점에 시작합니까? 그리고 'For every other weapon, if two hours pass first'는 Zarok's axe, Poison Dart, C4, landmine, drone도 제한합니까?
- [U-0337](../unknowns.md#u-0337) (보통): 인챈트 제한 'one enchanted weapon, or two with Dual Wield': 무기 슬롯 아이템이 아닌 C4, landmine, drone, Poison Dart도 포함합니까?
- [U-0308](../unknowns.md#u-0308) (높음): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까?
- [U-0006](../unknowns.md#u-0006) (높음): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)?

메모 ([M-0337](../rules/weapons.md#m-0337)): 특정 무기는 [M-0338](../rules/weapons.md#m-0338)에서 이 일반 규칙보다 우선합니다. 기본 가격 15는 Ingenuity에서 binary64 문제가 되는 가격에 해당하지 않습니다.

<a id="m-0338"></a>

### M-0338: 무기 인챈트 무기별 추가 효과

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0338](../rules/weapons.md#m-0338) `wiki-merchant-050`: "Zarok's Axe and Poison Dart get +10 damage for two uses, then they are used up." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Zarok's Axe와 Poison Dart는 2번 사용하는 동안 피해가 +10 되며, 그 후 소모됩니다.
- [M-0338](../rules/weapons.md#m-0338) `wiki-merchant-051`: "Landmines and C4 get +20 damage and +10m (33ft) radius for one use, then they are used up." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Landmine과 C4는 1번 사용하는 동안 피해 +20과 반경 +10m (33ft)를 얻으며, 그 후 소모됩니다.
- [M-0338](../rules/weapons.md#m-0338) `wiki-merchant-052`: "Drones get +10 damage for one use, then they are used up." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Drone은 1번 사용하는 동안 피해가 +10 되며, 그 후 소모됩니다.
- [M-0338](../rules/weapons.md#m-0338) `wiki-merchant-053`: "A bow gets +10 damage for five shots or two hours." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 활은 5발 동안 또는 2시간 동안 피해가 +10 됩니다.
- [M-0338](../rules/weapons.md#m-0338) `wiki-merchant-054`: "A Wizard Staff gets +10 damage and +10m (33ft) area radius for five uses, with no time limit." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Wizard Staff는 5회 사용하는 동안 피해 +10과 범위 반경 +10m (33ft)를 얻으며, 시간 제한은 없습니다.

**형식 모델:**

- [M-0338](../rules/weapons.md#m-0338) 해석 A: `Zarok's Axe와 Poison Dart: 2번 사용하는 동안 피해 +10, 그 후 소모. Landmines와 C4: 1번 사용하는 동안 피해 +20과 반경 +10 m, 그 후 소모. Drones: 1번 사용하는 동안 피해 +10, 그 후 소모. 활: 5발 동안 또는 2 h 동안 피해 +10. Wizard Staff: 5회 사용하는 동안 피해 +10과 범위 반경 +10 m, 시간 제한 없음`
- [M-0338](../rules/weapons.md#m-0338) 정의역: HP, 미터, 정수 사용 횟수
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `axe_dart_bonus_hp`: 10
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `axe_dart_uses`: 2
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `trap_bonus_hp`: 20
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `trap_bonus_radius_m`: 10
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `drone_bonus_hp`: 10
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `bow_bonus_hp`: 10
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `bow_bonus_shots`: 5
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `staff_bonus_hp`: 10
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `staff_bonus_radius_m`: 10
- [M-0338](../rules/weapons.md#m-0338) 매개변수 `staff_enchant_uses`: 5

**따름 결과:** [T-0001](../theorems/T-0001.md)

**미해결 질문:**

- [U-0317](../unknowns.md#u-0317) (보통): 지속 피해 아이템에서 'Poison Dart ... +10 damage for two uses'는 무엇을 뜻합니까?
- [U-0334](../unknowns.md#u-0334) (보통): 인챈트 시계: 2시간은 구매 시점에 시작합니까, 무기에 적용하는 시점에 시작합니까? 그리고 'For every other weapon, if two hours pass first'는 Zarok's axe, Poison Dart, C4, landmine, drone도 제한합니까?
- [U-0335](../unknowns.md#u-0335) (낮음): 인챈트된 bow의 'five shots or two hours': 먼저 오는 쪽입니까, 나중에 오는 쪽입니까?
- [U-0336](../unknowns.md#u-0336) (보통): 인챈트된 C4 또는 landmine: '+10m radius'는 발동 거리에도 적용됩니까? 그리고 인챈트된 함정으로 만든 trapped gift에 인챈트가 이어집니까?
- [U-0304](../unknowns.md#u-0304) (보통): 인챈트되지 않았을 때 drone, C4, landmine, Poison Dart는 각각 몇 번 사용할 수 있습니까?
- [U-0312](../unknowns.md#u-0312) (보통): Wizard staff: '10m damage area'는 반지름입니까, 지름입니까?

메모 ([M-0338](../rules/weapons.md#m-0338)): 인챈트된 staff에서 '+10 damage'가 범위의 총 10 HP에 더해지는지(총 20 HP) 여부는 [U-0010](../unknowns.md#u-0010)(틱)에 포함되며 따로 명시되어 있지 않습니다.

<a id="m-0523"></a>

### M-0523: Robot 조합품의 피해와 이동

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0523](../rules/weapons.md#m-0523) `wiki-sigils-ingenuity-015`: "For ten minutes it deals 1 HP every 2s to other players within 10m (33ft)." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
  - 번역: 10분 동안 10m (33ft) 이내의 다른 플레이어에게 2s마다 1 HP의 피해를 줍니다.
- [M-0523](../rules/weapons.md#m-0523) `wiki-sigils-ingenuity-017`: "Leave it still or pick a player to follow at 1.4m/s (3.13mph)." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
  - 번역: 가만히 두거나 따라갈 플레이어를 골라 1.4m/s (3.13mph)로 따라가게 합니다.

**형식 모델:**

- [M-0523](../rules/weapons.md#m-0523) 해석 A: `robot은 600 s 동안 활성. 전역 2 s 시계. 틱마다 10 m 이내의 다른 모든 플레이어가 1 HP 피해를 입음. robot은 가만히 있거나 선택한 플레이어를 1.4 m/s로 따라감`
- [M-0523](../rules/weapons.md#m-0523) 해석 B: `대상별 타이머, 첫 타격은 진입 2 s 후`
- [M-0523](../rules/weapons.md#m-0523) 해석 C: `대상별, 첫 타격은 진입 시점이고 이후 2 s마다`
- [M-0523](../rules/weapons.md#m-0523) 정의역: t는 0..600 s. 거리는 미터. 속도 1.4 m/s (3.13 mph)
- [M-0523](../rules/weapons.md#m-0523) 매개변수 `duration_s`: 600
- [M-0523](../rules/weapons.md#m-0523) 매개변수 `interval_s`: 2
- [M-0523](../rules/weapons.md#m-0523) 매개변수 `damage_hp`: 1
- [M-0523](../rules/weapons.md#m-0523) 매개변수 `radius_m`: 10
- [M-0523](../rules/weapons.md#m-0523) 매개변수 `speed_mps`: 1.4
- [M-0523](../rules/weapons.md#m-0523) 매개변수 `clock`: UNKNOWN, see [U-0527](../unknowns.md#u-0527)

**따름 결과:** [T-0305](../theorems/T-0305.md)

**상호작용:** [M-0522](../rules/items.md#m-0522), [M-0524](../rules/damage.md#m-0524)

**미해결 질문:**

- [U-0527](../unknowns.md#u-0527) (보통): Robot이 "10m 이내의 다른 플레이어에게 2s마다 1 HP 피해"를 줍니다. 2 s 시계는 전역입니까 대상별입니까, 그리고 첫 타격은 즉시 들어갑니까 한 간격 뒤에 들어갑니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, robot, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?

**모순:** [C-0500](../unknowns.md#c-0500)

메모 ([M-0523](../rules/weapons.md#m-0523)): 'other players'에는 소유자가 제외됩니다. robot은 피해 표(다른 페이지)의 출처이며, 그 피해가 7단계 타격 파이프라인을 거치는지는 [U-0002](../unknowns.md#u-0002)입니다. 상인 아이템으로 참가자가 robot에 목표를 줄 수 있습니다 (아이템 페이지). 차단 수단은 [M-0524](../rules/damage.md#m-0524)에 있습니다.

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0001](../theorems/T-0001.md), [T-0305](../theorems/T-0305.md)

## 미해결 질문

[U-0002](../unknowns.md#u-0002), [U-0006](../unknowns.md#u-0006), [U-0010](../unknowns.md#u-0010), [U-0015](../unknowns.md#u-0015), [U-0300](../unknowns.md#u-0300), [U-0301](../unknowns.md#u-0301), [U-0302](../unknowns.md#u-0302), [U-0303](../unknowns.md#u-0303), [U-0304](../unknowns.md#u-0304), [U-0305](../unknowns.md#u-0305), [U-0306](../unknowns.md#u-0306), [U-0307](../unknowns.md#u-0307), [U-0308](../unknowns.md#u-0308), [U-0309](../unknowns.md#u-0309), [U-0310](../unknowns.md#u-0310), [U-0311](../unknowns.md#u-0311), [U-0312](../unknowns.md#u-0312), [U-0313](../unknowns.md#u-0313), [U-0314](../unknowns.md#u-0314), [U-0315](../unknowns.md#u-0315), [U-0316](../unknowns.md#u-0316), [U-0317](../unknowns.md#u-0317), [U-0318](../unknowns.md#u-0318), [U-0332](../unknowns.md#u-0332), [U-0333](../unknowns.md#u-0333), [U-0334](../unknowns.md#u-0334), [U-0335](../unknowns.md#u-0335), [U-0336](../unknowns.md#u-0336), [U-0337](../unknowns.md#u-0337), [U-0527](../unknowns.md#u-0527)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
