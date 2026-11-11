# 규칙: 회복(healing)

## 요약

`healing` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

회복 계열은 살아 있는 동안 HP를 되찾는 모든 방법을 다룹니다. (죽음에서 되살리는 것은 대신 부활 계열에 속합니다.) 일반 소모품, 몇 가지 시길 보너스와 페널티, 그리고 Healing 시길 고유의 능력이 있습니다.

기본은 포션과 붕대입니다. 체력 포션은 등급별로 회복합니다. Small 5 HP, Medium 10 HP, Large 20 HP, Gigantic 40 HP입니다 ([M-0207](../rules/healing.md#m-0207)). Eddie의 포션은 도박입니다. 10% 확률로 최대 HP의 50%를 회복하고, 그렇지 않으면 최대 HP의 30%를 잃습니다 ([M-0208](../rules/healing.md#m-0208)). 붕대는 2분에 걸쳐 10 HP를 회복하며, 피해를 받아도 중단되지 않습니다 ([M-0233](../rules/healing.md#m-0233)). 붕대는 Deep Cut 출혈도 멈춥니다 ([M-0234](../rules/healing.md#m-0234)).

시길은 이 수치를 바꿉니다. Piety의 포션은 15% 더 회복하며 내림 처리됩니다 ([M-0505](../rules/healing.md#m-0505)). Protection의 포션은 50% 덜 회복하지만 ([M-0645](../rules/healing.md#m-0645)), 붕대는 1.1배의 시간 동안 지속됩니다 ([M-0646](../rules/healing.md#m-0646)). Ingenuity는 Campfire를 조합할 수 있는데, 10 m (33 ft) 이내의 모든 사람을 초당 1 HP씩 회복시키며, 회복량은 포션의 회복량과 같은 하나의 공유 풀에서 나옵니다 ([M-0525](../rules/healing.md#m-0525)). 또한 독을 치료하고 포션 등급만큼 회복하는 Everything potion도 조합할 수 있습니다 ([M-0526](../rules/healing.md#m-0526)). Healing 시길 자체는 근처 참가자를 1 HP 회복시키고, 그 참가자의 독을 치료하고 Deep Cut 출혈을 멈추며, 쿨다운은 10분입니다 ([M-0651](../rules/healing.md#m-0651)). 최대 HP까지 30분마다 1 HP를 재생하는 것은 다른 시길이 아니라 Healing 시길입니다 ([M-0652](../rules/healing.md#m-0652)).

플레이어가 느끼는 점: 회복은 대체로 무엇을 들고 다니느냐의 문제입니다. 포션은 빠르고, 붕대는 느리지만 방해받지 않습니다 ([M-0233](../rules/healing.md#m-0233)). Eddie의 포션에 담긴 도박은 손실이 크기 때문에 실제 위험입니다 ([M-0208](../rules/healing.md#m-0208)).

효과적인 대상: 붕대와 Healing 시길의 능력은 모두 Deep Cut 출혈을 멈춥니다 ([M-0234](../rules/healing.md#m-0234), [M-0651](../rules/healing.md#m-0651)). Healing 능력은 독도 치료합니다 ([M-0651](../rules/healing.md#m-0651)).

기재된 바에 따른 가장 약한 점: 작은 수치입니다. Healing 시길 자체의 회복은 1 HP이고 ([M-0651](../rules/healing.md#m-0651)), 재생은 30분마다 1 HP입니다 ([M-0652](../rules/healing.md#m-0652)).

알 수 없는 것: 포션, 붕대 틱, Eddie의 회복이 최대 HP에서 상한이 걸리는지 ([U-0203](../unknowns.md#u-0203)), 붕대 틱 일정 ([U-0214](../unknowns.md#u-0214)), Eddie의 수치가 어떻게 끝수 처리되는지 ([U-0204](../unknowns.md#u-0204))입니다. Eddie의 손실이 죽음을 일으킬 수 있는지는 미해결입니다 ([U-0004](../unknowns.md#u-0004)). Piety 보너스가 최대 HP 제한 전에 끝수 처리되는지 후에 처리되는지도 미해결입니다 ([U-0503](../unknowns.md#u-0503)). Protection에서 어떤 회복이 포션으로 취급되는지 ([U-0617](../unknowns.md#u-0617))와 그 끝수 처리 ([U-0618](../unknowns.md#u-0618))도 미해결입니다. 여러 사람이 있을 때 Campfire 풀이 어떻게 소진되는지 ([U-0520](../unknowns.md#u-0520))와 피해가 재생 타이머를 초기화하는지 ([U-0007](../unknowns.md#u-0007))도 미해결입니다.

이 페이지는 규칙 11개(1 `DOCUMENTED`, 10 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0207"></a>

### M-0207: 등급별 체력 포션 회복량

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0207](../rules/healing.md#m-0207) `wiki-items-008`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#health_potion))
  - 번역: 사용 가능
- [M-0207](../rules/healing.md#m-0207) `wiki-items-009`: "Heals by tier: Small 5 HP, Medium 10 HP, Large 20 HP, Gigantic 40 HP." ([출처](https://iceposeidon.com/safezone/wiki/items#health_potion))
  - 번역: 등급별로 회복합니다: Small 5 HP, Medium 10 HP, Large 20 HP, Gigantic 40 HP.

**형식 모델:**

- [M-0207](../rules/healing.md#m-0207) 해석 A: `hp' = min(maxHP, hp + h)`
- [M-0207](../rules/healing.md#m-0207) 해석 B: `hp' = hp + h, 최대 HP 상한 없음(상한은 다른 곳에서 적용되거나 전혀 적용되지 않음)`
- [M-0207](../rules/healing.md#m-0207) 정의역: tier in {Small, Medium, Large, Gigantic}; 0 < hp <= maxHP
- [M-0207](../rules/healing.md#m-0207) 매개변수 `Small`: 5 HP
- [M-0207](../rules/healing.md#m-0207) 매개변수 `Medium`: 10 HP
- [M-0207](../rules/healing.md#m-0207) 매개변수 `Large`: 20 HP
- [M-0207](../rules/healing.md#m-0207) 매개변수 `Gigantic`: 40 HP

**상호작용:** [M-0202](../rules/items.md#m-0202), [M-0208](../rules/healing.md#m-0208)

**미해결 질문:**

- [U-0203](../unknowns.md#u-0203) (보통): 체력 포션, bandage 틱, Eddie의 회복은 최대 HP로 제한됩니까?

메모 ([M-0207](../rules/healing.md#m-0207)): Piety는 자체 페이지에서 15% 내림을 더합니다: 정확한 정수 연산에서 5->5, 10->11, 20->23, 40->46입니다(binary64는 [U-0006](../unknowns.md#u-0006)). 현상금 보상은 무작위 체력 포션을 줍니다(공격 페이지).

<a id="m-0208"></a>

### M-0208: Eddie's potion의 도박

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0208](../rules/healing.md#m-0208) `wiki-items-010`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#eddies_potion))
  - 번역: 사용 가능
- [M-0208](../rules/healing.md#m-0208) `wiki-items-011`: "A gamble: 10% chance to heal 50% of your max HP." ([출처](https://iceposeidon.com/safezone/wiki/items#eddies_potion))
  - 번역: 도박입니다: 10% 확률로 최대 HP의 50%를 회복합니다.
- [M-0208](../rules/healing.md#m-0208) `wiki-items-012`: "Otherwise you lose 30% of your max HP." ([출처](https://iceposeidon.com/safezone/wiki/items#eddies_potion))
  - 번역: 그렇지 않으면 최대 HP의 30%를 잃습니다.

**형식 모델:**

- [M-0208](../rules/healing.md#m-0208) 해석 A: `p=0.1: hp += floor(M/2); 아니면 hp -= floor(3*M/10)`
- [M-0208](../rules/healing.md#m-0208) 해석 B: `p=0.1: hp += ceil(M/2); 아니면 hp -= ceil(3*M/10)`
- [M-0208](../rules/healing.md#m-0208) 해석 C: `p=0.1: hp += round(M/2); 아니면 hp -= round(3*M/10) (0.5는 올림)`
- [M-0208](../rules/healing.md#m-0208) 해석 D: `혼합: 회복과 손실의 어림 방향이 서로 반대임`
- [M-0208](../rules/healing.md#m-0208) 정의역: M = 최대 HP 정수; hp 1..M; 결과는 서로 배타적, P(heal)=1/10, P(loss)=9/10
- [M-0208](../rules/healing.md#m-0208) 매개변수 `heal_chance`: 10%
- [M-0208](../rules/healing.md#m-0208) 매개변수 `heal_fraction`: 최대 HP의 50%
- [M-0208](../rules/healing.md#m-0208) 매개변수 `loss_fraction`: 최대 HP의 30%
- [M-0208](../rules/healing.md#m-0208) 매개변수 `rounding`: UNKNOWN, [U-0204](../unknowns.md#u-0204) 참조

**상호작용:** [M-0207](../rules/healing.md#m-0207)

**미해결 질문:**

- [U-0004](../unknowns.md#u-0004) (높음): Eddie의 포션 30% 손실이 사망을 일으킬 수 있으며, armor, fortress 또는 Kick 상태가 여기에 적용됩니까?
- [U-0204](../unknowns.md#u-0204) (낮음): 최대 HP가 10의 배수가 아닐 때 Eddie의 포션의 50% 회복과 30% 손실은 어떤 방식으로 어림됩니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, robot, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?
- [U-0203](../unknowns.md#u-0203) (보통): 체력 포션, bandage 틱, Eddie의 회복은 최대 HP로 제한됩니까?

메모 ([M-0208](../rules/healing.md#m-0208)): M이 10의 배수이면 모든 해석이 일치합니다(회복 M/2, 손실 3M/10). 시길은 최대 HP를 10만큼 바꾸므로(Piety +10, Greed -10), 기본 HP가 10의 배수가 아닐 때만 반올림이 문제가 됩니다. 피해 페이지는 Eddie's Potion 역효과를 Shield, Safety bubble, Sleeping Bag, Body armor(흡수)가 막는 것으로 나열합니다([U-0004](../unknowns.md#u-0004) 참조). 회복량은 '잃은 HP'가 아니라 '최대 HP'의 비율입니다.

<a id="m-0233"></a>

### M-0233: Bandage의 지속 회복

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0233](../rules/healing.md#m-0233) `wiki-items-048`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#bandage))
  - 번역: 사용 가능
- [M-0233](../rules/healing.md#m-0233) `wiki-items-049`: "Heals 10 HP over 2min." ([출처](https://iceposeidon.com/safezone/wiki/items#bandage))
  - 번역: 2min 동안 10 HP를 회복합니다.
- [M-0233](../rules/healing.md#m-0233) `wiki-items-050`: "Taking damage does not stop it." ([출처](https://iceposeidon.com/safezone/wiki/items#bandage))
  - 번역: 피해를 받아도 중단되지 않습니다.

**형식 모델:**

- [M-0233](../rules/healing.md#m-0233) 해석 A: `1 HP씩 10틱, 첫 틱은 +12 s, 마지막 틱은 +120 s`
- [M-0233](../rules/healing.md#m-0233) 해석 B: `1 HP씩 10틱, 첫 틱은 +0 s, 마지막 틱은 +108 s`
- [M-0233](../rules/healing.md#m-0233) 해석 C: `24 s마다 2 HP씩 5틱`
- [M-0233](../rules/healing.md#m-0233) 해석 D: `12 s당 1 HP를 소수 단위로 누적하는 연속 회복 (총 120 s)`
- [M-0233](../rules/healing.md#m-0233) 정의역: t in [0,120] 초. 총 10 HP. 피해는 중단시키지 않음
- [M-0233](../rules/healing.md#m-0233) 매개변수 `total`: 10 HP
- [M-0233](../rules/healing.md#m-0233) 매개변수 `duration`: 2min
- [M-0233](../rules/healing.md#m-0233) 매개변수 `tick_schedule`: UNKNOWN, [U-0214](../unknowns.md#u-0214) 참조

**상호작용:** [M-0206](../rules/items.md#m-0206), [M-0234](../rules/healing.md#m-0234)

**미해결 질문:**

- [U-0214](../unknowns.md#u-0214) (보통): Bandage의 틱 일정은 어떻게 됩니까: 2min 동안 10 HP?
- [U-0203](../unknowns.md#u-0203) (보통): 체력 포션, bandage 틱, Eddie의 회복은 최대 HP로 제한됩니까?

메모 ([M-0233](../rules/healing.md#m-0233)): Protection 시길: bandage의 지속 시간이 1.1x가 됩니다 (132 s). 총 HP도 바뀌는지는 해당 페이지에 있습니다. 각 틱은 최대 HP에서 상한이 걸릴 수도 있고 아닐 수도 있습니다.

<a id="m-0234"></a>

### M-0234: Bandage는 Deep Cut 출혈을 멈춤

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0234](../rules/healing.md#m-0234) `wiki-items-051`: "It also stops Deep Cut bleeding." ([출처](https://iceposeidon.com/safezone/wiki/items#bandage))
  - 번역: Deep Cut 출혈도 멈춥니다.
- [M-0234](../rules/healing.md#m-0234) `wiki-merchant-043`: "Your next bow, knife, long sword, axe, machete or drone hit, or Poison Dart, causes bleeding: 1 HP every five minutes until a bandage or a Healing contestant cures it." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 당신의 다음 bow, knife, long sword, axe, machete 또는 drone 타격이나 Poison Dart는 출혈을 일으킵니다: bandage 또는 Healing 참가자가 치료할 때까지 5분마다 1 HP.

**형식 모델:**

- [M-0234](../rules/healing.md#m-0234) 해석 A: `bandage를 사용하면 Deep Cut 출혈이 끝남`
- [M-0234](../rules/healing.md#m-0234) 정의역: 출혈 불리언

**상호작용:** [M-0233](../rules/healing.md#m-0233)

메모 ([M-0234](../rules/healing.md#m-0234)): 상인 페이지: 출혈은 bandage 또는 Healing 참가자가 치료할 때까지 5분마다 1 HP입니다. 사용 시점에 멈추는지 회복이 끝날 때 멈추는지는 명시되어 있지 않습니다.

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

<a id="m-0525"></a>

### M-0525: Campfire 조합품

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0525](../rules/healing.md#m-0525) `wiki-sigils-ingenuity-019`: "Heals everyone within 10m (33ft) 1 HP per second from one shared pool equal to the potion's heal." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
  - 번역: 10m (33ft) 이내의 모든 이를 포션의 회복량과 같은 하나의 공유 풀에서 초당 1 HP씩 회복시킵니다.
- [M-0525](../rules/healing.md#m-0525) `wiki-sigils-ingenuity-020`: "It burns out when the pool is empty or after 10min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
  - 번역: 풀이 비거나 10min이 지나면 꺼집니다.
- [M-0525](../rules/healing.md#m-0525) `wiki-sigils-ingenuity-021`: "Piety and Protection potion changes do not apply." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
  - 번역: Piety와 Protection의 포션 변경은 적용되지 않습니다.

**형식 모델:**

- [M-0525](../rules/healing.md#m-0525) 해석 A: `campfire 풀 = 사용한 포션의 회복량 (small 5, medium 10, large 20, gigantic 40 HP, 기본값). 매초 10 m 이내에서 HP가 줄어든 모든 참가자가 +1 HP를 받고 풀은 -1. 풀이 0이 되거나 600 s 후에 끝남`
- [M-0525](../rules/healing.md#m-0525) 해석 B: `풀은 공유되어 합계로 초당 1 HP를 지급함`
- [M-0525](../rules/healing.md#m-0525) 해석 C: `범위 안의 모든 참가자가 줄어든 HP와 관계없이 초당 1 HP씩 풀에서 소모함`
- [M-0525](../rules/healing.md#m-0525) 정의역: 풀은 정수 0..40. 지속 시간 600 s
- [M-0525](../rules/healing.md#m-0525) 매개변수 `rate_hp_per_s`: 1
- [M-0525](../rules/healing.md#m-0525) 매개변수 `radius_m`: 10
- [M-0525](../rules/healing.md#m-0525) 매개변수 `max_duration_s`: 600
- [M-0525](../rules/healing.md#m-0525) 매개변수 `pool`: 포션의 등급 회복량, Piety +15% 없음, Protection -50% 없음
- [M-0525](../rules/healing.md#m-0525) 매개변수 `pool_drain`: UNKNOWN, see [U-0520](../unknowns.md#u-0520)

**상호작용:** [M-0501](../rules/economy.md#m-0501), [M-0505](../rules/healing.md#m-0505), [M-0518](../rules/items.md#m-0518), [M-0521](../rules/economy.md#m-0521)

**미해결 질문:**

- [U-0520](../unknowns.md#u-0520) (높음): Campfire 공유 풀: 여러 사람이 있을 때 풀은 어떻게 소모되며, HP가 가득 찬 주변인도 회복됩니까?
- [U-0502](../unknowns.md#u-0502) (높음): Piety 'from any source except revives, Campfires and healing circles included': Campfire와 healing circle은 집계됩니까(부활만 제외), 아니면 부활과 함께 제외됩니까?

메모 ([M-0525](../rules/healing.md#m-0525)): Piety와 Protection의 포션 변경은 적용되지 않는다고 명시되어 있으므로, 풀은 등급의 원래 값입니다. Campfire의 회복은 Ingenuity 수입(HP당 토큰 1개)에서 HP로 셈하며, Piety 제외/포함 문제 [U-0502](../unknowns.md#u-0502)에도 해당됩니다. 'Everyone'에는 소유자와 다른 시길이 포함되며, 적은 제외되지 않습니다.

<a id="m-0526"></a>

### M-0526: Everything potion 조합품

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0526](../rules/healing.md#m-0526) `wiki-sigils-ingenuity-023`: "Cures poison and heals by potion tier." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-everything_potion))
  - 번역: 독을 치료하고 포션 등급에 따라 회복합니다.

**형식 모델:**

- [M-0526](../rules/healing.md#m-0526) 해석 A: `사용 -> 독 치료. 재료인 Health potion의 등급만큼 HP 회복`
- [M-0526](../rules/healing.md#m-0526) 해석 B: `A와 같고, Anti poison 아이템처럼 600 s의 독 면역도 부여함`
- [M-0526](../rules/healing.md#m-0526) 정의역: 등급은 5, 10, 20, 40 HP
- [M-0526](../rules/healing.md#m-0526) 매개변수 `heal`: 재료 포션의 등급
- [M-0526](../rules/healing.md#m-0526) 매개변수 `immunity`: UNKNOWN, see [U-0521](../unknowns.md#u-0521)

**상호작용:** [M-0518](../rules/items.md#m-0518), [M-0522](../rules/items.md#m-0522)

**미해결 질문:**

- [U-0521](../unknowns.md#u-0521) (낮음): Everything potion의 "Cures poison and heals by potion tier": Anti poison의 10 min 독 면역도 부여합니까?

메모 ([M-0526](../rules/healing.md#m-0526)): 독 페이지는 Anti poison, Healing 시길의 회복, God's Fruit을 치료 수단으로 나열하며, Everything potion의 치료는 여기에서만 명시됩니다. Anti poison의 독 면역은 10 min 지속됩니다 (아이템 페이지).

<a id="m-0645"></a>

### M-0645: Protection의 포션은 50% 덜 회복함

라벨: `CONDITIONAL`. 시길: protection.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0645](../rules/healing.md#m-0645) `wiki-sigils-protection-016`: "Potions heal you 50% less." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 포션이 당신을 50% 덜 회복시킵니다.

**형식 모델:**

- [M-0645](../rules/healing.md#m-0645) 해석 A: `heal -> floor(h/2)`
- [M-0645](../rules/healing.md#m-0645) 해석 B: `heal -> ceil(h/2)`
- [M-0645](../rules/healing.md#m-0645) 해석 C: `heal -> h/2 (정확히)`
- [M-0645](../rules/healing.md#m-0645) 정의역: h는 정수: 체력 포션 등급 5, 10, 20, 40, Eddie의 포션은 최대 HP의 50%

**미해결 질문:**

- [U-0617](../unknowns.md#u-0617) (높음): Protection의 "Potions heal you 50% less": 어떤 회복이 "포션"입니까(회복 포션, Eddie의 포션, God's Fruit, 붕대, 회복 서클)?
- [U-0618](../unknowns.md#u-0618) (낮음): Protection의 포션 회복 "less 50%": 등급 수치가 홀수일 때(Small potion 5 HP) 끝수 처리는 어떻게 됩니까?

메모 ([M-0645](../rules/healing.md#m-0645)): 범위(어떤 아이템이 포션에 해당하는지)는 [U-0617](../unknowns.md#u-0617)입니다.

<a id="m-0646"></a>

### M-0646: Protection의 붕대는 1.1배 더 오래 지속됨

라벨: `CONDITIONAL`. 시길: protection.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0646](../rules/healing.md#m-0646) `wiki-sigils-protection-017`: "Bandages last 1.1x as long." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 붕대가 1.1배 더 오래 지속됩니다.
- [M-0646](../rules/healing.md#m-0646) `wiki-items-049`: "Heals 10 HP over 2min." ([출처](https://iceposeidon.com/safezone/wiki/items#bandage))
  - 번역: 2min에 걸쳐 10 HP를 회복합니다.

**형식 모델:**

- [M-0646](../rules/healing.md#m-0646) 해석 A: `붕대: 132 s에 걸쳐 총 10 HP`
- [M-0646](../rules/healing.md#m-0646) 해석 B: `붕대: 기존 속도 그대로 132 s에 걸쳐 총 11 HP`
- [M-0646](../rules/healing.md#m-0646) 정의역: 초, HP
- [M-0646](../rules/healing.md#m-0646) 매개변수 `duration_factor`: 1.1
- [M-0646](../rules/healing.md#m-0646) 매개변수 `base_duration_s`: 120

**미해결 질문:**

- [U-0619](../unknowns.md#u-0619) (보통): Protection의 "Bandages last 1.1x as long": 더 긴 시간에 걸쳐 총 회복량이 같습니까, 아니면 더 긴 시간 동안 회복 속도가 같습니까?

메모 ([M-0646](../rules/healing.md#m-0646)): 상호 참조: 붕대 아이템 페이지(2 min에 걸쳐 10 HP 회복).

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

**따름 결과:** [T-0011](../theorems/T-0011.md)

**미해결 질문:**

- [U-0007](../unknowns.md#u-0007) (보통): Healing 재생: 피해가 30 min 타이머를 초기화합니까?

메모 ([M-0652](../rules/healing.md#m-0652)): Necromancy가 아니라 Healing에 속합니다. 시계의 시작 시점(이벤트 시작인지, 시길 선택인지)도 미해결입니다.

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0011](../theorems/T-0011.md)

## 미해결 질문

[U-0002](../unknowns.md#u-0002), [U-0004](../unknowns.md#u-0004), [U-0006](../unknowns.md#u-0006), [U-0007](../unknowns.md#u-0007), [U-0203](../unknowns.md#u-0203), [U-0204](../unknowns.md#u-0204), [U-0214](../unknowns.md#u-0214), [U-0502](../unknowns.md#u-0502), [U-0503](../unknowns.md#u-0503), [U-0520](../unknowns.md#u-0520), [U-0521](../unknowns.md#u-0521), [U-0617](../unknowns.md#u-0617), [U-0618](../unknowns.md#u-0618), [U-0619](../unknowns.md#u-0619), [U-0622](../unknowns.md#u-0622), [U-0623](../unknowns.md#u-0623)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
