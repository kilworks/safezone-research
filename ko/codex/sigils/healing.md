# Healing(치유) 시길

## 요약

Healing(치유) 시길을 언급하는 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

Healing은 "의무병" 계열입니다. 수치는 평범한 편으로 최대 HP 100과 인벤토리 슬롯 3개이며 ([M-0606](../rules/sigil.md#m-0606)), 하는 일은 사람들을 살려 두는 것, 되살려 내는 것까지 포함합니다.

일상적인 도구는 회복 능력입니다. 근처의 참가자를 1 HP 회복시키고 독을 치료하며, Deep Cut 출혈도 멈추고, 쿨다운은 10분입니다 ([M-0651](../rules/healing.md#m-0651)). 독은 Anti poison, Healing의 회복, 또는 God's Fruit으로 치료할 수 있으므로, Healing 플레이어는 독에 대한 세 가지 해법 중 하나입니다 ([M-0174](../rules/poison.md#m-0174)). 또한 30분마다 1 HP씩 최대 HP까지 자연 회복합니다 ([M-0652](../rules/healing.md#m-0652)). 이 느린 자연 회복은 Healing 고유의 것이며 다른 시길의 능력이 아님에 유의하십시오 ([M-0652](../rules/healing.md#m-0652)).

큰 도구는 부활입니다. Healing 참가자는 어떤 시길의 참가자든 부활시킬 수 있으며, 최대 10번까지입니다 ([M-0654](../rules/revival.md#m-0654)). 부활은 사망 후 10분 이내에 이루어져야 하고 ([M-0655](../rules/revival.md#m-0655)), 부활시키는 쪽이 5 HP를 소모하며, 되살아난 참가자는 5 HP로 돌아옵니다 ([M-0656](../rules/revival.md#m-0656)). Healing 플레이어 자신도 더 쉽게 되살아납니다. 당신의 묘비로부터 10 m (33 ft) 이내에 있는 살아 있는 참가자라면 누구든 당신을 최대 2번 부활시킬 수 있습니다 ([M-0653](../rules/revival.md#m-0653)).

수입은 작지만 꾸준합니다. 회복 1번마다 블러드 토큰 1개, 부활 1번마다 20개입니다 ([M-0650](../rules/economy.md#m-0650)). 그래서 Healing 플레이어는 수입 대부분을 부활에서 얻습니다 ([M-0650](../rules/economy.md#m-0650)).

플레이어가 느낄 것은 인내심이 필요한 역할이라는 점입니다. 회복은 작고 느리므로 ([M-0651](../rules/healing.md#m-0651)), 이 시길의 무게는 부활 ([M-0654](../rules/revival.md#m-0654))과 독 치료 ([M-0174](../rules/poison.md#m-0174))에 놓입니다. 기록된 바로는 가장 강한 점은 어떤 시길이든 부활시킬 수 있다는 것 ([M-0654](../rules/revival.md#m-0654)), 그리고 독과 출혈 치료입니다 ([M-0651](../rules/healing.md#m-0651)). 가장 약한 점은 회복이 1 HP이고 쿨다운이 10분이라는 것 ([M-0651](../rules/healing.md#m-0651)), 그리고 부활에 HP가 든다는 것입니다 ([M-0656](../rules/revival.md#m-0656)).

알려지지 않은 것은 다음과 같습니다. 회복의 사거리 ([U-0622](../unknowns.md#u-0622)), 그리고 자기 자신이나 HP가 가득 찬 대상을 지정할 수 있는지, 그때도 쿨다운이 소모되는지 ([U-0623](../unknowns.md#u-0623))가 있습니다. 부활 횟수 카운터가 무엇에 붙는지, 곧 이벤트인지, 쌍인지, 대상인지 ([U-0107](../unknowns.md#u-0107), [U-0624](../unknowns.md#u-0624)), 그리고 Healing이 아닌 참가자를 누가 부활시킬 수 있는지 ([U-0108](../unknowns.md#u-0108))는 미해결입니다. 누구의 죽음이 10분 창을 시작하는지 ([U-0011](../unknowns.md#u-0011)), 5 HP 비용으로 자신이 죽을 수 있는지 ([U-0625](../unknowns.md#u-0625))도 미해결입니다. 피해를 입으면 자연 회복 타이머가 초기화되는지도 미해결입니다 ([U-0007](../unknowns.md#u-0007)).

이 페이지는 규칙 11개(2 `DOCUMENTED`, 9 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0112"></a>

### M-0112: 어떤 참가자든 Healing 참가자를 최대 2회까지 부활시킬 수 있음

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0112](../rules/revival.md#m-0112) `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 어떤 참가자든 Healing 참가자를 최대 2회까지 부활시킬 수 있습니다.

**형식 모델:**

- [M-0112](../rules/revival.md#m-0112) 해석 A: `각 Healing 참가자 h에 대해 revives_received(h) <= 2`
- [M-0112](../rules/revival.md#m-0112) 해석 B: `상한은 부활시키는 쪽과 대상의 쌍마다 따로 셈`
- [M-0112](../rules/revival.md#m-0112) 정의역: Healing 참가자 h
- [M-0112](../rules/revival.md#m-0112) 매개변수 `max_revives_received`: 2

**미해결 질문:**

- [U-0107](../unknowns.md#u-0107) (높음): 부활 횟수 제한 '2 times'(Healing 참가자에게)와 '10 times'(Healing 참가자에 의한)는 무엇에 붙는 카운터입니까?
- [U-0108](../unknowns.md#u-0108) (보통): 비Healing 참가자는 누가 부활시킬 수 있습니까? 두 규칙에서 암시되는 대로 Healing 참가자만입니까, 아니면 다른 규칙에 따라 누구든 가능합니까?

**모순:** [C-0105](../unknowns.md#c-0105)

메모 ([M-0112](../rules/revival.md#m-0112)): Healing 페이지는 '당신의 묘비로부터 10m 이내의 살아 있는 참가자'를 덧붙이고 '... 최대 10회까지 부활시킬 수 있다'고 합니다. [C-0104](../unknowns.md#c-0104)를 참조하십시오. 시길별 세부 사항은 비교만 하고 중복 기록하지 않았습니다.

<a id="m-0113"></a>

### M-0113: Healing 참가자는 어떤 시길이든 최대 10회까지 부활시킬 수 있음

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0113](../rules/revival.md#m-0113) `wiki-016`: "A Healing contestant can revive a contestant of any sigil, up to 10 times." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: Healing 참가자는 어떤 시길의 참가자든 최대 10회까지 부활시킬 수 있습니다.

**형식 모델:**

- [M-0113](../rules/revival.md#m-0113) 해석 A: `각 Healing 참가자 h에 대해 revives_performed(h) <= 10`
- [M-0113](../rules/revival.md#m-0113) 해석 B: `상한은 대상마다 따로 셈`
- [M-0113](../rules/revival.md#m-0113) 해석 C: `대상이 Healing이면 2회 상한([M-0112](../rules/revival.md#m-0112))이 우선 적용됨`
- [M-0113](../rules/revival.md#m-0113) 매개변수 `max_revives_performed`: 10

**상호작용:** [M-0112](../rules/revival.md#m-0112)

**미해결 질문:**

- [U-0107](../unknowns.md#u-0107) (높음): 부활 횟수 제한 '2 times'(Healing 참가자에게)와 '10 times'(Healing 참가자에 의한)는 무엇에 붙는 카운터입니까?
- [U-0108](../unknowns.md#u-0108) (보통): 비Healing 참가자는 누가 부활시킬 수 있습니까? 두 규칙에서 암시되는 대로 Healing 참가자만입니까, 아니면 다른 규칙에 따라 누구든 가능합니까?

<a id="m-0174"></a>

### M-0174: 독의 치료: Anti poison, Healing 회복, God's Fruit

라벨: `DOCUMENTED`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0174](../rules/poison.md#m-0174) `wiki-poison-005`: "Poison can be cured by: Anti poison, Healing healing, or God's Fruit" ([출처](https://iceposeidon.com/safezone/wiki/poison))
  - 번역: 독은 다음으로 치료할 수 있습니다: Anti poison, Healing 회복(Healing healing), 또는 God's Fruit

**형식 모델:**

- [M-0174](../rules/poison.md#m-0174) 해석 A: `치료 이벤트: Anti poison, Healing 참가자의 회복, God's Fruit`

메모 ([M-0174](../rules/poison.md#m-0174)): 귀속은 원문에 적힌 그대로 유지했습니다: 'Healing healing'은 Healing 시길에 의한 회복을 뜻합니다.

<a id="m-0606"></a>

### M-0606: Healing 기본 능력치: 최대 HP 100, 인벤토리 슬롯 3

라벨: `DOCUMENTED`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-002`: "Max HP" ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing))
  - 번역: Max HP
- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-003`: "100 HP" ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing))
  - 번역: 100 HP
- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-004`: "Slots" ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing))
  - 번역: Slots
- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-005`: "3" ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing))
  - 번역: 3

**형식 모델:**

- [M-0606](../rules/sigil.md#m-0606) 해석 A: `maxHP = 100. inventory_slots = 3`
- [M-0606](../rules/sigil.md#m-0606) 정의역: 이벤트 시작 시점
- [M-0606](../rules/sigil.md#m-0606) 매개변수 `max_hp`: 100
- [M-0606](../rules/sigil.md#m-0606) 매개변수 `inventory_slots`: 3

**따름 결과:** [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

메모 ([M-0606](../rules/sigil.md#m-0606)): 상인의 업그레이드(최대 HP +10, 인벤토리 슬롯)는 플레이 중에 이 값을 바꿉니다. 이 기록은 기본값만 다룹니다. 상인 페이지는 슬롯을 13개까지로 제한하며, Endurance는 20개까지입니다.

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

<a id="m-0651"></a>

### M-0651: Healing 능력: 1 HP 회복, 독 치료, 출혈 중단, 쿨다운 10min

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0651](../rules/healing.md#m-0651) `wiki-sigils-healing-008`: "Heal a nearby contestant for 1 HP and cure their poison." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 근처의 참가자를 1 HP 회복시키고 그 독을 치료합니다.
- [M-0651](../rules/healing.md#m-0651) `wiki-sigils-healing-007`: "Healing also stops Deep Cut bleeding." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: Healing은 Deep Cut 출혈도 멈춥니다.
- [M-0651](../rules/healing.md#m-0651) `wiki-sigils-healing-009`: "Cooldown 10min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 쿨다운 10min.

**형식 모델:**

- [M-0651](../rules/healing.md#m-0651) 해석 A: `범위 r 안의 대상: HP += 1 (최대 HP가 상한), 독 치료, Deep Cut 출혈 중단. 다음 사용은 600 s 후`
- [M-0651](../rules/healing.md#m-0651) 정의역: 초, HP
- [M-0651](../rules/healing.md#m-0651) 매개변수 `heal_hp`: 1
- [M-0651](../rules/healing.md#m-0651) 매개변수 `cooldown_s`: 600
- [M-0651](../rules/healing.md#m-0651) 매개변수 `range_m`: UNKNOWN, [U-0622](../unknowns.md#u-0622) 참조

**따름 결과:** [T-0305](../theorems/T-0305.md)

**미해결 질문:**

- [U-0622](../unknowns.md#u-0622) (보통): Healing 능력 "Heal a nearby contestant": 범위는 얼마입니까?
- [U-0623](../unknowns.md#u-0623) (보통): Healing 능력: 회복자 자신, 이미 HP가 가득 찬 대상, 중독되지 않은 대상을 대상으로 삼을 수 있습니까? 쿨다운과 토큰은 그래도 소모됩니까?

메모 ([M-0651](../rules/healing.md#m-0651)): 독 페이지('Healing healing'이 독을 치료함)와 상인의 Deep Cut 설명(붕대 또는 Healing 참가자가 치료)과 일치합니다.

<a id="m-0652"></a>

### M-0652: Healing 자연 재생: 30min마다 1 HP

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0652](../rules/healing.md#m-0652) `wiki-sigils-healing-010`: "You regenerate 1 HP every 30min, up to your max HP." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 30min마다 1 HP를 재생하며, 최대 HP까지입니다.

**형식 모델:**

- [M-0652](../rules/healing.md#m-0652) 해석 A: `고정된 시계로 1800 s마다, 피해를 입어도 초기화되지 않음`
- [M-0652](../rules/healing.md#m-0652) 해석 B: `피해를 입으면 1800 s 타이머가 초기화됨`
- [M-0652](../rules/healing.md#m-0652) 정의역: 초
- [M-0652](../rules/healing.md#m-0652) 매개변수 `regen_hp`: 1
- [M-0652](../rules/healing.md#m-0652) 매개변수 `period_s`: 1800

**따름 결과:** [T-0011](../theorems/T-0011.md), [T-0305](../theorems/T-0305.md)

**미해결 질문:**

- [U-0007](../unknowns.md#u-0007) (보통): Healing 재생: 피해가 30 min 타이머를 초기화합니까?

메모 ([M-0652](../rules/healing.md#m-0652)): Necromancy가 아니라 Healing에 속합니다. 시계의 시작 시점(이벤트 시작인지, 시길 선택인지)도 미해결입니다.

<a id="m-0653"></a>

### M-0653: Healing 참가자는 어떤 참가자에게든 최대 2회 부활될 수 있음

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0653](../rules/revival.md#m-0653) `wiki-sigils-healing-011`: "Any living contestant within 10m (33ft) of your gravestone can revive you, up to 2 times." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 당신의 묘비로부터 10m (33ft) 이내에 있는 생존 중인 참가자는 누구든 당신을 최대 2회까지 부활시킬 수 있습니다.
- [M-0653](../rules/revival.md#m-0653) `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 어떤 참가자든 Healing 참가자를 최대 2회까지 부활시킬 수 있습니다.
- [M-0653](../rules/revival.md#m-0653) `wiki-strategy-014`: "Death is not always the end, a Healing contestant could revive you." ([출처](https://iceposeidon.com/safezone/wiki/strategy#death))
  - 번역: 죽음이 항상 끝은 아닙니다. Healing 참가자가 당신을 부활시킬 수도 있습니다.

**형식 모델:**

- [M-0653](../rules/revival.md#m-0653) 해석 A: `부활시키는 사람이 생존 중이고, g로부터 10 m 이내에 있으며, revives_of(target) < 2일 때 revive(g) 허용`
- [M-0653](../rules/revival.md#m-0653) 해석 B: `제한을 부활시키는 사람별로 셈`
- [M-0653](../rules/revival.md#m-0653) 매개변수 `max_revives_of_healing`: 2
- [M-0653](../rules/revival.md#m-0653) 매개변수 `range_m`: 10

**미해결 질문:**

- [U-0624](../unknowns.md#u-0624) (높음): Healing 부활 카운터: "2 times"(부활되는 Healing 참가자)와 "10 times"(부활시키는 Healing 참가자): 이벤트당입니까, 쌍당입니까, 그리고 취소되거나 실패한 부활도 셉니까?
- [U-0011](../unknowns.md#u-0011) (보통): 부활 제한 시간: 소개 페이지의 'within 10min of their death'와 Healing 페이지의 'within 10min of the death' 중, 누구의 사망이 제한 시간을 시작시킵니까?

메모 ([M-0653](../rules/revival.md#m-0653)): 전략 페이지의 문장은 Healing 참가자만 부활시키는 사람으로 언급하며, 다른 경로는 언급하지 않습니다.

<a id="m-0654"></a>

### M-0654: Healing 참가자는 어떤 시길이든 최대 10회 부활시킴

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0654](../rules/revival.md#m-0654) `wiki-sigils-healing-012`: "You can revive a contestant of any sigil, up to 10 times." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 어떤 시길의 참가자든 최대 10회까지 부활시킬 수 있습니다.
- [M-0654](../rules/revival.md#m-0654) `wiki-016`: "A Healing contestant can revive a contestant of any sigil, up to 10 times." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: Healing 참가자는 어떤 시길의 참가자든 최대 10회까지 부활시킬 수 있습니다.

**형식 모델:**

- [M-0654](../rules/revival.md#m-0654) 해석 A: `Healing 참가자 h마다 revives_by(h) < 10, 성공한 부활 기준`
- [M-0654](../rules/revival.md#m-0654) 매개변수 `max_revives_by`: 10
- [M-0654](../rules/revival.md#m-0654) 매개변수 `range_m`: UNKNOWN, [U-0626](../unknowns.md#u-0626) 참조

**미해결 질문:**

- [U-0624](../unknowns.md#u-0624) (높음): Healing 부활 카운터: "2 times"(부활되는 Healing 참가자)와 "10 times"(부활시키는 Healing 참가자): 이벤트당입니까, 쌍당입니까, 그리고 취소되거나 실패한 부활도 셉니까?
- [U-0626](../unknowns.md#u-0626) (보통): Healing 참가자가 Healing이 아닌 참가자를 부활시키는 범위: Healing 페이지는 Healing 참가자가 부활되는 쪽일 때만 묘비로부터 10m를 제시합니다.

<a id="m-0655"></a>

### M-0655: 부활 가능 시간: 사망 후 10min

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0655](../rules/revival.md#m-0655) `wiki-sigils-healing-013`: "A revive must happen within 10min of the death." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 부활은 사망 후 10min 이내에 이루어져야 합니다.
- [M-0655](../rules/revival.md#m-0655) `wiki-008`: "revive you within 10min of their death." ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 그들의 사망 후 10min 이내에 당신을 부활시킵니다.

**형식 모델:**

- [M-0655](../rules/revival.md#m-0655) 해석 A: `t_now - t_death <= 600 s일 때에 한해 부활 허용, t_death는 사망한 참가자의 사망 시각`
- [M-0655](../rules/revival.md#m-0655) 해석 B: `t_death는 부활시키는 사람의 것`
- [M-0655](../rules/revival.md#m-0655) 정의역: 초
- [M-0655](../rules/revival.md#m-0655) 매개변수 `window_s`: 600

**미해결 질문:**

- [U-0011](../unknowns.md#u-0011) (보통): 부활 제한 시간: 소개 페이지의 'within 10min of their death'와 Healing 페이지의 'within 10min of the death' 중, 누구의 사망이 제한 시간을 시작시킵니까?

메모 ([M-0655](../rules/revival.md#m-0655)): 경계(<= 인지 < 인지)는 명시되어 있지 않습니다. wiki-012와 비교하십시오: 묘비 안의 블러드 토큰은 부활이 가능한 동안 잠겨 있습니다.

<a id="m-0656"></a>

### M-0656: 부활 비용 5 HP, 5 HP로 복귀

라벨: `CONDITIONAL`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0656](../rules/revival.md#m-0656) `wiki-sigils-healing-014`: "It costs the reviver 5 HP and brings the contestant back with 5 HP." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 부활시키는 사람은 5 HP를 소모하고, 참가자는 5 HP로 돌아옵니다.

**형식 모델:**

- [M-0656](../rules/revival.md#m-0656) 해석 A: `부활시키는 사람 HP -= 5 (HP > 5 필요), 대상 HP := 5`
- [M-0656](../rules/revival.md#m-0656) 해석 B: `부활시키는 사람이 0까지 떨어져 사망할 수 있음`
- [M-0656](../rules/revival.md#m-0656) 해석 C: `부활시키는 사람 HP -= min(5, HP-1)`
- [M-0656](../rules/revival.md#m-0656) 정의역: 정수 HP
- [M-0656](../rules/revival.md#m-0656) 매개변수 `cost_hp`: 5
- [M-0656](../rules/revival.md#m-0656) 매개변수 `revived_hp`: 5

**미해결 질문:**

- [U-0625](../unknowns.md#u-0625) (높음): 부활 비용 "costs the reviver 5 HP": HP가 5 이하인 부활자를 죽일 수 있습니까, 그리고 타격 파이프라인(방어구, Fortress, Kick 라이브)을 거칩니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, robot, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?

메모 ([M-0656](../rules/revival.md#m-0656)): 부활한 참가자는 묘비에서 아이템도 되찾습니다(소개 페이지). 비용이 피해 파이프라인을 거치는지는 [U-0002](../unknowns.md#u-0002)입니다.

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0011](../theorems/T-0011.md), [T-0305](../theorems/T-0305.md), [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

## 미해결 질문

[U-0002](../unknowns.md#u-0002), [U-0007](../unknowns.md#u-0007), [U-0011](../unknowns.md#u-0011), [U-0107](../unknowns.md#u-0107), [U-0108](../unknowns.md#u-0108), [U-0622](../unknowns.md#u-0622), [U-0623](../unknowns.md#u-0623), [U-0624](../unknowns.md#u-0624), [U-0625](../unknowns.md#u-0625), [U-0626](../unknowns.md#u-0626)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
