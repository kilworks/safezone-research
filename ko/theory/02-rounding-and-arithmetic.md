# 02. 내림·올림과 산술

> **적대적 검토, 2026-11-11:** T-0004는 새로운 검토자에 의해 BROKEN으로 판정되어 같은 날 수정되었습니다. 두 번째 새로운 검토자가 수정된 버전을 다시 공격했고(모든 수정자와 해석에 대해 d = 1..4999를 전수 확인) UPHELD로 판정했습니다. 이 페이지의 나머지 정리는 첫 검토에서 UPHELD로 판정되었습니다.

위키는 백분율 규칙을 말로 서술합니다. "10% more, rounded down", "50% less", "15% more, rounded down", "10% higher, rounded up" 등입니다. 이 파일은 각 규칙을 정확한 정수 산술로 바꾸고, 어떤 표현이 하나의 의미만 가지며 어떤 표현이 두 가지 의미를 가지는지 증명하며, 부동소수점 수로 작성한 코드가 정확한 규칙에서 어디서 벗어나는지 측정합니다.

테스트: `sim/tests/test_arith_theorems.py`(전수 검사). 편차 표: `analysis/scripts/float_drift.py`, 출력 `analysis/results/float_drift.json`. 구현: `sim/safezone_sim/arith.py`.

## 모든 곳에서 쓰이는 보조정리

**보조정리.** 모든 정수 $n$과 실수 $x$에 대해 $\lfloor n + x \rfloor = n + \lfloor x \rfloor$이고 $\lfloor -x \rfloor = -\lceil x \rceil$입니다.

둘 다 내림의 정의, 즉 인수를 넘지 않는 가장 큰 정수라는 정의에서 따라 나옵니다.

## T-0001: 공격자의 Kick 보너스는 해석이 하나뿐입니다

**정리 T-0001.** 모든 정수 $d \ge 0$에 대해: $\lfloor 11d/10 \rfloor = d + \lfloor d/10 \rfloor$.

*규칙:* M-0119(파이프라인 2단계), 인용문 "deal 10% more, rounded down".
*증명.* $11d/10 = d + d/10$이고 $d$는 정수이므로 보조정리에 의해 결과가 성립합니다. $\square$
*따름 결과.* "10% more, rounded down"은 합계를 내림하든 보너스를 내림하든 같은 뜻입니다. 보너스는 $\lfloor d/10 \rfloor$이므로 9 HP 이하의 타격에는 아무것도 더하지 않습니다. Kick 라이브 중인 공격자의 활(5 HP), 나이프(5 HP), 가짜 상자(5 HP), 체력이 가득 찬 Zarok의 도끼(5 HP)는 오프라인 공격자의 것과 정확히 같게 작동합니다. 10 HP 타격은 11이 되고, 20 HP 타격은 22가 됩니다. 이 값들은 기본값입니다. 강화된 무기는 +10을 더하므로(M-0338) 강화된 활은 15로 타격하고 라이브 중인 공격자의 활은 16으로 타격합니다.
*라벨:* `DERIVED`. *테스트:* `test_t0001_kick_attack_single_reading`, $0..10000$의 모든 $d$.

## T-0002: 방어자의 Kick 감소는 해석이 두 가지입니다

**정리 T-0002.** $R_A(d) = \lfloor 9d/10 \rfloor$(결과를 내림)이고 $R_B(d) = d - \lfloor d/10 \rfloor$(제거되는 10%를 내림)이라고 하겠습니다. 모든 정수 $d \ge 0$에 대해:

$$
R_A(d) = d - \lceil d/10 \rceil, \qquad R_B(d) - R_A(d) = \mathbb{1}[10 \nmid d].
$$

*규칙:* M-0122(파이프라인 4b단계), 인용문 "Being live on Kick then takes off 10%, rounded down."; 미해결 질문 U-0001.
*증명.* 보조정리에 의해 $\lfloor d - d/10 \rfloor = d + \lfloor -d/10 \rfloor = d - \lceil d/10 \rceil$입니다. 그러면 $R_B - R_A = \lceil d/10 \rceil - \lfloor d/10 \rfloor$이고, 이는 $10 \mid d$일 때 0, 그렇지 않으면 1입니다. $\square$
*따름 결과.* A에서는 2에서 10 HP까지의 모든 타격이 정확히 1 HP를 잃고, 1 HP 타격은 0으로 줄어듭니다(그 뒤 최소 단계에서 다시 1로 올라갑니다, T-0004). B에서는 10 HP 미만의 타격이 전혀 줄어들지 않습니다. 따라서 "you take 10% less damage"는 모든 작은 타격에서 약 1 HP의 가치가 있거나, 작은 타격에서는 아무 가치가 없습니다. 1 HP의 존 틱은 두 해석 모두에서 변하지 않습니다.
*정리의 라벨:* `DERIVED`. *게임 내 동작의 라벨:* U-0001에 따라 `CONDITIONAL`. *테스트:* `test_t0002_kick_defense_two_readings`.

## T-0003: Protection의 핵 절반 감소와 Kick 감소는 거의 교환 가능합니다

피해 페이지는 4단계를 다음 순서로 둡니다. Protection 참가자에 대해 핵을 절반으로 줄이고, 내림하고, 그다음 Kick 감소를 적용합니다(M-0121, M-0122; "damage left is rounded down"이 정확히 어디에 놓이는지는 U-0100입니다). 순서가 중요할까요?

**정리 T-0003.** $H(d) = \lfloor d/2 \rfloor$라고 하겠습니다. 모든 정수 $d \ge 0$에 대해:

- 해석 A에서, $R_A(H(d)) - H(R_A(d)) = -\mathbb{1}[d \bmod 20 \in \{3,5,7,9\}]$;
- 해석 B에서, $R_B(H(d)) - H(R_B(d)) = \mathbb{1}[d \bmod 20 \in \{10,12,14,16,18\}]$.

*증명.* $R \in \{R_A, R_B\}$에 대해 $R(x+10) = R(x) + 9$이고 $R(x+20) = R(x)+18$이며, $H(x+20) = H(x)+10$, $H(x+18) = H(x)+9$입니다. 따라서 $g_1 = R \circ H$와 $g_2 = H \circ R$ 모두 $g(d+20) = g(d) + 9$를 만족하므로 $g_1 - g_2$는 주기 20을 가집니다. $d = 0, \dots, 19$를 확인하면 위의 나머지 값들이 나오며, 테스트는 10000까지의 모든 $d$를 확인합니다. $\square$
*따름 결과.* 시청자 핵 20 HP는 어느 순서, 어느 해석에서든 라이브 중인 Protection 참가자에게 9 HP의 피해를 줍니다. 순서는 다른 피해 값을 가진 관리자 핵에서만 중요하며, 그때도 정확히 1 HP 차이입니다.
*라벨:* 산술에 대해서는 `DERIVED`; 순서 자체는 `DOCUMENTED`(M-0117). *테스트:* `test_t0003_protection_nuke_and_kick_order`.

## T-0004: 최소 1 HP가 결과를 바꾸는 경우

**정리 T-0004.** 4단계의 문서화된 순서에서, 최소 단계(M-0123, "A hit that gets through always does at least 1 HP")는 원래 타격 $d \ge 1$의 5단계 출력을 바꿉니다(최종 HP 손실을 반드시 바꾸는 것은 아닙니다. fortress와 armor가 그 뒤에 오기 때문입니다). 바뀌는 경우는 정확히 다음과 같습니다.

| 방어자 상태 | 해석 A | 해석 B |
|---|---|---|
| Kick 라이브 중 | $d = 1$ | 없음 |
| Protection, 핵, 오프라인 | $d = 1$ | $d = 1$ |
| Protection, 핵, 라이브 중, 연속 두 번 내림 (U-0100 해석 A) | $d \in \{1,2,3\}$ | $d = 1$ |
| Protection, 핵, 라이브 중, 최종 한 번 내림 $\lfloor 9d/20 \rfloor$ (U-0100 해석 B) | $d \in \{1,2\}$ | U-0100 B에서 정의되지 않음 |
| 그 외 | 없음 | 없음 |

*증명.* 최소 단계는 $d \ge 1$인데 줄어든 값이 0일 때, 그리고 그때에만 결과를 바꿉니다. $R_A(d) = 0 \iff 9d < 10 \iff d = 1$; $d \ge 1$에 대해 $R_B(d) = d - \lfloor d/10 \rfloor \ge 1$; $H(d) = 0 \iff d = 1$; $R_A(H(d)) = 0 \iff H(d) \le 1 \iff d \le 3$; 최종 한 번 내림이면 $\lfloor 9d/20 \rfloor = 0 \iff 9d < 20 \iff d \le 2$; $R_B(H(d)) = 0 \iff H(d) = 0 \iff d = 1$. 공격자의 Kick 보너스(2단계)는 모든 행을 그대로 둡니다. $d \le 9$에 대해 $\lfloor 11d/10 \rfloor = d$이고, 모든 행은 $d \le 3$만 다루기 때문입니다. $\square$
*따름 결과.* 최소 단계는 3 HP 이하의 타격에서만 중요합니다. 문서화된 공격 중 그렇게 적게 주는 것은 1 HP 틱(존, 언세이프 서클, robot, 독, 출혈, 공습 화재, 좀비 흡수)과 2 HP 틱(가드 좀비, 최루 가스), 그리고 Wizard staff 범위가 틱을 준다면 Wizard staff 틱(U-0010)뿐입니다. 이 틱들이 파이프라인을 통과하는 "타격"인지는 U-0002입니다. fortress와 armor가 그 마지막 1 HP를 여전히 흡수할 수 있는지는 U-0103입니다.
*라벨:* 명시된 각 행에 대해서는 `DERIVED`; 어느 행이 적용되는지는 U-0100에 따라 `CONDITIONAL`, 게임 내 관련성은 U-0002에 따라 `CONDITIONAL`. *테스트:* `test_t0004_minimum_step_changes_outcome_only_for_tiny_hits`.

## T-0005: Piety의 포션 보너스는 해석이 하나뿐입니다

**정리 T-0005.** 모든 정수 $x \ge 0$에 대해: $\lfloor 115x/100 \rfloor = x + \lfloor 15x/100 \rfloor$.

*증명.* $n = x$로 둔 보조정리입니다. $\square$
*따름 결과.* Piety 포션은 소형, 중형, 대형, 초대형 등급(기본값 $5, 10, 20, 40$)에 대해 $5, 11, 23, 46$ HP를 회복합니다. 소형 포션은 보너스에서 아무것도 얻지 못합니다($5.75$는 내림하면 5입니다).
*라벨:* 포션 등급과 Piety 규칙이 `DOCUMENTED`라는 전제하에 `DERIVED`. *테스트:* `test_t0005_piety_bonus_readings_coincide`.

## T-0006: 상인 사다리

**정리 T-0006.** 인벤토리 슬롯 또는 최대 HP +10의 $k$번째 구매($k = 0, 1, \dots$)가 $40 + 10k$ 블러드 토큰이라면, 처음 $n$번의 구매 비용은 $C(n) = 5n^2 + 35n$입니다. 특히 $C(10) = 850$입니다(최대 HP 100에서 200까지). 구매 $k$에서 사는 최대 HP 1포인트의 비용은 $4 + k$ 토큰입니다.

*증명.* $\sum_{k=0}^{n-1}(40 + 10k) = 40n + 10\,n(n-1)/2 = 5n^2 + 35n$. $\square$
*Ingenuity.* Ingenuity는 10% 더 많이 지불하며 올림합니다. 모든 사다리 가격은 10의 배수이므로 $\lceil 11p/10 \rceil = 11p/10$이 정확히 성립하고, 최대 HP 열 번의 구매는 $1.1 \times 850 = 935$ 토큰입니다.
*라벨:* `DERIVED`; 슬롯 사다리와 HP 사다리가 하나의 카운터를 공유하는지는 상인 형식화의 문제입니다. *테스트:* `test_t0006_merchant_ladder`.

## 부동소수점 편차 (H-0001)

서버는 어떤 언어로 계산하며, 아마도 IEEE 754 binary64 수를 쓸 것입니다. 정확한 정수 산술 대신 `Math.floor(x * 1.1)`을 쓰는 프로그래머는 binary64 곱이 정수 바로 아래나 위에 떨어질 때마다 다른 답을 얻습니다. `analysis/scripts/float_drift.py`는 위키가 명시한 모든 배수에 대해 각 양의 전체 정의역에서, Python과 Node.js(둘 다 binary64를 쓰며 모든 값에서 일치함)로 이를 측정합니다.

| 규칙 | 프로그래머가 쓸 수 있는 코드 | 정의역 | 정확한 규칙과 다른 값 |
|---|---|---|---|
| Kick 공격 보너스 | `Math.floor(d * 1.1)` | $0..500$ | 없음 |
| Kick 방어, 해석 A | `Math.floor(d * 0.9)` | $0..500$ | 없음 |
| Protection 핵, Protection 포션, Eddie의 +50% | `Math.floor(x * 0.5)` | $0..500$ | 없음 |
| Eddie의 -30%(내림 또는 올림), Death 5%, Death 60% 상한, 생존 20%, 왕관 20% | `* 0.3`, `* 0.05`, `* 0.6`, `* 0.2` | 각각의 정의역 | 없음 |
| Piety +15% | `Math.floor(h * 1.15)` | $0..400$ | 100, 180, 200, 220, 340, 360, 380, 400 |
| Ingenuity 가격 | `Math.ceil(p * 1.1)` | $1..400$ | 19개 값: 50, 90, 100, 110, 170, ..., 400 |

**가설 H-0001 (Ingenuity 가격 편차).** 서버가 Ingenuity 가격을 binary64의 `ceil(price * 1.1)`로 계산한다면, Ingenuity 참가자는 기본 가격 50, 90, 100, 110에서 규칙보다 블러드 토큰을 1개 더 지불합니다. Dual Wield(기본 50)는 55 대신 56이고, 최대 HP 업그레이드 열 번은 935 토큰 대신 939 토큰입니다. 테스트: VOD에서 Ingenuity 상인 화면 하나(U-0006). *라벨:* `HYPOTHESIS`.

Piety 편차 값(100, 180, ...)은 포션 회복량이 아닙니다. 문서화된 네 회복량 5, 10, 20, 40은 영향을 받지 않으므로, 문서화된 포션으로는 Piety 편차가 일어날 수 없습니다.
