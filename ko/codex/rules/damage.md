# 규칙: 피해(damage)

## 요약

`damage` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

피해 계열은 한 가지 질문에 답합니다. 무언가가 나를 해칠 때 실제로 얼마나 들어오는가? 위키는 두 가지 도구를 제공합니다. 하나는 피해 출처별로 무엇이 그것을 막는지 나열한 표입니다. 다른 하나는 모든 타격이 순서대로 거치는 7단계 "타격 파이프라인(hit pipeline)"입니다 ([M-0117](../rules/damage.md#m-0117)).

각 단계는 대략 다음과 같습니다. 1단계는 면역입니다. 무엇이든 타격을 막으면 피해를 받지 않습니다 ([M-0118](../rules/damage.md#m-0118)). 2단계는 공격자의 Kick 보너스로, 공격자가 Kick 라이브 중이면 목록에 있는 무기의 피해가 10% 늘어나며 내림 처리됩니다 ([M-0119](../rules/damage.md#m-0119)). 3단계는 Mirror forcefield로, 타격 전체를 공격자에게 되돌려 보내며 ([M-0120](../rules/damage.md#m-0120)) 목록에 있는 출처만 반사합니다 ([M-0135](../rules/damage.md#m-0135)). 4단계는 감소 효과를 다룹니다. Protection 참가자는 핵으로부터 받는 피해가 50% 줄고 ([M-0121](../rules/damage.md#m-0121)), Kick 라이브 중인 참가자는 10%를 덜 받으며 내림 처리됩니다 ([M-0122](../rules/damage.md#m-0122)). 5단계는 통과한 타격이 최소 1 HP의 피해를 준다고 규정합니다 ([M-0123](../rules/damage.md#m-0123)). 6단계는 Fortress로, 남은 내구도만큼 흡수합니다 ([M-0124](../rules/damage.md#m-0124)). 7단계는 Body armor로, 부서질 때까지 남은 피해를 흡수합니다 ([M-0125](../rules/damage.md#m-0125)).

실제로는 플레이어가 여러 겹으로 보호받습니다. Shield는 존 피해, 언세이프 서클(unsafe circle) 피해, Robot 피해를 막지 못하지만, Safety bubble과 Reality Shield는 막습니다 ([M-0128](../rules/damage.md#m-0128)). 취약한 참가자는 Shield나 Safety bubble의 보호를 받지 못합니다 ([M-0129](../rules/damage.md#m-0129)). 폭발 범위 안에 서 있으면 자신의 C4와 Landmine에도 맞습니다 ([M-0133](../rules/damage.md#m-0133)).

표에 따르면 각 방어 수단이 효과적인 대상은 다음과 같습니다. Flak jacket은 미사일, 핵, 공습 충격, 건십 폭탄을 막고 ([M-0158](../rules/damage.md#m-0158), [M-0159](../rules/damage.md#m-0159), [M-0160](../rules/damage.md#m-0160), [M-0162](../rules/damage.md#m-0162)), Protection은 독, Drone, C4, Landmine 등 여러 가지를 막습니다 ([M-0143](../rules/damage.md#m-0143), [M-0153](../rules/damage.md#m-0153), [M-0154](../rules/damage.md#m-0154), [M-0155](../rules/damage.md#m-0155)). Body armor는 거의 모든 행에서 흡수합니다 ([M-0125](../rules/damage.md#m-0125)).

규칙이 불안정한 부분은 다음과 같습니다. 위키는 Robot 피해를 무엇이 막는지에 대해 ([M-0524](../rules/damage.md#m-0524), [C-0500](../unknowns.md#c-0500)), 그리고 Reality Shield가 언세이프 서클을 막는지에 대해 ([M-0538](../rules/damage.md#m-0538), [C-0502](../unknowns.md#c-0502)) 스스로 모순됩니다. 어떤 출처가 파이프라인을 거치는지는 미해결 질문입니다 ([U-0002](../unknowns.md#u-0002)). 끝수 처리 관련 질문도 미해결입니다. Kick 감소 ([U-0001](../unknowns.md#u-0001))와 "내림"이 적용되는 위치 ([U-0100](../unknowns.md#u-0100))가 그렇습니다. 방어구가 초과 피해를 통과시키는지 ([U-0101](../unknowns.md#u-0101)), 여러 Fortress가 차례로 흡수하는지 ([U-0102](../unknowns.md#u-0102)), 반사된 타격이 공격자의 파이프라인을 사용하는지 ([U-0005](../unknowns.md#u-0005)), 여러 차단 수단이 적용될 때 어느 것이 사용되는지 ([U-0120](../unknowns.md#u-0120))도 미해결입니다.

이 페이지는 규칙 48개(15 `DOCUMENTED`, 31 `CONDITIONAL`, 2 `UNKNOWN`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0102"></a>

### M-0102: Kick 라이브 상태: 받는 피해 10% 감소, 주는 피해 10% 증가 (일반 서술)

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0102](../rules/damage.md#m-0102) `wiki-006`: "If you're live on Kick, you take 10% less damage and do 10% more damage" ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: Kick에서 라이브 중이면 받는 피해가 10% 줄고 주는 피해가 10% 늘어납니다

**형식 모델:**

- [M-0102](../rules/damage.md#m-0102) 해석 A: `방어자 라이브: d -> floor(9*d/10); 공격자 라이브: d -> floor(11*d/10)`
- [M-0102](../rules/damage.md#m-0102) 해석 B: `방어자 라이브: d -> d - floor(d/10); 공격자 라이브: d -> floor(11*d/10)`
- [M-0102](../rules/damage.md#m-0102) 해석 C: `공격자 보너스는 파이프라인 목록에 한정되지 않고 모든 피해 원천에 적용됨 (일반적 서술)`
- [M-0102](../rules/damage.md#m-0102) 정의역: d는 정수, d >= 0

**미해결 질문:**

- [U-0001](../unknowns.md#u-0001) (치명적): 방어자의 Kick 라이브 10% 감소는 결과를 내림하는 것입니까(A), 아니면 제거되는 10%를 내림하는 것입니까(B)?
- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?

**모순:** [C-0100](../unknowns.md#c-0100)

메모 ([M-0102](../rules/damage.md#m-0102)): 파이프라인 페이지는 공격자 보너스를 명시된 무기 목록으로 한정하고, 방어자 감소는 끝수 처리가 적용되는 별도 단계로 서술합니다. [C-0100](../unknowns.md#c-0100)을 참조하십시오. 감소의 끝수 처리 방식은 [U-0001](../unknowns.md#u-0001)입니다.

<a id="m-0117"></a>

### M-0117: 타격 파이프라인: 순서대로 일곱 단계

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0117](../rules/damage.md#m-0117) `wiki-damage-032`: "Every hit goes through these steps in order." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 모든 타격은 이 단계들을 순서대로 거칩니다.

**형식 모델:**

- [M-0117](../rules/damage.md#m-0117) 해석 A: `result = armor(fortress(minimum(reductions(mirror(kick_bonus(immunity(h)))))))`
- [M-0117](../rules/damage.md#m-0117) 정의역: h는 정수, h >= 0, 타격 1회

**따름 결과:** [T-0003](../theorems/T-0003.md), [T-0402](../theorems/T-0402.md)

**상호작용:** [M-0118](../rules/damage.md#m-0118), [M-0119](../rules/damage.md#m-0119), [M-0120](../rules/damage.md#m-0120), [M-0121](../rules/damage.md#m-0121), [M-0122](../rules/damage.md#m-0122), [M-0123](../rules/damage.md#m-0123), [M-0124](../rules/damage.md#m-0124), [M-0125](../rules/damage.md#m-0125)

**미해결 질문:**

- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?
- [U-0103](../unknowns.md#u-0103) (높음): 'A hit that gets through always does at least 1 HP'는 7단계 중 5단계입니다. fortress(6단계)와 armor(7단계)가 최종 HP 손실을 여전히 0으로 줄일 수 있습니까?

메모 ([M-0117](../rules/damage.md#m-0117)): 어떤 피해 원천이 타격에 해당하는지는 [U-0002](../unknowns.md#u-0002)입니다. 단계는 레코드 하나씩 모델링했습니다. 118 면역, 119 Kick 보너스, 120 mirror, 121과 122 감소, 123 최소, 124 fortress, 125 armor입니다.

<a id="m-0118"></a>

### M-0118: 파이프라인 1단계: 면역

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0118](../rules/damage.md#m-0118) `wiki-damage-034`: "Immunity" ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 면역
- [M-0118](../rules/damage.md#m-0118) `wiki-damage-035`: "If anything blocks the hit, you take nothing." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 무언가가 타격을 막으면 아무 피해도 입지 않습니다.

**형식 모델:**

- [M-0118](../rules/damage.md#m-0118) 해석 A: `원천에 대한 차단 수단(피해 표)이 하나라도 적용되면: d := 0 후 중단`

**따름 결과:** [T-0402](../theorems/T-0402.md)

**상호작용:** [M-0117](../rules/damage.md#m-0117)

**미해결 질문:**

- [U-0120](../unknowns.md#u-0120) (높음): 한 번의 타격에 여러 방어 수단(Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection)이 적용될 때, 어느 것이 'blocker'이고 어떤 아이템이 소모됩니까? 명시된 유일한 규칙은 'a hit already blocked by something else does not use [the Flak jacket] up'입니다.

메모 ([M-0118](../rules/damage.md#m-0118)): 차단 수단의 집합은 피해 표의 행([M-0140](../rules/damage.md#m-0140)..[M-0166](../rules/damage.md#m-0166))에서 가져옵니다. 여러 개가 적용될 때 어느 차단 수단이 소모되는지는 [U-0120](../unknowns.md#u-0120)입니다.

<a id="m-0119"></a>

### M-0119: 파이프라인 2단계: 공격자 Kick 보너스, 나열된 무기에 한정

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0119](../rules/damage.md#m-0119) `wiki-damage-038`: "If the attacker is live on Kick, their own bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest and trapped gift hits deal 10% more, rounded down." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 공격자가 Kick에서 라이브 중이면, 본인의 bow, staff, knife, long sword, axe, machete, drone, C4, landmine, 가짜 상자, trapped gift 타격이 10% 더 큰 피해를 주며, 내림합니다.

**형식 모델:**

- [M-0119](../rules/damage.md#m-0119) 해석 A: `공격자가 라이브이고 source in {bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest, trapped gift}이면: d := floor(11*d/10) = d + floor(d/10)`
- [M-0119](../rules/damage.md#m-0119) 정의역: d는 정수 >= 0; 무기 목록은 닫혀 있음 (Poison Dart, 미사일, 핵 등은 목록에 없음)
- [M-0119](../rules/damage.md#m-0119) 매개변수 `bonus`: 10 퍼센트
- [M-0119](../rules/damage.md#m-0119) 매개변수 `list`: bow, staff, knife, long sword, axe, machete, drone, C4, landmine, 가짜 상자, trapped gift

**따름 결과:** [T-0001](../theorems/T-0001.md)

**상호작용:** [M-0117](../rules/damage.md#m-0117)

**미해결 질문:**

- [U-0010](../unknowns.md#u-0010) (보통): Wizard staff의 '5 s 동안 총 10 HP': 한 번의 타격입니까, 여러 번의 틱입니까?
- [U-0121](../unknowns.md#u-0121) (낮음): 자해 타격('hit by your own C4 and landmine'): 공격자 = 방어자로 전체 파이프라인이 실행되어 Kick 보너스(2단계)와 Kick 감소(4단계)가 포함됩니까? 그리고 자신이 가진 차단 수단(Protection, Shield)이 적용됩니까?

**모순:** [C-0100](../unknowns.md#c-0100)

메모 ([M-0119](../rules/damage.md#m-0119)): 내림 해석은 하나뿐입니다 (1.1*d의 floor는 binary64에서 정확함). 'staff'는 Wizard staff 범위 피해(틱, [U-0010](../unknowns.md#u-0010))입니다. 소개 페이지의 일반 서술('주는 피해가 10% 늘어난다')은 더 넓으며, [C-0100](../unknowns.md#c-0100)을 참조하십시오. 보너스는 mirror보다 앞서므로 반사된 타격에도 포함됩니다.

<a id="m-0120"></a>

### M-0120: 파이프라인 3단계: Mirror forcefield가 타격 전체를 되돌려 보냄

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0120](../rules/damage.md#m-0120) `wiki-damage-041`: "A Mirror forcefield sends the whole hit back to the attacker instead, before any reduction." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Mirror forcefield는 어떤 감소도 거치기 전에 타격 전체를 대신 공격자에게 되돌려 보냅니다.

**형식 모델:**

- [M-0120](../rules/damage.md#m-0120) 해석 A: `방어자의 mirror가 활성 상태이고 source가 반사 가능하면: 공격자가 (2단계 이후의) d를 공격자 자신의 전체 파이프라인을 거쳐 받고, 방어자는 0을 받음`
- [M-0120](../rules/damage.md#m-0120) 해석 B: `공격자가 d를 원값 그대로 받음, 파이프라인 없음`

**상호작용:** [M-0117](../rules/damage.md#m-0117), [M-0119](../rules/damage.md#m-0119), [M-0134](../rules/items.md#m-0134), [M-0135](../rules/damage.md#m-0135)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0120](../rules/damage.md#m-0120)): '어떤 감소도 거치기 전에'는 mirror가 방어자의 4~7단계보다 앞선다는 뜻입니다. 반사되는 양에는 앞선 Kick 보너스(2단계)가 포함됩니다. 공격자의 파이프라인은 [U-0005](../unknowns.md#u-0005)입니다.

<a id="m-0121"></a>

### M-0121: 파이프라인 4a단계: Protection 시길이 핵 피해를 절반으로 줄임

라벨: `CONDITIONAL`. 시길: protection.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0121](../rules/damage.md#m-0121) `wiki-damage-044`: "A Protection contestant takes 50% less from a nuke." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Protection 참가자는 핵으로부터 받는 피해가 50% 줄어듭니다.
- [M-0121](../rules/damage.md#m-0121) `wiki-damage-045`: "The damage left is rounded down." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 남는 피해는 내림합니다.
- [M-0121](../rules/damage.md#m-0121) `wiki-damage-062`: "The Protection sigil is not immune to nukes, but takes 50% less from them." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Protection 시길은 핵에 면역이 아니지만, 받는 피해가 50% 줄어듭니다.

**형식 모델:**

- [M-0121](../rules/damage.md#m-0121) 해석 A: `방어자 시길이 Protection이고 source가 핵이면: d := floor(d/2); 다른 원천은 그대로`
- [M-0121](../rules/damage.md#m-0121) 정의역: d는 정수 >= 0
- [M-0121](../rules/damage.md#m-0121) 매개변수 `nuke_reduction`: 50 퍼센트

**상호작용:** [M-0117](../rules/damage.md#m-0117)

**미해결 질문:**

- [U-0100](../unknowns.md#u-0100) (낮음): 4단계의 'The damage left is rounded down'은 어디에 적용됩니까? Protection 50% 결과에만 적용됩니까, 아니면 모든 감소 이후의 최종 내림 한 번으로 적용되며 Kick 10%는 내림하지 않은 값에서 계산됩니까?

메모 ([M-0121](../rules/damage.md#m-0121)): 'nuke에 면역은 아니지만 50% 줄어듦'. Protection 페이지도 같은 규칙(50% 감소)을 다루며 불일치는 발견되지 않았습니다. floor가 어디에 적용되는지는 [U-0100](../unknowns.md#u-0100)입니다. Flak jacket([M-0130](../rules/items.md#m-0130))은 이 단계 이전에 핵을 막습니다.

<a id="m-0122"></a>

### M-0122: 파이프라인 4b단계: 방어자 Kick 감소

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0122](../rules/damage.md#m-0122) `wiki-damage-046`: "Being live on Kick then takes off 10%, rounded down." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Kick에서 라이브 중이면 그다음 10%가 차감되며, 내림합니다.

**형식 모델:**

- [M-0122](../rules/damage.md#m-0122) 해석 A: `방어자 라이브: d := floor(9*d/10)`
- [M-0122](../rules/damage.md#m-0122) 해석 B: `방어자 라이브: d := d - floor(d/10)`
- [M-0122](../rules/damage.md#m-0122) 정의역: d는 정수 >= 0
- [M-0122](../rules/damage.md#m-0122) 매개변수 `reduction`: 10 퍼센트

**따름 결과:** [T-0002](../theorems/T-0002.md)

**상호작용:** [M-0117](../rules/damage.md#m-0117), [M-0121](../rules/damage.md#m-0121)

**미해결 질문:**

- [U-0001](../unknowns.md#u-0001) (치명적): 방어자의 Kick 라이브 10% 감소는 결과를 내림하는 것입니까(A), 아니면 제거되는 10%를 내림하는 것입니까(B)?
- [U-0100](../unknowns.md#u-0100) (낮음): 4단계의 'The damage left is rounded down'은 어디에 적용됩니까? Protection 50% 결과에만 적용됩니까, 아니면 모든 감소 이후의 최종 내림 한 번으로 적용되며 Kick 10%는 내림하지 않은 값에서 계산됩니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?

메모 ([M-0122](../rules/damage.md#m-0122)): Protection 단계 이후에 적용됩니다 (명시된 순서). d가 10의 배수가 아니고 d >= 2이면 언제나 A와 B는 1 HP 차이가 납니다.

<a id="m-0123"></a>

### M-0123: 파이프라인 5단계: 통과한 타격은 최소 1 HP

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0123](../rules/damage.md#m-0123) `wiki-damage-048`: "Minimum" ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 최소
- [M-0123](../rules/damage.md#m-0123) `wiki-damage-049`: "A hit that gets through always does at least 1 HP." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 통과한 타격은 언제나 최소 1 HP의 피해를 줍니다.

**형식 모델:**

- [M-0123](../rules/damage.md#m-0123) 해석 A: `1단계에서 막히지 않았고 mirror로 반사되지 않은 타격이면 d := max(1, d)`
- [M-0123](../rules/damage.md#m-0123) 해석 B: `6단계와 7단계 이후의 최종 HP 손실 >= 1`
- [M-0123](../rules/damage.md#m-0123) 정의역: d는 정수 >= 0
- [M-0123](../rules/damage.md#m-0123) 매개변수 `minimum_hp`: 1

**따름 결과:** [T-0004](../theorems/T-0004.md), [T-0402](../theorems/T-0402.md), [T-0703](../theorems/T-0703.md)

**상호작용:** [M-0117](../rules/damage.md#m-0117), [M-0122](../rules/damage.md#m-0122)

**미해결 질문:**

- [U-0103](../unknowns.md#u-0103) (높음): 'A hit that gets through always does at least 1 HP'는 7단계 중 5단계입니다. fortress(6단계)와 armor(7단계)가 최종 HP 손실을 여전히 0으로 줄일 수 있습니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?

메모 ([M-0123](../rules/damage.md#m-0123)): '언제나'는 뒤따르는 6단계와 7단계와 취지상 충돌합니다 ([U-0103](../unknowns.md#u-0103)).

<a id="m-0124"></a>

### M-0124: 파이프라인 6단계: fortress는 남은 내구도까지 흡수

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0124](../rules/damage.md#m-0124) `wiki-damage-051`: "Fortress" ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Fortress
- [M-0124](../rules/damage.md#m-0124) `wiki-damage-052`: "A fortress you stand within absorbs up to its remaining durability, whoever built it." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 당신이 그 안에 서 있는 fortress는 누가 지었든 남은 내구도까지 피해를 흡수합니다.

**형식 모델:**

- [M-0124](../rules/damage.md#m-0124) 해석 A: `방어자가 fortress 안에 서 있으면 (소유자 무관): a := min(d, dur); d := d - a; dur := dur - a`
- [M-0124](../rules/damage.md#m-0124) 해석 B: `여러 fortress가 차례로 흡수함`
- [M-0124](../rules/damage.md#m-0124) 정의역: d, dur는 정수 >= 0
- [M-0124](../rules/damage.md#m-0124) 매개변수 `fortress_durability`: 이 페이지에서는 UNKNOWN, 아이템 페이지 참조

**상호작용:** [M-0117](../rules/damage.md#m-0117), [M-0123](../rules/damage.md#m-0123)

**미해결 질문:**

- [U-0102](../unknowns.md#u-0102) (보통): Fortress 단계: 참가자가 여러 fortress 안에 서 있을 때 한 번의 타격을 몇 개의 fortress가 흡수할 수 있으며, 어떤 순서이고, 내구도는 흡수한 HP 1당 1씩 줄어듭니까?
- [U-0103](../unknowns.md#u-0103) (높음): 'A hit that gets through always does at least 1 HP'는 7단계 중 5단계입니다. fortress(6단계)와 armor(7단계)가 최종 HP 손실을 여전히 0으로 줄일 수 있습니까?

메모 ([M-0124](../rules/damage.md#m-0124)): '누가 지었든': 소유자는 무관하며 적의 fortress도 보호합니다. 내구도 값은 다른 페이지 계열에 있습니다.

<a id="m-0125"></a>

### M-0125: 파이프라인 7단계: Body armor가 남은 피해를 파괴될 때까지 흡수함

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0125](../rules/damage.md#m-0125) `wiki-damage-054`: "Armor" ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 방어구 (Armor)
- [M-0125](../rules/damage.md#m-0125) `wiki-damage-055`: "Body armor absorbs what is left, until it breaks." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Body armor는 남은 피해를 파괴될 때까지 흡수합니다.

**형식 모델:**

- [M-0125](../rules/damage.md#m-0125) 해석 A: `a := min(d, dur); d := d - a; dur := dur - a; dur = 0이면 파괴됨`
- [M-0125](../rules/damage.md#m-0125) 해석 B: `남은 d 전체가 흡수되고 초과분은 소실되며, dur가 0에 도달하면 파괴됨`
- [M-0125](../rules/damage.md#m-0125) 정의역: d, dur는 0 이상의 정수
- [M-0125](../rules/damage.md#m-0125) 매개변수 `armor_durability`: 이 페이지에서는 UNKNOWN, 아이템 페이지 참조

**상호작용:** [M-0117](../rules/damage.md#m-0117), [M-0124](../rules/damage.md#m-0124), [M-0126](../rules/items.md#m-0126)

**미해결 질문:**

- [U-0101](../unknowns.md#u-0101) (높음): Body armor가 'absorbs what is left, until it breaks'일 때, 남은 내구도보다 큰 타격은 초과분을 통과시킵니까(A), 아니면 타격 전체가 흡수되고 armor만 부서집니까(B)? 내구도는 흡수한 HP 1당 1씩 줄어듭니까?
- [U-0103](../unknowns.md#u-0103) (높음): 'A hit that gets through always does at least 1 HP'는 7단계 중 5단계입니다. fortress(6단계)와 armor(7단계)가 최종 HP 손실을 여전히 0으로 줄일 수 있습니까?

<a id="m-0128"></a>

### M-0128: Shield는 존, 언세이프 서클(unsafe circle), robot 피해를 막지 못하며, Safety bubble과 Reality Shield는 막음

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0128](../rules/damage.md#m-0128) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Shield는 존, 언세이프 서클(unsafe circle), robot 피해를 막지 못합니다.
- [M-0128](../rules/damage.md#m-0128) `wiki-damage-059`: "A Safety bubble and a Reality Shield do." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Safety bubble과 Reality Shield는 막습니다.

**형식 모델:**

- [M-0128](../rules/damage.md#m-0128) 해석 A: `blocks(Shield)는 {outside circle, unsafe circle, robot}을 제외함; blocks(Safety bubble)와 blocks(Reality Shield)는 이를 포함함`

**따름 결과:** [T-0008](../theorems/T-0008.md)

메모 ([M-0128](../rules/damage.md#m-0128)): 표와 일치합니다: 세 행에는 Safety bubble이 있고 Shield는 없습니다. 해당 행에서 Reality Shield는 [M-0127](../rules/items.md#m-0127)에 의존합니다.

<a id="m-0129"></a>

### M-0129: 취약한 참가자: Shield나 Safety bubble의 보호를 받지 못함

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0129](../rules/damage.md#m-0129) `wiki-damage-060`: "A vulnerable contestant gets no protection from a Shield or a Safety Bubble." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 취약한 참가자는 Shield나 Safety Bubble의 보호를 받지 못합니다.

**형식 모델:**

- [M-0129](../rules/damage.md#m-0129) 해석 A: `vulnerable이면: Shield와 Safety bubble은 차단 집합에서 제거됨`

**따름 결과:** [T-0402](../theorems/T-0402.md)

메모 ([M-0129](../rules/damage.md#m-0129)): Vulnerability Dart 자체는 다른 페이지에 있습니다.

<a id="m-0133"></a>

### M-0133: 폭발 범위에 서 있으면 자신의 C4와 landmine에 피해를 입음

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0133](../rules/damage.md#m-0133) `wiki-damage-068`: "You are hit by your own C4 and landmine if you stand in the blast." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 폭발 범위에 서 있으면 자신의 C4와 landmine에 맞습니다.

**형식 모델:**

- [M-0133](../rules/damage.md#m-0133) 해석 A: `C4와 landmine에서는 attacker = defender가 허용됨; 타격은 파이프라인을 거침`

**미해결 질문:**

- [U-0121](../unknowns.md#u-0121) (낮음): 자해 타격('hit by your own C4 and landmine'): 공격자 = 방어자로 전체 파이프라인이 실행되어 Kick 보너스(2단계)와 Kick 감소(4단계)가 포함됩니까? 그리고 자신이 가진 차단 수단(Protection, Shield)이 적용됩니까?

메모 ([M-0133](../rules/damage.md#m-0133)): Mirror는 자신의 폭발물을 절대 반사하지 않습니다 ([M-0135](../rules/damage.md#m-0135)).

<a id="m-0135"></a>

### M-0135: Mirror forcefield가 반사할 수 있는 원천 목록

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0135](../rules/damage.md#m-0135) `wiki-damage-070`: "It only reflects Poison Darts, fake gravestones, bows, wizard staffs, knives, long swords, Zarok's axes, machetes, drones, C4, landmines, flashbangs and fake chests, and never your own explosives." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Poison Dart, fake gravestone, bow, wizard staff, knife, long sword, Zarok's axe, machete, drone, C4, landmine, flashbang, 가짜 상자만 반사하며, 자신의 폭발물은 절대 반사하지 않습니다.

**형식 모델:**

- [M-0135](../rules/damage.md#m-0135) 해석 A: `source in {Poison Dart, fake gravestone, bow, wizard staff, knife, long sword, Zarok's axe, machete, drone, C4, landmine, flashbang, fake chest}이고 자신의 폭발물이 아닐 때, 그리고 그때에만 반사`

**상호작용:** [M-0120](../rules/damage.md#m-0120)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

**모순:** [C-0101](../unknowns.md#c-0101)

메모 ([M-0135](../rules/damage.md#m-0135)): 표에는 Trapped gift 행에도 Mirror forcefield (reflects)가 있지만 이 목록에는 빠져 있습니다: [C-0101](../unknowns.md#c-0101).

<a id="m-0137"></a>

### M-0137: Death Ward: 서클 밖 첫 타격 차단 후 2 min 동안 서클 밖 면역, 쿨다운 2 h

라벨: `CONDITIONAL`. 시길: death.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0137](../rules/damage.md#m-0137) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Death Ward: Death 참가자가 서클 밖에서 받는 첫 타격은 차단되며, 서클 밖의 피해는 2min 동안 차단됩니다.
- [M-0137](../rules/damage.md#m-0137) `wiki-damage-074`: "Cooldown 2h." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 쿨다운 2h.

**형식 모델:**

- [M-0137](../rules/damage.md#m-0137) 해석 A: `Death 참가자: 서클 밖 첫 타격 차단; 서클 밖 피해는 120 s 동안 차단; 이후 쿨다운 7200 s`
- [M-0137](../rules/damage.md#m-0137) 해석 B: `차단 구간과 쿨다운은 활성화 시점에 시작됨`
- [M-0137](../rules/damage.md#m-0137) 매개변수 `window_s`: 120
- [M-0137](../rules/damage.md#m-0137) 매개변수 `cooldown_s`: 7200

**미해결 질문:**

- [U-0119](../unknowns.md#u-0119) (보통): Death Ward: 2 min의 면역은 첫 번째로 막은 타격에서 시작합니까, 시길을 선택한 때 시작합니까? 'Cooldown 2h'는 활성화 시점에 시작합니까, 2 min이 끝난 때 시작합니까? 그리고 Ward는 쿨다운당 한 번만 사용할 수 있습니까?

**모순:** [C-0103](../unknowns.md#c-0103)

메모 ([M-0137](../rules/damage.md#m-0137)): Death 시길 페이지는 Death Ward를 다르게 서술합니다 (언세이프 서클(unsafe circle)을 추가함): [C-0103](../unknowns.md#c-0103). 시길 고유 메커니즘은 중복 기록하지 않았습니다.

<a id="m-0140"></a>

### M-0140: 피해 원천 'Outside the circle'과 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0140](../rules/damage.md#m-0140) `wiki-damage-005`: "| Outside the circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Outside the circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (둔화), Body armor (흡수)

**형식 모델:**

- [M-0140](../rules/damage.md#m-0140) 해석 A: `blockers(Outside the circle) = {Safety bubble: 막음; Guardian angel: 막음; Death Ward: 막음; Hazmat suit: 둔화시킴; Body armor: 흡수함}`
- [M-0140](../rules/damage.md#m-0140) 정의역: 원천 'Outside the circle'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0003](../unknowns.md#u-0003) (보통): 존 피해: 세이프 존을 벗어난 뒤 첫 틱은 5 s입니까, 7 s입니까?

메모 ([M-0140](../rules/damage.md#m-0140)): 주기적 존 피해: Body armor가 흡수합니다(이 행과 피해 페이지의 'Body Armor works on every kind of damage'). 존 틱에 Kick 감소, 최소 1 HP, fortress가 적용되는지는 [U-0002](../unknowns.md#u-0002)에서 다루며 [M-0101](../rules/zone.md#m-0101)이 이를 담고 있습니다.

<a id="m-0141"></a>

### M-0141: 피해 원천 'Unsafe circle'과 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0141](../rules/damage.md#m-0141) `wiki-damage-006`: "| Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (둔화), Body armor (흡수)

**형식 모델:**

- [M-0141](../rules/damage.md#m-0141) 해석 A: `blockers(Unsafe circle) = {Safety bubble: 막음; Guardian angel: 막음; Death Ward: 막음; Hazmat suit: 둔화시킴; Body armor: 흡수함}`
- [M-0141](../rules/damage.md#m-0141) 정의역: 원천 'Unsafe circle'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0123](../unknowns.md#u-0123) (보통): 피해 표의 Hazmat suit '(slows)': 느려짐은 존 피해, 언세이프 서클(unsafe circle) 피해, Robot 피해에 어떤 영향을 줍니까(틱 간격 배수, 피해 비율)?

**모순:** [C-0103](../unknowns.md#c-0103)

메모 ([M-0141](../rules/damage.md#m-0141)): Unsafe circle (Trolling). Trolling 페이지는 Guardian angel, Safety bubble, Reality Shield, Death Ward를 차단 수단으로 열거합니다: 같은 집합이며, [C-0103](../unknowns.md#c-0103)은 Death Ward의 범위에 관한 것입니다.

<a id="m-0142"></a>

### M-0142: 피해 원천 'Robot'과 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0142](../rules/damage.md#m-0142) `wiki-damage-007`: "| Robot | Safety bubble, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Robot | Safety bubble, Hazmat suit (둔화), Body armor (흡수)

**형식 모델:**

- [M-0142](../rules/damage.md#m-0142) 해석 A: `blockers(Robot) = {Safety bubble: 막음; Hazmat suit: 둔화시킴; Body armor: 흡수함}`
- [M-0142](../rules/damage.md#m-0142) 정의역: 원천 'Robot'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0123](../unknowns.md#u-0123) (보통): 피해 표의 Hazmat suit '(slows)': 느려짐은 존 피해, 언세이프 서클(unsafe circle) 피해, Robot 피해에 어떤 영향을 줍니까(틱 간격 배수, 피해 비율)?

메모 ([M-0142](../rules/damage.md#m-0142)): Robot 피해는 Shield ([M-0128](../rules/damage.md#m-0128))로도 Sleeping Bag ([M-0132](../rules/items.md#m-0132))으로도 막히지 않습니다.

<a id="m-0143"></a>

### M-0143: 피해 원천 'Poison'과 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0143](../rules/damage.md#m-0143) `wiki-damage-008`: "| Poison | Shield, Safety bubble, Sleeping Bag, Protection, Anti poison, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Poison | Shield, Safety bubble, Sleeping Bag, Protection, Anti poison, Body armor (흡수)

**형식 모델:**

- [M-0143](../rules/damage.md#m-0143) 해석 A: `blockers(Poison) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Protection: 막음; Anti poison: 막음; Body armor: 흡수함}`
- [M-0143](../rules/damage.md#m-0143) 정의역: 원천 'Poison'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0117](../unknowns.md#u-0117) (높음): Shield 또는 Safety bubble은 'blocks each poison step while it lasts': 막힌 단계는 소모됩니까('all its damage'에 산입), 아니면 건너뜁니까(독이 연장)? 보호받는 동안 카운트다운은 계속됩니까?
- [U-0118](../unknowns.md#u-0118) (낮음): 'Sleeping in your own Sleeping Bag'은 Poison 면역 목록에 동사 없이 라벨로만 나옵니다: 새 독을 막습니까, 각 단계를 막습니까, 둘 다입니까?

메모 ([M-0143](../rules/damage.md#m-0143)): Poison 페이지: Protection은 면역, Anti poison은 새 독 없음, Reality Shield는 새 독 없음; 여기서 '막음'은 독 틱을 막는다는 뜻입니다. Poison Dart가 반사되는 공격이므로 Mirror는 없습니다 ([M-0180](../rules/poison.md#m-0180)).

<a id="m-0144"></a>

### M-0144: 피해 원천 'Tear gas'와 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0144](../rules/damage.md#m-0144) `wiki-damage-009`: "| Tear gas | Shield, Safety bubble, Sleeping Bag, Gas mask, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 최루 가스 | Shield, Safety bubble, Sleeping Bag, Gas mask, Body armor (흡수)

**형식 모델:**

- [M-0144](../rules/damage.md#m-0144) 해석 A: `blockers(Tear gas) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Gas mask: 막음; Body armor: 흡수함}`
- [M-0144](../rules/damage.md#m-0144) 정의역: 원천 'Tear gas'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

메모 ([M-0144](../rules/damage.md#m-0144)): 최루 가스: Gas mask가 열거되어 있으며 [M-0131](../rules/items.md#m-0131)과 일치합니다.

<a id="m-0145"></a>

### M-0145: 피해 원천 'Zombie drain'과 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0145](../rules/damage.md#m-0145) `wiki-damage-010`: "| Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (흡수)

**형식 모델:**

- [M-0145](../rules/damage.md#m-0145) 해석 A: `blockers(Zombie drain) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Necromancy / Repellent: 막음; Body armor: 흡수함}`
- [M-0145](../rules/damage.md#m-0145) 정의역: 원천 'Zombie drain'의 타격 1회

**따름 결과:** [T-0702](../theorems/T-0702.md)

**상호작용:** [M-0118](../rules/damage.md#m-0118)

메모 ([M-0145](../rules/damage.md#m-0145)): Zombie drain (주기적). 'Necromancy / Repellent'는 Necromancy 시길 또는 Zombie repellent로 해석합니다.

<a id="m-0146"></a>

### M-0146: 피해 원천 'Bow'와 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0146](../rules/damage.md#m-0146) `wiki-damage-011`: "| Bow | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Bow | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0146](../rules/damage.md#m-0146) 해석 A: `blockers(Bow) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Mirror forcefield: 반사함; Body armor: 흡수함}`
- [M-0146](../rules/damage.md#m-0146) 정의역: 원천 'Bow'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0146](../rules/damage.md#m-0146)): 공격자의 Kick 보너스가 이 원천에 적용됩니다 (2단계 목록).

<a id="m-0147"></a>

### M-0147: 피해 원천 'Wizard Staff area'와 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0147](../rules/damage.md#m-0147) `wiki-damage-012`: "| Wizard Staff area | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Wizard Staff area | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0147](../rules/damage.md#m-0147) 해석 A: `blockers(Wizard Staff area) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Mirror forcefield: 반사함; Body armor: 흡수함}`
- [M-0147](../rules/damage.md#m-0147) 정의역: 원천 'Wizard Staff area'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0010](../unknowns.md#u-0010) (보통): Wizard staff의 '5 s 동안 총 10 HP': 한 번의 타격입니까, 여러 번의 틱입니까?
- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0147](../rules/damage.md#m-0147)): Wizard staff 범위 피해 (5 s 동안의 범위 틱, [U-0010](../unknowns.md#u-0010)). 공격자의 Kick 보너스가 이 원천에 적용됩니다 (2단계 목록).

<a id="m-0148"></a>

### M-0148: 피해 원천 'Assassin's Knife'와 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0148](../rules/damage.md#m-0148) `wiki-damage-013`: "| Assassin's Knife | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Assassin's Knife | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0148](../rules/damage.md#m-0148) 해석 A: `blockers(Assassin's Knife) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Mirror forcefield: 반사함; Body armor: 흡수함}`
- [M-0148](../rules/damage.md#m-0148) 정의역: 원천 'Assassin's Knife'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0148](../rules/damage.md#m-0148)): 공격자의 Kick 보너스가 이 원천에 적용됩니다 (2단계 목록).

<a id="m-0149"></a>

### M-0149: 피해 원천 'Long Sword'와 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0149](../rules/damage.md#m-0149) `wiki-damage-014`: "| Long Sword | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Long Sword | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0149](../rules/damage.md#m-0149) 해석 A: `blockers(Long Sword) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Mirror forcefield: 반사함; Body armor: 흡수함}`
- [M-0149](../rules/damage.md#m-0149) 정의역: 원천 'Long Sword'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0149](../rules/damage.md#m-0149)): 공격자의 Kick 보너스가 이 원천에 적용됩니다 (2단계 목록).

<a id="m-0150"></a>

### M-0150: 피해 원천 'Zarok's Axe'와 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0150](../rules/damage.md#m-0150) `wiki-damage-015`: "| Zarok's Axe | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Zarok's Axe | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0150](../rules/damage.md#m-0150) 해석 A: `blockers(Zarok's Axe) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Mirror forcefield: 반사함; Body armor: 흡수함}`
- [M-0150](../rules/damage.md#m-0150) 정의역: 원천 'Zarok's Axe'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0150](../rules/damage.md#m-0150)): 공격자의 Kick 보너스가 이 원천에 적용됩니다 (2단계 목록).

<a id="m-0151"></a>

### M-0151: 피해 원천 'Huge Machete'와 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0151](../rules/damage.md#m-0151) `wiki-damage-016`: "| Huge Machete | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Huge Machete | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0151](../rules/damage.md#m-0151) 해석 A: `blockers(Huge Machete) = {Shield: 막음; Safety bubble: 막음; Sleeping Bag: 막음; Mirror forcefield: 반사함; Body armor: 흡수함}`
- [M-0151](../rules/damage.md#m-0151) 정의역: 원천 'Huge Machete'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0151](../rules/damage.md#m-0151)): 공격자의 Kick 보너스가 이 원천에 적용됩니다 (2단계 목록).

<a id="m-0152"></a>

### M-0152: 피해 원천 'Deep Cut bleeding': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0152](../rules/damage.md#m-0152) `wiki-damage-017`: "| Deep Cut bleeding | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Deep Cut bleeding | Shield, Safety bubble, Sleeping Bag, Body armor (흡수)

**형식 모델:**

- [M-0152](../rules/damage.md#m-0152) 해석 A: `blockers(Deep Cut bleeding) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Body armor: 흡수}`
- [M-0152](../rules/damage.md#m-0152) 정의역: 원천 'Deep Cut bleeding'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

메모 ([M-0152](../rules/damage.md#m-0152)): Deep Cut bleeding(주기적).

<a id="m-0153"></a>

### M-0153: 피해 원천 'Drone': 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0153](../rules/damage.md#m-0153) `wiki-damage-018`: "| Drone | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Drone | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0153](../rules/damage.md#m-0153) 해석 A: `blockers(Drone) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Mirror forcefield: 반사; Body armor: 흡수}`
- [M-0153](../rules/damage.md#m-0153) 정의역: 원천 'Drone'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0153](../rules/damage.md#m-0153)): 공격자의 Kick 보너스가 이 원천에 적용됩니다(2단계 목록).

<a id="m-0154"></a>

### M-0154: 피해 원천 'C4': 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0154](../rules/damage.md#m-0154) `wiki-damage-019`: "| C4 | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | C4 | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0154](../rules/damage.md#m-0154) 해석 A: `blockers(C4) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Mirror forcefield: 반사; Body armor: 흡수}`
- [M-0154](../rules/damage.md#m-0154) 정의역: 원천 'C4'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0154](../rules/damage.md#m-0154)): 공격자의 Kick 보너스가 이 원천에 적용됩니다(2단계 목록).

<a id="m-0155"></a>

### M-0155: 피해 원천 'Landmine': 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0155](../rules/damage.md#m-0155) `wiki-damage-020`: "| Landmine | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Landmine | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0155](../rules/damage.md#m-0155) 해석 A: `blockers(Landmine) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Mirror forcefield: 반사; Body armor: 흡수}`
- [M-0155](../rules/damage.md#m-0155) 정의역: 원천 'Landmine'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0155](../rules/damage.md#m-0155)): 공격자의 Kick 보너스가 이 원천에 적용됩니다(2단계 목록).

<a id="m-0156"></a>

### M-0156: 피해 원천 'Trapped gift': 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0156](../rules/damage.md#m-0156) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (반사)

**형식 모델:**

- [M-0156](../rules/damage.md#m-0156) 해석 A: `blockers(Trapped gift) = {Shield: 차단; Sleeping Bag: 차단; Protection: 차단; Mirror forcefield: 반사}`
- [M-0156](../rules/damage.md#m-0156) 정의역: 원천 'Trapped gift'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

**모순:** [C-0101](../unknowns.md#c-0101), [C-0102](../unknowns.md#c-0102)

메모 ([M-0156](../rules/damage.md#m-0156)): Safety bubble과 Body armor는 목록에 없습니다. 아이템 페이지에 'A trapped gift ignores it'(방어구)와 'A trapped gift still hurts the holder'(버블)라고 되어 있습니다. [C-0101](../unknowns.md#c-0101)과 [C-0102](../unknowns.md#c-0102)를 참조하십시오. 공격자의 Kick 보너스가 이 원천에 적용됩니다(2단계 목록).

<a id="m-0157"></a>

### M-0157: 피해 원천 'Fake chest': 이를 막는 수단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0157](../rules/damage.md#m-0157) `wiki-damage-022`: "| Fake chest | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 가짜 상자 | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (반사), Body armor (흡수)

**형식 모델:**

- [M-0157](../rules/damage.md#m-0157) 해석 A: `blockers(Fake chest) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Mirror forcefield: 반사; Body armor: 흡수}`
- [M-0157](../rules/damage.md#m-0157) 정의역: 원천 'Fake chest'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

메모 ([M-0157](../rules/damage.md#m-0157)): 공격자의 Kick 보너스가 이 원천에 적용됩니다(2단계 목록).

<a id="m-0158"></a>

### M-0158: 피해 원천 'Missile': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0158](../rules/damage.md#m-0158) `wiki-damage-023`: "| Missile | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 미사일 | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (흡수)

**형식 모델:**

- [M-0158](../rules/damage.md#m-0158) 해석 A: `blockers(Missile) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Flak jacket: 차단; Body armor: 흡수}`
- [M-0158](../rules/damage.md#m-0158) 정의역: 원천 'Missile'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0159"></a>

### M-0159: 피해 원천 'Nuke': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0159](../rules/damage.md#m-0159) `wiki-damage-024`: "| Nuke | Shield, Safety bubble, Sleeping Bag, Flak jacket, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 핵 | Shield, Safety bubble, Sleeping Bag, Flak jacket, Body armor (흡수)

**형식 모델:**

- [M-0159](../rules/damage.md#m-0159) 해석 A: `blockers(Nuke) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Flak jacket: 차단; Body armor: 흡수}`
- [M-0159](../rules/damage.md#m-0159) 정의역: 원천 'Nuke'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0160"></a>

### M-0160: 피해 원천 'Airstrike impact': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0160](../rules/damage.md#m-0160) `wiki-damage-025`: "| Airstrike impact | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 공습 충격 | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (흡수)

**형식 모델:**

- [M-0160](../rules/damage.md#m-0160) 해석 A: `blockers(Airstrike impact) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Flak jacket: 차단; Body armor: 흡수}`
- [M-0160](../rules/damage.md#m-0160) 정의역: 원천 'Airstrike impact'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0161"></a>

### M-0161: 피해 원천 'Airstrike fire': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0161](../rules/damage.md#m-0161) `wiki-damage-026`: "| Airstrike fire | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 공습 화재 | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (흡수)

**형식 모델:**

- [M-0161](../rules/damage.md#m-0161) 해석 A: `blockers(Airstrike fire) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Body armor: 흡수}`
- [M-0161](../rules/damage.md#m-0161) 정의역: 원천 'Airstrike fire'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0162"></a>

### M-0162: 피해 원천 'Gunship bomb': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0162](../rules/damage.md#m-0162) `wiki-damage-027`: "| Gunship bomb | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 건십 폭탄 | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (흡수)

**형식 모델:**

- [M-0162](../rules/damage.md#m-0162) 해석 A: `blockers(Gunship bomb) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Flak jacket: 차단; Body armor: 흡수}`
- [M-0162](../rules/damage.md#m-0162) 정의역: 원천 'Gunship bomb'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0163"></a>

### M-0163: 피해 원천 'Giant cyclops attack': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0163](../rules/damage.md#m-0163) `wiki-damage-028`: "| Giant cyclops attack | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Giant 사이클롭스 공격 | Shield, Safety bubble, Sleeping Bag, Body armor (흡수)

**형식 모델:**

- [M-0163](../rules/damage.md#m-0163) 해석 A: `blockers(Giant cyclops attack) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Body armor: 흡수}`
- [M-0163](../rules/damage.md#m-0163) 정의역: 원천 'Giant cyclops attack'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0164"></a>

### M-0164: 피해 원천 'Bounty mark': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0164](../rules/damage.md#m-0164) `wiki-damage-029`: "| Bounty mark | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 현상금 표시 | Shield, Safety bubble, Sleeping Bag, Body armor (흡수)

**형식 모델:**

- [M-0164](../rules/damage.md#m-0164) 해석 A: `blockers(Bounty mark) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Body armor: 흡수}`
- [M-0164](../rules/damage.md#m-0164) 정의역: 원천 'Bounty mark'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0165"></a>

### M-0165: 피해 원천 'Eddie's Potion backfire': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0165](../rules/damage.md#m-0165) `wiki-damage-030`: "| Eddie's Potion backfire | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Eddie's Potion backfire | Shield, Safety bubble, Sleeping Bag, Body armor (흡수)

**형식 모델:**

- [M-0165](../rules/damage.md#m-0165) 해석 A: `blockers(Eddie's Potion backfire) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Body armor: 흡수}`
- [M-0165](../rules/damage.md#m-0165) 정의역: 원천 'Eddie's Potion backfire'의 타격 1회

**따름 결과:** [T-0402](../theorems/T-0402.md)

**상호작용:** [M-0118](../rules/damage.md#m-0118)

메모 ([M-0165](../rules/damage.md#m-0165)): 시드 [U-0004](../unknowns.md#u-0004) 메모와 일치합니다: Shield, Safety bubble, Sleeping Bag, Body armor가 이를 막으며, 이는 차단에 대한 해석 B를 뒷받침합니다.

<a id="m-0166"></a>

### M-0166: 피해 원천 'Protection retribution': 이를 막는 수단

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0166](../rules/damage.md#m-0166) `wiki-damage-031`: "| Protection retribution | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Protection retribution | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (흡수)

**형식 모델:**

- [M-0166](../rules/damage.md#m-0166) 해석 A: `blockers(Protection retribution) = {Shield: 차단; Safety bubble: 차단; Sleeping Bag: 차단; Protection: 차단; Body armor: 흡수}`
- [M-0166](../rules/damage.md#m-0166) 정의역: 원천 'Protection retribution'의 타격 1회

**상호작용:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0524"></a>

### M-0524: Robot 피해 차단 수단

라벨: `UNKNOWN`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0524](../rules/damage.md#m-0524) `wiki-sigils-ingenuity-016`: "Shields and Sleeping Bags stop it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
  - 번역: Shield와 Sleeping Bag이 막아 줍니다.
- [M-0524](../rules/damage.md#m-0524) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Shield는 존 피해, 언세이프 서클 피해, robot 피해를 막지 못합니다.
- [M-0524](../rules/damage.md#m-0524) `wiki-damage-007`: "Robot | Safety bubble, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: Robot | Safety bubble, Hazmat suit (감속), Body armor (흡수)

**형식 모델:**

- [M-0524](../rules/damage.md#m-0524) 해석 A: `robot 피해는 Shield와 Sleeping Bag이 막음 (Ingenuity 페이지)`
- [M-0524](../rules/damage.md#m-0524) 해석 B: `robot 피해는 Shield나 Sleeping Bag이 막지 못함 (피해 페이지). Safety bubble이 막고, Hazmat suit이 감속시키고, Body armor가 흡수함`
- [M-0524](../rules/damage.md#m-0524) 정의역: 방어자 상태별 차단 여부 (참/거짓)
- [M-0524](../rules/damage.md#m-0524) 매개변수 `shield_blocks`: 모순, [C-0500](../unknowns.md#c-0500) 참조
- [M-0524](../rules/damage.md#m-0524) 매개변수 `sleeping_bag_blocks`: 모순, [C-0500](../unknowns.md#c-0500) 참조

**상호작용:** [M-0523](../rules/weapons.md#m-0523)

**모순:** [C-0500](../unknowns.md#c-0500)

메모 ([M-0524](../rules/damage.md#m-0524)): 모순 [C-0500](../unknowns.md#c-0500). 피해 페이지는 robot 피해를 sleeping bag 면역의 예외로도 나열합니다.

<a id="m-0529"></a>

### M-0529: Fortress 조합품

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0529](../rules/damage.md#m-0529) `wiki-sigils-ingenuity-030`: "Protects everyone within 20m (66ft) of it for up to 30 HP, and from Sigil of Greed stealing, and zone damage." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))
  - 번역: 20m (66ft) 이내의 모든 이를 최대 30 HP까지, 그리고 Sigil of Greed 훔치기와 존 피해로부터 보호합니다.
- [M-0529](../rules/damage.md#m-0529) `wiki-damage-052`: "A fortress you stand within absorbs up to its remaining durability, whoever built it." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 자신이 그 안에 서 있는 fortress는 누가 지었든 남은 내구도까지 흡수합니다.

**형식 모델:**

- [M-0529](../rules/damage.md#m-0529) 해석 A: `x에 있는 fortress: x의 20 m 이내 모든 참가자가 보호됨. 내구도 D = 30을 공유. 타격 6단계가 min(d, D)를 흡수하고 D -= 흡수량. Greed 훔치기도 막음. 존 피해는 완전히 면역`
- [M-0529](../rules/damage.md#m-0529) 해석 B: `보호받는 참가자마다 30 HP의 흡수`
- [M-0529](../rules/damage.md#m-0529) 해석 C: `존 피해는 내구도에서 흡수됨`
- [M-0529](../rules/damage.md#m-0529) 정의역: 미터 단위 dist 0..20. D는 정수 0..30
- [M-0529](../rules/damage.md#m-0529) 매개변수 `radius_m`: 20
- [M-0529](../rules/damage.md#m-0529) 매개변수 `durability_hp`: 30
- [M-0529](../rules/damage.md#m-0529) 매개변수 `duration_s`: UNKNOWN, see [U-0526](../unknowns.md#u-0526)

**따름 결과:** [T-0007](../theorems/T-0007.md), [T-0008](../theorems/T-0008.md), [T-0305](../theorems/T-0305.md)

**상호작용:** [M-0511](../rules/sigil.md#m-0511), [M-0522](../rules/items.md#m-0522)

**미해결 질문:**

- [U-0524](../unknowns.md#u-0524) (높음): Fortress의 "up to 30 HP": 20 m 안의 모두가 공유하는 하나의 풀입니까, 아니면 한 사람당 30 HP입니까?
- [U-0525](../unknowns.md#u-0525) (높음): Fortress와 존 피해: 존 피해는 30 HP 내구도에서 흡수됩니까, 아니면 완전히 무시됩니까?
- [U-0526](../unknowns.md#u-0526) (높음): Fortress의 지속 시간과 위치: 얼마나 유지되며, 설치한 자리에 고정됩니까?

메모 ([M-0529](../rules/damage.md#m-0529)): 피해 페이지: 'A fortress you stand within absorbs up to its remaining durability, whoever built it' (6단계, Armor 이전). Ingenuity 문구는 세 가지 보호를 나열합니다: HP 흡수, Greed 훔치기, 존 피해.

<a id="m-0533"></a>

### M-0533: 가짜 상자 획득 효과

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-009`: "A contestant who claims it takes 5 HP damage and cannot claim chests for 1h." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 이를 획득한 참가자는 5 HP 피해를 입고 1h 동안 상자를 획득할 수 없습니다.
- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-010`: "You heal 5 HP." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 5 HP를 회복합니다.
- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-012`: "A Shield blocks the damage but not the lockout." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: Shield는 피해는 막지만 잠금은 막지 못합니다.
- [M-0533](../rules/damage.md#m-0533) `wiki-items-056`: "A reflected fake chest also locks the troll out of chests instead of you." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 반사된 가짜 상자는 또한 본인 대신 troll이 상자를 획득하지 못하게 잠급니다.

**형식 모델:**

- [M-0533](../rules/damage.md#m-0533) 해석 A: `claim(fake chest by contestant v): v가 타격 파이프라인을 거쳐 5 HP 피해를 입음 (Kick 보너스는 troll의 타격에 적용되고, 감소는 v에 적용됨). v는 3600 s 동안 상자를 획득할 수 없음. troll이 5 HP를 회복함. Shield는 피해는 막지만 잠금은 막지 못함`
- [M-0533](../rules/damage.md#m-0533) 해석 B: `troll은 피해가 막히지 않았을 때만 회복함`
- [M-0533](../rules/damage.md#m-0533) 해석 C: `잠금은 보급 상자와 crate에도 적용됨`
- [M-0533](../rules/damage.md#m-0533) 정의역: 보정 전 피해 정수 5. 잠금 3600 s
- [M-0533](../rules/damage.md#m-0533) 매개변수 `damage_hp`: 5
- [M-0533](../rules/damage.md#m-0533) 매개변수 `lockout_s`: 3600
- [M-0533](../rules/damage.md#m-0533) 매개변수 `troll_heal_hp`: 5
- [M-0533](../rules/damage.md#m-0533) 매개변수 `lockout_scope`: UNKNOWN, see [U-0531](../unknowns.md#u-0531)
- [M-0533](../rules/damage.md#m-0533) 매개변수 `heal_condition`: UNKNOWN, see [U-0532](../unknowns.md#u-0532)

**상호작용:** [M-0504](../rules/items.md#m-0504), [M-0531](../rules/economy.md#m-0531), [M-0532](../rules/items.md#m-0532)

**미해결 질문:**

- [U-0531](../unknowns.md#u-0531) (보통): 가짜 상자 잠금 "1h 동안 상자를 열 수 없음": 보급 상자와 크레이트도 막습니까, 두 번째로 열면 연장됩니까, 그리고 Shield 외의 방어 수단(Safety bubble, Sleeping Bag, Body armor)도 잠금은 그대로 남겨 둡니까?
- [U-0532](../unknowns.md#u-0532) (보통): Trolling 가짜 상자 "5 HP를 회복합니다": 열 때 고정된 5 HP입니까, 실제로 들어간 피해입니까, 그리고 피해자가 보호받거나 상자가 반사된 경우에도 발생합니까?
- [U-0001](../unknowns.md#u-0001) (치명적): 방어자의 Kick 라이브 10% 감소는 결과를 내림하는 것입니까(A), 아니면 제거되는 10%를 내림하는 것입니까(B)?
- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?

메모 ([M-0533](../rules/damage.md#m-0533)): 피해 페이지 행: 가짜 상자는 Shield, Safety bubble, Sleeping Bag, Mirror forcefield(반사), Body armor(흡수)가 막으며, Kick 보너스 목록에 가짜 상자가 포함됩니다. Protection 참가자도 가짜 상자 피해를 입습니다. Mirror forcefield가 있으면 잠금을 포함한 전체 효과가 troll에게 되돌아갑니다 (아이템 페이지).

<a id="m-0536"></a>

### M-0536: 언세이프 서클 피해

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-017`: "Anyone inside it who is also inside a safe zone takes zone damage with no grace period" ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 서클 안에 있으면서 세이프 존 안에도 있는 사람은 유예 시간 없이 존 피해를 받습니다
- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-022`: "It hurts like the outside of the safe zone: 1 HP every 2s, first hit one interval after you enter, with no grace period." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: 세이프 존 바깥과 같이 피해를 줍니다. 2s마다 HP 1이며, 진입 후 한 간격이 지난 시점에 첫 타격이 들어오고 유예 시간은 없습니다.
- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-023`: "Only the part inside a safe zone hurts: outside every safe zone you take normal zone damage only." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: 세이프 존 안에 있는 부분만 피해를 줍니다. 모든 세이프 존 바깥에서는 일반 존 피해만 받습니다.

**형식 모델:**

- [M-0536](../rules/damage.md#m-0536) 해석 A: `서클 안이면서 세이프 존 안에 있는 참가자 v에 대해: 안에서 2 s가 지난 뒤 2 s마다 HP 1. 5 s 유예 없음. 모든 세이프 존 바깥에서는 일반 존 피해만 받음(첫 틱은 통상의 유예 이후)`
- [M-0536](../rules/damage.md#m-0536) 해석 B: `존 안쪽 부분과 바깥쪽 부분 사이를 오가도 타이머가 유지됨`
- [M-0536](../rules/damage.md#m-0536) 해석 C: `전역 2 s 틱`
- [M-0536](../rules/damage.md#m-0536) 정의역: 진입 이후 t >= 0 s, 틱당 HP 1
- [M-0536](../rules/damage.md#m-0536) 매개변수 `interval_s`: 2
- [M-0536](../rules/damage.md#m-0536) 매개변수 `damage_hp`: 1
- [M-0536](../rules/damage.md#m-0536) 매개변수 `grace_s`: 0
- [M-0536](../rules/damage.md#m-0536) 매개변수 `first_hit`: 진입 후 한 간격 뒤

**따름 결과:** [T-0305](../theorems/T-0305.md)

**상호작용:** [M-0537](../rules/items.md#m-0537), [M-0538](../rules/damage.md#m-0538)

**미해결 질문:**

- [U-0537](../unknowns.md#u-0537) (높음): 언세이프 서클(unsafe circle) 피해 시계: 첫 타격은 진입마다 2 s 뒤입니까(나갈 때 타이머 초기화), 아니면 전역 2 s 위상이 계속됩니까? 서클 중 세이프 존 안쪽 부분과 바깥 부분 사이를 이동하면 초기화됩니까?
- [U-0003](../unknowns.md#u-0003) (보통): 존 피해: 세이프 존을 벗어난 뒤 첫 틱은 5 s입니까, 7 s입니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)?

메모 ([M-0536](../rules/damage.md#m-0536)): Hazmat suit는 존 피해 간격마다 2 s를 늘리며(아이템 페이지), 피해 페이지에도 언세이프 서클 피해를 늦추는 것으로 나열되어 있습니다. Body armor는 이를 흡수합니다. 일반 존 피해의 첫 틱은 [U-0003](../unknowns.md#u-0003)입니다.

<a id="m-0538"></a>

### M-0538: 언세이프 서클 차단 수단

라벨: `UNKNOWN`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0538](../rules/damage.md#m-0538) `wiki-sigils-trolling-027`: "A Guardian angel, a Safety bubble, a Reality Shield or a Death Ward blocks it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: Guardian angel, Safety bubble, Reality Shield 또는 Death Ward가 이를 막습니다.
- [M-0538](../rules/damage.md#m-0538) `wiki-sigils-trolling-028`: "A Shield does not." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: Shield는 막지 못합니다.
- [M-0538](../rules/damage.md#m-0538) `wiki-damage-006`: "Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (늦춤), Body armor (흡수)

**형식 모델:**

- [M-0538](../rules/damage.md#m-0538) 해석 A: `언세이프 서클 피해와 아이템 상실은 Guardian angel, Safety bubble, Reality Shield 또는 Death Ward가 차단함(Trolling 페이지). Shield는 차단하지 못함`
- [M-0538](../rules/damage.md#m-0538) 해석 B: `피해 표의 행: Safety bubble, Guardian angel, Death Ward가 차단. Hazmat suit는 늦춤. Body armor는 흡수. Reality Shield는 이 행에 없음`
- [M-0538](../rules/damage.md#m-0538) 정의역: 방어자 상태별 불리언 차단 여부
- [M-0538](../rules/damage.md#m-0538) 매개변수 `shield_blocks`: false
- [M-0538](../rules/damage.md#m-0538) 매개변수 `reality_shield_blocks`: 모순, [C-0502](../unknowns.md#c-0502) 참조

**상호작용:** [M-0536](../rules/damage.md#m-0536), [M-0537](../rules/items.md#m-0537)

**모순:** [C-0502](../unknowns.md#c-0502)

메모 ([M-0538](../rules/damage.md#m-0538)): 불일치는 Reality Shield뿐입니다. 피해 페이지의 주석(다른 조항)에도 Safety bubble과 Reality Shield가 존 피해, 언세이프 서클 피해, Robot 피해를 막는다고 되어 있어 해석 A를 뒷받침합니다.

<a id="m-0643"></a>

### M-0643: Protection은 핵폭탄 피해를 50% 덜 받음

라벨: `DOCUMENTED`. 시길: protection.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0643](../rules/damage.md#m-0643) `wiki-sigils-protection-013`: "Nukes deal 50% less damage to you." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 핵폭탄은 당신에게 50% 적은 피해를 줍니다.
- [M-0643](../rules/damage.md#m-0643) `wiki-damage-044`: "A Protection contestant takes 50% less from a nuke." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Protection 참가자는 핵폭탄 피해를 50% 덜 받습니다.
- [M-0643](../rules/damage.md#m-0643) `wiki-damage-045`: "The damage left is rounded down." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 남은 피해는 내림합니다.
- [M-0643](../rules/damage.md#m-0643) `wiki-attacks-016`: "The Protection sigil is not immune, but takes 50% less." ([출처](https://iceposeidon.com/safezone/wiki/attacks#nuke))
  - 번역: Protection 시길은 면역이 아니지만, 피해를 50% 덜 받습니다.

**형식 모델:**

- [M-0643](../rules/damage.md#m-0643) 해석 A: `d -> floor(d/2) (감소 4단계, Kick 라이브 감소 이전)`
- [M-0643](../rules/damage.md#m-0643) 정의역: d는 정수

**모순:** [C-0602](../unknowns.md#c-0602)

메모 ([M-0643](../rules/damage.md#m-0643)): Kick 라이브 감소 및 최소 1 HP와의 순서는 피해 페이지(4단계와 5단계)에 주어져 있습니다. Kick 10%가 어디에 적용되는지는 [U-0001](../unknowns.md#u-0001)을 참조하십시오.

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0001](../theorems/T-0001.md), [T-0002](../theorems/T-0002.md), [T-0003](../theorems/T-0003.md), [T-0004](../theorems/T-0004.md), [T-0007](../theorems/T-0007.md), [T-0008](../theorems/T-0008.md), [T-0305](../theorems/T-0305.md), [T-0402](../theorems/T-0402.md), [T-0702](../theorems/T-0702.md), [T-0703](../theorems/T-0703.md)

## 미해결 질문

[U-0001](../unknowns.md#u-0001), [U-0002](../unknowns.md#u-0002), [U-0003](../unknowns.md#u-0003), [U-0005](../unknowns.md#u-0005), [U-0010](../unknowns.md#u-0010), [U-0100](../unknowns.md#u-0100), [U-0101](../unknowns.md#u-0101), [U-0102](../unknowns.md#u-0102), [U-0103](../unknowns.md#u-0103), [U-0117](../unknowns.md#u-0117), [U-0118](../unknowns.md#u-0118), [U-0119](../unknowns.md#u-0119), [U-0120](../unknowns.md#u-0120), [U-0121](../unknowns.md#u-0121), [U-0123](../unknowns.md#u-0123), [U-0524](../unknowns.md#u-0524), [U-0525](../unknowns.md#u-0525), [U-0526](../unknowns.md#u-0526), [U-0531](../unknowns.md#u-0531), [U-0532](../unknowns.md#u-0532), [U-0537](../unknowns.md#u-0537)

## 신뢰도

`UNKNOWN`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
