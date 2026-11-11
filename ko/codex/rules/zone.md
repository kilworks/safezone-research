# 규칙: 존(zone)

## 요약

`zone` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

존 계열은 모두를 움직이게 하고 정직하게 만드는 규칙입니다. 참가자는 세이프 존 안에 머물러야 하며, 이는 휴대폰의 GPS로 추적됩니다. 주최자가 존을 움직일 수 있으므로 크기나 속도가 바뀌거나 심지어 갈라질 수도 있습니다 ([M-0100](../rules/zone.md#m-0100)).

주된 페널티는 단순합니다. 밖에 있으면 5초 뒤부터 2초마다 1 HP의 피해를 받기 시작합니다 ([M-0101](../rules/zone.md#m-0101)).

실제로 밖으로 나가지 않고도 "밖"이 되는 방법이 두 가지 있습니다. 너무 빨리 움직이면 밖에 있는 것으로 칩니다. 1분 평균 20 mph보다 빠르거나 ([M-0105](../rules/zone.md#m-0105)), 15초 동안 어느 구간이든 30 mph보다 빠른 경우입니다 ([M-0106](../rules/zone.md#m-0106)). 그리고 마지막으로 알려진 위치가 세이프 존 안이었는데 휴대폰이 GPS 업데이트 전송을 멈추면, 15분 뒤, Kick 라이브 중이면 30분 뒤부터 피해를 받기 시작합니다 ([M-0104](../rules/zone.md#m-0104)). Kick 라이브 중인 참가자의 더 긴 오프라인 유예는 같은 규칙을 따로 서술한 것입니다 ([M-0103](../rules/zone.md#m-0103)).

Trolling 시길은 세이프 존의 일부를 위험 구역으로 바꿀 수 있습니다. 언세이프 서클은 세이프 존 안에 20분 동안 놓이며 쿨다운은 2시간입니다 ([M-0535](../rules/zone.md#m-0535)).

어떤 방어 수단이 있을까요? Hazmat suit는 소지하고 있는 동안 존 피해 간격마다 2 s를 늘려 줍니다 ([M-0209](../rules/items.md#m-0209)). Guardian angel은 10분 동안 존 피해에 대한 면역을 줍니다 ([M-0210](../rules/items.md#m-0210)). Safety bubble은 안에 있는 모든 사람을 존 피해를 포함한 피해에 면역으로 만듭니다 ([M-0213](../rules/items.md#m-0213)). Shield는 존 피해를 막지 못합니다 ([M-0128](../rules/damage.md#m-0128)).

기재된 바에 따른 가장 강한 점: 모두에게 똑같이 적용되며 어떤 시길에도 묶여 있지 않습니다 ([M-0101](../rules/zone.md#m-0101)). 가장 약한 점: 휴대폰과 GPS에 의존하는데, 이는 플레이어의 잘못 없이 실패할 수 있습니다 ([M-0104](../rules/zone.md#m-0104)).

알 수 없는 것: 첫 틱이 5초에 오는지 7초에 오는지 ([U-0003](../unknowns.md#u-0003))입니다. 오프라인 유예가 끝난 뒤 어떤 피해가 적용되는지 ([U-0110](../unknowns.md#u-0110))와 이후 GPS 업데이트가 유예 타이머를 초기화하는지 ([U-0111](../unknowns.md#u-0111))는 미해결입니다. 속도 평균이 슬라이딩 윈도우, 고정 윈도우, 비율 중 어떤 방식인지 ([U-0112](../unknowns.md#u-0112))와 속도 규칙이 발동하면 정확히 무슨 일이 일어나는지 ([U-0113](../unknowns.md#u-0113))도 미해결입니다. 세이프 존이 여러 개일 때 피해가 모든 존의 밖에 있을 때 시작되는지 마지막에 있던 존을 벗어날 때 시작되는지는 미해결입니다 ([U-0114](../unknowns.md#u-0114)). 언세이프 서클의 세부 사항, 즉 반지름인지 지름인지와 쿨다운이 언제 시작되는지도 미해결입니다 ([U-0535](../unknowns.md#u-0535), [U-0536](../unknowns.md#u-0536)).

이 페이지는 규칙 7개(7 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0100"></a>

### M-0100: 세이프 존은 주최자가 이동시킴 (크기, 속도, 분할)

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0100](../rules/zone.md#m-0100) `wiki-004`: "it can change in size or speed, or even split apart" ([출처](https://iceposeidon.com/safezone/wiki))
  - 번역: 크기나 속도가 바뀌거나 심지어 여러 개로 갈라질 수도 있습니다

**형식 모델:**

- [M-0100](../rules/zone.md#m-0100) 해석 A: `존의 기하는 주최자가 통제하는 외생적 과정 Z(t)이며, 규칙은 주어지지 않음`
- [M-0100](../rules/zone.md#m-0100) 매개변수 `zone_process`: UNKNOWN, [U-0114](../unknowns.md#u-0114) 참조

**미해결 질문:**

- [U-0114](../unknowns.md#u-0114) (높음): 존이 'split apart'할 수 있습니다: 세이프 존이 여럿일 때 'leave a safezone' 피해는 모든 존의 밖에 있을 때(A) 발동합니까, 아니면 마지막으로 있던 존을 떠날 때(B) 발동합니까?

메모 ([M-0100](../rules/zone.md#m-0100)): 크기 조정, 가속, 분할이 존재한다는 점만 명시되어 있습니다. 기하는 추상적인 상태로 둡니다.

<a id="m-0101"></a>

### M-0101: 세이프 존 밖 피해 틱

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0101](../rules/zone.md#m-0101) `wiki-005`: "after 5s you will start taking 1 HP damage every 2s (30 HP per minute)" ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 5s 후부터 2s마다 1 HP 피해를 입기 시작합니다 (분당 30 HP)

**형식 모델:**

- [M-0101](../rules/zone.md#m-0101) 해석 A: `t_out >= 5: t_out = 5, 7, 9, ...에서 HP 손실 1 (첫 틱은 5 s)`
- [M-0101](../rules/zone.md#m-0101) 해석 B: `t_out >= 5: t_out = 7, 9, 11, ...에서 HP 손실 1 (첫 틱은 한 간격 더 지난 뒤)`
- [M-0101](../rules/zone.md#m-0101) 정의역: t_out은 모든 세이프 존을 벗어난 뒤 경과한 정수 초, t_out >= 0
- [M-0101](../rules/zone.md#m-0101) 매개변수 `grace_s`: 5
- [M-0101](../rules/zone.md#m-0101) 매개변수 `interval_s`: 2
- [M-0101](../rules/zone.md#m-0101) 매개변수 `tick_hp`: 1

**미해결 질문:**

- [U-0003](../unknowns.md#u-0003) (보통): 존 피해: 세이프 존을 벗어난 뒤 첫 틱은 5 s입니까, 7 s입니까?
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, 로봇, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?
- [U-0114](../unknowns.md#u-0114) (높음): 존이 'split apart'할 수 있습니다: 세이프 존이 여럿일 때 'leave a safezone' 피해는 모든 존의 밖에 있을 때(A) 발동합니까, 아니면 마지막으로 있던 존을 떠날 때(B) 발동합니까?

메모 ([M-0101](../rules/zone.md#m-0101)): 분당 30 HP라는 수치는 60/2이며 두 해석 모두에서 성립합니다. 이 틱이 7단계 파이프라인의 타격인지는 [U-0002](../unknowns.md#u-0002)입니다. Kick 라이브 중에 내림 감소를 거친 1 HP는, [U-0002](../unknowns.md#u-0002)가 틱을 파이프라인에 포함시키는 경우에 한해 최소(minimum)에 의해 1로 올라갑니다. 언세이프 서클(unsafe circle, Trolling 시길 페이지)도 같은 방식으로 피해를 준다고 되어 있으며, 이는 이후 페이지 간 비교 단계에서 대조합니다.

<a id="m-0103"></a>

### M-0103: Kick 라이브 상태는 오프라인 유예 시간을 두 배로 늘림 (15분에서 30분)

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0103](../rules/zone.md#m-0103) `wiki-006`: "you have a longer offline grace period, so if your phone dies, you have 30min instead of 15min before you start taking damage" ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 오프라인 유예 시간이 더 길어서, 휴대폰이 꺼져도 피해를 입기 시작하기까지 15min이 아니라 30min이 주어집니다

**형식 모델:**

- [M-0103](../rules/zone.md#m-0103) 해석 A: `grace_s = Kick 라이브 중이면 1800, 아니면 900`
- [M-0103](../rules/zone.md#m-0103) 정의역: live in {true, false}
- [M-0103](../rules/zone.md#m-0103) 매개변수 `grace_live_s`: 1800
- [M-0103](../rules/zone.md#m-0103) 매개변수 `grace_base_s`: 900

**미해결 질문:**

- [U-0111](../unknowns.md#u-0111) (높음): 오프라인 유예 타이머의 의미: 마지막 GPS 갱신으로부터만 측정됩니까, 이후의 GPS 갱신이 타이머를 초기화합니까, 그리고 'live on Kick'은 GPS가 끊긴 순간(A), 만료 시점(B), 또는 부분 누적을 쓰는 연속 평가(C) 중 언제 판정됩니까?
- [U-0012](../unknowns.md#u-0012) (보통): Kick 라이브 상태는 어떻게 감지되며, 지연은 얼마입니까?

메모 ([M-0103](../rules/zone.md#m-0103)): 라이브 상태를 읽는 시점이 미해결 지점입니다 ([U-0111](../unknowns.md#u-0111)).

<a id="m-0104"></a>

### M-0104: 피해 전 GPS 오프라인 유예

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0104](../rules/zone.md#m-0104) `wiki-009`: "If your phone stops sending GPS updates, and your last known location was inside a safezone, you start taking damage after 15min, or 30min if you are live on Kick." ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 휴대폰이 GPS 갱신을 보내지 않고 마지막으로 알려진 위치가 세이프 존 안이었다면, 15min 후(Kick에서 라이브 중이면 30min 후)부터 피해를 입기 시작합니다.

**형식 모델:**

- [M-0104](../rules/zone.md#m-0104) 해석 A: `마지막 측위가 세이프 존 안이면: T_off >= grace (900 s, 라이브면 1800 s)에서 피해 시작`
- [M-0104](../rules/zone.md#m-0104) 해석 B: `마지막 측위가 세이프 존 안이면: T_off > grace (엄격 부등호)에서 피해 시작`
- [M-0104](../rules/zone.md#m-0104) 해석 C: `마지막 측위가 모든 세이프 존 밖이면: 유예 없음, 일반 존 밖 규칙이 적용됨 (명시되지 않았으며 조건에서 추정)`
- [M-0104](../rules/zone.md#m-0104) 정의역: T_off는 마지막 GPS 갱신 이후 경과한 정수 초
- [M-0104](../rules/zone.md#m-0104) 매개변수 `grace_base_s`: 900
- [M-0104](../rules/zone.md#m-0104) 매개변수 `grace_live_s`: 1800
- [M-0104](../rules/zone.md#m-0104) 매개변수 `damage_after_grace`: UNKNOWN, [U-0110](../unknowns.md#u-0110) 참조

**미해결 질문:**

- [U-0110](../unknowns.md#u-0110) (높음): 오프라인 유예가 끝난 뒤('you start taking damage after 15min') 어떤 피해가 적용됩니까? 서클 밖 규칙(5 s 유예 후 2 s마다 1 HP), 즉시 틱 주기, 또는 다른 것입니까?
- [U-0111](../unknowns.md#u-0111) (높음): 오프라인 유예 타이머의 의미: 마지막 GPS 갱신으로부터만 측정됩니까, 이후의 GPS 갱신이 타이머를 초기화합니까, 그리고 'live on Kick'은 GPS가 끊긴 순간(A), 만료 시점(B), 또는 부분 누적을 쓰는 연속 평가(C) 중 언제 판정됩니까?
- [U-0012](../unknowns.md#u-0012) (보통): Kick 라이브 상태는 어떻게 감지되며, 지연은 얼마입니까?

메모 ([M-0104](../rules/zone.md#m-0104)): 해석 C는 조건절 '마지막으로 알려진 위치가 세이프 존 안이었다면'에서만 나오며, 그렇지 않은 경우에 어떻게 되는지는 적혀 있지 않습니다. 소개 부분의 Kick 문장과 같은 수치(15min과 30min)이므로 일치합니다.

<a id="m-0105"></a>

### M-0105: 속도 규칙: 1 min 평균 속도가 20 mph를 넘으면 존 밖으로 간주

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0105](../rules/zone.md#m-0105) `wiki-010`: "Moving too fast counts as being outside: faster than 20mph (8.94m/s) on average over 1min" ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 너무 빠르게 움직이면 존 밖으로 간주됩니다: 1min 평균 20mph (8.94m/s)보다 빠른 경우

**형식 모델:**

- [M-0105](../rules/zone.md#m-0105) 해석 A: `60 s 구간의 mean_speed > 8.94 m/s이면 위반, 구간은 슬라이딩`
- [M-0105](../rules/zone.md#m-0105) 해석 B: `60 s 구간의 mean_speed > 8.9408 m/s (정확히 20 mph)이면 위반`
- [M-0105](../rules/zone.md#m-0105) 해석 C: `구간 변위는 이동 경로 길이가 아니라 양 끝점 사이 거리로 계산`
- [M-0105](../rules/zone.md#m-0105) 정의역: 속도 단위는 m/s, 구간은 60 s
- [M-0105](../rules/zone.md#m-0105) 매개변수 `threshold_ms`: 8.94
- [M-0105](../rules/zone.md#m-0105) 매개변수 `window_s`: 60

**미해결 질문:**

- [U-0112](../unknowns.md#u-0112) (높음): 속도 규칙의 평균: '20mph on average over 1min'은 슬라이딩 윈도, 고정 윈도, 거리 대 시간의 비율 중 무엇입니까? '30mph over any 15s'는 15 s 윈도의 같은 평균입니까, 아니면 최고 속도입니까? 비교는 엄격합니까? 8.94와 13.41 m/s가 정확한 임계값입니까?
- [U-0113](../unknowns.md#u-0113) (보통): 'Moving too fast counts as being outside': 속도 규칙이 발동하면 5 s 유예와 2 s당 1 HP가 서클 밖처럼 적용됩니까, 언제부터 시작됩니까, 그리고 속도가 떨어지는 즉시 끝납니까?

<a id="m-0106"></a>

### M-0106: 속도 규칙: 임의의 15 s 구간에서 속도가 30 mph를 넘으면 존 밖으로 간주

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0106](../rules/zone.md#m-0106) `wiki-010`: "or faster than 30mph (13.41m/s) over any 15s" ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 또는 어떤 15s 동안이든 30mph (13.41m/s)보다 빠른 경우

**형식 모델:**

- [M-0106](../rules/zone.md#m-0106) 해석 A: `어떤 15 s 구간의 mean_speed > 13.41 m/s이면 위반`
- [M-0106](../rules/zone.md#m-0106) 해석 B: `어떤 15 s 구간 중 최고 속도 > 13.41 m/s이면 위반`
- [M-0106](../rules/zone.md#m-0106) 해석 C: `정확한 임계값은 13.4112 m/s`
- [M-0106](../rules/zone.md#m-0106) 정의역: 속도 단위는 m/s, 구간은 15 s
- [M-0106](../rules/zone.md#m-0106) 매개변수 `threshold_ms`: 13.41
- [M-0106](../rules/zone.md#m-0106) 매개변수 `window_s`: 15

**미해결 질문:**

- [U-0112](../unknowns.md#u-0112) (높음): 속도 규칙의 평균: '20mph on average over 1min'은 슬라이딩 윈도, 고정 윈도, 거리 대 시간의 비율 중 무엇입니까? '30mph over any 15s'는 15 s 윈도의 같은 평균입니까, 아니면 최고 속도입니까? 비교는 엄격합니까? 8.94와 13.41 m/s가 정확한 임계값입니까?
- [U-0113](../unknowns.md#u-0113) (보통): 'Moving too fast counts as being outside': 속도 규칙이 발동하면 5 s 유예와 2 s당 1 HP가 서클 밖처럼 적용됩니까, 언제부터 시작됩니까, 그리고 속도가 떨어지는 즉시 끝납니까?

메모 ([M-0106](../rules/zone.md#m-0106)): 구간은 두 가지로 별개입니다 (8.94의 1 min 평균, 13.41의 15 s). 표기된 m/s 값은 8.9408과 13.4112에서 반올림한 것입니다.

<a id="m-0535"></a>

### M-0535: 언세이프 서클(unsafe circle) 설치

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-016`: "Unsafe circle: place a 50m (164ft) circle inside a safe zone for 20min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: Unsafe circle: 세이프 존 안에 50m (164ft) 서클을 20min 동안 설치합니다.
- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-018`: "Cooldown 2h." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 쿨다운은 2h입니다.
- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-019`: "No living contestant, you included, may be inside the circle when you place it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 설치할 때 본인을 포함해 서클 안에 살아 있는 참가자가 없어야 합니다.
- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-021`: "A Trolling contestant can place an unsafe circle inside a safe zone." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: Trolling 참가자는 세이프 존 안에 언세이프 서클을 설치할 수 있습니다.

**형식 모델:**

- [M-0535](../rules/zone.md#m-0535) 해석 A: `반지름 50 m의 place(circle, 중심 c) 수행. c는 세이프 존 안에 있어야 하고, 설치 시점에 설치자를 포함해 서클 안에 살아 있는 참가자가 없어야 함. 지속 시간 1200 s. 다음 설치는 설치 후 7200 s 뒤부터 허용`
- [M-0535](../rules/zone.md#m-0535) 해석 B: `지름 50 m (반지름 25 m)`
- [M-0535](../rules/zone.md#m-0535) 해석 C: `쿨다운 7200 s는 서클이 끝날 때부터 시작`
- [M-0535](../rules/zone.md#m-0535) 정의역: 시간(초 단위), 반지름(미터 단위)
- [M-0535](../rules/zone.md#m-0535) 매개변수 `size_m`: UNKNOWN, [U-0535](../unknowns.md#u-0535) 참조
- [M-0535](../rules/zone.md#m-0535) 매개변수 `duration_s`: 1200
- [M-0535](../rules/zone.md#m-0535) 매개변수 `cooldown_s`: 7200
- [M-0535](../rules/zone.md#m-0535) 매개변수 `cooldown_anchor`: UNKNOWN, [U-0536](../unknowns.md#u-0536) 참조

**상호작용:** [M-0536](../rules/damage.md#m-0536), [M-0537](../rules/items.md#m-0537)

**미해결 질문:**

- [U-0535](../unknowns.md#u-0535) (높음): 언세이프 서클(unsafe circle) "50m (164ft) 서클": 50 m는 반지름입니까 지름입니까?
- [U-0536](../unknowns.md#u-0536) (낮음): 언세이프 서클(unsafe circle) "쿨다운 2h"와 20 min 지속 시간: 쿨다운은 설치 시점에 시작됩니까 서클이 끝날 때 시작됩니까?

메모 ([M-0535](../rules/zone.md#m-0535)): '세이프 존 안'은 본문에서 설치 시점에 확인됩니다. 세이프 존은 이동하며, 세이프 존 안에 있는 부분만 피해를 줍니다([M-0536](../rules/damage.md#m-0536)).

## 시뮬레이션 검증

아직 이 페이지를 다루는 정리나 시뮬레이션이 없습니다.

## 미해결 질문

[U-0002](../unknowns.md#u-0002), [U-0003](../unknowns.md#u-0003), [U-0012](../unknowns.md#u-0012), [U-0110](../unknowns.md#u-0110), [U-0111](../unknowns.md#u-0111), [U-0112](../unknowns.md#u-0112), [U-0113](../unknowns.md#u-0113), [U-0114](../unknowns.md#u-0114), [U-0535](../unknowns.md#u-0535), [U-0536](../unknowns.md#u-0536)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
