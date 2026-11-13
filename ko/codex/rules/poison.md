# 규칙: 독(poison)

## 요약

`poison` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

독은 게임에서 서서히 괴롭히는 피해입니다. 큰 한 방이 아니라 무언가가 멈출 때까지 계속 흘러가는 시계입니다. 이 계열은 어떻게 중독되는지, 어떻게 피해를 주는지, 무엇이 그것을 끝내는지를 설명합니다.

중독되는 방법: Poison dart나 Fake gravestone에 의해 중독될 수 있으며, 그 외에는 없습니다 ([M-0173](../rules/poison.md#m-0173)). 중독되면 1분 30초마다 1 HP를 잃습니다 ([M-0170](../rules/poison.md#m-0170)). 다시 중독되면 타이머가 초기화되며 중첩되지 않습니다 ([M-0171](../rules/poison.md#m-0171)). 독은 모든 피해를 다 주었거나 치료되었을 때만 끝납니다 ([M-0172](../rules/poison.md#m-0172)). 따라서 치료하지 않은 독은 천천히 치르는 고정된 총 청구액입니다 ([M-0172](../rules/poison.md#m-0172)).

막는 방법: 독은 Anti poison, Healing의 회복, God's Fruit로 치료할 수 있습니다 ([M-0174](../rules/poison.md#m-0174)). Anti poison은 독을 치료하고 10분 동안 독에 면역이 되게 합니다 ([M-0221](../rules/poison.md#m-0221)). 다른 보호 수단은 독이 들어오기 전에 작동합니다. Reality Shield는 그 안에 서 있는 동안 새 독을 막고 ([M-0177](../rules/poison.md#m-0177)), Protection 시길은 완전히 면역입니다 ([M-0175](../rules/poison.md#m-0175)). Mirror forcefield는 Poison Dart나 Fake gravestone을 공격자에게 되돌립니다 ([M-0180](../rules/poison.md#m-0180)). Shield나 Safety bubble은 다르게 작동합니다. 독이 들어오는 것은 막지 않지만, 지속되는 동안 각 독 단계를 차단합니다 ([M-0136](../rules/poison.md#m-0136), [M-0179](../rules/poison.md#m-0179)).

플레이어가 느끼는 점: 90초마다 1 HP가 서서히 줄어들며 ([M-0170](../rules/poison.md#m-0170)), 총량이 다 치러지거나 치료가 들어올 때까지 이어집니다 ([M-0172](../rules/poison.md#m-0172)). 독에 효과적인 수단: 깔끔한 해결에는 Anti poison ([M-0221](../rules/poison.md#m-0221)), 영구적인 안전에는 Protection ([M-0175](../rules/poison.md#m-0175)), 되돌려 보내는 데에는 Mirror ([M-0180](../rules/poison.md#m-0180))입니다.

규칙에 적힌 대로 독 자체의 가장 약한 점: 느리고 ([M-0170](../rules/poison.md#m-0170)), 중첩되지 않으며 ([M-0171](../rules/poison.md#m-0171)), 알려진 대응 수단이 여러 개 있습니다 ([M-0174](../rules/poison.md#m-0174)).

알 수 없는 것: 첫 1 HP가 즉시 들어오는지 첫 간격 이후에 들어오는지 ([U-0115](../unknowns.md#u-0115))입니다. 두 번째 중독이 카운트다운만 다시 시작하는지 앞으로 남은 피해도 다시 채우는지는 미해결입니다 ([U-0116](../unknowns.md#u-0116)). Shield나 Safety bubble에 막힌 단계가 준 피해로 치는지 독을 지연시킬 뿐인지도 미해결입니다 ([U-0117](../unknowns.md#u-0117)). 자신의 Sleeping Bag에서 자면 새 독을 막는지, 틱을 막는지, 둘 다인지도 미해결입니다 ([U-0118](../unknowns.md#u-0118)). 반사된 독이 공격자 자신의 보호를 통과하는지도 미해결입니다 ([U-0005](../unknowns.md#u-0005)).

이 페이지는 규칙 13개(6 `DOCUMENTED`, 7 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0136"></a>

### M-0136: Shield나 Safety bubble은 착탄이 아니라 각 독 단계를 막음

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0136](../rules/poison.md#m-0136) `wiki-damage-056`: "A Shield or a Safety Bubble does not stop poison from landing, but blocks each poison step while it lasts." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Shield나 Safety Bubble은 독이 걸리는 것을 막지 못하지만, 지속되는 동안 각 독 단계를 막습니다.

**형식 모델:**

- [M-0136](../rules/poison.md#m-0136) 해석 A: `타격 시 poisoned := true; Shield나 Safety bubble이 활성인 동안 각 독 틱은 차단됨`

**상호작용:** [M-0179](../rules/poison.md#m-0179)

**미해결 질문:**

- [U-0117](../unknowns.md#u-0117) (높음): Shield 또는 Safety bubble은 'blocks each poison step while it lasts': 막힌 단계는 소모됩니까('all its damage'에 산입), 아니면 건너뜁니까(독이 연장)? 보호받는 동안 카운트다운은 계속됩니까?

메모 ([M-0136](../rules/poison.md#m-0136)): Poison 페이지의 면역 설명과 같습니다 ([M-0179](../rules/poison.md#m-0179)).

<a id="m-0170"></a>

### M-0170: 독 틱: 1min 30s마다 1 HP

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0170](../rules/poison.md#m-0170) `wiki-poison-001`: "Poison damages you for 1 HP every 1min 30s." ([출처](https://iceposeidon.com/safezone/wiki/poison))
  - 번역: 독은 1min 30s마다 1 HP의 피해를 줍니다.

**형식 모델:**

- [M-0170](../rules/poison.md#m-0170) 해석 A: `중독 상태 동안: t_p = 90, 180, ...에서 HP 1 감소`
- [M-0170](../rules/poison.md#m-0170) 해석 B: `첫 감소는 t_p = 0에서 발생`
- [M-0170](../rules/poison.md#m-0170) 정의역: 중독 이후 경과한 초 t_p
- [M-0170](../rules/poison.md#m-0170) 매개변수 `tick_hp`: 1
- [M-0170](../rules/poison.md#m-0170) 매개변수 `interval_s`: 90

**따름 결과:** [T-0304](../theorems/T-0304.md), [T-0305](../theorems/T-0305.md)

**미해결 질문:**

- [U-0115](../unknowns.md#u-0115) (보통): 독: 첫 1 HP가 즉시 들어갑니까, 1min 30s 뒤입니까, 아니면 고정된 전역 90 s 위상입니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?

메모 ([M-0170](../rules/poison.md#m-0170)): 30 min당 20 HP에 해당하며, Poison Dart가 30min 동안 20 HP만큼 중독시킨다는 다른 페이지와 일치합니다(이후의 유도 대상이며 여기서는 단정하지 않습니다). 1 HP에서는 Kick 감소가 의미가 없습니다(독이 타격일 때만 최소 1, [U-0002](../unknowns.md#u-0002)).

<a id="m-0171"></a>

### M-0171: 다시 중독되면 타이머가 초기화되며 중첩되지 않음

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0171](../rules/poison.md#m-0171) `wiki-poison-002`: "Getting poisoned again resets the timer, it doesn't stack." ([출처](https://iceposeidon.com/safezone/wiki/poison))
  - 번역: 다시 중독되면 타이머가 초기화되며, 중첩되지 않습니다.

**형식 모델:**

- [M-0171](../rules/poison.md#m-0171) 해석 A: `다시 중독: countdown := 90 s; damage_remaining은 변하지 않음`
- [M-0171](../rules/poison.md#m-0171) 해석 B: `countdown := 90 s 및 damage_remaining := total`
- [M-0171](../rules/poison.md#m-0171) 매개변수 `total_hp`: UNKNOWN, [U-0116](../unknowns.md#u-0116) 참조

**따름 결과:** [T-0009](../theorems/T-0009.md)

**미해결 질문:**

- [U-0116](../unknowns.md#u-0116) (높음): 독 'Getting poisoned again resets the timer, it doesn't stack': 초기화는 90 s 카운트다운만 다시 시작합니까, 아니면 아직 가해질 남은 총 피해도 복원합니까? 총량은 얼마입니까?

<a id="m-0172"></a>

### M-0172: 독은 모든 피해를 입히거나 치료되면 끝남

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0172](../rules/poison.md#m-0172) `wiki-poison-003`: "Poison ends only when it has done all its damage, or if it is cured." ([출처](https://iceposeidon.com/safezone/wiki/poison))
  - 번역: 독은 모든 피해를 입혔거나 치료된 경우에만 끝납니다.

**형식 모델:**

- [M-0172](../rules/poison.md#m-0172) 해석 A: `damage_dealt = total 또는 치료 이벤트일 때, 그리고 그때에만 poisoned := false`
- [M-0172](../rules/poison.md#m-0172) 매개변수 `total_hp`: UNKNOWN, [U-0116](../unknowns.md#u-0116) 참조

**미해결 질문:**

- [U-0116](../unknowns.md#u-0116) (높음): 독 'Getting poisoned again resets the timer, it doesn't stack': 초기화는 90 s 카운트다운만 다시 시작합니까, 아니면 아직 가해질 남은 총 피해도 복원합니까? 총량은 얼마입니까?
- [U-0117](../unknowns.md#u-0117) (높음): Shield 또는 Safety bubble은 'blocks each poison step while it lasts': 막힌 단계는 소모됩니까('all its damage'에 산입), 아니면 건너뜁니까(독이 연장)? 보호받는 동안 카운트다운은 계속됩니까?

메모 ([M-0172](../rules/poison.md#m-0172)): 차단된 틱이 입힌 피해로 계산되는지는 [U-0117](../unknowns.md#u-0117)에서 다룹니다.

<a id="m-0173"></a>

### M-0173: 독의 원천: Poison dart와 Fake gravestone

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0173](../rules/poison.md#m-0173) `wiki-poison-004`: "You can be poisoned by a Poison dart or a Fake gravestone." ([출처](https://iceposeidon.com/safezone/wiki/poison))
  - 번역: Poison dart 또는 Fake gravestone에 의해 중독될 수 있습니다.

**형식 모델:**

- [M-0173](../rules/poison.md#m-0173) 해석 A: `독 이벤트는 정확히 두 원천에서 발생: Poison dart, Fake gravestone`

메모 ([M-0173](../rules/poison.md#m-0173)): 다른 페이지에는 효과 존이나 다른 아이템이 중독시킬 수 있다고 되어 있지만, 이 페이지는 이 둘만 나열합니다('can be poisoned by').

<a id="m-0174"></a>

### M-0174: 독의 치료: Anti poison, Healing 회복, God's Fruit

라벨: `DOCUMENTED`. 시길: healing.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0174](../rules/poison.md#m-0174) `wiki-poison-005`: "Poison can be cured by: Anti poison, Healing healing, or God's Fruit" ([출처](https://iceposeidon.com/safezone/wiki/poison))
  - 번역: 독은 다음으로 치료할 수 있습니다: Anti poison, Healing 회복(Healing healing), 또는 God's Fruit

**형식 모델:**

- [M-0174](../rules/poison.md#m-0174) 해석 A: `치료 이벤트: Anti poison, Healing 참가자의 회복, God's Fruit`

메모 ([M-0174](../rules/poison.md#m-0174)): 귀속은 원문에 적힌 그대로 유지했습니다: 'Healing healing'은 Healing 시길에 의한 회복을 뜻합니다.

<a id="m-0175"></a>

### M-0175: Protection 시길은 독에 완전 면역

라벨: `DOCUMENTED`. 시길: protection.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0175](../rules/poison.md#m-0175) `wiki-poison-006`: "Protection sigil: fully immune" ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: Protection 시길: 완전 면역

**형식 모델:**

- [M-0175](../rules/poison.md#m-0175) 해석 A: `sigil = Protection: poisoned는 결코 true가 되지 않음`

메모 ([M-0175](../rules/poison.md#m-0175)): 피해 표의 Poison 행에 Protection이 나열되어 있어 일치합니다.

<a id="m-0176"></a>

### M-0176: Anti poison: 지속되는 동안 새 독 없음

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0176](../rules/poison.md#m-0176) `wiki-poison-007`: "Anti poison: no new poison while it lasts." ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: Anti poison: 지속되는 동안 새로운 독이 걸리지 않습니다.

**형식 모델:**

- [M-0176](../rules/poison.md#m-0176) 해석 A: `Anti poison 활성 동안: 새 독 이벤트는 무시됨; 기존 독은 이 조항의 영향을 받지 않음`

메모 ([M-0176](../rules/poison.md#m-0176)): 치료와 면역: 아이템 페이지에는 Anti poison이 독을 치료하고 10 min의 면역을 준다고 되어 있습니다. 이 페이지는 치료를 따로 나열합니다([M-0174](../rules/poison.md#m-0174)). 지속 시간은 아이템 페이지에 있습니다.

<a id="m-0177"></a>

### M-0177: Reality Shield: 내부에 서 있는 동안 새 독 없음

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0177](../rules/poison.md#m-0177) `wiki-poison-008`: "Reality Shield: no new poison while you stand inside it." ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: Reality Shield: 그 안에 서 있는 동안 새로운 독이 걸리지 않습니다.

**형식 모델:**

- [M-0177](../rules/poison.md#m-0177) 해석 A: `Reality Shield 내부 위치: 새 독 이벤트는 무시됨`

<a id="m-0178"></a>

### M-0178: 자신의 Sleeping Bag에서 잠자기(독 면역 목록)

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0178](../rules/poison.md#m-0178) `wiki-poison-009`: "Sleeping in your own Sleeping Bag" ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: 자신의 Sleeping Bag에서 잠자기

**형식 모델:**

- [M-0178](../rules/poison.md#m-0178) 해석 A: `자신의 Sleeping Bag(own bag)에서 수면 중: 새 독 없음`
- [M-0178](../rules/poison.md#m-0178) 해석 B: `자신의 Sleeping Bag(own bag)에서 수면 중: 독 틱이 차단됨`
- [M-0178](../rules/poison.md#m-0178) 해석 C: `둘 다`

**미해결 질문:**

- [U-0118](../unknowns.md#u-0118) (낮음): 'Sleeping in your own Sleeping Bag'은 Poison 면역 목록에 동사 없이 라벨로만 나옵니다: 새 독을 막습니까, 각 단계를 막습니까, 둘 다입니까?

메모 ([M-0178](../rules/poison.md#m-0178)): 스냅샷에는 동사 없이 항목명만 있습니다.

<a id="m-0179"></a>

### M-0179: Shield 또는 Safety bubble은 중독을 막지 않지만 독 피해는 차단함

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0179](../rules/poison.md#m-0179) `wiki-poison-010`: "A Shield or a Safety bubble does not stop you from being poisoned, but blocks the poison damage" ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: Shield 또는 Safety bubble은 중독 자체를 막지는 않지만, 독 피해는 차단합니다.

**형식 모델:**

- [M-0179](../rules/poison.md#m-0179) 해석 A: `독 이벤트는 수용됨; Shield 또는 Safety bubble이 활성인 동안 틱이 차단됨`

**상호작용:** [M-0136](../rules/poison.md#m-0136)

**미해결 질문:**

- [U-0117](../unknowns.md#u-0117) (높음): Shield 또는 Safety bubble은 'blocks each poison step while it lasts': 막힌 단계는 소모됩니까('all its damage'에 산입), 아니면 건너뜁니까(독이 연장)? 보호받는 동안 카운트다운은 계속됩니까?

메모 ([M-0179](../rules/poison.md#m-0179)): 피해 페이지의 메모([M-0136](../rules/poison.md#m-0136))와 동일하며, 불일치는 발견되지 않았습니다.

<a id="m-0180"></a>

### M-0180: Mirror forcefield가 Poison Dart 또는 Fake gravestone을 공격자에게 되돌림

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0180](../rules/poison.md#m-0180) `wiki-poison-011`: "A Mirror forcefield turns a Poison Dart or a fake gravestone back on the attacker." ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: Mirror forcefield는 Poison Dart 또는 fake gravestone을 공격자에게 되돌립니다.

**형식 모델:**

- [M-0180](../rules/poison.md#m-0180) 해석 A: `방어자의 mirror가 활성 상태이고 source in {Poison Dart, fake gravestone}: 공격자가 중독되고 방어자는 중독되지 않음`

**상호작용:** [M-0120](../rules/damage.md#m-0120), [M-0135](../rules/damage.md#m-0135)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0180](../rules/poison.md#m-0180)): 아이템 페이지에는 mirror를 가진 공격자를 상대로 하면 다트가 여전히 공격자를 중독시키고 그 mirror는 남는다고 덧붙여 있습니다. 중복 기록하지 않았습니다.

<a id="m-0221"></a>

### M-0221: Anti poison

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0221](../rules/poison.md#m-0221) `wiki-items-033`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#anti_poison))
  - 번역: 사용 가능
- [M-0221](../rules/poison.md#m-0221) `wiki-items-034`: "Cures poison and makes you immune to it for 10min." ([출처](https://iceposeidon.com/safezone/wiki/items#anti_poison))
  - 번역: 독을 치료하고 10min 동안 독에 면역이 됩니다.
- [M-0221](../rules/poison.md#m-0221) `wiki-poison-007`: "Anti poison: no new poison while it lasts." ([출처](https://iceposeidon.com/safezone/wiki/poison#immunity))
  - 번역: Anti poison: 지속되는 동안 새로운 독이 걸리지 않습니다.

**형식 모델:**

- [M-0221](../rules/poison.md#m-0221) 해석 A: `사용 시: 현재 독이 치료됨. 10min 동안 새로운 독이 적용될 수 없음`
- [M-0221](../rules/poison.md#m-0221) 정의역: t in [0, 600)초
- [M-0221](../rules/poison.md#m-0221) 매개변수 `duration`: 10min

**상호작용:** [M-0205](../rules/items.md#m-0205)

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0009](../theorems/T-0009.md), [T-0304](../theorems/T-0304.md), [T-0305](../theorems/T-0305.md)

## 미해결 질문

[U-0002](../unknowns.md#u-0002), [U-0005](../unknowns.md#u-0005), [U-0115](../unknowns.md#u-0115), [U-0116](../unknowns.md#u-0116), [U-0117](../unknowns.md#u-0117), [U-0118](../unknowns.md#u-0118)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
