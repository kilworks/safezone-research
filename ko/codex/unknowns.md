# 미해결 질문과 모순

2026-11-11 스냅샷 기준으로 공식 위키가 정하지 않은 모든 것입니다. 각 질문에는 경쟁하는 해석과 그것을 결정할 방법이 적혀 있습니다. 이 프로젝트의 어떤 모델도 해석을 몰래 고르지 않습니다. 모든 시뮬레이션은 중요한 해석마다 따로 실행됩니다.

우선순위별 미해결 질문: 5 치명적, 72 높음, 95 보통, 31 낮음 (출처: kb/unknowns/, 기록 204개).

## 우선순위: 치명적

### U-0000

[U-0000](unknowns.md#u-0000): 보고된 $5,000 시청자 상금의 출처와 정확한 조건은 무엇입니까? 상태: `open`.

중요한 이유 ([U-0000](unknowns.md#u-0000)): 시청자 경제 모델(8.10절)에서 시청자의 목표를 정합니다. 이것이 없으면 시청자 전략은 Cx-Buck당 피해를 최대화하는 것으로만 설정할 수 있습니다.

- [U-0000](unknowns.md#u-0000) 해석 A: $5,000 상금은 존재하지 않으며, 시청자 상금은 금액이 명시되지 않은 '상위 3명 시청자' 현금 상금입니다.
- [U-0000](unknowns.md#u-0000) 해석 B: $5,000 상금이 존재하며, 아직 찾지 못한 조건이 있습니다.
- [U-0000](unknowns.md#u-0000) 해결 방법: 주최자의 X 게시물을 직접 읽습니다(kil의 로그인된 브라우저 세션이 필요합니다).
- [U-0000](unknowns.md#u-0000) 해결 방법: 방송 중 주최자의 발언(VOD 타임스탬프).
- [U-0000](unknowns.md#u-0000) 해결 방법: kil이 SCOPE.md에 추가하는 경우 /events 또는 /safezone/recap 페이지.

### U-0001

[U-0001](unknowns.md#u-0001): 방어자의 Kick 라이브 10% 감소는 결과를 내림하는 것입니까(A), 아니면 제거되는 10%를 내림하는 것입니까(B)? 상태: `open`.

중요한 이유 ([U-0001](unknowns.md#u-0001)): 작은 타격마다 최대 1 HP씩 결과가 달라집니다. A에서는 2에서 10까지의 타격이 1 HP씩 줄어들고, B에서는 10 미만의 타격은 변하지 않습니다.

- [U-0001](unknowns.md#u-0001) 해석 A: d -> floor(9d/10)
- [U-0001](unknowns.md#u-0001) 해석 B: d -> d - floor(d/10)
- [U-0001](unknowns.md#u-0001) 해결 방법: VOD: 5 HP 타격(활, 칼, 가짜 상자)을 받는 라이브 참가자에게 -4(A) 또는 -5(B)가 표시됩니다.
- [U-0001](unknowns.md#u-0001) 해결 방법: REA: 배포된 코드의 피해 공식(클라이언트 코드에는 공식이 없습니다, RE-0001).

### U-0002

[U-0002](unknowns.md#u-0002): 개별 공격이 아닌 피해(존 틱, 언세이프 서클(unsafe circle), robot, 독, 최루 가스, 출혈, 좀비 드레인(drain), Eddie의 손실, Retribution)에 파이프라인의 4b단계(방어자의 Kick 라이브 감소), 5단계(최소 1 HP), 6단계(fortress)가 적용됩니까? 그리고 가드 좀비 드레인과 부활 비용은 애초에 피해의 한 종류입니까(둘 다 피해 표에 행이 없습니다)? 상태: `open`.

중요한 이유 ([U-0002](unknowns.md#u-0002)): 막는 수단과 Body armor는 더 이상 이 질문에 좌우되지 않습니다(아래의 범위 축소를 보십시오). 남은 부분에 따라 달라지는 것은 다음과 같습니다. Kick 라이브 참가자가 Retribution으로 잃는 HP(18 또는 20 HP), Eddie의 물약으로 잃는 HP(최대 HP 100일 때 27 또는 30 HP), 최루 가스와 가드 좀비의 2 HP 틱으로 잃는 HP(1 또는 2 HP, [U-0001](unknowns.md#u-0001) 해석 A에서만), fortress가 존 틱을 흡수하는지, 부활 비용이 줄어들거나 흡수될 수 있는지입니다. 1 HP 틱은 해석 A와 B 모두에서 1 HP로 유지됩니다([T-0002](theorems/T-0002.md), [T-0004](theorems/T-0004.md)).

- [U-0002](unknowns.md#u-0002) 해석 A: 피해 표의 모든 행은 타격이므로 4b, 5, 6단계가 모두에 적용됩니다.
- [U-0002](unknowns.md#u-0002) 해석 B: 4b, 5, 6단계는 개별 공격에만 적용됩니다. 주기적 피해와 자해 피해에는 1단계와 7단계만 적용되고 그 밖에는 아무것도 적용되지 않습니다.
- [U-0002](unknowns.md#u-0002) 해석 C: 원천별로 또는 단계별로 혼합됩니다.
- [U-0002](unknowns.md#u-0002) 해결 방법: VOD: Protection 참가자가, armor가 없고 fortress 안에 있지 않은 Kick 라이브 참가자로부터 30m 이내에서 사망합니다. 피해자는 [U-0001](unknowns.md#u-0001)의 두 해석 모두에서 18 HP(4b단계 적용) 또는 20 HP(미적용)를 잃습니다.
- [U-0002](unknowns.md#u-0002) 해결 방법: VOD: 최대 HP가 100인 Kick 라이브 참가자가 Eddie의 물약 도박에서 집니다: 27 HP 또는 30 HP.
- [U-0002](unknowns.md#u-0002) 해결 방법: VOD: 참가자가 모든 세이프 존 밖의 fortress 안에 서 있습니다. fortress의 내구도가 줄어들거나(6단계 적용) 참가자의 HP가 줄어듭니다.
- [U-0002](unknowns.md#u-0002) 해결 방법: VOD: Body armor를 착용한 부활 시전자: armor 내구도가 5 줄어들거나(비용이 피해임) HP가 줄어듭니다.
- [U-0002](unknowns.md#u-0002) 해결 방법: 검증 수단이 아님: armor가 없는 참가자가 받는 1 HP 틱(존, 독, 좀비 드레인)은 해석 A와 B 모두에서 1 HP입니다([T-0002](theorems/T-0002.md), [T-0004](theorems/T-0004.md)).
- [U-0002](unknowns.md#u-0002) 범위 축소: 2026-11-11 스냅샷의 본문만으로 2026-11-13에 범위를 좁혔으며, 해결된 것은 아닙니다. 확정된 내용: (1) 1단계는 원천별로 적용됩니다. 존, 언세이프 서클, robot, 독, 최루 가스, 좀비 드레인, 출혈, Eddie의 역효과, Retribution은 각각 피해 표에 막는 수단의 행이 있습니다(wiki-damage-005부터 wiki-damage-010, wiki-damage-017, wiki-damage-030, wiki-damage-031). (2) 7단계는 이들 모두에 적용됩니다. 각 행은 "Body armor (absorbs)"로 끝나므로, 이전의 해석 B(주기적 드레인은 파이프라인 전체를 우회한다)는 armor에 관해서는 반박됩니다(wiki-damage-071은 "Body Armor works on every kind of damage"라고 말하지만 이 문장은 일반 규칙이 아닙니다. "A trapped gift ignores it", wiki-items-027). (3) 2단계는 적용되지 않습니다. 공격자의 Kick 보너스는 닫힌 무기 목록(wiki-damage-038)이며 이 원천들은 거기에 없습니다. (4) 3단계는 적용되지 않습니다. Mirror forcefield는 닫힌 목록(wiki-damage-070)만 "only reflects" 하며 이 원천들은 거기에 없습니다(Poison Dart는 그 목록에 있고, 피해 표의 독 행에는 Mirror forcefield가 없습니다, wiki-damage-008). (5) 4a단계는 적용되지 않습니다. Protection의 감소는 핵에만 해당합니다(wiki-damage-044). 아직 미해결: 이 원천들에 대한 4b, 5, 6단계, 가드 좀비 드레인이 "Zombie drain"인지 여부, 그리고 본문이 비용이라고 부르는 부활 비용.

### U-0009

[U-0009](unknowns.md#u-0009): Miami의 참가자 수와 이벤트 기간. 상태: `open`.

중요한 이유 ([U-0009](unknowns.md#u-0009)): 지평 T, Death 시길의 '20% 이하 생존' 임계값, 그리고 모든 최후 생존자 모델을 정합니다.

- [U-0009](unknowns.md#u-0009) 해결 방법: 주최자의 발언 또는 이벤트 중 라이브 개요 페이지(SCOPE.md P2).

### U-0417

[U-0417](unknowns.md#u-0417): 현상금 획득: 'The first other contestant to stay within 5m of them for 1min claims it'. 60s는 연속(범위를 벗어나면 초기화)입니까, 누적입니까, 아니면 짧은 이탈을 허용합니까? 표시된 참가자의 이동이 관련됩니까, 그리고 여러 추적자가 각각 따로 집계됩니까? 상태: `open`.

중요한 이유 ([U-0417](unknowns.md#u-0417)): 추격으로 현상금을 획득할 수 있는지와 기대 지급 속도를 결정합니다.

- [U-0417](unknowns.md#u-0417) 해석 A: 추적자마다 연속 60s 카운터, 범위를 벗어나면 초기화
- [U-0417](unknowns.md#u-0417) 해석 B: 추적자마다 누적 60s 카운터
- [U-0417](unknowns.md#u-0417) 해석 C: 범위 안에 다른 참가자가 없을 때 초기화되는 공유 카운터 하나
- [U-0417](unknowns.md#u-0417) 해결 방법: 움직이는 대상에 대한 현상금 획득 VOD.

## 우선순위: 높음

### U-0004

[U-0004](unknowns.md#u-0004): Eddie의 포션 30% 손실이 사망을 일으킬 수 있으며, armor, fortress 또는 Kick 상태가 여기에 적용됩니까? 상태: `open`.

중요한 이유 ([U-0004](unknowns.md#u-0004)): 포션이 최후의 수단인지, 낮은 HP에서의 자살인지를 정합니다.

- [U-0004](unknowns.md#u-0004) 해석 A: 손실로 사망할 수 있으며 어떤 보호도 적용되지 않습니다.
- [U-0004](unknowns.md#u-0004) 해석 B: 손실로 사망할 수 있으며 파이프라인이 적용됩니다(armor가 흡수하고 Kick이 감소시킵니다).
- [U-0004](unknowns.md#u-0004) 해석 C: 손실로 HP가 1 아래로 내려갈 수 없습니다.
- [U-0004](unknowns.md#u-0004) 해결 방법: VOD: 최대 HP의 30% 이하인 참가자가 이 포션을 마시는 장면.
- [U-0004](unknowns.md#u-0004) 해결 방법: 피해 표는 'Eddie's Potion backfire'를 Shield, Safety bubble, Sleeping Bag, Body armor로 막을 수 있다고 기재하며, 이는 차단에 관해 B를 뒷받침합니다(공식화 예정).
- [U-0004](unknowns.md#u-0004) 범위 축소: 2026-11-11 스냅샷의 본문만으로 2026-11-13에 범위를 좁혔으며, 해결된 것은 아닙니다. 해석 A(어떤 보호도 적용되지 않음)는 반박됩니다. 피해 표에는 "Eddie's Potion backfire" 행이 있고, Shield, Safety bubble, Sleeping Bag이 막는 수단이며 "Body armor (absorbs)"가 붙어 있습니다(wiki-damage-030). 또한 "Body Armor works on every kind of damage"입니다(wiki-damage-071). 아직 미해결: 손실로 사망할 수 있는지 아니면 1 HP에서 멈추는지(해석 B와 C), 그리고 Kick 라이브 감소와 fortress가 적용되는지 여부이며, 후자는 [U-0002](unknowns.md#u-0002)에 남아 있는 부분입니다.

### U-0005

[U-0005](unknowns.md#u-0005): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까? 상태: `open`.

중요한 이유 ([U-0005](unknowns.md#u-0005)): armor를 가진 공격자 또는 라이브 공격자를 상대로 한 Mirror forcefield의 가치가 달라집니다.

- [U-0005](unknowns.md#u-0005) 해석 A: 반사된 타격은 공격자의 전체 파이프라인을 거칩니다.
- [U-0005](unknowns.md#u-0005) 해석 B: 반사된 타격은 가공 없이 그대로 적중합니다.
- [U-0005](unknowns.md#u-0005) 해결 방법: VOD: armor를 가진 공격자에게 반사된 타격.

### U-0006

[U-0006](unknowns.md#u-0006): 서버 연산은 정확합니까, 아니면 IEEE 754 binary64입니까(H-0001: Ingenuity 가격이 기본 50, 90, 100, 110일 때)? 상태: `open`.

중요한 이유 ([U-0006](unknowns.md#u-0006)): binary64의 ceil(p*1.1)은 해당 기본 가격에서 블러드 토큰 1개를 더 청구합니다.

- [U-0006](unknowns.md#u-0006) 해석 A: 정확한 정수 연산
- [U-0006](unknowns.md#u-0006) 해석 B: ceil(p * 1.1)을 쓰는 binary64
- [U-0006](unknowns.md#u-0006) 해결 방법: VOD: Ingenuity 참가자의 상인 화면에서 Dual Wield(기본 50)가 55(A) 또는 56(B)로 표시됩니다.

### U-0008

[U-0008](unknowns.md#u-0008): 좀비 30 HP 상한: 좀비 수명당입니까, 조우당입니까, 하루당입니까? 좀비가 죽으면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0008](unknowns.md#u-0008)): 좀비 피해 총량의 한계를 정합니다. 조우당이라면 좀비 피해는 무제한이 됩니다.

- [U-0008](unknowns.md#u-0008) 해석 A: 좀비 수명당, 참가자별
- [U-0008](unknowns.md#u-0008) 해석 B: 조우당
- [U-0008](unknowns.md#u-0008) 해석 C: 시간 구간당
- [U-0008](unknowns.md#u-0008) 해결 방법: VOD: 범위를 벗어난 뒤 참가자와 다시 교전하는 좀비 한 마리.

### U-0014

[U-0014](unknowns.md#u-0014): 시청자 공격의 Cx-Bucks 가격은 얼마입니까? 상태: `open`.

중요한 이유 ([U-0014](unknowns.md#u-0014)): 가격이 없으면 8.10절은 공격을 Cx-Buck당 피해가 아니라 피해만으로 순위를 매길 수 있고, 왕관 처치 보너스(가격의 20%)는 값을 갖지 못합니다.

- [U-0014](unknowns.md#u-0014) 해결 방법: SCOPE.md P3(api 경로 'purchasables', 호출하지 않음).
- [U-0014](unknowns.md#u-0014) 해결 방법: 시청자 상점의 VOD.
- [U-0014](unknowns.md#u-0014) 해결 방법: 상점 페이지, 현재는 범위 밖입니다.

### U-0015

[U-0015](unknowns.md#u-0015): 상자 규칙(종류, 획득 범위, 생성 빈도, 내용물)은 무엇입니까? 상자 페이지는 삭제되었습니다(RE-0004). 상태: `open`.

중요한 이유 ([U-0015](unknowns.md#u-0015)): Piety, Greed, Trolling, Ingenuity의 메커니즘은 모두 상자에 작용하므로, 그 가치는 상자 빈도에 달려 있습니다.

- [U-0015](unknowns.md#u-0015) 해결 방법: 주최자의 발언, 상자 생성 빈도를 관찰한 VOD.
- [U-0015](unknowns.md#u-0015) 해결 방법: SCOPE.md P1(검색 색인에 삭제된 텍스트가 남아 있을 수 있습니다).

### U-0101

[U-0101](unknowns.md#u-0101): Body armor가 'absorbs what is left, until it breaks'일 때, 남은 내구도보다 큰 타격은 초과분을 통과시킵니까(A), 아니면 타격 전체가 흡수되고 armor만 부서집니까(B)? 내구도는 흡수한 HP 1당 1씩 줄어듭니까? 상태: `open`.

중요한 이유 ([U-0101](unknowns.md#u-0101)): armor 내구도가 HP 풀(초과분이 통과)인지 타격 횟수인지를 정하며, armor를 가진 모든 참가자의 유효 HP가 달라집니다.

- [U-0101](unknowns.md#u-0101) 해석 A: absorbed = min(h, dur); dur -= absorbed; 초과분 h - absorbed가 HP에 도달
- [U-0101](unknowns.md#u-0101) 해석 B: if h > 0 and dur > 0: absorbed = h (타격 전체), dur -= h, 0 아래로는 내려가지 않음, dur이 0에 도달하면 armor가 부서지고 초과분은 소실
- [U-0101](unknowns.md#u-0101) 해석 C: 타격의 크기와 무관하게 타격 1회당 내구도 1 감소
- [U-0101](unknowns.md#u-0101) 해결 방법: VOD: 내구도가 보이는 armor 착용 참가자가 남은 내구도보다 큰 타격을 받는 장면.
- [U-0101](unknowns.md#u-0101) 해결 방법: REA: 배포된 armor 코드.

### U-0103

[U-0103](unknowns.md#u-0103): 'A hit that gets through always does at least 1 HP'는 7단계 중 5단계입니다. fortress(6단계)와 armor(7단계)가 최종 HP 손실을 여전히 0으로 줄일 수 있습니까? 상태: `open`.

중요한 이유 ([U-0103](unknowns.md#u-0103)): 6단계와 7단계가 전부 흡수할 수 있다면 'always at least 1 HP'는 5단계까지만 성립합니다. 최소 1 HP가 최종이라면 armor와 fortress는 아주 작은 타격으로부터 참가자를 완전히 보호할 수 없습니다.

- [U-0103](unknowns.md#u-0103) 해석 A: 명시된 순서: h5 = max(1, h4) 후 fortress와 armor가 차감하며, 최종 HP 손실은 0이 될 수 있음
- [U-0103](unknowns.md#u-0103) 해석 B: 최종 HP 손실 = max(1, h7): 최소가 마지막에 적용됨
- [U-0103](unknowns.md#u-0103) 해석 C: 최소는 5단계에 0이 아니고 흡수되지 않은 채 도달한 타격에만 적용
- [U-0103](unknowns.md#u-0103) 해결 방법: VOD: armor 착용 참가자가 1 HP 원천(존 틱, 독 단계, 감소 이후의 활)을 받는 장면.
- [U-0103](unknowns.md#u-0103) 해결 방법: REA: 배포된 코드의 피해 공식.

### U-0104

[U-0104](unknowns.md#u-0104): 'A final kill pays 25 blood tokens, or 50 if the killer or victim held the blood crown': 누가 지급받으며, 무엇이 처치를 'final'로 만들고, 지급은 언제 이루어집니까? 상태: `open`.

중요한 이유 ([U-0104](unknowns.md#u-0104)): 처치로 얻는 블러드 토큰 수입은 전투의 주된 자원 흐름입니다. 수령인과 시점에 따라 부활이 지급을 취소하는지가 정해집니다.

- [U-0104](unknowns.md#u-0104) 해석 A: 처치한 사람이 결정타 시점에 25를 지급받음(왕관이 있으면 50)
- [U-0104](unknowns.md#u-0104) 해석 B: 처치한 사람이 부활 제한 시간이 부활 없이 끝난 뒤 지급받음(final = 부활되지 않음)
- [U-0104](unknowns.md#u-0104) 해석 C: 처치한 사람이 25를 지급받고, 왕관이 관련되면 추가 25가 다른 곳으로 가므로 총 지급액은 50
- [U-0104](unknowns.md#u-0104) 해결 방법: VOD: 결정타 시점과 10 min 후의 처치자 블러드 토큰 카운터.
- [U-0104](unknowns.md#u-0104) 해결 방법: 주최자의 발언.

### U-0107

[U-0107](unknowns.md#u-0107): 부활 횟수 제한 '2 times'(Healing 참가자에게)와 '10 times'(Healing 참가자에 의한)는 무엇에 붙는 카운터입니까? 상태: `open`.

중요한 이유 ([U-0107](unknowns.md#u-0107)): Healing 참가자가 가진 목숨 수와, Healing 부활자가 이벤트 전체에서 수행할 수 있는 부활 횟수를 결정합니다.

- [U-0107](unknowns.md#u-0107) 해석 A: 2 = 특정 Healing 참가자가 (어떤 부활자에게서든) 평생 받을 수 있는 부활 총횟수. 10 = 특정 Healing 참가자가 평생 수행할 수 있는 부활 총횟수
- [U-0107](unknowns.md#u-0107) 해석 B: 2와 10은 (부활자, 대상) 쌍마다 적용됩니다
- [U-0107](unknowns.md#u-0107) 해석 C: 2 = 대상의 목숨당. 10 = 부활자당 하루 또는 한 시간당
- [U-0107](unknowns.md#u-0107) 해석 D: Healing 참가자가 다른 Healing 참가자를 부활시키면 두 제한이 모두 적용되고 더 낮은 쪽(2)이 우선하거나, 10만 적용됩니다
- [U-0107](unknowns.md#u-0107) 해결 방법: VOD: Healing 참가자가 세 번째로 부활한 장면, Healing 부활자가 열한 번째 부활을 수행한 장면.
- [U-0107](unknowns.md#u-0107) 해결 방법: 주최 측 설명.

### U-0110

[U-0110](unknowns.md#u-0110): 오프라인 유예가 끝난 뒤('you start taking damage after 15min') 어떤 피해가 적용됩니까? 서클 밖 규칙(5 s 유예 후 2 s마다 1 HP), 즉시 틱 주기, 또는 다른 것입니까? 상태: `open`.

중요한 이유 ([U-0110](unknowns.md#u-0110)): 휴대폰이 꺼진 참가자가 HP를 얼마나 빨리 잃는지, 유예 이후 사망까지의 시간을 정합니다.

- [U-0110](unknowns.md#u-0110) 해석 A: 서클 밖과 동일: 5 s 유예 후 2 s마다 1 HP
- [U-0110](unknowns.md#u-0110) 해석 B: 유예 종료 시점부터 2 s마다 1 HP, 추가 5 s 없음
- [U-0110](unknowns.md#u-0110) 해석 C: 이 페이지에 주어지지 않은 다른 속도
- [U-0110](unknowns.md#u-0110) 자유 매개변수 `offline_damage_start_delay_s`, 탐색 범위: 0 ~ 5 s: 피해가 유예 종료 시점에 시작하면 0, 서클 밖 유예가 다시 적용되면 5
- [U-0110](unknowns.md#u-0110) 해결 방법: VOD: 휴대폰이 꺼지고 15 min이 지난 참가자.
- [U-0110](unknowns.md#u-0110) 해결 방법: REA: 배포된 GPS 감시 로직.

### U-0111

[U-0111](unknowns.md#u-0111): 오프라인 유예 타이머의 의미: 마지막 GPS 갱신으로부터만 측정됩니까, 이후의 GPS 갱신이 타이머를 초기화합니까, 그리고 'live on Kick'은 GPS가 끊긴 순간(A), 만료 시점(B), 또는 부분 누적을 쓰는 연속 평가(C) 중 언제 판정됩니까? 상태: `open`.

중요한 이유 ([U-0111](unknowns.md#u-0111)): 장애 중 방송 끊김이나 재연결에 따라 유예가 15 min과 30 min 사이에서 달라지며, [U-0012](unknowns.md#u-0012)의 탐지 지연과 연결됩니다.

- [U-0111](unknowns.md#u-0111) 해석 A: 마지막 GPS 갱신 시점에 Kick 라이브 중이었으면 유예 = 30 min, 아니면 15 min이며 그 시점에 고정됩니다
- [U-0111](unknowns.md#u-0111) 해석 B: 라이브 상태는 15 min이 끝날 때 읽습니다. 그때 라이브 중이면 기한이 30 min으로 옮겨집니다
- [U-0111](unknowns.md#u-0111) 해석 C: 오프라인 경과 시간은 각 순간의 라이브 상태에 따라 분당 1/15 또는 1/30의 가중치로 누적됩니다
- [U-0111](unknowns.md#u-0111) 해결 방법: VOD: 라이브 중 휴대폰이 꺼지고 10분째에 방송이 끝난 경우의 피해 시작 시점.
- [U-0111](unknowns.md#u-0111) 해결 방법: 주최 측 설명.

### U-0112

[U-0112](unknowns.md#u-0112): 속도 규칙의 평균: '20mph on average over 1min'은 슬라이딩 윈도, 고정 윈도, 거리 대 시간의 비율 중 무엇입니까? '30mph over any 15s'는 15 s 윈도의 같은 평균입니까, 아니면 최고 속도입니까? 비교는 엄격합니까? 8.94와 13.41 m/s가 정확한 임계값입니까? 상태: `open`.

중요한 이유 ([U-0112](unknowns.md#u-0112)): 차량 탑승이나 GPS 점프에서 누가 너무 빠르게 이동하는 것으로 분류되는지, 그리고 발동 경계를 정확히 결정합니다.

- [U-0112](unknowns.md#u-0112) 해석 A: 슬라이딩 윈도, 평균 속도 = 변위 경로 길이 / 윈도 길이, 엄격한 >, 임계값은 표기된 대로 8.94와 13.41 m/s
- [U-0112](unknowns.md#u-0112) 해석 B: 같지만 임계값이 정확히 8.9408과 13.4112 m/s
- [U-0112](unknowns.md#u-0112) 해석 C: 경로 길이가 아니라 윈도 안에서 시작점과 끝점 사이의 직선 변위
- [U-0112](unknowns.md#u-0112) 해석 D: 15 s 규칙은 순간 최고 속도를 사용합니다
- [U-0112](unknowns.md#u-0112) 해결 방법: VOD/GPS 기록: 임계값 부근의 차량 이동.
- [U-0112](unknowns.md#u-0112) 해결 방법: REA: 배포된 속도 검사.

### U-0114

[U-0114](unknowns.md#u-0114): 존이 'split apart'할 수 있습니다: 세이프 존이 여럿일 때 'leave a safezone' 피해는 모든 존의 밖에 있을 때(A) 발동합니까, 아니면 마지막으로 있던 존을 떠날 때(B) 발동합니까? 상태: `open`.

중요한 이유 ([U-0114](unknowns.md#u-0114)): 두 존 사이를 건너는 것이 손실인지를 결정하며, 존이 갈라질 때 핵심입니다.

- [U-0114](unknowns.md#u-0114) 해석 A: 위치가 어느 세이프 존 안에도 없을 때만 피해 시계가 흐릅니다
- [U-0114](unknowns.md#u-0114) 해석 B: 존을 떠날 때 피해 시계가 흐르고, 어느 존에든 다시 들어가면 재시작됩니다
- [U-0114](unknowns.md#u-0114) 해석 C: 피해 시계는 참가자마다 지정된 하나의 존에 묶입니다
- [U-0114](unknowns.md#u-0114) 해결 방법: VOD: 존이 갈라지는 이벤트와 두 존 사이를 건너는 참가자.
- [U-0114](unknowns.md#u-0114) 해결 방법: 주최 측 설명.
- [U-0114](unknowns.md#u-0114) 범위 축소: 2026-11-11 스냅샷의 본문만으로 2026-11-13에 범위를 좁혔으며, 해결된 것은 아닙니다. 세 조항은 해석 A와 모순되지 않지만 피해 시계를 설명하지는 않습니다. "Only the part inside a safe zone hurts: outside every safe zone you take normal zone damage only"(wiki-sigils-trolling-023), 언세이프 서클은 "Anyone inside it who is also inside a safe zone"에게 피해를 주고(wiki-sigils-trolling-017), 거대 사이클롭스에 대해서는 "Outside the safe zones it takes zone damage"라고 합니다(wiki-attacks-071). 반대로 기본 규칙은 단수형과 leave라는 동사로 적혀 있어 B 또는 C처럼 읽힙니다. "If you leave a safezone, after 5s you will start taking 1 HP damage every 2s"(wiki-005). 존은 "even split apart"할 수 있지만(wiki-004), 갈라짐에 대한 규칙을 주거나 참가자를 하나의 존에 지정하는 조항은 없습니다. 아직 미해결: 갈라짐을 담은 VOD 또는 주최 측 설명.

### U-0116

[U-0116](unknowns.md#u-0116): 독 'Getting poisoned again resets the timer, it doesn't stack': 초기화는 90 s 카운트다운만 다시 시작합니까, 아니면 아직 가해질 남은 총 피해도 복원합니까? 총량은 얼마입니까? 상태: `open`.

중요한 이유 ([U-0116](unknowns.md#u-0116)): 재중독은 무한 연장(총량 복원)일 수도, 단순 지연일 수도 있으며, 페이지에는 총량이 주어져 있지 않습니다.

- [U-0116](unknowns.md#u-0116) 해석 A: 카운트다운이 다시 시작되고 남은 피해는 그대로입니다
- [U-0116](unknowns.md#u-0116) 해석 B: 카운트다운과 남은 피해가 모두 전체 총량으로 다시 시작됩니다
- [U-0116](unknowns.md#u-0116) 해석 C: 카운트다운이 다시 시작되고 남은 피해는 max(remaining, new total)입니다
- [U-0116](unknowns.md#u-0116) 자유 매개변수 `poison_total_hp`, 탐색 범위: 1 ~ 40 HP: 하한은 1틱, 상한은 어느 페이지에서든 확인된 가장 큰 총량(20 HP)의 두 배이며 스윕 선택입니다
- [U-0116](unknowns.md#u-0116) 해결 방법: VOD: 두 번 중독된 참가자의 시간 대비 손실 HP.
- [U-0116](unknowns.md#u-0116) 해결 방법: 아이템/공격 페이지가 독 한 가지 출처의 총량을 제시하므로 비교합니다.

### U-0117

[U-0117](unknowns.md#u-0117): Shield 또는 Safety bubble은 'blocks each poison step while it lasts': 막힌 단계는 소모됩니까('all its damage'에 산입), 아니면 건너뜁니까(독이 연장)? 보호받는 동안 카운트다운은 계속됩니까? 상태: `open`.

중요한 이유 ([U-0117](unknowns.md#u-0117)): 일시적 방어가 독을 무효로 하는지, 잠시 멈출 뿐인지를 결정합니다.

- [U-0117](unknowns.md#u-0117) 해석 A: 막힌 단계는 소모됩니다: 남은 단계가 줄어들고 HP는 잃지 않습니다
- [U-0117](unknowns.md#u-0117) 해석 B: 막힌 단계는 건너뜁니다: 남은 단계는 그대로이며 독이 연장됩니다
- [U-0117](unknowns.md#u-0117) 해석 C: 보호받는 동안 독 타이머가 멈춥니다
- [U-0117](unknowns.md#u-0117) 해결 방법: VOD: 중독된 참가자가 bubble에 들어갔다 나오는 장면.

### U-0120

[U-0120](unknowns.md#u-0120): 한 번의 타격에 여러 방어 수단(Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection)이 적용될 때, 어느 것이 'blocker'이고 어떤 아이템이 소모됩니까? 명시된 유일한 규칙은 'a hit already blocked by something else does not use [the Flak jacket] up'입니다. 상태: `open`.

중요한 이유 ([U-0120](unknowns.md#u-0120)): 소모품을 겹쳐 쓰면 낭비되는지, 어떤 방어를 먼저 장착해야 하는지를 결정합니다.

- [U-0120](unknowns.md#u-0120) 해석 A: 고정된 우선순위가 있고, 적용 가능한 첫 번째 차단 수단만 소모됩니다
- [U-0120](unknowns.md#u-0120) 해석 B: 적용 가능한 차단 수단이 모두 소모됩니다
- [U-0120](unknowns.md#u-0120) 해석 C: 소모되지 않는 차단 수단(면역)이 소모품보다 우선하며, 소모품은 다른 것이 막지 않을 때만 소모됩니다
- [U-0120](unknowns.md#u-0120) 해결 방법: VOD: Flak jacket과 Shield를 가진 참가자에 대한 타격.
- [U-0120](unknowns.md#u-0120) 해결 방법: REA: 배포된 타격 판정 로직.

### U-0125

[U-0125](unknowns.md#u-0125): Blood crown: 처치 시점에 누가 이를 'held'했습니까(처치 이전인지, 같은 처치로 이전된 이후인지), 그리고 어떻게 얻고 잃습니까? 상태: `open`.

중요한 이유 ([U-0125](unknowns.md#u-0125)): 25 대 50 토큰 지급이 이에 달려 있으며, 이 조항 집합의 페이지에는 crown 규칙이 없습니다.

- [U-0125](unknowns.md#u-0125) 해석 A: 처치가 확정되기 전의 보유자 상태를 읽습니다
- [U-0125](unknowns.md#u-0125) 해석 B: crown 이전이 확정된 후의 보유자 상태를 읽습니다
- [U-0125](unknowns.md#u-0125) 해결 방법: 주최 측 설명. crown을 설명하는 페이지(패밀리 교차).

### U-0205

[U-0205](unknowns.md#u-0205): Hazmat suit의 '간격당 +2s'는 어떤 피해 원인과 어떤 타이밍(첫 틱, 유예)을 늘립니까? 상태: `open`.

중요한 이유 ([U-0205](unknowns.md#u-0205)): 존 밖에서의 사망까지 걸리는 시간과, 언세이프 서클 및 robot에 대한 이 슈트의 가치가 달라집니다.

- [U-0205](unknowns.md#u-0205) 해석 A: 존 밖 간격만 해당, 2s -> 4s, 첫 틱은 변하지 않음
- [U-0205](unknowns.md#u-0205) 해석 B: 간격 4s이고 첫 틱이 2s 지연됨
- [U-0205](unknowns.md#u-0205) 해석 C: 피해 페이지에서 'slows'로 표시된 언세이프 서클 및 robot 간격도 포함
- [U-0205](unknowns.md#u-0205) 자유 매개변수 `hazmat_added_interval_s`, 탐색 범위: 0..4 s (페이지에는 2라고 되어 있으며, 상한 4는 두 배가 된다는 해석을 포함)
- [U-0205](unknowns.md#u-0205) 해결 방법: VOD: Hazmat 보유자가 화면 타이머가 있는 상태로 존을 벗어나는 장면.
- [U-0205](unknowns.md#u-0205) 해결 방법: robot 간격은 아이템 페이지에 없습니다.
- [U-0205](unknowns.md#u-0205) 범위 축소: 2026-11-11 스냅샷의 본문만으로 2026-11-13에 범위를 좁혔으며, 해결된 것은 아닙니다. 원천은 확정되었습니다. 피해 표는 정확히 세 행, 즉 Outside the circle, Unsafe circle, Robot에 "Hazmat suit (slows)"를 표시하므로(wiki-damage-005, wiki-damage-006, wiki-damage-007), 원천 목록에 관해서는 해석 A(존 밖 피해만)가 반박됩니다. 수치는 존 피해에 대해서만 적혀 있습니다. "While you carry it, each zone damage interval is 2s longer"(wiki-items-013). 언세이프 서클은 존 피해를 주며(wiki-sigils-trolling-017), robot 간격은 어느 페이지에도 없습니다. 아직 미해결: 첫 틱과 5 s 지연([U-0003](unknowns.md#u-0003)과 함께), 그리고 robot이 얼마나 느려지는지.

### U-0207

[U-0207](unknowns.md#u-0207): Guardian angel을 끝내는 '당신을 공격한다'는 무엇을 뜻합니까? 상태: `open`.

중요한 이유 ([U-0207](unknowns.md#u-0207)): 함정, 독, 범위 효과, drone 또는 도둑질이 면역을 끝내는지가 결정됩니다.

- [U-0207](unknowns.md#u-0207) 해석 A: 다른 참가자가 당신을 대상으로 한 모든 공격 행동 (막혔는지 여부와 무관)
- [U-0207](unknowns.md#u-0207) 해석 B: 피해를 주지 않는 적대 행동과 함정도 포함
- [U-0207](unknowns.md#u-0207) 해석 C: 당신에게 피해를 줄 공격만 해당
- [U-0207](unknowns.md#u-0207) 해결 방법: VOD: Guardian angel 보유자가 함정, 던진 다트 또는 도둑질을 당하는 장면.

### U-0209

[U-0209](unknowns.md#u-0209): Body armor의 15 HP는 줄어드는 풀입니까, 타격당 상한입니까? 일부만 흡수된 타격은 어떻게 처리됩니까? 상태: `open`.

중요한 이유 ([U-0209](unknowns.md#u-0209)): 반복되는 작은 타격(존 틱, 독)에 대한 생존력이 달라집니다.

- [U-0209](unknowns.md#u-0209) 해석 A: 15 HP의 줄어드는 풀, 마지막 타격은 부분 흡수
- [U-0209](unknowns.md#u-0209) 해석 B: 타격당 상한 15 HP, 소모되지 않음
- [U-0209](unknowns.md#u-0209) 해결 방법: VOD: 반복 타격 후의 armor 내구도.
- [U-0209](unknowns.md#u-0209) 해결 방법: 피해 페이지: 'absorbs what is left, until it breaks'는 A를 뒷받침합니다.
- [U-0209](unknowns.md#u-0209) 범위 축소: 2026-11-11 스냅샷의 본문만으로 2026-11-13에 범위를 좁혔으며, 해결된 것은 아닙니다. 해석 B는 반박됩니다. armor는 "absorbs what is left, until it breaks"이고(wiki-damage-055), 변하는 내구도를 가집니다. "+10 durability, up to 45"(wiki-merchant-057), 그 뒤에는 "loses one durability every twenty minutes, down to 15"입니다(wiki-merchant-058). 결코 소모되지 않는 armor는 부서질 수 없습니다. 아직 미해결이며 [U-0101](unknowns.md#u-0101)과 같은 질문: 한 번의 타격이 내구도에서 무엇을 가져가는지(흡수한 HP, 타격 전체, 또는 타격당 1), 따라서 "Absorbs up to 15 HP of damage"(wiki-items-026)가 HP로 세는 풀인지 여부.

### U-0305

[U-0305](unknowns.md#u-0305): Drone: 사용 후 대상은 발사 시점에 고정되어 무슨 일이 있어도 30s 뒤에 타격받습니까, 아니면 drone이 대상이 계속 보이거나 살아 있어야 합니까? 상태: `open`.

중요한 이유 ([U-0305](unknowns.md#u-0305)): 30s 지연 동안 drone을 피할 수 있는지(shield, bubble, 수면, 거리, Greed의 drone 도둑질)가 결정됩니다.

- [U-0305](unknowns.md#u-0305) 해석 A: 대상은 발사 시점에 고정, 가시성에 무슨 일이 있어도 30s 뒤에 타격 적용
- [U-0305](unknowns.md#u-0305) 해석 B: t+30s에 대상이 여전히 보일 때만 타격 적용
- [U-0305](unknowns.md#u-0305) 해석 C: 타격이 대상을 따라가며 방어 여부는 t+30s 시점에만 확인됨
- [U-0305](unknowns.md#u-0305) 해결 방법: VOD: drone 발사 후, 30s 동안 대상이 숨거나 Shield를 얻는 장면.

### U-0307

[U-0307](unknowns.md#u-0307): 쿨다운 의미(bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): 시도 시점에 시작됩니까, 타격 시점에 시작됩니까? 그리고 무기 아이템별입니까, 참가자별입니까(Dual Wield)? 상태: `open`.

중요한 이유 ([U-0307](unknowns.md#u-0307)): Dual Wield와 두 번째 무기가 있을 때 참가자별 쿨다운은 무기별 쿨다운에 비해 처리량을 절반으로 줄이며, 막히거나 빗나간 공격에도 영향을 줍니다.

- [U-0307](unknowns.md#u-0307) 해석 A: 무기 아이템별, 공격 시점에 시작
- [U-0307](unknowns.md#u-0307) 해석 B: 참가자별 (모든 무기가 공유), 공격 시점에 시작
- [U-0307](unknowns.md#u-0307) 해석 C: 무기 아이템별, 타격이 확정될 때 시작
- [U-0307](unknowns.md#u-0307) 해결 방법: VOD: Dual Wield 참가자가 쿨다운 안에 두 무기를 번갈아 쓰는 장면.

### U-0308

[U-0308](unknowns.md#u-0308): 사용(무기 사용, 화살, Deep Cut 충전, 인챈트 사용)은 막히거나 반사되거나 사거리 밖이거나 빗나간 공격에서도 소모됩니까? 상태: `open`.

중요한 이유 ([U-0308](unknowns.md#u-0308)): Shield, Safety Bubble, Mirror, Sleeping Bag이 공격자의 제한된 사용 횟수(knife 2, long sword 3)와 충전을 헛되이 소모시키는지 결정합니다.

- [U-0308](unknowns.md#u-0308) 해석 A: 시도할 때마다 소모됨
- [U-0308](unknowns.md#u-0308) 해석 B: 타격이 적중할 때만 소모됨
- [U-0308](unknowns.md#u-0308) 해석 C: 방어 아이템에 막힌 타격을 제외하고 소모됨
- [U-0308](unknowns.md#u-0308) 해결 방법: VOD: Shield를 가진 참가자를 knife로 찌른 뒤 남은 knife 사용 횟수를 셉니다.

### U-0309

[U-0309](unknowns.md#u-0309): Poison Dart, Zarok's axe, Huge machete의 '근처(nearby)'의 범위는 얼마입니까? 상태: `open`.

중요한 이유 ([U-0309](unknowns.md#u-0309)): 다른 근접 무기는 10m(knife, long sword)로 명시되어 있지만, 이 세 가지는 수치가 없어 사거리와 위치 선정을 모델링할 수 없습니다.

- [U-0309](unknowns.md#u-0309) 자유 매개변수 `nearby_range_m`, 탐색 범위: 5에서 50 m: knife와 long sword의 사거리는 10m, bow는 20m, staff 설치는 50m이므로 근접 무기의 '근처'는 5와 50 사이로 한정됩니다
- [U-0309](unknowns.md#u-0309) 해결 방법: 주최 측의 발표.
- [U-0309](unknowns.md#u-0309) 해결 방법: VOD: axe 또는 machete 타격이 성공했을 때의 측정 거리.

### U-0310

[U-0310](unknowns.md#u-0310): Zarok's axe: 사용자의 체력이 떨어질수록 피해가 최대 체력일 때 5 HP에서 25 HP로 어떻게 올라갑니까(선형인지, 단계적인지, 최대 HP에 대한 비율인지, 25는 어디에서 도달하는지)? 상태: `open`.

중요한 이유 ([U-0310](unknowns.md#u-0310)): axe의 가치 전체가 이 곡선에 달려 있습니다. 모든 HP 수준에서의 피해와 25 HP에 도달할 수 있는지 여부를 정합니다.

- [U-0310](unknowns.md#u-0310) 해석 A: 사용자의 최대 HP 대비 손실 비율에 선형: 5 + 20*(1 - h/H), H = 현재 최대 HP, 25는 h = 0에서 도달
- [U-0310](unknowns.md#u-0310) 해석 B: 손실 비율에 선형이며 25는 h = 1(생존 상태의 최저 HP)에서 도달
- [U-0310](unknowns.md#u-0310) 해석 C: 고정된 100 HP 기준에 대한 절대 HP에 선형: 5 + 20*(100 - h)/100, [5, 25]로 제한
- [U-0310](unknowns.md#u-0310) 해석 D: 사용자의 HP 구간별 단계적 변화(구간 경계는 명시되지 않음)
- [U-0310](unknowns.md#u-0310) 해결 방법: VOD: 사용자의 여러 HP 값(최대, 절반, 낮음)에서의 axe 타격.
- [U-0310](unknowns.md#u-0310) 해결 방법: REA: 무기 피해 공식이 배포물에 포함되어 있다면 그것.

### U-0320

[U-0320](unknowns.md#u-0320): 상인 복귀 지연: 'after 30min to 1h'는 떠난 시점부터 측정합니까, 도착한 시점부터 측정합니까? 그 범위 안에서의 분포는 어떻습니까? 상태: `open`.

중요한 이유 ([U-0320](unknowns.md#u-0320)): 방문 사이에 참가자가 블러드 토큰을 얼마나 모아야 하는지(부재 30에서 60 min 대 15에서 45 min)와 상인이 있는 시간의 장기 비율을 정합니다.

- [U-0320](unknowns.md#u-0320) 해석 A: 떠난 시점부터 [30, 60] min에 걸쳐 균등
- [U-0320](unknowns.md#u-0320) 해석 B: 도착한 시점부터 [30, 60] min에 걸쳐 균등(부재 15에서 45 min)
- [U-0320](unknowns.md#u-0320) 해석 C: 떠난 시점부터 [30, 60] min 안에서 고정값이거나 비균등 분포
- [U-0320](unknowns.md#u-0320) 자유 매개변수 `merchant_return_delay_min`, 탐색 범위: 명시된 대로 30에서 60 min, 해석 A 또는 B. 분포 형태(균등, 양 끝값만)를 바꿔 가며 탐색함
- [U-0320](unknowns.md#u-0320) 해결 방법: VOD: 여러 주기에 걸친 상인의 출발과 다음 도착 타임스탬프.

### U-0322

[U-0322](unknowns.md#u-0322): Ingenuity의 'pay 10% more, rounded up'은 40 + 10k 업그레이드 사다리에 어떻게 적용됩니까? 상태: `open`.

중요한 이유 ([U-0322](unknowns.md#u-0322)): 현재 가격마다 적용하는지, 시작 가격에만 적용하는지, 증가분에 적용하는지에 따라 사다리 전체와 업그레이드 N개를 사는 총비용이 달라집니다.

- [U-0322](unknowns.md#u-0322) 해석 A: 각 가격 p가 ceil(1.1*p)가 됨: 44, 55, 66, ...
- [U-0322](unknowns.md#u-0322) 해석 B: 시작 가격만 인상됨: 44, 54, 64, ...
- [U-0322](unknowns.md#u-0322) 해결 방법: VOD: 처음 세 번의 슬롯 업그레이드에 대한 Ingenuity 참가자의 상인 화면.

### U-0325

[U-0325](unknowns.md#u-0325): Sleeping Bag: 'sleep from 18:00 to 06:00 ... for eight hours of sleep in total' 규칙은 무엇입니까? 상태: `open`.

중요한 이유 ([U-0325](unknowns.md#u-0325)): 허용 시간대는 12시간인데 수면은 8시간입니다. 위키는 8h가 연속된 블록인지, 총 예산인지, 하룻밤의 상한인지 밝히지 않습니다.

- [U-0325](unknowns.md#u-0325) 해석 A: 수면은 18:00과 06:00 사이에만 허용됨. 총 수면 시간은 8h로 제한되며 나누어 잘 수 있음
- [U-0325](unknowns.md#u-0325) 해석 B: 허용 시간대 안에 들어가야 하는 연속 8h 블록 하나
- [U-0325](unknowns.md#u-0325) 해석 C: bag은 이벤트 전체에 걸쳐 총 8h의 수면을 담음
- [U-0325](unknowns.md#u-0325) 자유 매개변수 `sleep_total_h`, 탐색 범위: 명시된 대로 8. 예산을 나누어 쓰는 경우를 테스트함
- [U-0325](unknowns.md#u-0325) 해결 방법: VOD: 허용 시간대 내내 잠을 자는 참가자.
- [U-0325](unknowns.md#u-0325) 해결 방법: 주최 측의 발표.

### U-0327

[U-0327](unknowns.md#u-0327): Sleeping Bag: 65 s의 수면은 연속이어야 합니까? 잠든 사람이 15m 반경을 벗어나거나 깨어나거나 맞으면 어떻게 됩니까? 깨어나면 면역이 즉시 끝납니까? 상태: `open`.

중요한 이유 ([U-0327](unknowns.md#u-0327)): 처음 65 s가 노출 구간입니다. 범위를 벗어나거나 깨어나면 카운터가 초기화되는지가 정해지며, flashbang(섬광탄) 면역과 피해 면역이 여기에 달려 있습니다.

- [U-0327](unknowns.md#u-0327) 해석 A: 65 s는 연속이어야 함. 15m를 벗어나거나 깨어나면 초기화되고 면역이 끝남
- [U-0327](unknowns.md#u-0327) 해석 B: 65 s는 밤 동안 누적됨
- [U-0327](unknowns.md#u-0327) 해석 C: 한 번 도달하면 면역은 잠든 사람이 깨어날 때까지, 15m 밖에서도 지속됨
- [U-0327](unknowns.md#u-0327) 해결 방법: VOD: bag의 범위를 벗어나는 잠든 사람. 수면 30초째의 타격.

### U-0328

[U-0328](unknowns.md#u-0328): Sleeping Bag: 20분의 '다시 잠들 수 없음(cannot sleep again)' 제한은 언제 시작됩니까(bag이 처음 보호하는 순간, 깨어날 때, 마지막으로 막은 피해 시점 중)? 상태: `open`.

중요한 이유 ([U-0328](unknowns.md#u-0328)): 참가자가 얼마나 오래 잘 수 있는지가 달라집니다. 보호가 시작되는 65 s 시점에 제한이 시작되면 8h 동안 자는 사람은 깨어나기 훨씬 전에 제한에 걸립니다.

- [U-0328](unknowns.md#u-0328) 해석 A: bag이 보호를 시작할 때(65 s 수면 후) 시작됨
- [U-0328](unknowns.md#u-0328) 해석 B: 잠든 사람이 깨어날 때 시작됨
- [U-0328](unknowns.md#u-0328) 해석 C: bag이 마지막으로 막은 피해 시점에 시작됨
- [U-0328](unknowns.md#u-0328) 해결 방법: VOD: 깨어난 뒤 다시 자려고 하는 참가자.

### U-0329

[U-0329](unknowns.md#u-0329): Inventory slot과 +10 maximum HP의 'for each one you already bought' 카운터는 별개입니까, 공유됩니까? 상태: `open`.

중요한 이유 ([U-0329](unknowns.md#u-0329)): 공유 카운트에서는 슬롯 10개와 HP 업그레이드 10개를 사는 비용이 크게 달라집니다(두 번째 종류가 첫 번째가 멈춘 곳에서 시작합니다).

- [U-0329](unknowns.md#u-0329) 해석 A: 별개의 카운터: 각 사다리는 40 + 10k이며 k는 그 사다리의 구매 횟수
- [U-0329](unknowns.md#u-0329) 해석 B: 두 업그레이드에 걸쳐 하나의 공유 카운터
- [U-0329](unknowns.md#u-0329) 해결 방법: VOD: 슬롯 업그레이드 한 번 뒤의 상인 화면(HP 가격이 40입니까, 50입니까?).

### U-0333

[U-0333](unknowns.md#u-0333): 무기 인챈트 'Twice the uses ... keeps the uses it had before or the uses it has left, whichever is lower': 무엇의 두 배이며, 'the uses it had before'는 무엇입니까? 상태: `open`.

중요한 이유 ([U-0333](unknowns.md#u-0333)): 인챈트 후의 사용 횟수와, 사용 횟수가 적게 남은 무기가 2시간 뒤에 무엇을 유지하는지를 정합니다.

- [U-0333](unknowns.md#u-0333) 해석 A: 사용 횟수는 2 * (인챈트 시점의 남은 횟수)가 됨, 'before' = 인챈트 시점의 남은 횟수
- [U-0333](unknowns.md#u-0333) 해석 B: 사용 횟수는 2 * (무기의 최대 사용 횟수)가 됨, 'before' = 인챈트 시점의 남은 횟수
- [U-0333](unknowns.md#u-0333) 해석 C: 사용 횟수는 남은 횟수 + 최대 사용 횟수가 됨, 'before' = 최대 사용 횟수
- [U-0333](unknowns.md#u-0333) 해결 방법: VOD: 절반 사용한 knife를 인챈트하고 사용 횟수 확인.

### U-0340

[U-0340](unknowns.md#u-0340): 정확한 위치에 30 s 후 떨어진다고 할 때, 상인의 'standard missile'은 피해와 반경이 얼마입니까? 상태: `open`.

중요한 이유 ([U-0340](unknowns.md#u-0340)): 공격 페이지는 3min 무작위 낙하의 시청자 미사일을 설명하지만, 상인 텍스트는 'standard missile'을 언급할 뿐 피해나 반경을 주지 않습니다.

- [U-0340](unknowns.md#u-0340) 해석 A: 시청자 미사일과 같은 피해와 폭발 반경(공격 페이지에 따르면 25 m 이내 10 HP)
- [U-0340](unknowns.md#u-0340) 해석 B: 명시되지 않은 다른 피해
- [U-0340](unknowns.md#u-0340) 자유 매개변수 `merchant_missile_damage_hp`, 탐색 범위: 10 ~ 20 HP: 공격 페이지에서 시청자 미사일은 10, 핵은 20을 줍니다
- [U-0340](unknowns.md#u-0340) 해결 방법: VOD: 상인 미사일 착탄 시 HP 손실과 반경.

### U-0400

[U-0400](unknowns.md#u-0400): 미사일 낙하 편차: 'a random spot near that point'이며 폭발 전체가 100m 이내입니다. 낙하 오프셋은 최대 75m(폭발 가장자리가 100m 이내)입니까, 최대 100m입니까, 그리고 분포는 무엇입니까? 상태: `open`.

중요한 이유 ([U-0400](unknowns.md#u-0400)): 조준점에 서 있는 참가자에 대한 명중 확률과, 시청자가 한 참가자를 안정적으로 겨냥할 수 있는지를 결정합니다.

- [U-0400](unknowns.md#u-0400) 해석 A: 낙하 오프셋 r <= 100 - 25 = 75m, 따라서 25m 폭발이 100m 이내에 머묾
- [U-0400](unknowns.md#u-0400) 해석 B: 낙하 오프셋 r <= 100m(폭발 중심), 이 문장은 'near'를 뜻함
- [U-0400](unknowns.md#u-0400) 해석 C: 그 반경의 원판 위에서 균등
- [U-0400](unknowns.md#u-0400) 해석 D: 거리 r에서 균등, 각도는 무작위(중심 쪽으로 치우침)
- [U-0400](unknowns.md#u-0400) 자유 매개변수 `missile_max_offset_m`, 탐색 범위: 0 ~ 100 m; 위키는 폭발을 조준점에서 100m 이내로 제한하므로 중심 오프셋은 0과 100 사이에 있습니다
- [U-0400](unknowns.md#u-0400) 해결 방법: VOD: 여러 미사일의 조준점과 크레이터를 비교 기록.
- [U-0400](unknowns.md#u-0400) 해결 방법: 관리자 또는 주최자의 진술.

### U-0403

[U-0403](unknowns.md#u-0403): 좀비 수명: Horde는 20min, 가드 좀비는 1h(Necromancy 페이지)로 유지되지만, Summon, Death, Horde 보너스 좀비의 수명과 방출 시점부터 센 horde 좀비의 수명은 얼마입니까? 상태: `open`.

중요한 이유 ([U-0403](unknowns.md#u-0403)): 시간이 명시되지 않은 'A zombie disappears when its time runs out'은 좀비 압박 총량과 Necromancy 수입이 무제한인지 유한한지를 좌우합니다.

- [U-0403](unknowns.md#u-0403) 해석 A: 출처와 관계없이 각 좀비는 자신의 생성 시점부터 20min 동안 존재
- [U-0403](unknowns.md#u-0403) 해석 B: horde 좀비만 20min에 사라지고, Summon, Death, 보너스 좀비는 이벤트 끝까지 존재
- [U-0403](unknowns.md#u-0403) 해석 C: 출처마다 공개되지 않은 고유의 시간이 있음
- [U-0403](unknowns.md#u-0403) 자유 매개변수 `zombie_lifetime_s`, 탐색 범위: 60 ~ 86400 s; 20min이 명시된 유일한 좀비 타이머이고, 하루 상한은 이벤트 규모입니다
- [U-0403](unknowns.md#u-0403) 해결 방법: VOD: Summon 좀비가 사라질 때까지 추적.

### U-0404

[U-0404](unknowns.md#u-0404): 최루 가스 기하: '25m cloud'는 반경입니까 지름입니까? 그리고 구름 가장자리는 모든 참가자로부터 최소 20m 떨어져야 합니다. 구매 시점에만 그렇습니까, 설치 시점에도 그렇습니까? 구름 전체가 세이프 존 안에 있어야 합니까? 상태: `open`.

중요한 이유 ([U-0404](unknowns.md#u-0404)): 가장 가까운 참가자까지의 최소 조준 거리(중심에서 45m 또는 32.5m)와, 시청자가 참가자에게 가스를 쓸 수 있는지 자체를 정합니다.

- [U-0404](unknowns.md#u-0404) 해석 A: 반경 25m, 따라서 중심은 모든 참가자로부터 최소 45m
- [U-0404](unknowns.md#u-0404) 해석 B: 지름 25m(반경 12.5m), 따라서 중심은 모든 참가자로부터 최소 32.5m
- [U-0404](unknowns.md#u-0404) 해석 C: 20m 규칙은 설치 시점 검사일 뿐이며, 이후 구름으로 이동하는 것은 자유
- [U-0404](unknowns.md#u-0404) 자유 매개변수 `tear_gas_radius_m`, 탐색 범위: 12.5 ~ 25 m; 위키는 '25m'만 크기로 제시합니다
- [U-0404](unknowns.md#u-0404) 해결 방법: VOD: 참가자 근처에 최루 가스를 설치하고 거부 임계값을 기록.

### U-0406

[U-0406](unknowns.md#u-0406): 공습 띠의 너비(위키는 중심과 방향만 제시합니다). 상태: `open`.

중요한 이유 ([U-0406](unknowns.md#u-0406)): 5 HP 공습과 5min 화재의 명중 확률.

- [U-0406](unknowns.md#u-0406) 자유 매개변수 `airstrike_strip_width_m`, 탐색 범위: 5 ~ 100 m; 25m 폭발보다 좁지만 다른 공격의 100m 규모 이내입니다
- [U-0406](unknowns.md#u-0406) 해결 방법: VOD: 지도에서 불탄 띠를 측정.

### U-0407

[U-0407](unknowns.md#u-0407): 공습 띠의 길이, 그리고 띠가 선택한 지점을 중심으로 하는지와 세이프 존을 벗어날 수 있는지. 상태: `open`.

중요한 이유 ([U-0407](unknowns.md#u-0407)): 너비와 함께 불타는 면적을 정하고, 불이 언세이프 존에 닿을 수 있는지를 정합니다.

- [U-0407](unknowns.md#u-0407) 자유 매개변수 `airstrike_strip_length_m`, 탐색 범위: 50 ~ 1000 m; 위키는 크기를 주지 않으며 지도 규모로 제한됩니다
- [U-0407](unknowns.md#u-0407) 해결 방법: VOD: 지도에서 불탄 띠를 측정.

### U-0409

[U-0409](unknowns.md#u-0409): 건십 폭탄 수와 타이밍: 'a gunship for 5min', 'one every 10s', 'each bomb lands 5s later'. 폭탄은 몇 개까지 투하할 수 있고, 첫 투하는 t=0입니까 t=10s입니까, 5min 이후에 착탄하는 폭탄도 떨어집니까? 상태: `open`.

중요한 이유 ([U-0409](unknowns.md#u-0409)): 폭탄 수는 30, 29, 31(구매자가 클릭해야 한다면 그보다 적음)이며, 총 피해와 Flak jacket의 가치를 정합니다.

- [U-0409](unknowns.md#u-0409) 해석 A: t=10,20,...,300s에 투하: 폭탄 30개, 마지막은 305s에 착탄
- [U-0409](unknowns.md#u-0409) 해석 B: t=0,10,...,290s에 투하: 폭탄 30개
- [U-0409](unknowns.md#u-0409) 해석 C: t=0,...,300s에 투하: 폭탄 31개
- [U-0409](unknowns.md#u-0409) 해석 D: t=10,...,290s에 투하: 폭탄 29개(만료 전 마지막 투하)
- [U-0409](unknowns.md#u-0409) 해석 E: 폭탄 발사는 10s 쿨다운의 수동 조작이며, 개수는 플레이어에 따라 다름
- [U-0409](unknowns.md#u-0409) 자유 매개변수 `gunship_bombs_max`, 탐색 범위: 폭탄 29 ~ 31개; 5min 구간과 10s 간격에서 도출했고, 'manual' 해석은 상한으로 추가했습니다
- [U-0409](unknowns.md#u-0409) 해결 방법: VOD: 타이머로 건십 한 번 전체의 폭탄 수를 셈.

### U-0418

[U-0418](unknowns.md#u-0418): 현상금의 결과: 현상금은 획득되면 끝납니까(위키는 1h 또는 사망 시 종료로 기술), 그래서 반복 획득이 가능합니까? 표시된 참가자의 10 HP는 획득 시 한 번만 차감됩니까? 현상금이 없는 생존 참가자가 없을 때 누가 대상이 됩니까? 상태: `open`.

중요한 이유 ([U-0418](unknowns.md#u-0418)): 획득 후에도 지속되는 현상금은 반복해서 지급되고 피해를 줄 것입니다.

- [U-0418](unknowns.md#u-0418) 해석 A: 획득하면 현상금이 끝나고 10 HP 피해는 한 번만 발생
- [U-0418](unknowns.md#u-0418) 해석 B: 현상금이 지속되며 매 1min마다 다시 획득 가능
- [U-0418](unknowns.md#u-0418) 해석 C: 현상금이 지속되며 다른 추적자의 획득에 대해서만 유효
- [U-0418](unknowns.md#u-0418) 해결 방법: VOD: 획득 후의 현상금 표시.

### U-0425

[U-0425](unknowns.md#u-0425): 좀비 흡수 타이밍: 'drain 1 HP from any contestants within 5m every 10s'. 10s 타이머는 좀비마다(전역 위상)입니까, 아니면 진입 시점부터 참가자마다입니까? 첫 흡수는 언제 발생합니까, 각 흡수는 '타격'([U-0002](unknowns.md#u-0002))입니까, 그리고 1 HP 하한 또는 Kick 라이브 중 감소가 적용됩니까? 상태: `open`.

중요한 이유 ([U-0425](unknowns.md#u-0425)): 많은 좀비에 의한 초당 흡수량: 좀비 50마리가 모두 범위 안에 있으면 5 HP/s입니다.

- [U-0425](unknowns.md#u-0425) 해석 A: 좀비마다: 틱 시점에 5m 안에 있는 모든 참가자가 1 HP를 잃음
- [U-0425](unknowns.md#u-0425) 해석 B: 좀비와 참가자 쌍마다, 타이머는 진입 시 시작
- [U-0425](unknowns.md#u-0425) 해석 C: 좀비마다, 첫 틱은 스폰 후 10s
- [U-0425](unknowns.md#u-0425) 해결 방법: VOD: 좀비 한 마리가 접근한 참가자, 시간 측정.

### U-0500

[U-0500](unknowns.md#u-0500): Piety 'one blood token per 5 HP healed': 나머지는 회복 사건 사이에 이월됩니까(누적 카운터), 아니면 사건마다 내림됩니까? 상태: `open`.

중요한 이유 ([U-0500](unknowns.md#u-0500)): 작은 회복(campfire 초당 1 HP, bandage 틱, Healing 시길의 1 HP 회복, 5/11/23/46 HP 포션)이 토큰을 전혀 주는지를 결정합니다. 사건마다 내림하면 1 HP씩의 잔회복은 0이 될 수 있습니다.

- [U-0500](unknowns.md#u-0500) 해석 A: 토큰 = floor(H_total / 5), H_total은 시작 이후 누적된 해당 회복 HP(나머지 이월)
- [U-0500](unknowns.md#u-0500) 해석 B: 사건당 토큰 = floor(h / 5), 회복 사건마다 나머지를 버림
- [U-0500](unknowns.md#u-0500) 해석 C: B와 같지만 지속 회복(2min 동안 10 HP의 bandage, Campfire 1 HP/s)은 틱마다 하나의 사건이므로 1 HP 틱은 아무것도 주지 않음
- [U-0500](unknowns.md#u-0500) 해결 방법: VOD: 여러 번의 회복에 걸쳐 Piety 참가자의 블러드 토큰 카운터를 관찰합니다. 연속된 3 HP 회복 두 번은 합계 토큰 1개(A) 또는 0개(B, C)를 줍니다.
- [U-0500](unknowns.md#u-0500) 해결 방법: REA: 배포된 서버 로직의 토큰 지급 코드(클라이언트 코드에는 없음, RE-0001).

### U-0501

[U-0501](unknowns.md#u-0501): Piety 토큰 카운터: 'HP healed'는 포션의 명목상 수치를 뜻합니까, 실제로 회복된 HP를 뜻합니까, 그리고 +15% 보너스가 포함됩니까? 상태: `open`.

중요한 이유 ([U-0501](unknowns.md#u-0501)): 최대 HP에 가까운 Piety 참가자는 거의 HP를 얻지 못한 채 포션을 마실 수 있습니다. 포션당 토큰 수확량이 최대 9개까지 달라집니다(gigantic potion).

- [U-0501](unknowns.md#u-0501) 해석 A: 실제로 회복된 HP(최대 HP로 제한), +15% 보너스 적용 후
- [U-0501](unknowns.md#u-0501) 해석 B: +15% 보너스 적용 후의 명목 회복량(초과 회복 포함)
- [U-0501](unknowns.md#u-0501) 해석 C: 보너스 적용 전의 명목 회복량(원래 등급 값 5/10/20/40, 초과 회복 포함)
- [U-0501](unknowns.md#u-0501) 해석 D: 실제로 회복된 HP, 보너스는 포함하지 않음
- [U-0501](unknowns.md#u-0501) 해결 방법: VOD: 여러 번의 회복에 걸쳐 Piety 참가자의 블러드 토큰 카운터를 관찰합니다. 최대 HP일 때와 최대치보다 1 HP 낮을 때 포션을 마시고 토큰 증가량을 비교합니다.
- [U-0501](unknowns.md#u-0501) 해결 방법: REA: 회복 처리 코드.

### U-0502

[U-0502](unknowns.md#u-0502): Piety 'from any source except revives, Campfires and healing circles included': Campfire와 healing circle은 집계됩니까(부활만 제외), 아니면 부활과 함께 제외됩니까? 상태: `open`.

중요한 이유 ([U-0502](unknowns.md#u-0502)): 끝의 'included'라는 구절은 예외 목록에 붙거나 집계되는 출처에 붙습니다. 'healing circle'이라는 용어는 코퍼스의 다른 곳에는 나오지 않습니다. Ingenuity Campfire 옆에 서 있는 것이 Piety 토큰을 주는지 여부가 달라집니다.

- [U-0502](unknowns.md#u-0502) 해석 A: 부활을 제외한 모든 회복이 집계됨. Campfire 회복과 healing circle은 명시적으로 포함
- [U-0502](unknowns.md#u-0502) 해석 B: 부활, Campfire, healing circle이 모두 제외됨. 그 밖의 모든 것은 집계
- [U-0502](unknowns.md#u-0502) 해결 방법: VOD: Campfire로 회복되는 Piety 참가자, 회복 전후의 토큰 카운터.
- [U-0502](unknowns.md#u-0502) 해결 방법: 주최 측의 발표.

### U-0504

[U-0504](unknowns.md#u-0504): Piety 참가자가 상자나 크레이트에서 얻는 "random health potion"의 크기 분포는 어떠합니까? 상태: `open`.

중요한 이유 ([U-0504](unknowns.md#u-0504)): 상자당 기대 회복량과 변환된 포션의 블러드 토큰 가치(토큰 1, 2, 3 또는 4개)는 등급별 가중치에 달려 있으나, 위키는 이를 제시하지 않습니다.

- [U-0504](unknowns.md#u-0504) 해석 A: 네 등급에 균등 (각 1/4)
- [U-0504](unknowns.md#u-0504) 해석 B: 작은 등급 쪽으로 치우침 (일반적인 체력 포션 드롭 표처럼)
- [U-0504](unknowns.md#u-0504) 해석 C: 등급은 대체되는 아이템 또는 상자 종류에 따라 달라짐
- [U-0504](unknowns.md#u-0504) 자유 매개변수 `piety_potion_tier_weights`, 탐색 범위: 4개의 가중치 각각이 [0,1] 범위이며 합은 1입니다. 균등 벡터(각 0.25)가 기준선이고, 두 극단(모두 작은 등급, 모두 거대(gigantic) 등급)이 상자의 가치 범위를 정합니다
- [U-0504](unknowns.md#u-0504) 해결 방법: VOD: 많은 Piety 획득 사례에서 포션 등급을 집계.
- [U-0504](unknowns.md#u-0504) 해결 방법: 주최 측의 발표.

### U-0507

[U-0507](unknowns.md#u-0507): Greed의 "A successful steal earns five blood tokens, once per victim every 24 hours": 24 h 제한은 토큰 지급만 제한합니까, 아니면 훔치기 자체를 제한합니까? 상태: `open`.

중요한 이유 ([U-0507](unknowns.md#u-0507)): 지급만 제한된다면 Greed 참가자는 아이템을 노리고 한 피해자에게서 30 min마다 계속 훔칠 수 있습니다. 그렇지 않다면 각 피해자는 같은 도둑에게 하루에 최대 한 개의 아이템만 잃습니다.

- [U-0507](unknowns.md#u-0507) 해석 A: 같은 피해자에게서의 훔치기는 쿨다운마다 허용되며, 토큰 5개는 피해자당 24 h에 최대 한 번만 지급됨
- [U-0507](unknowns.md#u-0507) 해석 B: 특정 피해자는 해당 도둑에게 24 h에 최대 한 번만 훔치기에 성공당할 수 있음
- [U-0507](unknowns.md#u-0507) 해결 방법: VOD: Greed 참가자가 24 h 안에 같은 피해자에게서 두 번 훔치는 장면 (쿨다운 30 min).
- [U-0507](unknowns.md#u-0507) 해결 방법: 주최 측의 발표.

### U-0510

[U-0510](unknowns.md#u-0510): Greed가 두 배로 늘리는("2x as far away") 상자와 크레이트의 기본 획득 범위는 얼마입니까? 상태: `open`.

중요한 이유 ([U-0510](unknowns.md#u-0510)): 자료 어디에도 일반 획득 또는 가져가기 범위가 없어서(상자 페이지가 삭제됨) Greed의 사거리는 아직 숫자가 아닙니다.

- [U-0510](unknowns.md#u-0510) 자유 매개변수 `chest_claim_range_base_m`, 탐색 범위: 2에서 20 m: 위키의 다른 접촉 행동은 10 m(훔치기, 상인, 묘비 루팅, 회복 범위)를 사용하므로 10 m이 중심값이고, 2 m / 20 m은 근접 접촉과 넓은 사거리의 경계입니다
- [U-0510](unknowns.md#u-0510) 해결 방법: VOD: Greed가 아닌 참가자와 Greed 참가자가 상자를 획득할 수 있는 거리.
- [U-0510](unknowns.md#u-0510) 해결 방법: SCOPE.md P1 (삭제된 상자 페이지).

### U-0512

[U-0512](unknowns.md#u-0512): Greed의 "adds a blood token to your money bag": money bag은 일반 블러드 토큰 잔액입니까, 아니면 나중에 지급되는 별도의 저장소입니까? 상태: `open`.

중요한 이유 ([U-0512](unknowns.md#u-0512)): 이 용어는 자료에 한 번만 나옵니다. 별도의 bag이라면 상인에게서 토큰을 쓸 수 있는 시점과 토큰이 묘비에 떨어지는지 여부가 달라집니다.

- [U-0512](unknowns.md#u-0512) 해석 A: money bag은 일반 잔액이며, 토큰 +1은 즉시 반영되고 사용 가능함
- [U-0512](unknowns.md#u-0512) 해석 B: 별도 저장소이며 어떤 조건(시간, 상인 방문, 사망)에서 풀림
- [U-0512](unknowns.md#u-0512) 해석 C: 별도 저장소이며 사망 시 사라지거나 묘비에 잠김
- [U-0512](unknowns.md#u-0512) 해결 방법: VOD: 상자를 획득한 직후 Greed 참가자의 토큰 카운터.
- [U-0512](unknowns.md#u-0512) 해결 방법: 주최 측의 발표.

### U-0514

[U-0514](unknowns.md#u-0514): landmine 또는 C4에 대한 "hack"은 무엇을 하며, 제한이 있습니까? 상태: `open`.

중요한 이유 ([U-0514](unknowns.md#u-0514)): Ingenuity는 해킹마다 블러드 토큰 하나를 얻습니다. 그 효과(해제, 탈취, 훔치기)가 적의 폭발물에 대한 대응이 되는지, 아니면 그것을 역이용하는지를 결정합니다.

- [U-0514](unknowns.md#u-0514) 해석 A: 해킹이 폭발물을 해제하거나 파괴함
- [U-0514](unknowns.md#u-0514) 해석 B: 해킹이 Ingenuity 참가자에게 통제권을 넘김 (시길 문구에 "take control of traps"라고 되어 있음)
- [U-0514](unknowns.md#u-0514) 해석 C: 해킹이 폭발물을 드러내고 Ingenuity 참가자가 집어 들 수 있게 함
- [U-0514](unknowns.md#u-0514) 해결 방법: VOD: Ingenuity 참가자가 적의 landmine을 해킹하는 장면.

### U-0517

[U-0517](unknowns.md#u-0517): Ingenuity 조합: 명시된 재료 두 개가 모두 소모됩니까, 조합 하나가 5개 조합 칸 중 하나를 차지합니까, 그리고 레시피 6개가 5칸에 어떻게 맞습니까? 상태: `open`.

중요한 이유 ([U-0517](unknowns.md#u-0517)): 레시피는 6개이고 조합 칸은 5개입니다. 같은 종류의 조합이 중첩되는지, 재료가 돌아오는지가 몇 개의 조합을 보유할 수 있는지를 결정합니다.

- [U-0517](unknowns.md#u-0517) 해석 A: 재료 두 개가 모두 소모되고, 각 조합은 5개 조합 칸 중 하나를 차지하며, 칸이 가득 찰 때까지 같은 레시피를 반복해서 조합할 수 있음
- [U-0517](unknowns.md#u-0517) 해석 B: 조합은 한 칸 안에서 종류별로 중첩됨
- [U-0517](unknowns.md#u-0517) 해석 C: 재료 하나만 소모됨
- [U-0517](unknowns.md#u-0517) 해결 방법: VOD: 조합 인벤토리가 가득 찬 Ingenuity 참가자가 조합하는 장면.
- [U-0517](unknowns.md#u-0517) 해결 방법: 주최 측의 발표.

### U-0518

[U-0518](unknowns.md#u-0518): 고유 조합의 "40% chance to be destroyed by Zombie hits": 굴림은 흡수 타격마다, 좀비마다, 아니면 조합마다 이루어지며, 막힌 타격도 굴립니까? 상태: `open`.

중요한 이유 ([U-0518](unknowns.md#u-0518)): 좀비 근처에서 조합의 기대 수명을 정합니다. 좀비는 10 s마다(가드 좀비는 5 s마다) 흡수하므로, 타격마다 굴리면 거의 모든 조합이 빠르게 파괴됩니다.

- [U-0518](unknowns.md#u-0518) 해석 A: 각 흡수 타격이 보유한 조합마다 한 번씩 굴리며 각각 40%
- [U-0518](unknowns.md#u-0518) 해석 B: 각 흡수 타격이 한 번 굴리고 무작위 조합 하나를 파괴함
- [U-0518](unknowns.md#u-0518) 해석 C: 좀비와의 조우당 한 번 굴림
- [U-0518](unknowns.md#u-0518) 해석 D: A 또는 B와 같으나 Shield, repellent 또는 bubble에 막힌 타격은 굴리지 않음
- [U-0518](unknowns.md#u-0518) 해결 방법: VOD: 좀비 근처에서 여러 조합을 가진 Ingenuity 참가자.

### U-0520

[U-0520](unknowns.md#u-0520): Campfire 공유 풀: 여러 사람이 있을 때 풀은 어떻게 소모되며, HP가 가득 찬 주변인도 회복됩니까? 상태: `open`.

중요한 이유 ([U-0520](unknowns.md#u-0520)): "Heals everyone within 10m 1 HP per second from one shared pool"은 대상 N명에 대해 풀 소모가 N HP/s라는 뜻일 수도, 전체 1 HP/s라는 뜻일 수도 있습니다. 풀은 포션의 회복량(5, 10, 20, 40 HP)과 같지만 10 min 상한도 있으므로 거대(gigantic) 포션은 40 HP만 줍니다.

- [U-0520](unknowns.md#u-0520) 해석 A: 범위 안에서 HP가 부족한 사람마다 풀에서 초당 1 HP를 가져감 (풀은 N HP/s로 소모됨)
- [U-0520](unknowns.md#u-0520) 해석 B: 풀은 범위 안의 사람들에게 나누어 합계 초당 1 HP를 지급함
- [U-0520](unknowns.md#u-0520) 해석 C: 범위 안의 모든 사람이 해당되며, HP가 가득 찬 사람도 각각 1 HP/s를 소모함
- [U-0520](unknowns.md#u-0520) 해결 방법: VOD: 범위 안에 참가자가 1명, 이어서 2명 있는 Campfire.

### U-0524

[U-0524](unknowns.md#u-0524): Fortress의 "up to 30 HP": 20 m 안의 모두가 공유하는 하나의 풀입니까, 아니면 한 사람당 30 HP입니까? 상태: `open`.

중요한 이유 ([U-0524](unknowns.md#u-0524)): 공유 풀 30 HP는 미사일 2발이면 사라집니다. 인원별이면 집단을 훨씬 오래 보호합니다. 피해 페이지는 "absorbs up to its remaining durability"라고 하는데, 이는 하나의 공유 내구도를 시사합니다.

- [U-0524](unknowns.md#u-0524) 해석 A: 30 HP의 공유 내구도 하나이며, 안에 있는 누구에게든 타격이 있으면 소모됨
- [U-0524](unknowns.md#u-0524) 해석 B: 보호받는 참가자마다 30 HP의 흡수량
- [U-0524](unknowns.md#u-0524) 해결 방법: VOD: fortress 안의 참가자 두 명이 모두 타격을 받는 장면.

### U-0525

[U-0525](unknowns.md#u-0525): Fortress와 존 피해: 존 피해는 30 HP 내구도에서 흡수됩니까, 아니면 완전히 무시됩니까? 상태: `open`.

중요한 이유 ([U-0525](unknowns.md#u-0525)): 페이지는 존 피해를 30 HP 흡수 옆에 나열하지만, "from Sigil of Greed stealing, and zone damage"로부터 보호한다고도 하며, 이는 별개 종류의 보호입니다.

- [U-0525](unknowns.md#u-0525) 해석 A: fortress 안에서 존 피해는 완전히 면역되며 내구도를 사용하지 않음
- [U-0525](unknowns.md#u-0525) 해석 B: 존 피해는 틱당 1 HP씩 30 HP 내구도에서 흡수됨
- [U-0525](unknowns.md#u-0525) 해결 방법: VOD: 세이프 존 밖의 fortress 안에 서 있는 참가자.

### U-0526

[U-0526](unknowns.md#u-0526): Fortress의 지속 시간과 위치: 얼마나 유지되며, 설치한 자리에 고정됩니까? 상태: `open`.

중요한 이유 ([U-0526](unknowns.md#u-0526)): 지속 시간이 없으면 30 HP는 영구적인 거점이 될 수 있는데, 페이지에는 지속 시간이 없습니다.

- [U-0526](unknowns.md#u-0526) 자유 매개변수 `fortress_duration_s`, 탐색 범위: 600 s(Campfire와 Robot의 상한)부터 이벤트 길이까지: 10 min은 비슷한 조합 아이템이 정하는 하한이고, 이벤트 전체가 상한입니다
- [U-0526](unknowns.md#u-0526) 해결 방법: VOD: 몇 분이 지난 뒤의 fortress.
- [U-0526](unknowns.md#u-0526) 해결 방법: 주최 측 발표.

### U-0528

[U-0528](unknowns.md#u-0528): Trolling의 "다른 플레이어에게 가한 5 HP당 블러드 토큰 1개": 나머지는 이월됩니까, 그리고 "가한"은 명목상의 타격입니까 실제로 통과한 HP(방어구, fortress, Kick 감소 적용 후)입니까? 상태: `open`.

중요한 이유 ([U-0528](unknowns.md#u-0528)): 5 HP짜리 가짜 상자는 5 HP 전체가 인정될 때만 토큰 1개를 줍니다. Kick 라이브 중인 피해자는 [U-0001](unknowns.md#u-0001)의 해석 A에서 4 HP를 받으며, 방어구나 Shield가 전부 흡수할 수도 있습니다.

- [U-0528](unknowns.md#u-0528) 해석 A: 피해자가 실제로 잃은 HP에 대한 누적 카운터, floor(total / 5)개의 토큰, 나머지 이월
- [U-0528](unknowns.md#u-0528) 해석 B: 감소 적용 후의 타격에 대해 타격마다 floor(d / 5), 나머지 폐기
- [U-0528](unknowns.md#u-0528) 해석 C: 누적이든 타격별이든, 방어구, fortress, Kick 감소 이전의 명목상 타격에 대해 계산
- [U-0528](unknowns.md#u-0528) 해석 D: Body Armor나 fortress가 흡수한 피해도 가한 것으로 인정
- [U-0528](unknowns.md#u-0528) 해결 방법: VOD: 방어구를 입은, Shield를 가진, Kick 라이브 중인 피해자에게 가짜 상자를 열게 한 뒤의 Trolling 참가자 토큰 카운터.

### U-0529

[U-0529](unknowns.md#u-0529): Trolling 수입 범위: 어떤 피해가 "다른 플레이어에게 가한 HP"로 인정됩니까(무기, 가짜 상자, 언세이프 서클 틱, fake gravestone의 독, 반사된 타격), 그리고 어떤 크레이트가 "누가 소환했든 파괴된 크레이트"로 인정됩니까? 상태: `open`.

중요한 이유 ([U-0529](unknowns.md#u-0529)): 언세이프 서클 틱은 각각 1 HP이며 주기적인 피해원입니다. 이것이 보상을 주는지는 주기적 피해가 타격인지에 달려 있습니다([U-0002](unknowns.md#u-0002)). Ingenuity의 Black hole이나 다른 참가자가 파괴한 크레이트가 Trolling 참가자에게 보상을 줄 수도, 주지 않을 수도 있습니다.

- [U-0529](unknowns.md#u-0529) 해석 A: 참가자 본인의 무기와 함정이 입힌 피해만, 참가자 본인의 행동으로 파괴된 크레이트만
- [U-0529](unknowns.md#u-0529) 해석 B: 참가자의 함정이 일으킨 언세이프 서클 틱과 독 단계도 포함, 그 근처에서 누구든 파괴한 크레이트
- [U-0529](unknowns.md#u-0529) 해석 C: 피해는 대상의 HP를 실제로 줄일 때만 인정, 시청자가 구매한 크레이트를 포함해 참가자 본인이 파괴한 크레이트만
- [U-0529](unknowns.md#u-0529) 해결 방법: VOD: 피해자가 안에 있는 언세이프 서클 뒤의 Trolling 토큰 카운터.
- [U-0529](unknowns.md#u-0529) 해결 방법: 주최 측 발표.

### U-0535

[U-0535](unknowns.md#u-0535): 언세이프 서클(unsafe circle) "50m (164ft) 서클": 50 m는 반지름입니까 지름입니까? 상태: `open`.

중요한 이유 ([U-0535](unknowns.md#u-0535)): 면적이 4배 차이 납니다(약 7854 m2 대 1963 m2).

- [U-0535](unknowns.md#u-0535) 해석 A: 반지름 50 m
- [U-0535](unknowns.md#u-0535) 해석 B: 지름 50 m(반지름 25 m)
- [U-0535](unknowns.md#u-0535) 자유 매개변수 `unsafe_circle_radius_m`, 탐색 범위: 25에서 50 m(지름 해석 대 반지름 해석)
- [U-0535](unknowns.md#u-0535) 해결 방법: VOD: 서클을 설치하고 지도에서 측정.
- [U-0535](unknowns.md#u-0535) 해결 방법: 주최 측 발표.

### U-0537

[U-0537](unknowns.md#u-0537): 언세이프 서클(unsafe circle) 피해 시계: 첫 타격은 진입마다 2 s 뒤입니까(나갈 때 타이머 초기화), 아니면 전역 2 s 위상이 계속됩니까? 서클 중 세이프 존 안쪽 부분과 바깥 부분 사이를 이동하면 초기화됩니까? 상태: `open`.

중요한 이유 ([U-0537](unknowns.md#u-0537)): 가장자리를 스치듯 지나가는 참가자의 피해가 달라집니다. 또한 일반 존 피해의 5 s 유예([U-0003](unknowns.md#u-0003))와도 상호작용합니다.

- [U-0537](unknowns.md#u-0537) 해석 A: 참가자별 타이머: 피해를 주는 부분에 들어간 뒤 2 s 후 첫 타격, 나가면 초기화
- [U-0537](unknowns.md#u-0537) 해석 B: 참가자가 서클 안에 있는 동안 타이머 유지, 존 안쪽 부분과 존 바깥 부분을 오가는 경우에도 유지
- [U-0537](unknowns.md#u-0537) 해석 C: 안에 있는 동안 전역 2 s 틱
- [U-0537](unknowns.md#u-0537) 해결 방법: VOD: 언세이프 서클에 들어가고 나가는 참가자.

### U-0538

[U-0538](unknowns.md#u-0538): 언세이프 서클(unsafe circle) 아이템 손실: 첫 손실은 진입과 첫 타격에 대해 언제 발생합니까? 상태: `open`.

중요한 이유 ([U-0538](unknowns.md#u-0538)): 두 조항의 표현이 다릅니다(안에 있는 동안 "5초마다" 대 "첫 타격 후 ... 5초마다"). 첫 손실 시점이 0에서 5 s까지 차이 납니다.

- [U-0538](unknowns.md#u-0538) 해석 A: 첫 손실은 t_hit + 5 s, 이후 5 s마다
- [U-0538](unknowns.md#u-0538) 해석 B: 첫 손실은 첫 타격 시점, 이후 5 s마다
- [U-0538](unknowns.md#u-0538) 해석 C: 첫 손실은 진입 5 s 후, 이후 5 s마다, 첫 타격과 무관
- [U-0538](unknowns.md#u-0538) 해결 방법: VOD: 방어 아이템 여러 개를 가지고 서클에 들어가는 참가자.

### U-0601

[U-0601](unknowns.md#u-0601): Death 회복 "지금까지 탈락한 모든 참가자마다, 본인 포함": 무엇을 셉니까, 그리고 부활한 참가자도 여전히 셉니까? 상태: `open`.

중요한 이유 ([U-0601](unknowns.md#u-0601)): 근처 사망마다의 회복 크기 N을 정합니다. N은 이벤트 중에 커지므로 선택에 따라 Death의 총 회복량이 달라집니다.

- [U-0601](unknowns.md#u-0601) 해석 A: N = 이벤트 시작 이후의 사망 횟수, 새 희생자 포함(부활해도 줄지 않음)
- [U-0601](unknowns.md#u-0601) 해석 B: N = 현재 죽어 있는 참가자 수, 새 희생자 포함(부활하면 줄어듦)
- [U-0601](unknowns.md#u-0601) 해석 C: N = 한 번 이상 사망한 서로 다른 참가자 수
- [U-0601](unknowns.md#u-0601) 해결 방법: VOD: 부활 뒤에 이어진 사망 후 Death 참가자에게 표시되는 회복량.

### U-0602

[U-0602](unknowns.md#u-0602): Death 상한 "참가자의 20% 이하가 생존했을 때": 20%는 무엇을 기준으로 하며 어떻게 반올림하고, 생존자 수는 회복을 일으키는 사망 이전에 셉니까 이후에 셉니까? 상태: `open`.

중요한 이유 ([U-0602](unknowns.md#u-0602)): 60% 상한이 켜지는 정확한 탈락 시점을 정합니다. 전체 참가자가 N명일 때 임계값이 참가자 한 명만큼 달라집니다.

- [U-0602](unknowns.md#u-0602) 해석 A: 정확히 alive * 5 <= N (alive <= floor(N/5)와 같음)
- [U-0602](unknowns.md#u-0602) 해석 B: alive <= ceil(N/5)
- [U-0602](unknowns.md#u-0602) 해석 C: 생존자 수를 회복을 일으키는 사망 이후에 셈; D: 생존자 수를 그 사망 이전에 셈(A 또는 B와 조합)
- [U-0602](unknowns.md#u-0602) 해결 방법: 주최 측의 N 발표([U-0009](unknowns.md#u-0009)), 그다음 60%에서 멈추는 첫 Death 회복의 VOD.

### U-0603

[U-0603](unknowns.md#u-0603): Death 60% 상한: HP가 이미 최대 HP의 60%를 넘는 경우, 회복이 HP를 상한까지 낮춥니까, 아무 일도 없습니까, 아니면 상한이 반올림됩니까? 상태: `open`.

중요한 이유 ([U-0603](unknowns.md#u-0603)): 문자 그대로의 상한은 건강한 Death 참가자의 HP를 깎을 수 있습니다. 또한 M이 5의 배수가 아니면 상한값 0.6*M이 소수입니다.

- [U-0603](unknowns.md#u-0603) 해석 A: HP' = min(HP + h, 0.6*M), HP를 낮출 수 있음
- [U-0603](unknowns.md#u-0603) 해석 B: HP' = max(HP, min(HP + h, 0.6*M)), 절대 낮추지 않음
- [U-0603](unknowns.md#u-0603) 해석 C: B와 같고 상한 = floor(0.6*M)
- [U-0603](unknowns.md#u-0603) 해석 D: B와 같고 상한 = ceil(0.6*M)
- [U-0603](unknowns.md#u-0603) 해결 방법: VOD: 20% 이하가 생존한 상태에서 사망 근처에 있는, HP가 60%를 넘는 Death 참가자.

### U-0604

[U-0604](unknowns.md#u-0604): Death ward: 2h 쿨다운은 언제 시작됩니까(막힌 타격 시점, 2min 면역이 끝날 때, 또는 시길 선택 시점부터), ward는 선택 시점에 준비되어 있습니까, 그리고 어떤 피해 틱이 "첫 타격"으로 인정됩니까? 상태: `open`.

중요한 이유 ([U-0604](unknowns.md#u-0604)): 이벤트 중 ward가 몇 번 보호할 수 있는지(2h당 2 min 윈도)와 존 틱이 이를 소모하는지가 정해집니다.

- [U-0604](unknowns.md#u-0604) 해석 A: 쿨다운은 첫 번째로 막은 타격에서 시작, 시길 선택 시점부터 준비됨
- [U-0604](unknowns.md#u-0604) 해석 B: 쿨다운은 2min 면역이 끝날 때 시작
- [U-0604](unknowns.md#u-0604) 해석 C: 선택 2h 후에야 준비됨
- [U-0604](unknowns.md#u-0604) 해석 D: 주기적인 존 틱도 타격으로 인정([U-0002](unknowns.md#u-0002) 참조), E: 개별 공격만 인정
- [U-0604](unknowns.md#u-0604) 해결 방법: VOD: 2h 안에 존을 두 번 벗어나는 Death 참가자.

### U-0606

[U-0606](unknowns.md#u-0606): Death "약탈": 아이템이나 블러드 토큰을 처음 루팅하는 것이 "묘비 약탈" 행동과 같은 5% 회복과 10 토큰을 줍니까, 그리고 부활을 위해 잠겨 있는 동안 블러드 토큰을 루팅할 수 있습니까? 상태: `open`.

중요한 이유 ([U-0606](unknowns.md#u-0606)): 소개 페이지는 부활이 가능한 동안 묘 안의 토큰이 잠겨 있다고 하는데, Death 페이지는 토큰을 처음 루팅하면 묘를 약탈한다고 합니다.

- [U-0606](unknowns.md#u-0606) 해석 A: 아이템이나 토큰의 첫 루팅은 완전한 약탈(회복, 10 토큰, 묘가 부활 불가가 됨), 토큰은 즉시 루팅 가능
- [U-0606](unknowns.md#u-0606) 해석 B: 첫 루팅은 약탈이지만 부활 가능 기간이 끝날 때까지 토큰은 루팅할 수 없으므로 아이템 루팅만 일찍 약탈이 됨
- [U-0606](unknowns.md#u-0606) 해석 C: 첫 루팅은 묘를 봉인할 뿐이고, 회복과 10 토큰은 명시적인 약탈 행동이 필요함
- [U-0606](unknowns.md#u-0606) 해결 방법: VOD: 사망 후 10 min이 지나기 전에 묘를 루팅하는 Death 참가자.

### U-0607

[U-0607](unknowns.md#u-0607): Endurance 보급 상자 "2h 30min마다": 첫 투하는 이벤트 시작 2h30 후입니까, 시길 선택 후입니까, 이전 수령 후입니까, 그리고 어떤 상자가 "자신의 것"입니까? 상태: `open`.

중요한 이유 ([U-0607](unknowns.md#u-0607)): 이벤트 동안 Endurance 참가자가 6 토큰 수령을 몇 번 할 수 있는지와 보급이 언제 도착하는지가 정해집니다.

- [U-0607](unknowns.md#u-0607) 해석 A: 이벤트 시작부터의 고정 시계
- [U-0607](unknowns.md#u-0607) 해석 B: 시길 선택부터의 고정 시계
- [U-0607](unknowns.md#u-0607) 해석 C: 이전 상자를 수령하거나 착지할 때 타이머가 재시작
- [U-0607](unknowns.md#u-0607) 해석 D: "자신의 것" = 누가 서 있든 자기 근처에 떨어진 상자; E: 수령자도 본인이어야 함
- [U-0607](unknowns.md#u-0607) 해결 방법: VOD: 이벤트 시작과 시길 선택 대비 첫 Endurance 투하 타임스탬프.

### U-0612

[U-0612](unknowns.md#u-0612): 소환 좀비, 죽음 좀비, 호드 보너스 좀비는 얼마나 오래 존재합니까("A zombie disappears when its time runs out")? 상태: `open`.

중요한 이유 ([U-0612](unknowns.md#u-0612)): 수명은 좀비의 흡수량과 Necromancy 블러드 토큰 수입의 상한을 정합니다. 지속 시간이 명시된 것은 가드 좀비(1h)뿐입니다.

- [U-0612](unknowns.md#u-0612) 자유 매개변수 `zombie_lifetime_s`, 탐색 범위: 60 ~ 86400 s: 좀비가 의미를 가지려면 최소 1분, 어떤 이벤트 길이보다도 긴 상한으로 하루 전체이며, 기준값은 3600 s인 가드 좀비입니다.
- [U-0612](unknowns.md#u-0612) 해결 방법: VOD: 소환부터 좀비가 사라질 때까지의 시간.

### U-0613

[U-0613](unknowns.md#u-0613): Necromancy의 "The HP goes to you": 얻는 HP는 피해자가 실제로 잃은 HP입니까, 소유자의 최대 HP로 제한됩니까, 그리고 막히거나 방어구가 받아낸 흡수(drain)도 HP와 토큰을 줍니까? 상태: `open`.

중요한 이유 ([U-0613](unknowns.md#u-0613)): 흡수 틱당 Necromancy의 지속력과 블러드 토큰 수입을 정합니다.

- [U-0613](unknowns.md#u-0613) 해석 A: 소유자는 피해자에게서 실제로 제거된 HP를 얻으며, 최대 HP로 제한됨
- [U-0613](unknowns.md#u-0613) 해석 B: 방어구가 이를 받아내더라도 소유자는 틱당 명목상의 1 HP(또는 2 HP)를 얻으며, 최대 HP로 제한됨
- [U-0613](unknowns.md#u-0613) 해석 C: 소유자는 명목상의 HP를 얻고 최대 HP를 넘을 수 있음
- [U-0613](unknowns.md#u-0613) 해석 D: 블러드 토큰("one per HP your zombies drain")은 HP와 같은 기준을 따름
- [U-0613](unknowns.md#u-0613) 해결 방법: VOD: 방어구를 입은 피해자를 흡수할 때의 소유자 HP와 토큰 카운터.

### U-0617

[U-0617](unknowns.md#u-0617): Protection의 "Potions heal you 50% less": 어떤 회복이 "포션"입니까(회복 포션, Eddie의 포션, God's Fruit, 붕대, 회복 서클)? 상태: `open`.

중요한 이유 ([U-0617](unknowns.md#u-0617)): Protection 참가자가 여전히 얼마나 많은 회복을 쓸 수 있는지를 결정합니다.

- [U-0617](unknowns.md#u-0617) 해석 A: 모든 등급의 회복 포션만
- [U-0617](unknowns.md#u-0617) 해석 B: 회복 포션과 Eddie의 포션(최대 HP의 50%를 회복하는 도박)
- [U-0617](unknowns.md#u-0617) 해석 C: 아이템으로 인한 모든 회복
- [U-0617](unknowns.md#u-0617) 해결 방법: VOD: Protection 참가자가 각 회복 아이템을 사용하는 장면.
- [U-0617](unknowns.md#u-0617) 범위 축소: 2026-11-11 스냅샷의 본문만으로 2026-11-13에 범위를 좁혔으며, 해결된 것은 아닙니다. Campfire는 이 규칙에서 제외됩니다. "Piety and Protection potion changes do not apply"(wiki-sigils-ingenuity-021). 붕대는 Protection 페이지에서 포션 줄 옆에 자체 줄이 있습니다. "Bandages last 1.1x as long"(wiki-sigils-protection-017). 이는 붕대가 포션으로 계산되지 않음을 시사하지만, 그렇다고 명시하지는 않습니다. 문구는 해석 A와 B 중 어느 쪽도 택하지 않습니다. Protection은 "Potions heal you 50% less"라고 하고(wiki-sigils-protection-016) Piety는 "Health potions heal you 15% more"라고 하며(wiki-sigils-piety-013), 포션이라고 불리는 것이 둘 더 있습니다. Eddie의 포션과 "heals by potion tier"인 Everything potion입니다(wiki-sigils-ingenuity-023). 아직 미해결: Eddie의 포션, Everything potion, God's Fruit, 회복 서클.

### U-0624

[U-0624](unknowns.md#u-0624): Healing 부활 카운터: "2 times"(부활되는 Healing 참가자)와 "10 times"(부활시키는 Healing 참가자): 이벤트당입니까, 쌍당입니까, 그리고 취소되거나 실패한 부활도 셉니까? 상태: `open`.

중요한 이유 ([U-0624](unknowns.md#u-0624)): Healing 참가자의 생명 수와 총 부활 횟수의 상한을 정합니다.

- [U-0624](unknowns.md#u-0624) 해석 A: 각 Healing 참가자에 대해 이벤트 전체 합계이며, 성공한 부활만 집계
- [U-0624](unknowns.md#u-0624) 해석 B: 2회 규칙은 부활시키는 사람별
- [U-0624](unknowns.md#u-0624) 해석 C: 부활이 취소되더라도 시도가 집계됨
- [U-0624](unknowns.md#u-0624) 해결 방법: VOD: Healing 참가자의 세 번째 부활.

### U-0625

[U-0625](unknowns.md#u-0625): 부활 비용 "costs the reviver 5 HP": HP가 5 이하인 부활자를 죽일 수 있습니까, 그리고 타격 파이프라인(방어구, Fortress, Kick 라이브)을 거칩니까? 상태: `open`.

중요한 이유 ([U-0625](unknowns.md#u-0625)): HP가 5 이하인 부활자는 부활 때문에 죽을 수 있으며, 부활한 참가자는 5 HP를 받습니다.

- [U-0625](unknowns.md#u-0625) 해석 A: 부활에는 HP > 5가 필요하며, 그렇지 않으면 거부됨
- [U-0625](unknowns.md#u-0625) 해석 B: 부활에는 HP >= 5가 필요하며 HP가 0이 될 수 있음(부활자 사망)
- [U-0625](unknowns.md#u-0625) 해석 C: 비용은 min(5, HP - 1)
- [U-0625](unknowns.md#u-0625) 해석 D: 비용이 타격 파이프라인을 거침([U-0002](unknowns.md#u-0002) 참조)
- [U-0625](unknowns.md#u-0625) 해결 방법: VOD: HP 5인 부활자가 부활을 시도하는 장면.

## 우선순위: 보통

### U-0003

[U-0003](unknowns.md#u-0003): 존 피해: 세이프 존을 벗어난 뒤 첫 틱은 5 s입니까, 7 s입니까? 상태: `open`.

중요한 이유 ([U-0003](unknowns.md#u-0003)): 존 밖에서 사망하기까지의 시간이 2 s 달라집니다(T(100) = 203 s 또는 205 s).

- [U-0003](unknowns.md#u-0003) 해석 A: 첫 틱은 5 s, 이후 2 s마다
- [U-0003](unknowns.md#u-0003) 해석 B: 첫 틱은 7 s(5 s 유예 후 2 s 간격 한 번)
- [U-0003](unknowns.md#u-0003) 해결 방법: 존을 벗어나는 참가자를 화면 내 타이머와 함께 담은 VOD.

### U-0007

[U-0007](unknowns.md#u-0007): Healing 재생: 피해가 30 min 타이머를 초기화합니까? 상태: `open`.

중요한 이유 ([U-0007](unknowns.md#u-0007)): 주기적 피해 상황에서 지속 재생 속도를 정합니다.

- [U-0007](unknowns.md#u-0007) 해석 A: 30 min 고정 시계이며 피해가 이를 초기화하지 않습니다
- [U-0007](unknowns.md#u-0007) 해석 B: 피해가 타이머를 초기화합니다
- [U-0007](unknowns.md#u-0007) 해결 방법: VOD: 타격을 받는 Healing 참가자의 한 시간 동안의 HP.

### U-0010

[U-0010](unknowns.md#u-0010): Wizard staff의 '5 s 동안 총 10 HP': 한 번의 타격입니까, 여러 번의 틱입니까? 상태: `open`.

중요한 이유 ([U-0010](unknowns.md#u-0010)): Kick 보너스, Kick 감소, 최소 1 HP가 한 번만 적용되는지 틱마다 적용되는지를 정합니다.

- [U-0010](unknowns.md#u-0010) 해석 A: 10 HP 타격 한 번
- [U-0010](unknowns.md#u-0010) 해석 B: 2 HP 틱 다섯 번
- [U-0010](unknowns.md#u-0010) 해석 C: 1 HP 틱 열 번
- [U-0010](unknowns.md#u-0010) 해결 방법: VOD: staff 범위 효과 중의 HP 표시.

### U-0011

[U-0011](unknowns.md#u-0011): 부활 제한 시간: 소개 페이지의 'within 10min of their death'와 Healing 페이지의 'within 10min of the death' 중, 누구의 사망이 제한 시간을 시작시킵니까? 상태: `open`.

중요한 이유 ([U-0011](unknowns.md#u-0011)): 문자 그대로 읽으면 'their'는 부활시키는 참가자들을 가리킬 수 있습니다.

- [U-0011](unknowns.md#u-0011) 해석 A: 죽은 참가자의 사망(유일하게 일관된 해석)
- [U-0011](unknowns.md#u-0011) 해석 B: 부활시키는 사람의 사망
- [U-0011](unknowns.md#u-0011) 해결 방법: Healing 페이지의 표현이 A를 뒷받침합니다.

### U-0012

[U-0012](unknowns.md#u-0012): Kick 라이브 상태는 어떻게 감지되며, 지연은 얼마입니까? 상태: `open`.

중요한 이유 ([U-0012](unknowns.md#u-0012)): 스트림이 끊기면 전투 도중 10% 보정이 뒤바뀔 수 있습니다.

- [U-0012](unknowns.md#u-0012) 해결 방법: 주최자의 발언, 전투 중 스트림 재접속이 담긴 VOD.

### U-0102

[U-0102](unknowns.md#u-0102): Fortress 단계: 참가자가 여러 fortress 안에 서 있을 때 한 번의 타격을 몇 개의 fortress가 흡수할 수 있으며, 어떤 순서이고, 내구도는 흡수한 HP 1당 1씩 줄어듭니까? 상태: `open`.

중요한 이유 ([U-0102](unknowns.md#u-0102)): 중첩된 fortress가 내구도를 합산하는지, 그리고 fortress 내구도가 HP 풀인지를 정합니다.

- [U-0102](unknowns.md#u-0102) 해석 A: fortress 하나(가장 가깝거나 먼저 지어진 것)가 min(h, dur)을 흡수하고 dur -= absorbed
- [U-0102](unknowns.md#u-0102) 해석 B: 범위 안의 모든 fortress가 h = 0이 될 때까지 차례로 흡수
- [U-0102](unknowns.md#u-0102) 해석 C: 흡수는 HP당이 아니라 타격당
- [U-0102](unknowns.md#u-0102) 해결 방법: VOD: 겹치는 fortress 두 개 안에 있는 참가자가 타격을 받는 장면.
- [U-0102](unknowns.md#u-0102) 해결 방법: 아이템 페이지의 fortress 규칙을 이 단계와 대조해 읽습니다(교차 계열).

### U-0105

[U-0105](unknowns.md#u-0105): 'Blood tokens in the grave stay locked while revival is possible': 누구의 토큰이며, 얼마 동안이고, 잠금이 끝나면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0105](unknowns.md#u-0105)): 루팅하는 사람(Death 시길 포함)이 묘비에서 토큰을 가져갈 수 있는 시점과, 부활한 참가자가 돌려받는 것을 정합니다.

- [U-0105](unknowns.md#u-0105) 해석 A: 죽은 참가자의 토큰은 10 min 동안 잠기고 그 후 루팅할 수 있으며, 부활하면 돌려받음
- [U-0105](unknowns.md#u-0105) 해석 B: 부활이 일어나거나 다른 이유(부활 상한, 강탈)로 부활이 불가능해질 때까지 잠김
- [U-0105](unknowns.md#u-0105) 해석 C: 처치한 사람에게 지급된 토큰도 제한 시간이 끝날 때까지 묘비에 잠김
- [U-0105](unknowns.md#u-0105) 해결 방법: VOD: 10 min 전과 후에 루팅된 묘비.
- [U-0105](unknowns.md#u-0105) 해결 방법: Death 시길 페이지의 'first to loot items or blood tokens' 규칙과 대조합니다.

### U-0106

[U-0106](unknowns.md#u-0106): 시청자 왕관 처치 보너스 'equal to 20% of the attack's purchase price': 끝수 처리 규칙, 'kills'가 최종 처치를 뜻하는지 여부, 그리고 여러 시청자가 보유자를 공격했을 때 어느 공격이 해당되는지. 상태: `open`.

중요한 이유 ([U-0106](unknowns.md#u-0106)): 이 규칙이 없으면 가격([U-0014](unknowns.md#u-0014))을 알게 되더라도 시청자에게 왕관 처치의 가치를 계산할 수 없습니다.

- [U-0106](unknowns.md#u-0106) 해석 A: bonus = floor(0.2*p)
- [U-0106](unknowns.md#u-0106) 해석 B: bonus = ceil(0.2*p)
- [U-0106](unknowns.md#u-0106) 해석 C: bonus = 0.2*p 그대로(소수 Cx-Bucks 허용)
- [U-0106](unknowns.md#u-0106) 해결 방법: VOD/화면: 가격이 알려진 공격으로 왕관 처치를 한 뒤 시청자의 Cx-Bucks 잔액.
- [U-0106](unknowns.md#u-0106) 해결 방법: 주최자의 발언.

### U-0108

[U-0108](unknowns.md#u-0108): 비Healing 참가자는 누가 부활시킬 수 있습니까? 두 규칙에서 암시되는 대로 Healing 참가자만입니까, 아니면 다른 규칙에 따라 누구든 가능합니까? 상태: `open`.

중요한 이유 ([U-0108](unknowns.md#u-0108)): 주변에 살아 있는 Healing 참가자가 없을 때 죽은 비Healing 참가자를 부활시킬 수 있는지를 결정합니다.

- [U-0108](unknowns.md#u-0108) 해석 A: Healing 참가자만 비Healing 참가자를 부활시킬 수 있고, 다른 참가자는 Healing 참가자만 부활시킬 수 있습니다
- [U-0108](unknowns.md#u-0108) 해석 B: 어떤 참가자든 모든 참가자를 부활시킬 수 있고, 2-times 규칙은 Healing 대상에만 해당하는 제한입니다
- [U-0108](unknowns.md#u-0108) 해결 방법: VOD: 비Healing 참가자가 다른 비Healing 참가자를 부활시키는 장면.
- [U-0108](unknowns.md#u-0108) 해결 방법: 주최 측 설명.

### U-0113

[U-0113](unknowns.md#u-0113): 'Moving too fast counts as being outside': 속도 규칙이 발동하면 5 s 유예와 2 s당 1 HP가 서클 밖처럼 적용됩니까, 언제부터 시작됩니까, 그리고 속도가 떨어지는 즉시 끝납니까? 상태: `open`.

중요한 이유 ([U-0113](unknowns.md#u-0113)): 빠른 이동의 대가를 정합니다: 즉시 틱인지, 5 s 지연과 히스테리시스인지.

- [U-0113](unknowns.md#u-0113) 해석 A: 위반 = 서클 밖. 일반 5 s 유예 뒤 틱이 시작되고, 윈도가 다시 정상이 되면 끝납니다
- [U-0113](unknowns.md#u-0113) 해석 B: 유예 없이 틱이 즉시 시작됩니다
- [U-0113](unknowns.md#u-0113) 해석 C: 윈도가 다시 정상이 될 때까지 서클 밖 상태가 유지되며, 이는 속도 하락보다 최대 윈도 길이만큼 늦습니다
- [U-0113](unknowns.md#u-0113) 자유 매개변수 `speed_violation_grace_s`, 탐색 범위: 0 ~ 5 s: 유예가 없으면 0, 서클 밖 유예와 같으면 5
- [U-0113](unknowns.md#u-0113) 해결 방법: VOD: 빠른 탑승 중인 참가자의 속도 대비 HP 타임라인.

### U-0115

[U-0115](unknowns.md#u-0115): 독: 첫 1 HP가 즉시 들어갑니까, 1min 30s 뒤입니까, 아니면 고정된 전역 90 s 위상입니까? 상태: `open`.

중요한 이유 ([U-0115](unknowns.md#u-0115)): 어느 시점에서 끊어도 총 피해가 1 HP 달라지며, 해독 수단의 가치가 달라집니다.

- [U-0115](unknowns.md#u-0115) 해석 A: 중독 후 t = 90 s에 첫 틱, 이후 90 s마다
- [U-0115](unknowns.md#u-0115) 해석 B: t = 0에 첫 틱, 이후 90 s마다
- [U-0115](unknowns.md#u-0115) 해석 C: 중독 시작과 무관하게 전역 90 s 격자에 따라 틱
- [U-0115](unknowns.md#u-0115) 해결 방법: VOD: Poison Dart에 맞은 뒤 시계가 있는 중독 참가자의 HP.

### U-0119

[U-0119](unknowns.md#u-0119): Death Ward: 2 min의 면역은 첫 번째로 막은 타격에서 시작합니까, 시길을 선택한 때 시작합니까? 'Cooldown 2h'는 활성화 시점에 시작합니까, 2 min이 끝난 때 시작합니까? 그리고 Ward는 쿨다운당 한 번만 사용할 수 있습니까? 상태: `open`.

중요한 이유 ([U-0119](unknowns.md#u-0119)): Death 참가자가 서클 밖 피해를 얼마나 자주 무시할 수 있는지를 정합니다.

- [U-0119](unknowns.md#u-0119) 해석 A: 2 min 윈도는 첫 번째로 막은 타격에서 시작하며, 쿨다운 2 h는 그 시점부터입니다
- [U-0119](unknowns.md#u-0119) 해석 B: 2 min 윈도는 참가자의 활성화로 시작하며, 쿨다운 2 h는 활성화 시점부터입니다
- [U-0119](unknowns.md#u-0119) 해석 C: 쿨다운은 2 min 윈도가 끝날 때 시작합니다
- [U-0119](unknowns.md#u-0119) 해결 방법: VOD: 첫 서클 밖 타격 이후의 Death 참가자.
- [U-0119](unknowns.md#u-0119) 해결 방법: 이 기록에 대조해 읽는 Death 시길 페이지(패밀리 교차).

### U-0122

[U-0122](unknowns.md#u-0122): Wiki-damage-002는 'Reality Shield block every kind of damage. absorbs every kind of damage.'(뒤섞임)로 되어 있습니다: 어느 문장이 어느 아이템의 것입니까(Reality Shield는 모든 종류를 막고, Body armor는 모든 종류를 흡수)? 상태: `open`.

중요한 이유 ([U-0122](unknowns.md#u-0122)): Reality Shield가 모든 피해를 막는다는 유일한 진술이며, 표에는 나열되어 있지 않습니다.

- [U-0122](unknowns.md#u-0122) 해석 A: Reality Shield는 모든 종류의 피해를 막고, Body armor는 모든 종류의 피해를 흡수합니다(표의 설명문)
- [U-0122](unknowns.md#u-0122) 해석 B: Reality Shield는 Shield 주석이 제외하는 것을 뺀 모든 종류의 피해를 막습니다
- [U-0122](unknowns.md#u-0122) 해결 방법: 렌더링된 페이지를 다시 가져와 머리글 텍스트 확인.
- [U-0122](unknowns.md#u-0122) 해결 방법: 아이템 페이지의 Reality Shield 섹션.

### U-0123

[U-0123](unknowns.md#u-0123): 피해 표의 Hazmat suit '(slows)': 느려짐은 존 피해, 언세이프 서클(unsafe circle) 피해, Robot 피해에 어떤 영향을 줍니까(틱 간격 배수, 피해 비율)? 상태: `open`.

중요한 이유 ([U-0123](unknowns.md#u-0123)): 계수가 없으면 존 생존 면에서 Hazmat suit을 Body armor와 비교해 가격을 매길 수 없습니다.

- [U-0123](unknowns.md#u-0123) 해석 A: 틱 간격에 배수를 곱합니다(틱이 줄어듦)
- [U-0123](unknowns.md#u-0123) 해석 B: 시간에 따라 각 틱이 1 HP 미만으로 줄어듭니다(분수 누적)
- [U-0123](unknowns.md#u-0123) 해석 C: 이동만 느려지고 피해는 느려지지 않습니다
- [U-0123](unknowns.md#u-0123) 자유 매개변수 `hazmat_slow_factor`, 탐색 범위: 틱 간격의 1.0 ~ 4.0배: 1.0은 효과 없음, 4.0은 'slows'에 대한 상한 추측이며 스윕 선택입니다
- [U-0123](unknowns.md#u-0123) 해결 방법: 아이템 페이지의 Hazmat suit 섹션(패밀리 교차).

### U-0200

[U-0200](unknowns.md#u-0200): C4, landmine, 화살 외에 어떤 아이템이 한 슬롯에 중첩됩니까(Piety가 아닌 체력 포션, mirror forcefield, 기타)? 상태: `open`.

중요한 이유 ([U-0200](unknowns.md#u-0200)): 인벤토리 공간은 3 슬롯이므로, 중첩 규칙이 방어 수단과 포션이 몇 개 들어가는지를 결정합니다.

- [U-0200](unknowns.md#u-0200) 해석 A: 명시된 C4, landmine, 화살만 중첩됩니다
- [U-0200](unknowns.md#u-0200) 해석 B: 다른 종류도 중첩됩니다(목록은 열려 있음: 'such as')
- [U-0200](unknowns.md#u-0200) 해결 방법: VOD: 인벤토리가 가득 찬 상태에서 두 번째 mirror forcefield 또는 체력 포션을 줍는 참가자.
- [U-0200](unknowns.md#u-0200) 해결 방법: 무기 페이지의 중첩 크기는 한 중첩당 5와 10입니다.

### U-0201

[U-0201](unknowns.md#u-0201): 여러 mirror forcefield는 하나의 효과로 셉니까, 아니면 각각 효과 3개 상한에 하나씩 산입됩니까? 상태: `open`.

중요한 이유 ([U-0201](unknowns.md#u-0201)): 상한 3 아래에 mirror가 몇 개 들어가는지와 Shield 및 Flak jacket을 위해 남는 자리를 결정합니다.

- [U-0201](unknowns.md#u-0201) 해석 A: 각 mirror를 따로 셉니다
- [U-0201](unknowns.md#u-0201) 해석 B: 모든 mirror가 하나의 효과로 셉니다
- [U-0201](unknowns.md#u-0201) 해석 C: 들고만 있고 'used'하지 않은 mirror는 활성화되기 전까지 세지 않습니다
- [U-0201](unknowns.md#u-0201) 해결 방법: VOD: mirror 두 개를 든 참가자가 상한 상태에서 세 번째 효과 아이템을 사용하는 장면.

### U-0202

[U-0202](unknowns.md#u-0202): 상한 목록에 명시되지 않은 효과는 어떻게 동작합니까: EMP(10min), Thermal goggles(소지), Body armor, Sleeping Bag, 체력 포션? 그리고 상한 상태에서 Hazmat suit을 주우면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0202](unknowns.md#u-0202)): 상한의 'count' 및 'do not count' 목록은 모든 아이템을 다루지 않으며, 장비 구성 계획이 여기에 달려 있습니다.

- [U-0202](unknowns.md#u-0202) 해석 A: 명시된 아이템만 세며, EMP와 goggles는 세지 않습니다
- [U-0202](unknowns.md#u-0202) 해석 B: EMP는 시간제 아이템 효과로 세고, goggles는 Hazmat suit처럼 소지하는 동안 셉니다
- [U-0202](unknowns.md#u-0202) 해석 C: 상한에서는 Hazmat suit 줍기가 거부됩니다
- [U-0202](unknowns.md#u-0202) 해결 방법: VOD: 효과 3개를 가진 참가자가 EMP를 사용하거나 goggles 또는 Hazmat을 줍는 장면.

### U-0203

[U-0203](unknowns.md#u-0203): 체력 포션, bandage 틱, Eddie의 회복은 최대 HP로 제한됩니까? 상태: `open`.

중요한 이유 ([U-0203](unknowns.md#u-0203)): 최대치를 넘는 회복 문제는 높은 HP에서 포션이 낭비되는지, Eddie의 회복이 일부 손실되는지를 결정합니다.

- [U-0203](unknowns.md#u-0203) 해석 A: hp = min(maxHP, hp + h)
- [U-0203](unknowns.md#u-0203) 해석 B: hp가 최대 HP를 넘을 수 있습니다
- [U-0203](unknowns.md#u-0203) 해결 방법: VOD: 가득 찬 HP 또는 그에 가까운 HP에서 포션을 마시는 장면.
- [U-0203](unknowns.md#u-0203) 해결 방법: Healing 페이지는 재생이 'up to your max HP'까지라고 합니다(명시된 곳은 여기뿐).

### U-0206

[U-0206](unknowns.md#u-0206): Guardian angel의 '존 피해'에 언세이프 서클 피해가 포함됩니까? 상태: `open`.

중요한 이유 ([U-0206](unknowns.md#u-0206)): 피해 페이지의 표는 Guardian angel을 둘 다에 올려 두었지만, 아이템 페이지의 Shield 항목은 둘을 따로 언급합니다.

- [U-0206](unknowns.md#u-0206) 해석 A: 존 피해만 해당
- [U-0206](unknowns.md#u-0206) 해석 B: 서클 밖 피해와 언세이프 서클 피해
- [U-0206](unknowns.md#u-0206) 해결 방법: VOD: Guardian angel 보유자가 Trolling 언세이프 서클 안에 있는 장면.

### U-0208

[U-0208](unknowns.md#u-0208): Safety bubble의 '10m'는 반지름입니까, 지름입니까? 상태: `open`.

중요한 이유 ([U-0208](unknowns.md#u-0208)): 보호 범위의 면적이 두 배가 되거나 4분의 1이 됩니다.

- [U-0208](unknowns.md#u-0208) 해석 A: 반지름 10 m
- [U-0208](unknowns.md#u-0208) 해석 B: 지름 10 m, 반지름 5 m
- [U-0208](unknowns.md#u-0208) 자유 매개변수 `bubble_radius_m`, 탐색 범위: 5..10 m (지름 10 해석에서 반지름 10 해석까지)
- [U-0208](unknowns.md#u-0208) 해결 방법: VOD: 참가자들이 bubble 생성자로부터 측정된 거리에 있는 장면.

### U-0211

[U-0211](unknowns.md#u-0211): smoke bomb 구름은 터뜨린 위치에 고정됩니까, 사용자를 따라갑니까? 상태: `open`.

중요한 이유 ([U-0211](unknowns.md#u-0211)): 아이템 페이지에는 'within 50m of you'와 'inside it'이라고 되어 있습니다.

- [U-0211](unknowns.md#u-0211) 해석 A: 중심이 고정됨
- [U-0211](unknowns.md#u-0211) 해석 B: 사용자를 중심으로 함
- [U-0211](unknowns.md#u-0211) 해결 방법: VOD: 사용자가 자신의 구름에서 걸어 나가는 장면.

### U-0212

[U-0212](unknowns.md#u-0212): smoke bomb을 터뜨린 참가자를 구름 밖에서 대상으로 삼을 수 있습니까? 상태: `open`.

중요한 이유 ([U-0212](unknowns.md#u-0212)): 'Nobody outside can target anyone inside'라는 문장과 터뜨린 사람에 대한 예외가 그 사람에 관해 서로 맞지 않습니다.

- [U-0212](unknowns.md#u-0212) 해석 A: 아니요, 터뜨린 사람은 구름 안에 있어 보호됨
- [U-0212](unknowns.md#u-0212) 해석 B: 예, 터뜨린 사람은 영향을 받지 않으므로 대상이 될 수 있음
- [U-0212](unknowns.md#u-0212) 해결 방법: VOD: 구름 밖에서 smoke bomb을 터뜨린 사람을 공격하는 장면.

### U-0213

[U-0213](unknowns.md#u-0213): Thermal goggles의 예외는 smoke의 공격 차단과 블랙아웃에만 적용됩니까, 아니면 구름 안에서의 회복, 도둑질, 거래 제한에도 적용됩니까? 상태: `open`.

중요한 이유 ([U-0213](unknowns.md#u-0213)): Items 067은 'block your attacks'라고 하는데, 회복/도둑질/거래 제한(043)은 공격이 아닙니다.

- [U-0213](unknowns.md#u-0213) 해석 A: 공격 차단과 블랙아웃만 해당
- [U-0213](unknowns.md#u-0213) 해석 B: smoke의 모든 제한
- [U-0213](unknowns.md#u-0213) 해결 방법: VOD: goggles 보유자가 구름 안에서 도둑질이나 거래를 시도하는 장면.

### U-0214

[U-0214](unknowns.md#u-0214): Bandage의 틱 일정은 어떻게 됩니까: 2min 동안 10 HP? 상태: `open`.

중요한 이유 ([U-0214](unknowns.md#u-0214)): 피해, 최대 HP 상한, 치료 타이밍과의 상호작용이 달라집니다.

- [U-0214](unknowns.md#u-0214) 해석 A: +12 s..+120 s에 1 HP씩 10틱
- [U-0214](unknowns.md#u-0214) 해석 B: +0 s..+108 s에 1 HP씩 10틱
- [U-0214](unknowns.md#u-0214) 해석 C: 24 s마다 2 HP씩 5틱
- [U-0214](unknowns.md#u-0214) 해석 D: 소수 단위의 연속 회복
- [U-0214](unknowns.md#u-0214) 자유 매개변수 `bandage_tick_count`, 탐색 범위: 120 s 동안 1..120틱 (틱당 1 HP부터 소수 단위까지)
- [U-0214](unknowns.md#u-0214) 해결 방법: VOD: bandage 사용 후의 HP 바.

### U-0215

[U-0215](unknowns.md#u-0215): mirror forcefield를 여러 개 가지고 있을 때, 한 번의 반사는 하나를 소모합니까, 전부를 소모합니까, 아니면 여러 번 반사합니까? 상태: `open`.

중요한 이유 ([U-0215](unknowns.md#u-0215)): 페이지에는 'Several stack'과 'Ends when it reflects an attack'이라고 하지만 개수는 밝히지 않습니다.

- [U-0215](unknowns.md#u-0215) 해석 A: 반사 한 번에 하나 소모
- [U-0215](unknowns.md#u-0215) 해석 B: 전부 소모됨
- [U-0215](unknowns.md#u-0215) 해석 C: 연속으로 여러 번 반사
- [U-0215](unknowns.md#u-0215) 해결 방법: VOD: mirror 두 개를 가진 참가자가 두 번 타격당하는 장면.

### U-0216

[U-0216](unknowns.md#u-0216): 다른 방어(Shield, Safety bubble, Sleeping Bag)가 이미 막은 타격으로 Flak jacket이 소모됩니까? 상태: `open`.

중요한 이유 ([U-0216](unknowns.md#u-0216)): Guardian angel은 막힌 타격에 대해 명시하지만 Flak jacket은 그렇지 않습니다.

- [U-0216](unknowns.md#u-0216) 해석 A: 당신에 대한 모든 타격이 이를 소모함
- [U-0216](unknowns.md#u-0216) 해석 B: 그것에 도달한 타격만 소모함
- [U-0216](unknowns.md#u-0216) 해결 방법: VOD: Shield와 Flak jacket을 가진 보유자가 미사일에 맞는 장면.

### U-0300

[U-0300](unknowns.md#u-0300): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까? 상태: `open`.

중요한 이유 ([U-0300](unknowns.md#u-0300)): 모든 'within Xm'과 'comes within Xm' 문장이 경계에서 달라집니다. 정확히 X 미터에 있는 참가자는 한 해석에서는 타격을 받고 다른 해석에서는 안전합니다.

- [U-0300](unknowns.md#u-0300) 해석 A: d <= R일 때, 그리고 그때에만 안쪽 (포함)
- [U-0300](unknowns.md#u-0300) 해석 B: d < R일 때, 그리고 그때에만 안쪽 (미포함)
- [U-0300](unknowns.md#u-0300) 해결 방법: VOD: C4 또는 landmine으로부터 명시된 반경과 같은 측정 거리에 있는 참가자.
- [U-0300](unknowns.md#u-0300) 해결 방법: REA: 배포된 거리 비교 코드 (클라이언트 코드에는 서버 로직이 없음, RE-0001).

### U-0301

[U-0301](unknowns.md#u-0301): Ingenuity 함정 부착의 'once every 16h' 제한은 C4와 landmine이 공유하는 하나의 타이머입니까, 종류별 타이머입니까? 그리고 부착 시점에 시작됩니까, 폭발 시점에 시작됩니까? 상태: `open`.

중요한 이유 ([U-0301](unknowns.md#u-0301)): Ingenuity 참가자가 임의의 48h 동안 가질 수 있는 함정 선물의 수와, 오래된 함정이 다음 함정을 막는지가 결정됩니다.

- [U-0301](unknowns.md#u-0301) 해석 A: 공유 타이머 하나, 부착 시점에 시작
- [U-0301](unknowns.md#u-0301) 해석 B: 종류별(C4, landmine) 타이머 하나씩, 부착 시점에 시작
- [U-0301](unknowns.md#u-0301) 해석 C: 공유 타이머, 함정 선물이 작동하거나 제거될 때 시작
- [U-0301](unknowns.md#u-0301) 해결 방법: VOD: Ingenuity 참가자가 16h 안에 C4를 붙이고 이어서 landmine을 붙이는 장면.

### U-0303

[U-0303](unknowns.md#u-0303): '각각 최대 5개가 한 슬롯을 공유한다 / 각각 최대 5개를 소지한다'라는 상한은 'An enchanted one uses its own slot'과 어떻게 맞물립니까? 상태: `open`.

중요한 이유 ([U-0303](unknowns.md#u-0303)): 참가자가 가질 수 있는 C4와 landmine의 최대 개수와 그것들이 차지하는 슬롯이 정해집니다.

- [U-0303](unknowns.md#u-0303) 해석 A: 인챈트된 것도 5개 상한에 포함되고 별도 슬롯을 차지함
- [U-0303](unknowns.md#u-0303) 해석 B: 인챈트된 것은 5개 상한 밖 (일반 5개 + 자체 슬롯)
- [U-0303](unknowns.md#u-0303) 해석 C: 인챈트된 것은 한 번에 하나, 상한 밖
- [U-0303](unknowns.md#u-0303) 해결 방법: VOD: 일반 C4 5개와 인챈트된 것 하나가 있는 인벤토리 화면.

### U-0304

[U-0304](unknowns.md#u-0304): 인챈트되지 않았을 때 drone, C4, landmine, Poison Dart는 각각 몇 번 사용할 수 있습니까? 상태: `open`.

중요한 이유 ([U-0304](unknowns.md#u-0304)): 위키는 knife, machete, sword, axe, bow의 사용 횟수는 알려 주지만 이 네 가지는 알려 주지 않으며, 인챈트 설명은 보너스 사용 횟수 후에 '소모된다'고 합니다.

- [U-0304](unknowns.md#u-0304) 해석 A: 각각 1회 사용 (사용 시 소모)
- [U-0304](unknowns.md#u-0304) 해석 B: 일부는 여러 번 사용 가능 (명시되지 않음)
- [U-0304](unknowns.md#u-0304) 자유 매개변수 `uses_unstated_items`, 탐색 범위: 1에서 3회 사용. 인챈트 설명은 인챈트된 C4, landmine, drone이 1회, dart가 2회라고 하므로 1이 자연스러운 하한이고 3은 knife/long sword 규모를 포함
- [U-0304](unknowns.md#u-0304) 해결 방법: VOD: 각 아이템의 사용 장면.
- [U-0304](unknowns.md#u-0304) 해결 방법: 주최 측의 발표.

### U-0306

[U-0306](unknowns.md#u-0306): Ingenuity landmine 부착의 '자신에게 사용하는 아이템'에는 어떤 아이템이 해당합니까? 상태: `open`.

중요한 이유 ([U-0306](unknowns.md#u-0306)): C4 설명은 'another item you hold'라고 하고, landmine 설명은 자신에게 사용하는 아이템으로 제한합니다. 유효한 아이템의 집합이 landmine 함정을 어디에 숨길 수 있는지를 결정합니다.

- [U-0306](unknowns.md#u-0306) 해석 A: 자기 효과가 있는 소모품 (포션, bandage, shield)
- [U-0306](unknowns.md#u-0306) 해석 B: 사용 가능한 모든 아이템
- [U-0306](unknowns.md#u-0306) 해석 C: 회복하는 아이템만 해당
- [U-0306](unknowns.md#u-0306) 해결 방법: VOD: Ingenuity 참가자가 landmine을 여러 종류의 아이템에 붙이는 장면.

### U-0311

[U-0311](unknowns.md#u-0311): Zarok's axe: 정수가 아닌 피해 값은 어떤 방식으로 정수로 처리됩니까? 상태: `open`.

중요한 이유 ([U-0311](unknowns.md#u-0311)): 대부분의 HP 수준에서 피해가 최대 1 HP까지 달라집니다(그 위에 Kick 보너스와 최소 1 HP가 적용됩니다).

- [U-0311](unknowns.md#u-0311) 해석 A: floor
- [U-0311](unknowns.md#u-0311) 해석 B: ceil
- [U-0311](unknowns.md#u-0311) 해석 C: 반올림(round half up)
- [U-0311](unknowns.md#u-0311) 해결 방법: VOD: 곡선이 소수를 내는 HP에서의 axe 타격.

### U-0312

[U-0312](unknowns.md#u-0312): Wizard staff: '10m damage area'는 반지름입니까, 지름입니까? 상태: `open`.

중요한 이유 ([U-0312](unknowns.md#u-0312)): 덮는 면적이 두 배가 되거나 4분의 1이 됩니다. 인챈트 문구는 '+10m area radius'라고 하여 반지름임을 시사할 뿐입니다.

- [U-0312](unknowns.md#u-0312) 해석 A: 반지름 10m
- [U-0312](unknowns.md#u-0312) 해석 B: 지름 10m(반지름 5m)
- [U-0312](unknowns.md#u-0312) 해결 방법: VOD: 중심에서 측정한 거리별 참가자의 HP 손실.

### U-0313

[U-0313](unknowns.md#u-0313): Wizard staff: 5s 중 일부 시간만 범위 안에 있던 참가자는 10 HP 전체를 받습니까, 일부만 받습니까? 설치 후에 들어온 참가자도 피해를 받습니까? 상태: `open`.

중요한 이유 ([U-0313](unknowns.md#u-0313)): 범위에서 재빨리 벗어나면 피해를 피할 수 있는지, 이동 경로 앞에 설치하는 것이 통하는지를 결정합니다.

- [U-0313](unknowns.md#u-0313) 해석 A: 설치 시점에 범위 안에 있던 모두가 10 HP 전체를 받음
- [U-0313](unknowns.md#u-0313) 해석 B: 범위 안에 있는 동안에만 피해가 누적됨(범위 안에 있던 시간에 비례)
- [U-0313](unknowns.md#u-0313) 해석 C: 5s 중 어느 순간이든 범위 안에 있던 모두가 10 HP 전체를 한 번 받음
- [U-0313](unknowns.md#u-0313) 해결 방법: VOD: 활성 staff 범위를 벗어나거나 들어오는 참가자.

### U-0315

[U-0315](unknowns.md#u-0315): Poison Dart: 이미 중독된 참가자가 다시 다트를 맞으면(또는 Fake gravestone에 맞으면) 새 독이 20 HP 전체 일정을 다시 시작합니까, 남은 분량을 대체합니까, 더해집니까? 상태: `open`.

중요한 이유 ([U-0315](unknowns.md#u-0315)): 독 페이지는 재중독이 타이머를 초기화하고 중첩되지 않는다고 하지만, 초기화되는 양(20 HP 전체인지 남은 분량인지)은 명시되어 있지 않습니다.

- [U-0315](unknowns.md#u-0315) 해석 A: 새 다트로부터 20 HP 일정을 새로 시작함
- [U-0315](unknowns.md#u-0315) 해석 B: 이전 독의 남은 HP를 유지하고 간격 타이머만 다시 시작함
- [U-0315](unknowns.md#u-0315) 해석 C: 중독된 동안 두 번째 다트는 무시됨
- [U-0315](unknowns.md#u-0315) 해결 방법: VOD: 다트를 두 번 맞은 참가자의 HP와 타이머.

### U-0317

[U-0317](unknowns.md#u-0317): 지속 피해 아이템에서 'Poison Dart ... +10 damage for two uses'는 무엇을 뜻합니까? 상태: `open`.

중요한 이유 ([U-0317](unknowns.md#u-0317)): 인챈트된 다트의 독은 총 10 HP를 더할 수도, 사용마다 10 HP를 더할 수도, 즉발 타격일 수도 있습니다.

- [U-0317](unknowns.md#u-0317) 해석 A: 인챈트된 다트 각각은 같은 30min 동안 총 30 HP로 중독시킴
- [U-0317](unknowns.md#u-0317) 해석 B: 인챈트된 다트 각각은 30min 동안 20 HP로 중독시키고 즉시 10 HP를 더함
- [U-0317](unknowns.md#u-0317) 해석 C: 인챈트된 다트 각각은 간격을 1min 30s로 유지한 채 30 HP로 중독시킴(따라서 45min)
- [U-0317](unknowns.md#u-0317) 해결 방법: VOD: 참가자에게 사용한 인챈트된 다트.

### U-0318

[U-0318](unknowns.md#u-0318): 둘 다 붙어 있는 Poison Dart와 Zarok's axe에서 Equippable과 Usable 라벨은 무엇을 뜻합니까? 상태: `open`.

중요한 이유 ([U-0318](unknowns.md#u-0318)): 다트와 axe가 무기 슬롯에 들어가는지, 던지거나 인벤토리에서 소모되는지, 두 방식이 모두 존재하는지를 결정합니다.

- [U-0318](unknowns.md#u-0318) 해석 A: Equippable = 무기 슬롯에 들고 있음, Usable = 사용 시 소모됨. 두 라벨은 아이템을 어느 쪽으로든 쓸 수 있다는 뜻
- [U-0318](unknowns.md#u-0318) 해석 B: 두 라벨은 순차적: 장착해서 들고, 그다음 한 번 사용
- [U-0318](unknowns.md#u-0318) 해결 방법: VOD: axe 또는 다트를 든 참가자의 인벤토리와 무기 슬롯.

### U-0319

[U-0319](unknowns.md#u-0319): 이벤트 시작 후 첫 무작위 상인은 언제 나타납니까? 상태: `open`.

중요한 이유 ([U-0319](unknowns.md#u-0319)): 상인 주기(15min 체류, 30min에서 1h 부재)에는 명시된 위상이 없습니다. 초반 구매력과 토큰 비축이 이에 달려 있습니다.

- [U-0319](unknowns.md#u-0319) 자유 매개변수 `merchant_first_spawn_min`, 탐색 범위: 이벤트 시작 후 0에서 75 min: 75 min은 가장 긴 전체 주기(15 min 체류 + 1h 부재)이므로 한 주기 안의 모든 위상이 포함됩니다
- [U-0319](unknowns.md#u-0319) 해결 방법: VOD: 이벤트 시작부터 상인이 처음 나타날 때까지.
- [U-0319](unknowns.md#u-0319) 해결 방법: 주최 측의 발표.

### U-0321

[U-0321](unknowns.md#u-0321): 어떤 상인 구매에 빈 인벤토리 슬롯이 필요합니까('Items need a free inventory slot')? 상태: `open`.

중요한 이유 ([U-0321](unknowns.md#u-0321)): 아이템만 명시되어 있습니다. 미사일, Deep Cut, Dual Wield, 인챈트, 업그레이드는 슬롯이 필요하지 않을 수 있습니다. 인벤토리가 가득 찬 상태의 보급 상자는 다루어지지 않습니다.

- [U-0321](unknowns.md#u-0321) 해석 A: 보급 상자, anti poison, Vulnerability Dart, Sleeping Bag은 슬롯이 필요하고 미사일과 업그레이드는 필요 없음
- [U-0321](unknowns.md#u-0321) 해석 B: 미사일도 슬롯이 필요함
- [U-0321](unknowns.md#u-0321) 해석 C: 보급 상자 아이템이 무기라면 무기 슬롯으로 갈 수 있으며 그 경우 슬롯이 필요 없음
- [U-0321](unknowns.md#u-0321) 해결 방법: VOD: 인벤토리가 가득 찬 상태에서의 구매.

### U-0323

[U-0323](unknowns.md#u-0323): 상인의 보급 상자는 어떤 아이템을 줍니까: 'One random item'의 분포는? 상태: `open`.

중요한 이유 ([U-0323](unknowns.md#u-0323)): 10 블러드 토큰의 기댓값을 정합니다. 무기, C4, Drone이 나오는지, 결과가 무기 슬롯에 들어가는지도 포함됩니다.

- [U-0323](unknowns.md#u-0323) 자유 매개변수 `merchant_care_package_item_distribution`, 탐색 범위: 아이템 페이지와 무기 페이지의 아이템 목록 전체에 걸친 균등 분포 대 저렴한 아이템 쪽으로 치우친 가중 분포. 둘을 구별하려면 최소 30회의 개봉을 표본으로 삼습니다
- [U-0323](unknowns.md#u-0323) 해결 방법: VOD: 상인 보급 상자 결과의 표본.
- [U-0323](unknowns.md#u-0323) 해결 방법: 주최 측의 발표.

### U-0324

[U-0324](unknowns.md#u-0324): Vulnerability Dart: 이미 취약한 참가자에게 두 번째 다트를 쓰면 초기화됩니까, 연장됩니까, 아무 일도 없습니까? 10분은 던진 시점부터입니까, 명중한 시점부터입니까? 상태: `open`.

중요한 이유 ([U-0324](unknowns.md#u-0324)): 무방비 구간의 길이를 정합니다. 다트를 반복하면 대상을 영구히 취약한 상태로 둘 수 있습니다.

- [U-0324](unknowns.md#u-0324) 해석 A: 새 다트가 10 min 타이머를 지금부터 새 10 min으로 초기화함
- [U-0324](unknowns.md#u-0324) 해석 B: 새 다트가 10 min을 더함
- [U-0324](unknowns.md#u-0324) 해석 C: 이미 취약한 동안에는 효과 없음
- [U-0324](unknowns.md#u-0324) 해결 방법: VOD: 5 min 간격으로 다트 두 발을 맞은 참가자.

### U-0330

[U-0330](unknowns.md#u-0330): Max HP upgrade: HP 상한(200, Piety는 220) 외에 구매 한도가 있습니까? 시길별로 각 상한에 도달하려면 몇 번을 구매해야 합니까? 상태: `open`.

중요한 이유 ([U-0330](unknowns.md#u-0330)): 기본 HP 100에서 상한 200은 10번 구매입니다. Piety(기본 110)는 11번이어야 220에 도달하고, Greed(기본 90)는 200에 11번이 필요합니다. 위키는 구매 한도를 슬롯에만 명시합니다.

- [U-0330](unknowns.md#u-0330) 해석 A: 구매 한도 없음, HP 상한만 있음(Greed 11, Piety 11, 나머지는 10번 구매)
- [U-0330](unknowns.md#u-0330) 해석 B: 모두 10번 구매 한도(Piety는 210에서 멈추며 이는 220 상한과 모순됨)
- [U-0330](unknowns.md#u-0330) 자유 매개변수 `hp_upgrade_purchase_limit`, 탐색 범위: 10에서 12번 구매: 상한은 기본 100이면 10, 기본 90 또는 110이면 11을 의미함
- [U-0330](unknowns.md#u-0330) 해결 방법: VOD: HP 업그레이드를 10번, 11번 한 뒤의 Piety 참가자.

### U-0331

[U-0331](unknowns.md#u-0331): '+10 maximum HP'는 현재 HP도 10 올립니까? 상태: `open`.

중요한 이유 ([U-0331](unknowns.md#u-0331)): 이 업그레이드가 최대치 상승일 뿐 아니라 회복이기도 한지를 결정합니다.

- [U-0331](unknowns.md#u-0331) 해석 A: 최대 HP +10, 현재 HP는 그대로
- [U-0331](unknowns.md#u-0331) 해석 B: 최대 HP +10 그리고 현재 HP +10
- [U-0331](unknowns.md#u-0331) 해결 방법: VOD: 체력이 가득 차지 않은 상태에서 업그레이드 전후의 HP 표시.

### U-0332

[U-0332](unknowns.md#u-0332): Deep Cut: 첫 출혈 틱은 언제이며, 출혈 중에 새 타격을 받으면 타이머가 초기화되고, 사용하지 않은 충전은 얼마나 오래 유지되며, 출혈 틱은 타격으로 계산됩니까? 상태: `open`.

중요한 이유 ([U-0332](unknowns.md#u-0332)): 출혈은 이 페이지에서 유일하게 상한이 없는 지속 피해이며, 붕대나 Healing 참가자로만 끝납니다.

- [U-0332](unknowns.md#u-0332) 해석 A: 첫 틱은 타격 5 min 후, 새 출혈 타격은 무시, 충전은 만료되지 않음, 틱은 일반 피해 이벤트
- [U-0332](unknowns.md#u-0332) 해석 B: 첫 틱은 즉시, 이후 5 min마다, 새 타격이 5 min 타이머를 재시작, 충전은 만료되지 않음
- [U-0332](unknowns.md#u-0332) 해석 C: 충전은 명시되지 않은 기간 후 만료
- [U-0332](unknowns.md#u-0332) 해결 방법: VOD: Deep Cut 무기에 타격당한 참가자의 출혈 타임라인.

### U-0334

[U-0334](unknowns.md#u-0334): 인챈트 시계: 2시간은 구매 시점에 시작합니까, 무기에 적용하는 시점에 시작합니까? 그리고 'For every other weapon, if two hours pass first'는 Zarok's axe, Poison Dart, C4, landmine, drone도 제한합니까? 상태: `open`.

중요한 이유 ([U-0334](unknowns.md#u-0334)): 시간 제한이 없으면 그 아이템들은 무기한 인챈트 상태로 남을 수 있습니다(사용으로만 끝남).

- [U-0334](unknowns.md#u-0334) 해석 A: 구매 후 2 h, 제한은 knife, machete, long sword('every other weapon' 그룹)와 bow에만 적용
- [U-0334](unknowns.md#u-0334) 해석 B: 구매 후 2 h, 제한은 staff를 제외한 모든 인챈트 무기에 적용
- [U-0334](unknowns.md#u-0334) 해석 C: 무기에 인챈트를 적용한 시점부터 2 h
- [U-0334](unknowns.md#u-0334) 해결 방법: VOD: 2 h 넘게 보유한 인챈트 axe 또는 landmine.

### U-0336

[U-0336](unknowns.md#u-0336): 인챈트된 C4 또는 landmine: '+10m radius'는 발동 거리에도 적용됩니까? 그리고 인챈트된 함정으로 만든 trapped gift에 인챈트가 이어집니까? 상태: `open`.

중요한 이유 ([U-0336](unknowns.md#u-0336)): trapped gift의 +20 피해(기본 23 HP와 11 HP)와 발동 범위가 모두 인챈트된 함정의 효과를 바꿉니다.

- [U-0336](unknowns.md#u-0336) 해석 A: 발동과 폭발 모두 반경 +10 m, 인챈트된 함정으로 만든 trapped gift는 +20 유지
- [U-0336](unknowns.md#u-0336) 해석 B: 폭발에만 반경 +10 m, trapped gift는 기본 23 또는 11 HP 사용
- [U-0336](unknowns.md#u-0336) 해석 C: 인챈트된 함정은 부착할 수 없음
- [U-0336](unknowns.md#u-0336) 해결 방법: VOD: 15 m에서 발동한 인챈트 landmine.

### U-0337

[U-0337](unknowns.md#u-0337): 인챈트 제한 'one enchanted weapon, or two with Dual Wield': 무기 슬롯 아이템이 아닌 C4, landmine, drone, Poison Dart도 포함합니까? 상태: `open`.

중요한 이유 ([U-0337](unknowns.md#u-0337)): 참가자가 인챈트된 C4와 인챈트된 bow를 한 슬롯에서 함께 가질 수 있는지를 결정합니다.

- [U-0337](unknowns.md#u-0337) 해석 A: 제한은 C4, landmine, drone을 포함한 모든 인챈트 아이템을 셈
- [U-0337](unknowns.md#u-0337) 해석 B: 제한은 무기 슬롯 아이템(근접 무기, bow, staff, Poison Dart)만 셈
- [U-0337](unknowns.md#u-0337) 해결 방법: VOD: 인챈트된 C4를 든 채 두 번째 무기 인챈트 구매.

### U-0338

[U-0338](unknowns.md#u-0338): 방어구 인챈트 '+10 durability, up to 45': 반복 구매할 수 있습니까, 45는 인챈트 후 내구도의 상한입니까, 그리고 어떤 기준값에서 시작합니까? 상태: `open`.

중요한 이유 ([U-0338](unknowns.md#u-0338)): 방어구 기본 내구도는 다른 페이지(Body Armor 15 HP absorb)에 있으며, 반복 구매 경로로 45에 도달할 수 있습니다.

- [U-0338](unknowns.md#u-0338) 해석 A: 구매마다 10 추가, 총 내구도 45에서 상한
- [U-0338](unknowns.md#u-0338) 해석 B: 방어구당 인챈트 한 번, 상한은 시작 내구도만 제약
- [U-0338](unknowns.md#u-0338) 해석 C: 인챈트는 내구도를 min(current + 10, 45)로 설정
- [U-0338](unknowns.md#u-0338) 해결 방법: VOD: 두 번 구매하기 전후의 방어구 내구도 표시.

### U-0339

[U-0339](unknowns.md#u-0339): 인챈트된 방어구 감쇠 'loses one durability every twenty minutes, down to 15': 시계는 언제 시작하고, 피해로 15보다 낮아졌어도 감쇠가 15에서 멈추며, 재인챈트하면 다시 시작합니까? 상태: `open`.

중요한 이유 ([U-0339](unknowns.md#u-0339)): 45 내구도의 수명과 인챈트된 방어구의 하한을 정합니다.

- [U-0339](unknowns.md#u-0339) 해석 A: 시계는 인챈트 시점에 시작, 첫 감소는 20 min 후, 내구도 <= 15이면 감소 없음
- [U-0339](unknowns.md#u-0339) 해석 B: 시계는 첫 인챈트부터 계속 흐르고 재인챈트는 다시 시작하지 않음
- [U-0339](unknowns.md#u-0339) 해석 C: 감쇠는 인챈트 여부와 관계없이 15를 넘는 모든 방어구에 적용
- [U-0339](unknowns.md#u-0339) 해결 방법: VOD: 인챈트 후 한 시간 동안의 방어구 내구도.

### U-0401

[U-0401](unknowns.md#u-0401): EMP 차단의 범위: 위키는 미사일, 핵, horde, 최루 가스, 공습, 건십, 사이클롭스, 현상금을 나열합니다. 긴급 에어드롭, 회복 서클, 환영, 시청자 상자도 차단됩니까? 차단은 구매 시점을 검사합니까, 착탄 시점을 검사합니까? 상태: `open`.

중요한 이유 ([U-0401](unknowns.md#u-0401)): EMP 보유자가 막을 수 있는 시청자 행동과, 비행 중인 회복 서클이나 에어드롭이 살아남는지를 결정합니다.

- [U-0401](unknowns.md#u-0401) 해석 A: 나열된 8개 공격만 거부되며 에어드롭, 회복 서클, 환영, 상자는 항상 통과
- [U-0401](unknowns.md#u-0401) 해석 B: EMP가 활성인 동안 모든 시청자 행동이 거부되며 목록은 예시일 뿐
- [U-0401](unknowns.md#u-0401) 해석 C: 차단은 구매 시점만 검사하고, 비행 중 파괴는 미사일, 핵, 공습, 건십에만 적용
- [U-0401](unknowns.md#u-0401) 해결 방법: 아이템 페이지의 EMP 텍스트(10 min)와 EMP 중에 보낸 시청자 에어드롭 또는 회복 서클의 VOD.

### U-0405

[U-0405](unknowns.md#u-0405): 최루 가스와 좀비 처치 타이밍: 10s마다 2 HP 틱은 진입 10s 후에 시작합니까, 진입 시에 시작합니까, 구름 전체 공통의 10s 위상입니까? 좀비는 진입 즉시 죽습니까, 틱에 죽습니까? 틱은 '타격'([U-0002](unknowns.md#u-0002))입니까? 상태: `open`.

중요한 이유 ([U-0405](unknowns.md#u-0405)): 짧게 지나갈 때의 피해가 달라지고(9s 통과는 진입 타이머면 0 HP, 전역 위상이면 2 HP), 좀비의 가스 사망도 달라집니다.

- [U-0405](unknowns.md#u-0405) 해석 A: 참가자별 타이머: 첫 손실은 진입 10s 후, 이후 10s마다
- [U-0405](unknowns.md#u-0405) 해석 B: 첫 손실은 진입 시, 이후 10s마다
- [U-0405](unknowns.md#u-0405) 해석 C: 구름 전체 공통 위상, 틱 시점에 안에 있는 모든 참가자가 2 HP 손실
- [U-0405](unknowns.md#u-0405) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 라이브로 관찰.

### U-0408

[U-0408](unknowns.md#u-0408): 공습 타임라인: 20s에 착탄하고 'the strip then burns for 5min'. 화재는 착탄부터 5min 지속됩니까, 첫 1 HP 틱은 착탄 시입니까 2s 후입니까, 화재 중에 띠로 들어가면 HP를 잃습니까? 화재 틱은 타격([U-0002](unknowns.md#u-0002))입니까? 상태: `open`.

중요한 이유 ([U-0408](unknowns.md#u-0408)): 띠 안에 서 있을 때 5min 동안의 총 화재 피해(최대 150 또는 149 HP)와, 늦게 들어가는 것이 불이익을 받는지.

- [U-0408](unknowns.md#u-0408) 해석 A: 화재는 t=20s부터 t=320s까지, 첫 틱은 22s, 그 구간의 어느 시점에 진입해도 계산됨
- [U-0408](unknowns.md#u-0408) 해석 B: 화재는 t=20s부터 t=320s까지, 첫 틱은 20s
- [U-0408](unknowns.md#u-0408) 해석 C: 화재 타이머는 구매 시점에 시작하므로 t=300s에 끝남
- [U-0408](unknowns.md#u-0408) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 라이브로 관찰.

### U-0410

[U-0410](unknowns.md#u-0410): 건십 폭탄 위치와 표적 서클: 서클은 'sweeps around a random safe zone at 75m/s'입니다(서클 반경과 경로는 명시되지 않음). 폭탄은 투하 시점에 서클이 있던 곳에 떨어집니까, 5s 후 서클이 있는 곳(75m/s x 5s = 375m 떨어진 곳)에 떨어집니까? 상태: `open`.

중요한 이유 ([U-0410](unknowns.md#u-0410)): 폭탄을 조준할 수 있는지, 참가자가 어디에 서야 하는지를 결정합니다.

- [U-0410](unknowns.md#u-0410) 해석 A: 폭탄은 투하 순간의 서클 위치에 떨어짐
- [U-0410](unknowns.md#u-0410) 해석 B: 폭탄은 5s 후의 서클 위치에 떨어짐
- [U-0410](unknowns.md#u-0410) 해석 C: 서클 반경이 폭탄 폭발 반경 25m와 같음
- [U-0410](unknowns.md#u-0410) 자유 매개변수 `gunship_circle_radius_m`, 탐색 범위: 10 ~ 50 m; 위키는 25m 폭탄 반경만 제시하며 서클 크기는 없습니다
- [U-0410](unknowns.md#u-0410) 해결 방법: VOD: 서클이 보이는 건십.

### U-0411

[U-0411](unknowns.md#u-0411): 보급 상자 Trolling 규칙: 3% 판정은 각 상자에 개별로 적용됩니까(긴급 에어드롭의 5개, Endurance 상자, 상인 상자 포함)? 'within 5m'는 'next to'와 같습니까? 그리고 Trolling 참가자가 여럿이면 누가 선택됩니까? 상태: `open`.

중요한 이유 ([U-0411](unknowns.md#u-0411)): 모든 보급 출처에 걸친 Trolling 수입의 기댓값과 상자의 방어 가치를 정합니다.

- [U-0411](unknowns.md#u-0411) 해석 A: 시청자가 보낸 상자마다 독립적인 3% 판정, 가장 가까운 또는 무작위의 Trolling 참가자
- [U-0411](unknowns.md#u-0411) 해석 B: Endurance와 상인 상자를 포함한 모든 보급 상자에 3% 판정
- [U-0411](unknowns.md#u-0411) 해석 C: 단일 보급 상자에만 판정하고, 에어드롭의 5개에는 판정하지 않음
- [U-0411](unknowns.md#u-0411) 해결 방법: VOD: 시청자 상자 100개 이상이 떨어지는 위치를 기록.
- [U-0411](unknowns.md#u-0411) 해결 방법: Trolling 페이지 텍스트(시청자 상자).

### U-0413

[U-0413](unknowns.md#u-0413): Healing circle: 50m 원은 반지름입니까 지름입니까, 구성원 판정은 +60s에만 이루어집니까 아니면 지속적으로 이루어집니까, 그리고 25 HP 회복은 최대 HP를 넘어서도 적용됩니까? 이 회복은 Healing 및 Piety 토큰에 포함됩니까? 상태: `open`.

중요한 이유 ([U-0413](unknowns.md#u-0413)): 누가 혜택을 받는지(이동하는 참가자는 60s 전에 벗어날 수 있음)와 최대 HP일 때의 회복량을 결정합니다.

- [U-0413](unknowns.md#u-0413) 해석 A: 반지름 50m, 구성원은 t+60s에 판정, 회복 min(25, max-hp)
- [U-0413](unknowns.md#u-0413) 해석 B: 지름 50m(반지름 25m), t+60s에 판정
- [U-0413](unknowns.md#u-0413) 해석 C: 구성원을 지속적으로 판정, 60s 후 진입 시 회복
- [U-0413](unknowns.md#u-0413) 자유 매개변수 `healing_circle_radius_m`, 탐색 범위: 25 ~ 50 m: 위키는 크기로 '50m'만 제시합니다
- [U-0413](unknowns.md#u-0413) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0414

[U-0414](unknowns.md#u-0414): Illusion 복사본 수: 'a copy of every living contestant'이고, 10명 미만 생존 시 'several copies, up to 30 in total'입니다. 각자 몇 개씩 생기고, 30개는 어떻게 나뉘며, 10명 이상일 때 총합은 30으로 제한됩니까? 상태: `open`.

중요한 이유 ([U-0414](unknowns.md#u-0414)): 복사본의 밀도와 공격이 실제 참가자에게 적중할 확률을 정합니다.

- [U-0414](unknowns.md#u-0414) 해석 A: n < 10일 때 각자 복사본 수 = floor(30/n), 총합 최대 30
- [U-0414](unknowns.md#u-0414) 해석 B: 각자 복사본 수 = ceil(30/n), 총합은 30으로 제한
- [U-0414](unknowns.md#u-0414) 해석 C: 정확히 30개를 무작위로 분배
- [U-0414](unknowns.md#u-0414) 해석 D: n >= 10: n개 복사본, 제한 없음. n >= 30이면 30개를 초과
- [U-0414](unknowns.md#u-0414) 자유 매개변수 `illusion_total_cap`, 탐색 범위: 복사본 10 ~ 40개: 30은 10명 미만의 참가자에 대해 명시되어 있고, n>=10인 경우는 위키가 제한하지 않습니다
- [U-0414](unknowns.md#u-0414) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0419

[U-0419](unknowns.md#u-0419): 사이클롭스 블러드 토큰: 죽을 때 '1 blood token per damage dealt'입니다. 피해는 초과 피해를 빼고 200 HP를 상한으로 집계됩니까, 상인 미사일은 '시청자 아이템'입니까, 그리고 참가자들이 먼저 피해를 입혔더라도 존 피해로 죽으면 여전히 아무것도 지급되지 않습니까? 상태: `open`.

중요한 이유 ([U-0419](unknowns.md#u-0419)): 사이클롭스는 주요 토큰 공급원이며, 총합은 200으로 제한되거나 초과 피해로 인해 제한이 없습니다.

- [U-0419](unknowns.md#u-0419) 해석 A: 지급량 = 실제로 제거된 HP(총 <= 200). 상인 미사일 포함
- [U-0419](unknowns.md#u-0419) 해석 B: 초과 피해를 포함한 원래 피해로 지급량 계산
- [U-0419](unknowns.md#u-0419) 해석 C: 상인 미사일은 시청자 아이템으로 취급되어 아무것도 지급하지 않음
- [U-0419](unknowns.md#u-0419) 해결 방법: 토큰 기록이 있는 사이클롭스 처치 VOD.

### U-0420

[U-0420](unknowns.md#u-0420): 사이클롭스 공격 타이밍과 대상: 'Every 5s it hits the nearest contestant within 30m for 10 HP'. 첫 타격은 스폰+5s입니까, 아니면 대상이 처음 범위에 들어올 때입니까? 동률은 어떻게 처리합니까? 이 피해는 피해 파이프라인([U-0002](unknowns.md#u-0002))을 거칩니까? 상태: `open`.

중요한 이유 ([U-0420](unknowns.md#u-0420)): 사이클롭스 근처에 서 있는 참가자가 받는 피해: 10 HP / 5s = 2 HP/s.

- [U-0420](unknowns.md#u-0420) 해석 A: 스폰부터 전역 5s 타이머, 범위 안에 참가자가 있으면 타격
- [U-0420](unknowns.md#u-0420) 해석 B: 참가자가 범위에 들어올 때 타이머 시작
- [U-0420](unknowns.md#u-0420) 해석 C: 타격은 7단계 파이프라인을 거침
- [U-0420](unknowns.md#u-0420) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0424

[U-0424](unknowns.md#u-0424): 좀비 대상 지정: 'nearest valid contestant, at any distance'. 무엇이 참가자를 유효하게 만듭니까(생존, 면역 아님, repellent 아님, Necromancy 아님)? 가장 가까운 대상은 얼마나 자주 다시 평가됩니까, 그리고 좀비는 지형을 따라 경로를 찾습니까? 상태: `open`.

중요한 이유 ([U-0424](unknowns.md#u-0424)): 좀비가 확실한 추격자인지 여부를 결정합니다.

- [U-0424](unknowns.md#u-0424) 해석 A: 유효 = 생존이고 현재 좀비에 면역이 아님, 가장 가까운 대상을 매 틱 다시 평가
- [U-0424](unknowns.md#u-0424) 해석 B: 유효 = 생존만. 면역은 흡수 시점에 적용
- [U-0424](unknowns.md#u-0424) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0426

[U-0426](unknowns.md#u-0426): 포션 파괴 판정: '10% chance to break one of your health potions'. 흡수 틱마다입니까, 조우마다입니까, 좀비마다입니까? 어느 포션이 파괴됩니까, 그리고 포션이 없을 때나 흡수가 차단될 때도 판정이 이루어집니까? 상태: `open`.

중요한 이유 ([U-0426](unknowns.md#u-0426)): 틱마다 판정하면 좀비 옆에서 약 100s마다 포션 하나가 깨집니다. 조우마다라면 훨씬 적습니다.

- [U-0426](unknowns.md#u-0426) 해석 A: 좀비마다 흡수 틱당 한 번 판정
- [U-0426](unknowns.md#u-0426) 해석 B: 좀비마다 참가자당 한 번 판정(첫 접촉)
- [U-0426](unknowns.md#u-0426) 해석 C: HP가 실제로 줄어든 흡수 사건에 대해서만 한 번 판정
- [U-0426](unknowns.md#u-0426) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0427

[U-0427](unknowns.md#u-0427): 조합 파괴 판정: '40% chance to destroy crafted items'(Ingenuity 페이지는 'unique crafts'와 'Zombie hits'라고 함). 흡수 틱마다입니까 조우마다입니까, 아이템 하나입니까 모든 조합품입니까, 그리고 고유하지 않은 조합품도 포함됩니까? 상태: `open`.

중요한 이유 ([U-0427](unknowns.md#u-0427)): Ingenuity의 조합품이 좀비와 접촉한 뒤에도 남는지를 결정합니다.

- [U-0427](unknowns.md#u-0427) 해석 A: 흡수 틱마다, 무작위 조합품 하나
- [U-0427](unknowns.md#u-0427) 해석 B: 조우마다, 무작위 조합품 하나
- [U-0427](unknowns.md#u-0427) 해석 C: 틱마다, 모든 조합품이 각각 독립적으로 판정
- [U-0427](unknowns.md#u-0427) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0429

[U-0429](unknowns.md#u-0429): 가드 좀비: 가드 좀비는 스폰 지점에 머뭅니까 추격합니까? Necromancy 참가자마다 하나 나타납니까 사망마다 나타납니까? 소유자와 죽은 자도 흡수합니까, 그리고 그 페이지(Necromancy 페이지)에만 명시된 대로 1h 동안 존재합니까? 상태: `open`.

중요한 이유 ([U-0429](unknowns.md#u-0429)): 가드 좀비는 2 HP/5s(0.4 HP/s)를 흡수하며 최대 30 HP까지: 상한을 채우는 데 75s입니다.

- [U-0429](unknowns.md#u-0429) 해석 A: 1h 동안 정지, 10m 안의 Necromancy가 아닌 참가자를 흡수
- [U-0429](unknowns.md#u-0429) 해석 B: 일반 좀비처럼 추격
- [U-0429](unknowns.md#u-0429) 해석 C: Necromancy 수와 관계없이 사망마다 하나
- [U-0429](unknowns.md#u-0429) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0432

[U-0432](unknowns.md#u-0432): 시청자 공격의 동시성: 미사일, 핵, 무리, 최루 가스, 공습, 건십, 현상금, healing circle에 대해 제한이 명시되어 있지 않습니다(cyclops와 illusion만 하나로 제한). 마음대로 중첩할 수 있습니까? 상태: `open`.

중요한 이유 ([U-0432](unknowns.md#u-0432)): 제한 없는 중첩은 총 피해가 가격으로만 제한되게 만듭니다([U-0014](unknowns.md#u-0014)).

- [U-0432](unknowns.md#u-0432) 해석 A: 제한 없이 중첩 가능, Cx-Bucks로 제한
- [U-0432](unknowns.md#u-0432) 해석 B: 유형별 제한이 있으나 비공개
- [U-0432](unknowns.md#u-0432) 해결 방법: 상점 페이지와 VOD.

### U-0503

[U-0503](unknowns.md#u-0503): Piety의 "heal you 15% more, rounded down": 무엇이 내림되며, 최대 HP 상한 적용과 비교해 어느 단계에서 내림됩니까? 상태: `open`.

중요한 이유 ([U-0503](unknowns.md#u-0503)): 네 가지 포션 등급은 정확한 산술에서도 binary64에서도 같은 합계(5, 11, 23, 46)를 줍니다. 따라서 미해결인 부분은 HP 상한에서의 연산 순서와 사용되는 기본값입니다.

- [U-0503](unknowns.md#u-0503) 해석 A: heal = floor(1.15 * h)이며 h는 등급 값이고, 그다음 부족한 HP로 상한 적용
- [U-0503](unknowns.md#u-0503) 해석 B: heal = h + floor(0.15 * h)이고, 그다음 상한 적용 (모든 정수 h에서 A와 동일)
- [U-0503](unknowns.md#u-0503) 해석 C: heal = floor(1.15 * min(h, missing HP)): 보너스가 실제 회복량에 적용됨
- [U-0503](unknowns.md#u-0503) 해결 방법: VOD: 최대 HP보다 1에서 10 HP 낮은 Piety 참가자가 중간 포션을 마시는 장면.
- [U-0503](unknowns.md#u-0503) 해결 방법: VOD: 낮은 HP에서 각 등급을 마신 뒤의 HP 표시 (+5, +11, +23, +46 예상).

### U-0505

[U-0505](unknowns.md#u-0505): Piety 상자 변환 범위: "item chests"와 크레이트만 변환됩니까, 아니면 다른 보급 상자(에어드롭, 관리자, 시청자, Endurance)도 포션으로 바뀝니까? 상태: `open`.

중요한 이유 ([U-0505](unknowns.md#u-0505)): 상인 보급 상자만 변하지 않는다고 명시되어 있으며, 루팅의 큰 비중을 차지하는 다른 모든 보급 상자에 대해서는 본문이 아무 말도 하지 않습니다.

- [U-0505](unknowns.md#u-0505) 해석 A: item chests와 크레이트만 변환되고, 모든 보급 상자는 변하지 않음 (상인 문장은 부연 설명)
- [U-0505](unknowns.md#u-0505) 해석 B: 상인 것을 제외한 item chests, 크레이트, 모든 보급 상자가 변환됨
- [U-0505](unknowns.md#u-0505) 해결 방법: VOD: 시청자 또는 에어드롭 보급 상자를 획득하는 Piety 참가자.
- [U-0505](unknowns.md#u-0505) 해결 방법: 주최 측의 발표.

### U-0508

[U-0508](unknowns.md#u-0508): Greed 타이머: 30 min 쿨다운은 모든 훔치기 시도에서 시작됩니까, 아니면 성공한 훔치기에서만 시작됩니까? 그리고 피해자별 24 h 구간은 마지막 지급 시점을 기준(롤링)으로 합니까, 아니면 일일 시계를 기준으로 합니까? 상태: `open`.

중요한 이유 ([U-0508](unknowns.md#u-0508)): 실패한 훔치기(fortress, Piety 피해자, 빈 인벤토리)는 30 min을 소모하거나 아무것도 소모하지 않습니다. 일일 시계에서는 초기화 시점 전후의 짧은 시간 안에 두 번 지급될 수 있습니다.

- [U-0508](unknowns.md#u-0508) 해석 A: 쿨다운은 Steal을 사용하기만 하면 시작되고, 24 h 구간은 해당 피해자에 대한 마지막 지급부터 롤링됨
- [U-0508](unknowns.md#u-0508) 해석 B: 쿨다운은 성공한 훔치기에서만 시작되고, 24 h 구간은 롤링됨
- [U-0508](unknowns.md#u-0508) 해석 C: A 또는 B와 같으나 24 h 구간이 고정된 일일 시각에 초기화됨
- [U-0508](unknowns.md#u-0508) 해결 방법: VOD: Greed 참가자가 fortress로 보호받는 대상 또는 Piety 대상에게 Steal을 사용한 뒤 다시 시도하는 장면.

### U-0511

[U-0511](unknowns.md#u-0511): Greed 상자 Shield: 참가자가 이미 활성 Shield(아이템 또는 이전 상자 Shield)를 가지고 있으면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0511](unknowns.md#u-0511)): 반복된 상자 획득이 보호를 연장하는지, 그리고 Greed 참가자가 얼마나 오래 면역을 유지할 수 있는지를 결정합니다. 위키는 상자 Shield가 3개 효과 제한에 포함되지 않는다고도 말합니다.

- [U-0511](unknowns.md#u-0511) 해석 A: 새 Shield가 타이머를 20 min으로 갱신함
- [U-0511](unknowns.md#u-0511) 해석 B: 새 Shield가 남은 시간에 20 min을 더함
- [U-0511](unknowns.md#u-0511) 해석 C: Shield가 활성인 동안 새 굴림은 무시됨
- [U-0511](unknowns.md#u-0511) 해석 D: 독립된 Shield들이 공존함
- [U-0511](unknowns.md#u-0511) 해결 방법: VOD: Greed 참가자가 Shield 상태에서 두 번째 상자를 획득하는 장면.

### U-0513

[U-0513](unknowns.md#u-0513): Ingenuity의 "Recognize fake chests and gravestones, see traps, and hack landmines or C4 within 50m (164ft)": 50 m 제한은 세 능력 모두에 적용됩니까, 아니면 해킹에만 적용됩니까? 상태: `open`.

중요한 이유 ([U-0513](unknowns.md#u-0513)): 가짜 탐지의 범위는 Ingenuity 참가자가 지도의 어느 범위까지 Trolling 함정을 간파하는지를 결정합니다.

- [U-0513](unknowns.md#u-0513) 해석 A: 세 능력 모두 50 m 이내에서만 작동함
- [U-0513](unknowns.md#u-0513) 해석 B: 해킹만 50 m로 제한되고, 가짜 알아보기와 함정 보기에는 명시된 범위가 없음
- [U-0513](unknowns.md#u-0513) 해석 C: 알아보기와 보기는 소유자에게 지도 전체에 적용되고, 해킹은 50 m 이내
- [U-0513](unknowns.md#u-0513) 자유 매개변수 `ingenuity_detect_radius_m`, 탐색 범위: 50 m(기재된 대로)에서 지도 전체까지. 하한은 문자 그대로의 50 m입니다
- [U-0513](unknowns.md#u-0513) 해결 방법: VOD: 가짜 상자로부터 여러 거리에 있을 때 Ingenuity 참가자의 지도.

### U-0516

[U-0516](unknowns.md#u-0516): Trapped gift: 16 h 제한은 landmine과 C4 부착이 공유합니까, 그리고 누가 함정을 볼 수 있습니까(소유자만, 아니면 다른 Ingenuity 참가자도)? 상태: `open`.

중요한 이유 ([U-0516](unknowns.md#u-0516)): Ingenuity 페이지는 이 둘에 대해 "once every 16h"라고 하며, C4와 Landmine 페이지는 각각에 대해 이를 반복하고, 한 줄은 "Only you and Sigil of Ingenuity contestants can see it"라고 합니다.

- [U-0516](unknowns.md#u-0516) 해석 A: 어떤 부착이든 16 h의 단일 공유 쿨다운
- [U-0516](unknowns.md#u-0516) 해석 B: C4 부착과 landmine 부착에 각각 별도의 16 h 쿨다운
- [U-0516](unknowns.md#u-0516) 해석 C: 가시성: 소유자만 함정을 봄
- [U-0516](unknowns.md#u-0516) 해석 D: 가시성: 소유자와 모든 Ingenuity 참가자가 봄
- [U-0516](unknowns.md#u-0516) 해결 방법: VOD: Ingenuity 참가자가 16 h 안에 landmine을 부착한 뒤 C4를 부착하는 장면.
- [U-0516](unknowns.md#u-0516) 해결 방법: VOD: 두 번째 Ingenuity 참가자가 trapped gift를 살펴보는 장면.

### U-0519

[U-0519](unknowns.md#u-0519): Ingenuity 수입: "craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed"에 무엇이 포함됩니까? 상태: `open`.

중요한 이유 ([U-0519](unknowns.md#u-0519)): 크레이트, 보급 상자, 에어드롭, 가짜 상자도 Black Hole에 파괴되지만 "chest"만 적혀 있습니다. "zombie killed"는 누구의 처치인지 말하지 않으며, Campfire HP는 명목값일 수도 실효값일 수도 있습니다.

- [U-0519](unknowns.md#u-0519) 해석 A: zombie killed = 참가자의 Zombie killer가 처치한 좀비. chests = 실제 아이템 상자만. Campfire HP = 실제로 회복된 HP (HP가 가득 찬 주변인은 아무것도 지급하지 않음)
- [U-0519](unknowns.md#u-0519) 해석 B: zombie killed = 참가자가 어떤 수단으로든 처치한 좀비. chests = Black Hole이 파괴하는 모든 상자, 크레이트, 보급 상자, 가짜 상자. Campfire HP = 소모된 풀
- [U-0519](unknowns.md#u-0519) 해석 C: 항목마다 혼합
- [U-0519](unknowns.md#u-0519) 해결 방법: VOD: 여러 보관함 근처에서 Black Hole이 터진 뒤 Ingenuity 참가자의 토큰 카운터.

### U-0522

[U-0522](unknowns.md#u-0522): Zombie killer의 "Kills the next ten zombies that come within 10m": 사용 시점에 이미 10 m 안에 있는 좀비도 죽입니까, 어떤 좀비 유형이 포함되며, 범위 안에 열 마리를 넘으면 어떻게 처리됩니까? 상태: `open`.

중요한 이유 ([U-0522](unknowns.md#u-0522)): 이 조합이 무리(좀비 50마리)로부터 지켜 주는지, 아니면 도착하는 열 마리에게만 작동하는지를 결정합니다. 가드 좀비와 무리가 포함되는지도 결정합니다.

- [U-0522](unknowns.md#u-0522) 해석 A: 10 m 안으로 들어오거나 이미 안에 있는 첫 열 마리(유형 무관)를 도착 순간마다 한 마리씩 죽임
- [U-0522](unknowns.md#u-0522) 해석 B: 사용 후에 10 m 안으로 들어온 좀비만 해당하며, 이미 안에 있는 좀비는 세지 않음
- [U-0522](unknowns.md#u-0522) 해석 C: 가드 좀비와 무리 좀비는 제외됨
- [U-0522](unknowns.md#u-0522) 해결 방법: VOD: 무리 한가운데에서 이 조합을 사용하는 장면.

### U-0523

[U-0523](unknowns.md#u-0523): Black hole: 즉시 발동입니까, 지속됩니까, 어디를 중심으로 하며, 누가 이득을 얻습니까? 상태: `open`.

중요한 이유 ([U-0523](unknowns.md#u-0523)): "Destroys every chest and crate within 200m"는 발동 시점의 일회성으로 읽힙니다. 남아 있는 장이라면 나중에 생성되는 상자도 파괴할 것입니다.

- [U-0523](unknowns.md#u-0523) 해석 A: 사용한 장소에서 반경 200 m의 일회성
- [U-0523](unknowns.md#u-0523) 해석 B: 명시되지 않은 시간 동안 지속되는 장
- [U-0523](unknowns.md#u-0523) 해석 C: 사용 시 참가자를 중심으로 함
- [U-0523](unknowns.md#u-0523) 자유 매개변수 `black_hole_duration_s`, 탐색 범위: 0(기재된 대로 즉시)에서 600 s: 10 min은 다른 조합(Robot, Campfire)의 가장 긴 명시 타이머와 일치합니다
- [U-0523](unknowns.md#u-0523) 해결 방법: VOD: Black hole 사용 뒤 새 상자가 생성되는 장면.

### U-0527

[U-0527](unknowns.md#u-0527): Robot이 "10m 이내의 다른 플레이어에게 2s마다 1 HP 피해"를 줍니다. 2 s 시계는 전역입니까 대상별입니까, 그리고 첫 타격은 즉시 들어갑니까 한 간격 뒤에 들어갑니까? 상태: `open`.

중요한 이유 ([U-0527](unknowns.md#u-0527)): 빠르게 지나가는 사람에게 가는 총 피해량과, 1 s만 머무는 대상이 타격을 받는지 여부가 달라집니다.

- [U-0527](unknowns.md#u-0527) 해석 A: 전역 2 s 시계: 각 틱이 그 순간 범위 안의 모두를 타격함
- [U-0527](unknowns.md#u-0527) 해석 B: 대상별 타이머, 첫 타격은 대상이 범위에 들어온 뒤 한 간격(2 s) 후(언세이프 서클(unsafe circle)과 같음)
- [U-0527](unknowns.md#u-0527) 해석 C: 대상별, 첫 타격은 진입 즉시이고 이후 2 s마다
- [U-0527](unknowns.md#u-0527) 해결 방법: VOD: robot 옆을 지나가는 참가자.

### U-0530

[U-0530](unknowns.md#u-0530): 가짜 상자 "롤링 1시간당 최대 2개": 설치 시각에 대한 슬라이딩 윈도입니까, 아니면 충전되는 2회분입니까? 상태: `open`.

중요한 이유 ([U-0530](unknowns.md#u-0530)): 가짜 상자의 최대 설치 속도가 달라집니다. 슬라이딩 윈도에서는 60 min 안에 세 번째가 허용되지 않고, 토큰 버킷에서는 2개가 즉시 허용된 뒤 30 min마다 1개입니다.

- [U-0530](unknowns.md#u-0530) 해석 A: 임의의 60 min 윈도 안에 최대 2번 설치(슬라이딩)
- [U-0530](unknowns.md#u-0530) 해석 B: 2회분, 30 min마다 1회분 회복
- [U-0530](unknowns.md#u-0530) 해석 C: 시계 기준 1시간당 2개(고정 윈도), 롤링이라는 말과 상반됨
- [U-0530](unknowns.md#u-0530) 해결 방법: VOD: 0, 10, 40 min에 가짜 상자를 설치하는 Trolling 참가자.

### U-0531

[U-0531](unknowns.md#u-0531): 가짜 상자 잠금 "1h 동안 상자를 열 수 없음": 보급 상자와 크레이트도 막습니까, 두 번째로 열면 연장됩니까, 그리고 Shield 외의 방어 수단(Safety bubble, Sleeping Bag, Body armor)도 잠금은 그대로 남겨 둡니까? 상태: `open`.

중요한 이유 ([U-0531](unknowns.md#u-0531)): 가짜 상자는 보급 상자처럼 보입니다. 잠금은 피해자가 다음에 열 것까지 포함할 때만 트롤의 아이템을 보호합니다.

- [U-0531](unknowns.md#u-0531) 해석 A: 잠금은 아이템 상자만 포함, 잠금 중에 가짜 상자를 두 번째로 여는 것은 불가능
- [U-0531](unknowns.md#u-0531) 해석 B: 잠금은 상자, 보급 상자, 크레이트를 포함
- [U-0531](unknowns.md#u-0531) 해석 C: 5 HP를 막는 모든 방어 수단에서도 잠금은 그대로 남음(피해와 잠금은 별개의 효과)
- [U-0531](unknowns.md#u-0531) 해석 D: Shield만 잠금을 그대로 남긴다고 명시되어 있고, 다른 방어 수단은 명시되지 않음
- [U-0531](unknowns.md#u-0531) 해결 방법: VOD: 가짜 상자를 연 피해자가 1 h 안에 보급 상자를 여는 경우.

### U-0532

[U-0532](unknowns.md#u-0532): Trolling 가짜 상자 "5 HP를 회복합니다": 열 때 고정된 5 HP입니까, 실제로 들어간 피해입니까, 그리고 피해자가 보호받거나 상자가 반사된 경우에도 발생합니까? 상태: `open`.

중요한 이유 ([U-0532](unknowns.md#u-0532)): Shield, Safety bubble, Mirror가 트롤의 회복을 막는지, 그리고 Kick 감소가 적용된 타격이 4를 회복시키는지 5를 회복시키는지가 결정됩니다.

- [U-0532](unknowns.md#u-0532) 해석 A: 보호 여부와 관계없이 상자를 열 때마다 5 HP 회복
- [U-0532](unknowns.md#u-0532) 해석 B: 회복량은 피해자가 잃은 피해량과 같음
- [U-0532](unknowns.md#u-0532) 해석 C: 피해가 막히지 않았을 때만 회복, 반사된 상자는 아무도 회복시키지 않음
- [U-0532](unknowns.md#u-0532) 해결 방법: VOD: Shield를 가진 피해자가 상자를 열기 전과 후의 트롤 HP.

### U-0533

[U-0533](unknowns.md#u-0533): Fake gravestone: 얼마나 지속되며, 2 h 대기는 설치 시점에 시작됩니까 이전 것이 사라질 때 시작됩니까? 상태: `open`.

중요한 이유 ([U-0533](unknowns.md#u-0533)): 페이지에는 fake gravestone의 지속 시간이 없습니다. 2 h 쿨다운 또는 "대기"는 설치 시점이나 제거 시점부터 흐를 수 있습니다.

- [U-0533](unknowns.md#u-0533) 해석 A: 설치 시점부터 2 h, 루팅될 때까지 지속 시간 무제한
- [U-0533](unknowns.md#u-0533) 해석 B: 이전 fake gravestone이 사라진 시점부터 2 h
- [U-0533](unknowns.md#u-0533) 해석 C: 설치 시점부터 2 h, 지속 시간은 2 h보다 짧음
- [U-0533](unknowns.md#u-0533) 자유 매개변수 `fake_gravestone_lifetime_s`, 탐색 범위: 600 s부터 이벤트 길이까지: 600 s 미만이면 아무도 루팅하기 전에 사라지고, 상한은 영구입니다
- [U-0533](unknowns.md#u-0533) 해결 방법: VOD: 몇 시간 동안 관찰한 fake gravestone.

### U-0539

[U-0539](unknowns.md#u-0539): 언세이프 서클(unsafe circle) 아이템 손실: 잃은 아이템은 파괴됩니까 떨어집니까, "면역 아님" 조건은 시계를 멈춥니까 손실만 건너뜁니까, 그리고 활성 효과(인벤토리가 아닌 것)도 영향을 받습니까? 상태: `open`.

중요한 이유 ([U-0539](unknowns.md#u-0539)): 떨어진 아이템은 트롤이 루팅할 수 있고, 파괴된 아이템은 사라집니다. Guardian angel, Safety bubble, Reality Shield, Death Ward에 의한 면역은 피해와 손실을 모두 막습니다.

- [U-0539](unknowns.md#u-0539) 해석 A: 파괴됨, 인벤토리 아이템과 고유 조합 아이템만
- [U-0539](unknowns.md#u-0539) 해석 B: 참가자의 발밑에 떨어짐
- [U-0539](unknowns.md#u-0539) 해석 C: 파괴됨, 활성 효과(실행 중인 Shield, 착용 중인 Hazmat suit)도 제거됨
- [U-0539](unknowns.md#u-0539) 해석 D: 면역 중에는 시계가 계속 흐르고 손실만 건너뜀, 또는 면역 중에는 시계가 멈춤
- [U-0539](unknowns.md#u-0539) 해결 방법: VOD: 언세이프 서클에서 아이템을 잃는 참가자.

### U-0540

[U-0540](unknowns.md#u-0540): Trolling 보급 상자 유인 "Trolling 참가자 옆에 떨어질 확률 3%": 어떤 상자가 굴림 대상이며, Trolling 참가자가 여러 명일 때 참가자는 어떻게 정해지고, 추첨은 상자당 한 번입니까? 상태: `open`.

중요한 이유 ([U-0540](unknowns.md#u-0540)): Trolling 페이지는 시청자의 크레이트와 보급 상자라고 하고, 공격 페이지는 보급 상자(모든 보급 상자)만이며 5 m 이내에 떨어진다고 합니다. Trolling 참가자가 N명일 때 유인 확률은 전체 3%일 수도, 각각 3%일 수도 있습니다.

- [U-0540](unknowns.md#u-0540) 해석 A: 모든 보급 상자가 한 번씩 굴림(3%), 성공하면 Trolling 참가자를 균등하게 선택, 크레이트는 영향 없음
- [U-0540](unknowns.md#u-0540) 해석 B: 시청자가 구매한 크레이트와 보급 상자가 각각 한 번씩 굴림(3%)
- [U-0540](unknowns.md#u-0540) 해석 C: 각 Trolling 참가자가 독립적으로 굴림, 상자마다 각각 3%
- [U-0540](unknowns.md#u-0540) 해결 방법: VOD: 많은 투하에 걸친 보급 상자 착지 지점 집계.
- [U-0540](unknowns.md#u-0540) 해결 방법: 주최 측 발표.

### U-0600

[U-0600](unknowns.md#u-0600): Death 묘비 약탈 회복: 최대 HP의 5%인데, 소수 결과의 끝수는 어떻게 처리합니까(기본 최대 HP는 100이지만 상인이 최대 HP를 10씩 올려 팔기 때문에 110의 5%는 5.5입니다)? 상태: `open`.

중요한 이유 ([U-0600](unknowns.md#u-0600)): 최대 HP가 20의 배수가 아니면 모든 약탈 회복이 최대 1 HP 달라집니다. Death의 지속력에 영향을 줍니다.

- [U-0600](unknowns.md#u-0600) 해석 A: 회복 = floor(M*5/100)
- [U-0600](unknowns.md#u-0600) 해석 B: 회복 = ceil(M*5/100)
- [U-0600](unknowns.md#u-0600) 해석 C: 회복 = M*5/100의 반올림(half up)
- [U-0600](unknowns.md#u-0600) 해석 D: 소수 HP를 그대로 유지
- [U-0600](unknowns.md#u-0600) 해결 방법: VOD: 최대 HP 110인 Death 참가자가 묘비를 약탈하면 +5(A), +6(B 또는 C), +5.5(D)로 표시됩니다.

### U-0605

[U-0605](unknowns.md#u-0605): Death 시길 "다른 참가자가 죽을 때마다 블러드 토큰 1개": 거리 제한이 있습니까(회복은 50m 기준), 그리고 부활이나 두 번째 사망도 다시 보상을 줍니까? 상태: `open`.

중요한 이유 ([U-0605](unknowns.md#u-0605)): 상인 구매의 재원이 되는 Death의 블러드 토큰 수입을 정합니다.

- [U-0605](unknowns.md#u-0605) 해석 A: 경기장 어디에서든 발생한 사망
- [U-0605](unknowns.md#u-0605) 해석 B: Death 참가자로부터 50m 이내의 사망만
- [U-0605](unknowns.md#u-0605) 해석 C: A 또는 B, 그리고 부활 후 다시 죽은 참가자는 다시 보상을 줌
- [U-0605](unknowns.md#u-0605) 해결 방법: VOD: 멀리서 발생한 사망 뒤의 Death 참가자 블러드 토큰 카운터.

### U-0608

[U-0608](unknowns.md#u-0608): Endurance의 "Earn one more for every five item uses": 추가 토큰은 언제 지급됩니까? 상태: `open`.

중요한 이유 ([U-0608](unknowns.md#u-0608)): Endurance 토큰 획득률이 달라집니다(5회 사용당 최대 토큰 1개 대 수령한 보급 상자당 토큰 1개).

- [U-0608](unknowns.md#u-0608) 해석 A: 아이템 사용 5회째마다 즉시 토큰 +1 (누적 카운터)
- [U-0608](unknowns.md#u-0608) 해석 B: floor(마지막 수령 이후 사용 횟수 / 5)가 다음 보급 상자 수령 시 추가됨
- [U-0608](unknowns.md#u-0608) 해석 C: 마지막 수령 이후 5회 사용이 있었다면 보급 상자 수령마다 최대 토큰 +1
- [U-0608](unknowns.md#u-0608) 해결 방법: VOD: 아이템을 5번째 사용할 때의 Endurance 토큰 카운터.

### U-0609

[U-0609](unknowns.md#u-0609): Endurance 아이템 사용 보너스: 어떤 행동이 "아이템 사용"입니까(무기 발사, 붕대, Safety bubble, 조합, 상인 업그레이드, 계속 활성 상태인 효과)? 상태: `open`.

중요한 이유 ([U-0609](unknowns.md#u-0609)): [U-0608](unknowns.md#u-0608)의 카운터가 얼마나 빠르게 증가하는지를 결정합니다.

- [U-0609](unknowns.md#u-0609) 해석 A: 활성 아이템 효과 규칙과 같이, 소비하거나 활성화한 모든 인벤토리 아이템
- [U-0609](unknowns.md#u-0609) 해석 B: A에서 아이템 페이지에 나열된 제외 항목(Safety bubble, 연막탄, 붕대, 조합, 상인 업그레이드)을 뺀 것
- [U-0609](unknowns.md#u-0609) 해석 C: 활 발사 같은 무기 공격도 포함
- [U-0609](unknowns.md#u-0609) 해결 방법: VOD: 행동 유형별로 각 행동 뒤의 카운터 변화.

### U-0610

[U-0610](unknowns.md#u-0610): Endurance의 "cannot trade, loot gravestones, drop items or pick up dropped items": 거래 금지는 다른 사람의 제안 수신, 선물 주기, 부활로 돌려받는 아이템도 포함합니까? 상태: `open`.

중요한 이유 ([U-0610](unknowns.md#u-0610)): Endurance 참가자가 실제로 얼마나 고립되는지, 그리고 팀원이 그에게 아이템을 전달할 수 있는지를 보여 줍니다.

- [U-0610](unknowns.md#u-0610) 해석 A: Endurance 참가자가 시작하는 행동만 차단됨
- [U-0610](unknowns.md#u-0610) 해석 B: 다른 사람의 제안을 포함해 그와 관련된 모든 거래가 차단됨
- [U-0610](unknowns.md#u-0610) 해석 C: B와 같으며, 부활 시 자신의 묘비에서 복원되는 아이템도 거부됨
- [U-0610](unknowns.md#u-0610) 해결 방법: VOD: 다른 참가자가 Endurance 참가자에게 거래 요청을 보내는 장면.

### U-0611

[U-0611](unknowns.md#u-0611): Necromancy 소환 "up to 3 times every 6h": 롤링 구간입니까, 6h 고정 구간입니까, 아니면 타이머로 채워지는 3회분의 충전입니까? 상태: `open`.

중요한 이유 ([U-0611](unknowns.md#u-0611)): 시간당 좀비 수와 소환으로 얻는 블러드 토큰의 상한을 정합니다.

- [U-0611](unknowns.md#u-0611) 해석 A: 롤링 구간: 임의의 6h 구간 안에서 소환은 최대 3회
- [U-0611](unknowns.md#u-0611) 해석 B: 고정 구간: 카운터가 이벤트 시작부터 6h의 배수 시점에 초기화됨
- [U-0611](unknowns.md#u-0611) 해석 C: 각 묶음의 첫 소환 6h 후에 카운터가 초기화됨
- [U-0611](unknowns.md#u-0611) 해석 D: 2h마다 충전 1회분이 채워짐
- [U-0611](unknowns.md#u-0611) 해결 방법: VOD: 첫 소환으로부터 6h 이내와 6h 직후에 4번째 소환을 시도하는 장면.

### U-0614

[U-0614](unknowns.md#u-0614): 가드 좀비와 호드 보너스 좀비도 Necromancy 소유자에게 HP를 흡수해 주며 "one per HP your zombies drain"에 포함됩니까? 상태: `open`.

중요한 이유 ([U-0614](unknowns.md#u-0614)): 가드 좀비가 흡수량의 큰 부분일 수도 있고, 단지 존 통제 수단일 수도 있습니다.

- [U-0614](unknowns.md#u-0614) 해석 A: 소유자의 모든 좀비(소환, 죽음, 호드 보너스, 가드)가 HP와 토큰을 공급함
- [U-0614](unknowns.md#u-0614) 해석 B: 소환, 죽음, 호드 보너스 좀비만 공급하며, 가드 좀비는 흡수만 하고 공급하지 않음
- [U-0614](unknowns.md#u-0614) 해결 방법: VOD: 피해자가 가드 좀비 근처에 서 있는 동안의 소유자 HP와 토큰.

### U-0615

[U-0615](unknowns.md#u-0615): 가드 좀비의 "up to 30 HP per contestant": 가드 좀비 한 마리당입니까, 같은 참가자에 대해 모든 가드 좀비가 공유합니까? 한 시간 내내 제자리에 서 있습니까? 상태: `open`.

중요한 이유 ([U-0615](unknowns.md#u-0615)): 한 묘비 근처에서 여러 번 사망이 일어나면 가드가 중첩될 수 있으며, 상한에 따라 가드가 총량을 배가시키는지가 결정됩니다.

- [U-0615](unknowns.md#u-0615) 해석 A: 참가자 한 명에 대해 가드 좀비 한 마리당 30 HP 상한(일반 좀비 규칙과 같음)
- [U-0615](unknowns.md#u-0615) 해석 B: 참가자 한 명에 대해 모든 가드 좀비를 합쳐 30 HP 상한
- [U-0615](unknowns.md#u-0615) 해석 C: A이며, 한 참가자에게 상한에 도달한 가드는 그 참가자에 대해서만 흡수를 멈춤
- [U-0615](unknowns.md#u-0615) 해결 방법: VOD: 두 가드 좀비 사이에 서 있는 참가자.

### U-0616

[U-0616](unknowns.md#u-0616): Necromancy의 "Fully immune from zombies": 다른 Necromancy 참가자의 호드 좀비와 가드 좀비에도 적용되고, 10% 포션 파괴와 40% 조합 파괴에도 적용됩니까? 상태: `open`.

중요한 이유 ([U-0616](unknowns.md#u-0616)): Necromancy 참가자가 호드를 안전하게 가로지를 수 있는지를 결정합니다.

- [U-0616](unknowns.md#u-0616) 해석 A: 모든 좀비의 모든 좀비 효과(흡수, 포션 파괴, 조합 파괴)에 면역
- [U-0616](unknowns.md#u-0616) 해석 B: 흡수에만 면역이며, 다른 좀비 효과는 여전히 적용될 수 있음
- [U-0616](unknowns.md#u-0616) 해석 C: 모든 좀비의 흡수에는 면역이지만, 좀비 landmine 발동에는 면역이 아님
- [U-0616](unknowns.md#u-0616) 해결 방법: VOD: 회복 포션을 가진 Necromancy 참가자가 호드 안에 있는 장면.

### U-0619

[U-0619](unknowns.md#u-0619): Protection의 "Bandages last 1.1x as long": 더 긴 시간에 걸쳐 총 회복량이 같습니까, 아니면 더 긴 시간 동안 회복 속도가 같습니까? 상태: `open`.

중요한 이유 ([U-0619](unknowns.md#u-0619)): 132 s 동안 10 HP이거나 132 s 동안 11 HP입니다.

- [U-0619](unknowns.md#u-0619) 해석 A: 지속 시간 = 132 s, 총량은 10 HP로 유지됨(속도 감소)
- [U-0619](unknowns.md#u-0619) 해석 B: 지속 시간 = 132 s, 초당 HP는 같고 총량은 11 HP
- [U-0619](unknowns.md#u-0619) 해석 C: 지속 시간이 붕대의 틱 격자에 맞춰 어림됨
- [U-0619](unknowns.md#u-0619) 해결 방법: VOD: Protection 참가자의 붕대로 인한 총 HP 증가량.

### U-0620

[U-0620](unknowns.md#u-0620): 막은 타격으로 얻는 Protection 블러드 토큰: 공습의 화염 틱, 자신의 landmine, 나열되지 않은 면역(함정 선물, 독, 보복)도 토큰을 지급합니까? 상태: `open`.

중요한 이유 ([U-0620](unknowns.md#u-0620)): Protection 블러드 토큰 수입과, 시청자가 이를 위해 토큰을 파밍하는지를 정합니다.

- [U-0620](unknowns.md#u-0620) 해석 A: 공습 충격 또는 건십 폭탄당 토큰 1개뿐이며, 독, 함정 선물, 보복, 시길 자신의 landmine은 아무것도 지급하지 않음
- [U-0620](unknowns.md#u-0620) 해석 B: A에 더해 화염 틱당 토큰 1개
- [U-0620](unknowns.md#u-0620) 해석 C: "already blocked"가 적용되는 경우를 제외하고 모든 면역이 토큰 1개를 지급함
- [U-0620](unknowns.md#u-0620) 해결 방법: VOD: 공습 화염 아래에 있는 Protection 참가자.

### U-0621

[U-0621](unknowns.md#u-0621): Protection landmine 능력: 시길 선택 즉시 준비됩니까, 2h 후에 준비됩니까, 2h는 설치 시점부터 시작됩니까, 그리고 이것은 아이템 Landmine(5개 중첩, Kick 라이브 보너스, 인챈트, 가시성)입니까? 상태: `open`.

중요한 이유 ([U-0621](unknowns.md#u-0621)): Protection이 설치할 수 있는 무료 landmine의 수와, 아이템 규칙과의 상호작용을 정합니다.

- [U-0621](unknowns.md#u-0621) 해석 A: 선택 즉시 준비됨. 쿨다운은 설치 시점부터 시작되며, 그 외에는 일반 landmine 아이템 규칙이 적용됨
- [U-0621](unknowns.md#u-0621) 해석 B: 첫 landmine은 선택 2h 후
- [U-0621](unknowns.md#u-0621) 해석 C: 능력 landmine은 자체 규칙을 가지며 Kick 라이브 보너스를 받지 않음
- [U-0621](unknowns.md#u-0621) 해결 방법: VOD: Protection 참가자가 landmine을 설치하는 장면.

### U-0622

[U-0622](unknowns.md#u-0622): Healing 능력 "Heal a nearby contestant": 범위는 얼마입니까? 상태: `open`.

중요한 이유 ([U-0622](unknowns.md#u-0622)): 범위는 회복자가 얼마나 가까이 서야 하는지를 정합니다.

- [U-0622](unknowns.md#u-0622) 자유 매개변수 `healing_ability_range_m`, 탐색 범위: 1 ~ 50 m: 1 m는 의미 있는 가장 가까운 접촉, 50 m는 명시된 가장 큰 시길 범위(Death 회복, Necromancy 가드 발동)에 해당하며, 5 m와 10 m는 명시된 다른 범위입니다.
- [U-0622](unknowns.md#u-0622) 해결 방법: VOD: 측정된 거리에 있는 회복자와 대상.

### U-0623

[U-0623](unknowns.md#u-0623): Healing 능력: 회복자 자신, 이미 HP가 가득 찬 대상, 중독되지 않은 대상을 대상으로 삼을 수 있습니까? 쿨다운과 토큰은 그래도 소모됩니까? 상태: `open`.

중요한 이유 ([U-0623](unknowns.md#u-0623)): 회복당 블러드 토큰을 파밍할 수 있는지, 그리고 10min 쿨다운이 어떻게 작동하는지를 결정합니다.

- [U-0623](unknowns.md#u-0623) 해석 A: 대상은 다른 사람이어야 하고, 어떤 대상이든 가능하며, 효과와 상관없이 토큰과 쿨다운이 소모됨
- [U-0623](unknowns.md#u-0623) 해석 B: 대상이 이득을 얻어야 하며(HP가 최대 미만이거나 중독 또는 출혈 상태), 그때만 쿨다운과 토큰이 소모됨
- [U-0623](unknowns.md#u-0623) 해석 C: A이되 자기 자신도 허용됨
- [U-0623](unknowns.md#u-0623) 해결 방법: VOD: 회복자가 HP가 가득 찬 대상에게 능력을 사용하는 장면.

### U-0626

[U-0626](unknowns.md#u-0626): Healing 참가자가 Healing이 아닌 참가자를 부활시키는 범위: Healing 페이지는 Healing 참가자가 부활되는 쪽일 때만 묘비로부터 10m를 제시합니다. 상태: `open`.

중요한 이유 ([U-0626](unknowns.md#u-0626)): 부활 경쟁 모델에 필요합니다.

- [U-0626](unknowns.md#u-0626) 자유 매개변수 `revive_range_other_m`, 탐색 범위: 1 ~ 30 m: 1 m는 최소 접촉, 30 m는 명시된 비슷한 범위 중 가장 긴 것(10m)보다 큰 값입니다.
- [U-0626](unknowns.md#u-0626) 해결 방법: VOD: 측정된 거리에서의 부활.

### U-0627

[U-0627](unknowns.md#u-0627): 시길 선택: 이벤트 시작 이후 마감 시한이 있습니까, 그리고 선택하지 않은 참가자에게는 무엇이 적용됩니까(기본 능력치, 능력 없음)? 상태: `open`.

중요한 이유 ([U-0627](unknowns.md#u-0627)): 지연은 시길의 패시브 타이머와 능력을 잃게 하며, 선택하지 않으면 참가자가 시길 효과 없이 남을 수 있습니다.

- [U-0627](unknowns.md#u-0627) 자유 매개변수 `sigil_pick_deadline_s`, 탐색 범위: 0 ~ 이벤트 지속 시간([U-0009](unknowns.md#u-0009)): 0은 선택이 이벤트 시작 시점에 이미 끝나 있음을 뜻하고, 상한은 가능한 가장 긴 지연입니다.
- [U-0627](unknowns.md#u-0627) 해결 방법: 주최자의 발표, 선택 화면이 담긴 VOD.

## 우선순위: 낮음

### U-0013

[U-0013](unknowns.md#u-0013): events/safe-zone/ 에셋은 규칙이 다른 이전 판에 속합니까? 상태: `resolved`.

중요한 이유 ([U-0013](unknowns.md#u-0013)): 재사용된 콘텐츠와 새 콘텐츠를 구분할 수 있게 됩니다.

- [U-0013](unknowns.md#u-0013) 해결 방법: RE-0002, corpus/diffs/
- [U-0013](unknowns.md#u-0013) 해결됨: 그렇습니다. 2026년 10월 Austin 판입니다(RE-0002, RE-0005). 규칙 모델과는 무관합니다. 2026-11-11 스냅샷만이 규칙의 출처입니다(프로젝트 소유자 결정, 2026-11-11).

### U-0100

[U-0100](unknowns.md#u-0100): 4단계의 'The damage left is rounded down'은 어디에 적용됩니까? Protection 50% 결과에만 적용됩니까, 아니면 모든 감소 이후의 최종 내림 한 번으로 적용되며 Kick 10%는 내림하지 않은 값에서 계산됩니까? 상태: `open`.

중요한 이유 ([U-0100](unknowns.md#u-0100)): Kick 라이브 중인 Protection 참가자가 핵을 맞을 때 홀수 피해가 달라집니다. 중간 내림 후 Kick을 적용하는 경우와, 정확한 절반에 Kick을 적용하는 경우의 차이입니다.

- [U-0100](unknowns.md#u-0100) 해석 A: x -> floor(x/2) 후, 그 정수에 Kick 감소([U-0001](unknowns.md#u-0001) 해석)를 적용
- [U-0100](unknowns.md#u-0100) 해석 B: x -> floor(0.9*(x/2)), 최종 내림 한 번만 적용(Kick 비율을 정확한 절반에 적용)
- [U-0100](unknowns.md#u-0100) 해결 방법: VOD: 라이브 Protection 참가자가 기본 피해가 홀수인 핵을 맞고, HP 감소량을 읽습니다.
- [U-0100](unknowns.md#u-0100) 해결 방법: REA: 배포된 코드의 피해 공식.

### U-0109

[U-0109](unknowns.md#u-0109): 'Items that do not fit stay in the gravestone': 부활 시 용량 규칙은 무엇이며, 묘비에 남은 아이템은 이후 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0109](unknowns.md#u-0109)): 사망 후 인벤토리가 얼마나 남는지, 남은 아이템을 계속 루팅할 수 있는지를 결정합니다.

- [U-0109](unknowns.md#u-0109) 해석 A: 용량은 범주별 일반 소지 한도이며, 남은 아이템은 누구나 루팅할 수 있는 상태로 남습니다
- [U-0109](unknowns.md#u-0109) 해석 B: 남은 아이템은 묘비에 남지만 해당 시간 동안만 블러드 토큰처럼 잠깁니다
- [U-0109](unknowns.md#u-0109) 자유 매개변수 `inventory_capacity`, 탐색 범위: 모든 범주 합산 0 ~ 12 슬롯. 상한은 아이템 페이지에서 확인된 어떤 소지 구성보다 높게 잡은 스윕 선택이며 위키 값이 아닙니다
- [U-0109](unknowns.md#u-0109) 해결 방법: VOD: 사망과 부활 사이에 새 아이템을 주운 참가자의 부활.
- [U-0109](unknowns.md#u-0109) 해결 방법: 아이템 페이지의 소지 한도를 이 규칙에 대조해 읽기(패밀리 교차).

### U-0118

[U-0118](unknowns.md#u-0118): 'Sleeping in your own Sleeping Bag'은 Poison 면역 목록에 동사 없이 라벨로만 나옵니다: 새 독을 막습니까, 각 단계를 막습니까, 둘 다입니까? 상태: `open`.

중요한 이유 ([U-0118](unknowns.md#u-0118)): 라벨의 의미에 따라 자는 사람이 아예 중독될 수 있는지가 달라집니다(다트는 여전히 중독시키고 단계는 막힘). Poison에 대해 Sleeping Bag을 나열한 피해 표의 행을 참조하십시오.

- [U-0118](unknowns.md#u-0118) 해석 A: 자신의 bag에서 자는 동안 새 독이 없습니다(Anti poison과 같음)
- [U-0118](unknowns.md#u-0118) 해석 B: 자는 동안 기존 및 새 독 단계가 막힙니다(Shield와 같음)
- [U-0118](unknowns.md#u-0118) 해석 C: 둘 다
- [U-0118](unknowns.md#u-0118) 해결 방법: VOD: 자고 있는 참가자에게 쓴 Poison Dart.

### U-0121

[U-0121](unknowns.md#u-0121): 자해 타격('hit by your own C4 and landmine'): 공격자 = 방어자로 전체 파이프라인이 실행되어 Kick 보너스(2단계)와 Kick 감소(4단계)가 포함됩니까? 그리고 자신이 가진 차단 수단(Protection, Shield)이 적용됩니까? 상태: `open`.

중요한 이유 ([U-0121](unknowns.md#u-0121)): 자신 근처에서 폭발시키는 것의 실제 비용을 결정합니다.

- [U-0121](unknowns.md#u-0121) 해석 A: 전체 파이프라인, 공격자 보너스와 방어자 감소가 모두 적용되고 Mirror는 건너뜁니다(자기 폭발물에는 절대 적용되지 않음)
- [U-0121](unknowns.md#u-0121) 해석 B: 자해 타격에는 Kick 보너스가 없습니다
- [U-0121](unknowns.md#u-0121) 해석 C: 자신이 가진 Protection 또는 Shield가 있으면 무해합니다
- [U-0121](unknowns.md#u-0121) 해결 방법: VOD: 라이브 중인 참가자의 자폭.

### U-0124

[U-0124](unknowns.md#u-0124): 묘비 위치 'where you were last seen': 사망 순간의 위치입니까, 마지막으로 수신된 GPS 위치입니까? 상태: `open`.

중요한 이유 ([U-0124](unknowns.md#u-0124)): GPS가 없는 사망(오프라인)과 루팅하는 사람의 10 m 식 범위에서 중요합니다.

- [U-0124](unknowns.md#u-0124) 해석 A: 사망 시 위치
- [U-0124](unknowns.md#u-0124) 해석 B: 사망 전 마지막으로 수신된 GPS 위치
- [U-0124](unknowns.md#u-0124) 해결 방법: VOD: 오프라인 참가자의 사망.

### U-0204

[U-0204](unknowns.md#u-0204): 최대 HP가 10의 배수가 아닐 때 Eddie의 포션의 50% 회복과 30% 손실은 어떤 방식으로 어림됩니까? 상태: `open`.

중요한 이유 ([U-0204](unknowns.md#u-0204)): 죽을 수도 있는 도박에서 1 차이(off-by-one)가 발생하며, 어떤 기본 최대 HP가 존재하는지와도 연결됩니다.

- [U-0204](unknowns.md#u-0204) 해석 A: 둘 다 내림
- [U-0204](unknowns.md#u-0204) 해석 B: 둘 다 올림
- [U-0204](unknowns.md#u-0204) 해석 C: 둘 다 반올림(half up)
- [U-0204](unknowns.md#u-0204) 해석 D: 회복과 손실에 서로 다른 어림 방식 적용
- [U-0204](unknowns.md#u-0204) 자유 매개변수 `eddie_rounding`, 탐색 범위: 내림, 올림, 반올림(half up)을 회복과 손실에 각각 따로 적용 (4에서 9가지 조합). 시길이 알 수 없는 기본값에서 최대 HP를 10씩 바꾸므로 최대 HP는 90..110을 1 단위로 변화
- [U-0204](unknowns.md#u-0204) 해결 방법: VOD: 최대 HP 95 또는 105인 참가자(있다면)가 이를 마시는 장면.
- [U-0204](unknowns.md#u-0204) 해결 방법: 시드 [U-0004](unknowns.md#u-0004)는 이것이 죽일 수 있는지를 묻는 것이며, 어림 방식과는 무관합니다.

### U-0210

[U-0210](unknowns.md#u-0210): Body armor를 착용 중이거나 소지 중일 때 두 번째 Body armor를 얻으면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0210](unknowns.md#u-0210)): 새 armor가 거부되는지, 교체되는지, 버려지는지가 결정됩니다.

- [U-0210](unknowns.md#u-0210) 해석 A: 거부됨
- [U-0210](unknowns.md#u-0210) 해석 B: 착용 중인 것을 교체함
- [U-0210](unknowns.md#u-0210) 해결 방법: VOD: 두 번째 armor를 줍는 장면.

### U-0217

[U-0217](unknowns.md#u-0217): Mirror 대 mirror와 flashbang: 던진 사람도 mirror를 가지고 있다면 던진 사람이 실명합니까? 상태: `open`.

중요한 이유 ([U-0217](unknowns.md#u-0217)): Mirror 규칙은 둘 다 소모되고 아무 일도 일어나지 않는다고 하고, flashbang 규칙은 대신 던진 사람이 실명한다고 합니다.

- [U-0217](unknowns.md#u-0217) 해석 A: mirror-mirror 규칙이 우선, 실명 없음
- [U-0217](unknowns.md#u-0217) 해석 B: flashbang 규칙이 우선, 던진 사람이 실명함
- [U-0217](unknowns.md#u-0217) 해결 방법: VOD: mirror 보유자가 mirror 보유자에게 flashbang을 던지는 장면.

### U-0218

[U-0218](unknowns.md#u-0218): 실명한 참가자가 또 다른 flashbang에 맞으면 실명이 연장됩니까, 초기화됩니까, 무시됩니까? 상태: `open`.

중요한 이유 ([U-0218](unknowns.md#u-0218)): flashbang 압박의 중첩에 영향을 줍니다.

- [U-0218](unknowns.md#u-0218) 해석 A: 무시됨
- [U-0218](unknowns.md#u-0218) 해석 B: 30 s로 초기화
- [U-0218](unknowns.md#u-0218) 해석 C: 더해짐
- [U-0218](unknowns.md#u-0218) 자유 매개변수 `flashbang_reapply_rule`, 탐색 범위: 무시, 초기화, 최대 2 중첩까지 가산
- [U-0218](unknowns.md#u-0218) 해결 방법: VOD: flashbang 이중 타격.

### U-0302

[U-0302](unknowns.md#u-0302): 'Only you can see the trap.' (C4 섹션)은 함정 선물(C4가 부착된 아이템)을 가리킵니까, 설치된 C4를 가리킵니까? 상태: `open`.

중요한 이유 ([U-0302](unknowns.md#u-0302)): 다음 문장들은 설치된 C4를 본인과 Ingenuity 참가자만 볼 수 있다고 합니다. 지시 대상에 따라 함정 선물을 누가 보는지, Ingenuity 참가자가 보는지가 결정됩니다.

- [U-0302](unknowns.md#u-0302) 해석 A: 함정 선물만 가리킴
- [U-0302](unknowns.md#u-0302) 해석 B: 설치된 C4만 가리킴 (그러면 마지막 C4 문장은 Ingenuity를 더해 이를 반복하는 것)
- [U-0302](unknowns.md#u-0302) 해석 C: 둘 다 가리킴
- [U-0302](unknowns.md#u-0302) 해결 방법: VOD: Ingenuity가 아닌 참가자의 지도에서, 근처에 설치된 C4가 있고 함정 아이템을 들고 있는 장면.

### U-0314

[U-0314](unknowns.md#u-0314): Wizard staff 'Each use costs 2 blood tokens': Ingenuity의 10% 할증이 여기에 적용됩니까? 토큰이 2개 미만이면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0314](unknowns.md#u-0314)): ceil(2*1.1) = 3이면 Ingenuity 참가자에게 staff가 3분의 1 비싸집니다. 이것은 상인 가격이 아닙니다.

- [U-0314](unknowns.md#u-0314) 해석 A: 모든 시길에 2 토큰(상인 가격이 아님)
- [U-0314](unknowns.md#u-0314) 해석 B: Ingenuity는 ceil(2*1.1) = 3을 지불
- [U-0314](unknowns.md#u-0314) 해석 C: 비용보다 적은 토큰으로는 사용할 수 없음
- [U-0314](unknowns.md#u-0314) 해결 방법: VOD: staff 사용 전후의 Ingenuity 참가자의 토큰 수.

### U-0316

[U-0316](unknowns.md#u-0316): Poison Dart: '20 HP over 30min'과 독 페이지의 1min 30s마다 1 HP를 함께 보면, 첫 틱은 1min 30s에 옵니까, 즉시 옵니까? 상태: `open`.

중요한 이유 ([U-0316](unknowns.md#u-0316)): 모든 다트 틱이 1min 30s씩 밀리고 마지막 HP의 시각도 달라집니다.

- [U-0316](unknowns.md#u-0316) 해석 A: 틱이 90, 180, ..., 1800 s에 발생(20틱, 마지막은 30min)
- [U-0316](unknowns.md#u-0316) 해석 B: 틱이 0, 90, ..., 1710 s에 발생(20틱, 첫 틱은 즉시)
- [U-0316](unknowns.md#u-0316) 해결 방법: VOD: 중독된 참가자의 HP 타임라인.

### U-0326

[U-0326](unknowns.md#u-0326): 'Local solar time'(지역 태양시): 무엇에 대한 지역입니까(참가자의 위치, 이벤트 장소, 기준 도시 하나)? 상태: `open`.

중요한 이유 ([U-0326](unknowns.md#u-0326)): 기상 및 수면 허용 시간대가 이에 달려 있습니다. 경도 1도당 약 4분씩 차이가 나며, 기준 시계를 쓰면 시간대에 따라 더 크게 달라집니다.

- [U-0326](unknowns.md#u-0326) 해석 A: 참가자 자신의 위치에서의 태양시
- [U-0326](unknowns.md#u-0326) 해석 B: 이벤트의 기준 위치 한 곳에서의 태양시
- [U-0326](unknowns.md#u-0326) 해석 C: 참가자 휴대폰의 현지 시계 시각
- [U-0326](unknowns.md#u-0326) 해결 방법: 주최 측의 발표.

### U-0335

[U-0335](unknowns.md#u-0335): 인챈트된 bow의 'five shots or two hours': 먼저 오는 쪽입니까, 나중에 오는 쪽입니까? 상태: `open`.

중요한 이유 ([U-0335](unknowns.md#u-0335)): 보너스가 긴 대기 시간을 견디는지, 다섯 발 뒤에 끝나는지를 결정합니다.

- [U-0335](unknowns.md#u-0335) 해석 A: 5발 또는 2 h 중 먼저 오는 쪽에서 끝남
- [U-0335](unknowns.md#u-0335) 해석 B: 둘 다 도달해야만 끝남
- [U-0335](unknowns.md#u-0335) 해결 방법: VOD: 2 h 안에 5발을 쏜 후의 인챈트 bow.

### U-0402

[U-0402](unknowns.md#u-0402): Protection 시길의 핵 피해 감소: 20 HP의 '50% less'는 10 HP이지만, 관리자가 정한 홀수 피해는 어떻게 반올림되며, 감소는 다른 경감 전에 적용됩니까 후에 적용됩니까? 상태: `open`.

중요한 이유 ([U-0402](unknowns.md#u-0402)): 관리자 핵은 임의의 피해를 설정할 수 있고, 홀수 값이면 floor, ceil, 정확한 분수가 서로 달라지며, 순서에 따라 Kick 라이브 중과 방어구가 있을 때의 합계가 바뀝니다.

- [U-0402](unknowns.md#u-0402) 해석 A: d -> floor(d/2)
- [U-0402](unknowns.md#u-0402) 해석 B: d -> ceil(d/2)
- [U-0402](unknowns.md#u-0402) 해석 C: d -> d/2 정확값(반올림 없음)
- [U-0402](unknowns.md#u-0402) 자유 매개변수 `admin_nuke_damage`, 탐색 범위: 1 ~ 100 HP; 위키는 기본값 20 HP만 제시하며 관리자 범위는 없습니다
- [U-0402](unknowns.md#u-0402) 해결 방법: Protection 참가자에게 홀수 피해의 관리자 핵을 쓴 VOD.
- [U-0402](unknowns.md#u-0402) 해결 방법: 피해 페이지의 연산 순서([U-0001](unknowns.md#u-0001), [U-0006](unknowns.md#u-0006)).

### U-0412

[U-0412](unknowns.md#u-0412): 무작위 아이템: 보급 상자와 에어드롭에서 'a random item'의 분포는 무엇이며, 에어드롭에서 'within 10m of a random point'의 분포는 무엇입니까? 상태: `open`.

중요한 이유 ([U-0412](unknowns.md#u-0412)): 보급 상자의 기댓값 계산에 필요하며, 아이템 풀은 자료 어디에도 명시되어 있지 않습니다.

- [U-0412](unknowns.md#u-0412) 해결 방법: VOD: 에어드롭의 아이템 내용을 기록.
- [U-0412](unknowns.md#u-0412) 해결 방법: 상자 페이지는 삭제되었습니다([U-0015](unknowns.md#u-0015)).

### U-0415

[U-0415](unknowns.md#u-0415): 'attacking a copy uses up your attack'는 무엇을 소모합니까: 무기 내구도, 공격 슬롯, 아이템, 쿨다운? 이는 staff, drone, C4, landmine에도 적용되며, 복사본을 식별하는 Thermal goggle 보유자에게도 적용됩니까? 상태: `open`.

중요한 이유 ([U-0415](unknowns.md#u-0415)): 공격자가 대상을 잘못 식별했을 때의 비용입니다.

- [U-0415](unknowns.md#u-0415) 해석 A: 일반 타격과 마찬가지로 아이템의 충전 또는 사용 1회
- [U-0415](unknowns.md#u-0415) 해석 B: 쿨다운만
- [U-0415](unknowns.md#u-0415) 해석 C: 내구도 1 포인트와 쿨다운
- [U-0415](unknowns.md#u-0415) 해결 방법: illusion 복사본에 대한 무기 타격 VOD.

### U-0416

[U-0416](unknowns.md#u-0416): Illusion 쿨다운: 'The next one can start 30min after it ends'. 'it ends'는 10min 만료를 뜻합니까, 파괴된 illusion을 뜻합니까? 그리고 illusion이 진행 중일 때 이루어진 구매는 어떻게 됩니까(대기열, 거부, 환불)? 상태: `open`.

중요한 이유 ([U-0416](unknowns.md#u-0416)): illusion의 발생 빈도를 제한합니다(약 40min에 한 번).

- [U-0416](unknowns.md#u-0416) 해석 A: 10min 만료 후 30min, 대기 중의 구매는 거부
- [U-0416](unknowns.md#u-0416) 해석 B: 직전 시작 후 30min
- [U-0416](unknowns.md#u-0416) 해석 C: 구매는 대기열에 들어가 가능한 가장 이른 시각에 시작
- [U-0416](unknowns.md#u-0416) 해결 방법: VOD: 화면 타이머와 함께 이벤트를 실시간으로 관찰합니다.

### U-0421

[U-0421](unknowns.md#u-0421): 사이클롭스 조종 투표: 방향의 집합은 무엇이며, 아무도 투표하지 않으면 승자가 유지됩니까, 그리고 투표는 시청자마다 5s 구간마다 집계됩니까? 상태: `open`.

중요한 이유 ([U-0421](unknowns.md#u-0421)): 사이클롭스를 참가자 쪽으로 얼마나 유도할 수 있는지를 결정합니다.

- [U-0421](unknowns.md#u-0421) 해석 A: 연속적인 방위, 투표의 평균
- [U-0421](unknowns.md#u-0421) 해석 B: 이산적인 방향, 5s 구간마다 최다 득표
- [U-0421](unknowns.md#u-0421) 해석 C: 투표가 없으면 이전 방향 유지
- [U-0421](unknowns.md#u-0421) 해결 방법: 사이클롭스 투표 UI의 VOD.

### U-0422

[U-0422](unknowns.md#u-0422): 사이클롭스 존 피해: 'Outside the safe zones it takes zone damage'. 참가자와 같은 속도([U-0003](unknowns.md#u-0003))입니까, 같은 단계적 증가입니까, 아니면 고정입니까? 상태: `open`.

중요한 이유 ([U-0422](unknowns.md#u-0422)): 세이프 존 밖의 사이클롭스가 존 피해만으로 죽어 아무것도 지급하지 않는지 여부입니다.

- [U-0422](unknowns.md#u-0422) 해석 A: 참가자와 같은 2s 틱과 같은 규칙
- [U-0422](unknowns.md#u-0422) 해석 B: 다른 규칙
- [U-0422](unknowns.md#u-0422) 해결 방법: 존 밖에 있는 사이클롭스의 VOD.

### U-0423

[U-0423](unknowns.md#u-0423): Reality Shield: 지속 시간이 주어지지 않았고, 'Everyone within 30m'는 반지름입니까 지름입니까, 그리고 'immune to all damage, zombies and new poison'은 이미 걸린 독이 계속 진행되는 것을 뜻합니까? 상태: `open`.

중요한 이유 ([U-0423](unknowns.md#u-0423)): 관리자용 도구이지만 핵 대응과 독 치료를 결정합니다.

- [U-0423](unknowns.md#u-0423) 해석 A: 제거될 때까지 영구
- [U-0423](unknowns.md#u-0423) 해석 B: 시간 제한 있음(비공개)
- [U-0423](unknowns.md#u-0423) 해석 C: 반지름 30m
- [U-0423](unknowns.md#u-0423) 해석 D: 지름 30m
- [U-0423](unknowns.md#u-0423) 자유 매개변수 `reality_shield_duration_s`, 탐색 범위: 60 ~ 86400 s: 시간이 명시되지 않았으며, 이벤트 규모가 상한입니다
- [U-0423](unknowns.md#u-0423) 해결 방법: 관리자의 발표.

### U-0428

[U-0428](unknowns.md#u-0428): Summon 빈도: 'up to 3 times every 6h'. 고정된 6h 구간입니까, 이동하는 6h 창입니까, 아니면 세 번째 사용 후 쿨다운입니까? 상태: `open`.

중요한 이유 ([U-0428](unknowns.md#u-0428)): Summon으로 얻는 Necromancy 수입의 상한을 정합니다.

- [U-0428](unknowns.md#u-0428) 해석 A: 이동 창: 임의의 6h 안에 최대 3회 사용
- [U-0428](unknowns.md#u-0428) 해석 B: 이벤트 시작부터 고정된 6h 구간
- [U-0428](unknowns.md#u-0428) 해석 C: 세 번째 사용 후 6h 잠금
- [U-0428](unknowns.md#u-0428) 해결 방법: Necromancy 참가자가 네 번 summon하는 VOD.

### U-0430

[U-0430](unknowns.md#u-0430): Ingenuity Zombie Killer: 'kills the next ten zombies that come within 10m of its owner'와 'stops zombies draining you until it has killed ten'. 함께 도착한 열 마리도 집계됩니까, 흡수 차단은 열 마리까지로 제한됩니까, 그리고 순서는 접근 순입니까? 상태: `open`.

중요한 이유 ([U-0430](unknowns.md#u-0430)): 50마리 무리에 대한 방어 가치입니다.

- [U-0430](unknowns.md#u-0430) 해석 A: 열 마리를 처치한 뒤 종료, 동시에 도착한 좀비는 거리순으로 처치
- [U-0430](unknowns.md#u-0430) 해석 B: 임의의 순간에 10m 안에 있는 서로 다른 좀비 열 마리
- [U-0430](unknowns.md#u-0430) 해결 방법: VOD.

### U-0431

[U-0431](unknowns.md#u-0431): Zombie repellent: 'zombies ignore you for 20min'(Zombies 페이지)과 'stop zombies hurting you'(Items)가 다릅니다. 무시한다는 것은 대상 지정에서 제외되어 좀비가 다른 참가자를 쫓는다는 뜻입니까, 아니면 흡수만 막는다는 뜻입니까? 상태: `open`.

중요한 이유 ([U-0431](unknowns.md#u-0431)): 보호받지 못하는 참가자들 사이에서 좀비가 어떻게 재분배되는지에 영향을 줍니다.

- [U-0431](unknowns.md#u-0431) 해석 A: 흡수에만 면역, 여전히 추격당함
- [U-0431](unknowns.md#u-0431) 해석 B: 대상 집합에서 제외
- [U-0431](unknowns.md#u-0431) 해결 방법: VOD.

### U-0506

[U-0506](unknowns.md#u-0506): 포션 중첩이 이미 6개이거나(또는 인벤토리가 포션을 받을 수 없을 때) Piety가 상자나 크레이트를 획득하면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0506](unknowns.md#u-0506)): 상한에서 상자 획득이 비용 없는 행동인지, 그리고 포션이 사라지는지 떨어지는지를 결정합니다.

- [U-0506](unknowns.md#u-0506) 해석 A: 획득이 거부되고 상자는 그대로 남음
- [U-0506](unknowns.md#u-0506) 해석 B: 상자가 소모되고 포션은 사라짐
- [U-0506](unknowns.md#u-0506) 해석 C: 포션이 참가자의 발치에 떨어짐 (공격 페이지의 hunter potion처럼)
- [U-0506](unknowns.md#u-0506) 해결 방법: VOD: 중첩이 6개로 가득 찬 Piety 참가자가 상자를 획득하는 장면.

### U-0509

[U-0509](unknowns.md#u-0509): 도둑에게 공간이 없을 때의 Greed Steal: 인벤토리가 가득 찼거나, 도둑이 이미 방어구를 가진 상태에서 Body Armor를 훔치면 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0509](unknowns.md#u-0509)): Body Armor는 "at most one, including equipped armor"를 허용하므로, 방어구를 착용한 Greed 참가자에게서 이를 훔치는 것은 불가능하거나 방어구 하나를 버리게 됩니다.

- [U-0509](unknowns.md#u-0509) 해석 A: 도둑이 아이템을 가질 수 없으면 훔치기가 거부됨
- [U-0509](unknowns.md#u-0509) 해석 B: 아이템이 도둑의 발치에 떨어짐
- [U-0509](unknowns.md#u-0509) 해석 C: 훔친 아이템이 기존 아이템을 대체하거나 버리게 함
- [U-0509](unknowns.md#u-0509) 해결 방법: VOD: 인벤토리가 가득 찬 Greed 참가자가 Steal을 사용하는 장면.

### U-0515

[U-0515](unknowns.md#u-0515): Ingenuity 포션 합치기: "two matching potions"는 무슨 뜻이며, 비용이나 제한이 있습니까? 상태: `open`.

중요한 이유 ([U-0515](unknowns.md#u-0515)): 회복 값은 정확히 더해지므로(5+5=10, 10+10=20, 20+20=40) 합치기는 회복에서 손실이 없지만 2칸 시길에서는 칸을 절약합니다. 제한은 명시되어 있지 않습니다.

- [U-0515](unknowns.md#u-0515) 해석 A: 같은 크기의 체력 포션 두 개가 다음 크기 하나가 됨 (작은 것에서 중간, 큰 것, 거대(gigantic)로). 거대 포션은 합칠 수 없음
- [U-0515](unknowns.md#u-0515) 해석 B: 같은 종류의 포션 두 개(Eddie's potion이나 Anti poison 포함)는 모두 합칠 수 있음
- [U-0515](unknowns.md#u-0515) 해석 C: A와 같으나 명시되지 않은 쿨다운 또는 비용이 있음
- [U-0515](unknowns.md#u-0515) 해결 방법: VOD: Ingenuity 참가자가 포션을 합치는 장면.

### U-0521

[U-0521](unknowns.md#u-0521): Everything potion의 "Cures poison and heals by potion tier": Anti poison의 10 min 독 면역도 부여합니까? 상태: `open`.

중요한 이유 ([U-0521](unknowns.md#u-0521)): 레시피는 Anti poison과 Health potion을 사용하며, Anti poison 아이템은 10 min 면역을 줍니다.

- [U-0521](unknowns.md#u-0521) 해석 A: 독을 치료하고 등급만큼만 HP를 회복함
- [U-0521](unknowns.md#u-0521) 해석 B: 10 min의 독 면역도 부여함
- [U-0521](unknowns.md#u-0521) 해결 방법: VOD: Ingenuity 참가자가 포션을 사용한 뒤 중독되는 장면.

### U-0534

[U-0534](unknowns.md#u-0534): Fake gravestone 복사 원본: 누군가 탈락했을 때, 탈락한 참가자 중 누구를 복사할지 누가 정합니까? 상태: `open`.

중요한 이유 ([U-0534](unknowns.md#u-0534)): "탈락한 참가자의 묘비를 복사하거나, 탈락자가 없는 동안에는 무작위 생존자의 묘비를 복사합니다": 이 대비는 무작위성이 대체 경우에만 있음을 시사합니다.

- [U-0534](unknowns.md#u-0534) 해석 A: 트롤이 탈락한 참가자 중 한 명을 고름, 탈락자가 없을 때만 무작위 생존 참가자
- [U-0534](unknowns.md#u-0534) 해석 B: 탈락한 참가자 중 무작위, 없으면 생존자 중 무작위
- [U-0534](unknowns.md#u-0534) 해석 C: 가장 최근에 탈락한 참가자
- [U-0534](unknowns.md#u-0534) 해결 방법: VOD: 탈락 1회 후와 여러 회 후에 설치된 fake gravestone.

### U-0536

[U-0536](unknowns.md#u-0536): 언세이프 서클(unsafe circle) "쿨다운 2h"와 20 min 지속 시간: 쿨다운은 설치 시점에 시작됩니까 서클이 끝날 때 시작됩니까? 상태: `open`.

중요한 이유 ([U-0536](unknowns.md#u-0536)): 설치 시점 기준이면 이전 서클이 만료되고 100 min 뒤에 새 서클이 가능하고, 종료 시점 기준이면 120 min 뒤입니다.

- [U-0536](unknowns.md#u-0536) 해석 A: 설치 시점부터 2 h
- [U-0536](unknowns.md#u-0536) 해석 B: 서클 종료 시점부터 2 h(설치 시점부터 2 h 20 min)
- [U-0536](unknowns.md#u-0536) 해결 방법: VOD: 2 h와 2 h 20 min에 설치한 두 번째 서클.

### U-0618

[U-0618](unknowns.md#u-0618): Protection의 포션 회복 "less 50%": 등급 수치가 홀수일 때(Small potion 5 HP) 끝수 처리는 어떻게 됩니까? 상태: `open`.

중요한 이유 ([U-0618](unknowns.md#u-0618)): Small potion이 2, 3 또는 2.5 HP를 줍니다.

- [U-0618](unknowns.md#u-0618) 해석 A: floor(h/2)
- [U-0618](unknowns.md#u-0618) 해석 B: ceil(h/2)
- [U-0618](unknowns.md#u-0618) 해석 C: h/2 (정확한 분수)
- [U-0618](unknowns.md#u-0618) 해결 방법: VOD: Protection 참가자가 Small potion을 마시는 장면.

## 페이지 사이의 모순

### C-0100

[C-0100](unknowns.md#c-0100): 소개 글은 Kick 라이브 중인 참가자가 10% 더 많은 피해를 준다고 하지만(모든 피해), 타격 파이프라인은 이 보너스를 공격자 본인의 무기 타격이라는 한정된 목록으로 제한합니다. 상태: `open`.

- [C-0100](unknowns.md#c-0100) `wiki-006`: "you take 10% less damage and do 10% more damage" ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 받는 피해는 10% 줄고 주는 피해는 10% 늘어납니다
- [C-0100](unknowns.md#c-0100) `wiki-damage-038`: "If the attacker is live on Kick, their own bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest and trapped gift hits deal 10% more, rounded down." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: 공격자가 Kick 라이브 중이면 본인의 bow, staff, knife, long sword, axe, machete, drone, C4, landmine, 가짜 상자, trapped gift 타격이 10% 더 큰 피해를 주며, 내림 처리됩니다.

### C-0101

[C-0101](unknowns.md#c-0101): Mirror 반사 목록에는 trapped gift가 없지만, 피해 표는 Trapped gift 행에 Mirror forcefield(반사)를 나열합니다. 상태: `open`.

- [C-0101](unknowns.md#c-0101) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (반사)
- [C-0101](unknowns.md#c-0101) `wiki-damage-070`: "It only reflects Poison Darts, fake gravestones, bows, wizard staffs, knives, long swords, Zarok's axes, machetes, drones, C4, landmines, flashbangs and fake chests, and never your own explosives." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Poison Dart, fake gravestone, bow, wizard staff, knife, long sword, Zarok's axe, machete, drone, C4, landmine, flashbang, 가짜 상자만 반사하며, 자신의 폭발물은 절대 반사하지 않습니다.

### C-0102

[C-0102](unknowns.md#c-0102): Body Armor는 '모든 종류의 피해에 작동한다'는 설명과, Trapped gift 행(Body armor 없음) 및 아이템 페이지('trapped gift는 이를 무시한다')가 충돌합니다. 상태: `open`.

- [C-0102](unknowns.md#c-0102) `wiki-damage-071`: "Body Armor works on every kind of damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Body Armor는 모든 종류의 피해에 작동합니다.
- [C-0102](unknowns.md#c-0102) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (반사)
- [C-0102](unknowns.md#c-0102) `wiki-items-027`: "A trapped gift ignores it." ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: trapped gift는 이를 무시합니다.

### C-0103

[C-0103](unknowns.md#c-0103): Death Ward의 범위: 피해 페이지는 서클 밖에서 오는 피해만 막지만, Death 시길 페이지는 언세이프 서클(unsafe circle)에서 오는 타격까지 추가하고 둘 모두에 대해 2min 동안 면역이라고 합니다(Unsafe circle 피해 표 행에도 Death Ward가 나열되어 있습니다). 상태: `open`.

- [C-0103](unknowns.md#c-0103) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Death Ward: Death 참가자가 서클 밖에서 받는 첫 타격은 차단되며, 서클 밖에서 오는 피해는 2min 동안 차단됩니다.
- [C-0103](unknowns.md#c-0103) `wiki-damage-006`: "| Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (둔화), Body armor (흡수)
- [C-0103](unknowns.md#c-0103) `wiki-sigils-death-013`: "Death ward: the first hit from outside the circle or from an unsafe circle is blocked and you are immune to both for 2min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
  - 번역: Death ward: 서클 밖 또는 언세이프 서클에서 오는 첫 타격이 차단되며, 둘 모두에 대해 2min 동안 면역입니다.

### C-0104

[C-0104](unknowns.md#c-0104): Sleeping Bag 면역: 피해 페이지에는 지연이 없고 존, 언세이프 서클, robot을 제외합니다. 상인 페이지는 65초의 수면이 필요하고, flashbang을 포함하며, 존과 언세이프 서클만 제외합니다. 상태: `open`.

- [C-0104](unknowns.md#c-0104) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 자신의 Sleeping Bag으로부터 15m(49ft) 이내에서 자고 있는 참가자는 존 피해, 언세이프 서클 피해, robot 피해를 제외한 모든 피해에 면역입니다.
- [C-0104](unknowns.md#c-0104) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 65초 동안 자고 나면 flashbang과, 존 피해 및 언세이프 서클 피해를 제외한 모든 피해에 면역입니다.

### C-0105

[C-0105](unknowns.md#c-0105): Healing 참가자의 부활: 소개 글은 어떤 참가자든 최대 2회까지 가능하다고 하지만, Healing 페이지는 묘비로부터 10m 이내에 살아 있는 참가자가 있어야 한다고 요구합니다. 상태: `open`.

- [C-0105](unknowns.md#c-0105) `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 어떤 참가자든 Healing 참가자를 최대 2회까지 부활시킬 수 있습니다.
- [C-0105](unknowns.md#c-0105) `wiki-sigils-healing-011`: "Any living contestant within 10m (33ft) of your gravestone can revive you, up to 2 times." ([출처](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
  - 번역: 묘비로부터 10m(33ft) 이내에 있는 살아 있는 참가자라면 누구든 최대 2회까지 당신을 부활시킬 수 있습니다.

### C-0200

[C-0200](unknowns.md#c-0200): 아이템 페이지는 trapped gift를 제외한 13가지 반사 가능 공격을 나열하지만, 피해 페이지 표는 Trapped gift 행에 Mirror forcefield(반사)를 나열합니다. 상태: `open`.

- [C-0200](unknowns.md#c-0200) `wiki-items-055`: "Only reflects Poison Darts, fake gravestones, knives, Zarok's axes, long swords, machetes, bows, staffs, drones, C4, landmines, flashbangs and fake chests." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: Poison Dart, fake gravestone, knife, Zarok's axe, long sword, machete, bow, staff, drone, C4, landmine, flashbang, 가짜 상자만 반사합니다.
- [C-0200](unknowns.md#c-0200) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (반사)

### C-0201

[C-0201](unknowns.md#c-0201): 아이템 페이지: trapped gift는 Body armor를 무시합니다. 피해 페이지: Body Armor는 모든 종류의 피해에 작동합니다. 상태: `open`.

- [C-0201](unknowns.md#c-0201) `wiki-items-027`: "A trapped gift ignores it." ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: trapped gift는 이를 무시합니다.
- [C-0201](unknowns.md#c-0201) `wiki-damage-071`: "Body Armor works on every kind of damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Body Armor는 모든 종류의 피해에 작동합니다.

### C-0202

[C-0202](unknowns.md#c-0202): 아이템 페이지의 Shield 예외에는 robot 피해가 없지만, 피해 페이지는 차단되지 않는 목록에 robot을 추가합니다. 상태: `open`.

- [C-0202](unknowns.md#c-0202) `wiki-items-023`: "Immune to damage for 20min, except zone damage and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/items#shield))
  - 번역: 20min 동안 피해에 면역이며, 존 피해와 언세이프 서클 피해는 예외입니다.
- [C-0202](unknowns.md#c-0202) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Shield는 존 피해, 언세이프 서클 피해, robot 피해를 막지 못합니다.

### C-0203

[C-0203](unknowns.md#c-0203): 아이템 페이지: 자고 있는 참가자는 flashbang에 면역입니다. 상인 페이지: 65초 동안 잔 뒤에만 면역입니다. 상태: `open`.

- [C-0203](unknowns.md#c-0203) `wiki-items-075`: "Sleeping contestants are immune." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 자고 있는 참가자는 면역입니다.
- [C-0203](unknowns.md#c-0203) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 65초 동안 자고 나면 flashbang과, 존 피해 및 언세이프 서클 피해를 제외한 모든 피해에 면역입니다.

### C-0204

[C-0204](unknowns.md#c-0204): 아이템 페이지: 취약 상태의 참가자는 Safety bubble의 보호를 받지 못합니다. 상인 페이지: Vulnerability Dart는 그들이 소유했거나 안에 서 있는 모든 Safety Bubble을 터뜨립니다. 상태: `open`.

- [C-0204](unknowns.md#c-0204) `wiki-items-021`: "It does not protect a vulnerable contestant, and you cannot use it while vulnerable." ([출처](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
  - 번역: 취약 상태의 참가자는 보호하지 못하며, 취약 상태에서는 사용할 수 없습니다.
- [C-0204](unknowns.md#c-0204) `wiki-merchant-017`: "It removes their Shield and pops every Safety Bubble they own or stand in, and stops Shields and Safety Bubbles protecting them for 10 minutes." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 그들의 Shield를 제거하고 그들이 소유했거나 안에 서 있는 모든 Safety Bubble을 터뜨리며, 10분 동안 Shield와 Safety Bubble이 그들을 보호하지 못하게 합니다.

### C-0205

[C-0205](unknowns.md#c-0205): 아이템 페이지: Zombie repellent는 좀비가 당신에게 피해를 주지 못하게 합니다. 좀비 페이지: 좀비가 당신을 무시합니다. 상태: `open`.

- [C-0205](unknowns.md#c-0205) `wiki-items-031`: "Use it to stop zombies hurting you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
  - 번역: 사용하면 20min 동안 좀비가 당신에게 피해를 주지 못합니다.
- [C-0205](unknowns.md#c-0205) `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/zombies#defence))
  - 번역: Zombie repellent: 사용하면 20min 동안 좀비가 당신을 무시합니다.

### C-0300

[C-0300](unknowns.md#c-0300): Sleeping Bag 면역 예외: 상인 페이지는 존 피해와 언세이프 서클 피해만 나열하지만, 피해 페이지는 robot 피해도 차단되지 않는 것으로 나열합니다. 상태: `open`.

- [C-0300](unknowns.md#c-0300) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 65초 동안 자고 나면 flashbang과, 존 피해 및 언세이프 서클 피해를 제외한 모든 피해에 면역입니다.
- [C-0300](unknowns.md#c-0300) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 자신의 Sleeping Bag으로부터 15m(49ft) 이내에서 자고 있는 참가자는 존 피해, 언세이프 서클 피해, robot 피해를 제외한 모든 피해에 면역입니다.

### C-0301

[C-0301](unknowns.md#c-0301): Sleeping Bag 면역 시점: 상인 페이지는 65초 동안 자고 난 뒤에만 면역을 부여합니다. 피해 페이지는 자신의 Sleeping Bag으로부터 15m 이내에서 자는 모든 참가자에게 지연 없이 부여합니다. 아이템 페이지는 자고 있는 참가자가 지연 없이 flashbang에 면역이라고 합니다. 상태: `open`.

- [C-0301](unknowns.md#c-0301) `wiki-merchant-023`: "After 65 seconds of sleep you are immune" ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 65초 동안 자고 나면 면역입니다
- [C-0301](unknowns.md#c-0301) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 자신의 Sleeping Bag으로부터 15m(49ft) 이내에서 자고 있는 참가자는 존 피해, 언세이프 서클 피해, robot 피해를 제외한 모든 피해에 면역입니다.
- [C-0301](unknowns.md#c-0301) `wiki-items-075`: "Sleeping contestants are immune." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 자고 있는 참가자는 면역입니다.

### C-0400

[C-0400](unknowns.md#c-0400): 차단 목록이 다릅니다. 공격 페이지는 최루 가스에 Gas mask, 건십 폭탄에 Flak jacket을 들지만, 피해 페이지는 같은 피해원에 대해 Shield, Safety bubble, Sleeping Bag, Body armor도 나열합니다. 상태: `open`.

- [C-0400](unknowns.md#c-0400) `wiki-attacks-025`: "A Gas mask blocks it." ([출처](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))
  - 번역: Gas mask가 이를 막습니다.
- [C-0400](unknowns.md#c-0400) `wiki-damage-009`: "| Tear gas | Shield, Safety bubble, Sleeping Bag, Gas mask, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 최루 가스 | Shield, Safety bubble, Sleeping Bag, Gas mask, Body armor (흡수)
- [C-0400](unknowns.md#c-0400) `wiki-attacks-041`: "A Flak jacket blocks one bomb." ([출처](https://iceposeidon.com/safezone/wiki/attacks#gunship))
  - 번역: Flak jacket은 폭탄 1개를 막습니다.
- [C-0400](unknowns.md#c-0400) `wiki-damage-027`: "| Gunship bomb | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | 건십 폭탄 | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (흡수)

### C-0401

[C-0401](unknowns.md#c-0401): 좀비 면역 목록에는 Necromancy가 없지만, Necromancy 페이지는 좀비에 완전히 면역이라고 합니다(피해 페이지에는 나열되어 있습니다). 상태: `open`.

- [C-0401](unknowns.md#c-0401) `wiki-zombies-018`: "A Shield, a Safety bubble, a Reality Shield or sleeping in your own Sleeping Bag makes you immune." ([출처](https://iceposeidon.com/safezone/wiki/zombies#defence))
  - 번역: Shield, Safety bubble, Reality Shield, 또는 자신의 Sleeping Bag에서 자는 것으로 면역이 됩니다.
- [C-0401](unknowns.md#c-0401) `wiki-sigils-necromancy-016`: "Fully immune from zombies." ([출처](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
  - 번역: 좀비에 완전히 면역입니다.
- [C-0401](unknowns.md#c-0401) `wiki-damage-010`: "| Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (흡수)

### C-0402

[C-0402](unknowns.md#c-0402): Repellent 효과: 좀비가 '당신을 무시한다'(대상 지정)와 '좀비가 당신에게 피해를 주지 못한다'(피해만) 사이의 차이입니다. 상태: `open`.

- [C-0402](unknowns.md#c-0402) `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/zombies#defence))
  - 번역: Zombie repellent: 사용하면 20min 동안 좀비가 당신을 무시합니다.
- [C-0402](unknowns.md#c-0402) `wiki-items-031`: "Use it to stop zombies hurting you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
  - 번역: 사용하면 20min 동안 좀비가 당신에게 피해를 주지 못합니다.

### C-0403

[C-0403](unknowns.md#c-0403): 보급 상자의 Trolling 유도: 모든 보급 상자에 대해 'Trolling 참가자로부터 5m 이내'라고 하는 반면, Trolling 페이지는 '바로 옆'이라고 하며 '시청자가 보낸' 것만 해당합니다. 상태: `open`.

- [C-0403](unknowns.md#c-0403) `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([출처](https://iceposeidon.com/safezone/wiki/attacks#care-package))
  - 번역: 대신 Trolling 참가자로부터 5m(16ft) 이내에 떨어질 확률이 3%입니다.
- [C-0403](unknowns.md#c-0403) `wiki-sigils-trolling-020`: "Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 시청자가 보낸 각 crate 또는 보급 상자는 대신 Trolling 참가자 바로 옆에 떨어질 확률이 3%입니다.

### C-0404

[C-0404](unknowns.md#c-0404): 조합 파괴: 좀비 페이지는 '조합한 아이템'이라고 하지만, Ingenuity 페이지는 '좀비 타격'으로 파괴되는 것을 '고유 조합'으로만 한정합니다. 상태: `open`.

- [C-0404](unknowns.md#c-0404) `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([출처](https://iceposeidon.com/safezone/wiki/zombies))
  - 번역: 조합한 아이템을 파괴할 확률 40%
- [C-0404](unknowns.md#c-0404) `wiki-sigils-ingenuity-012`: "Unique crafts cannot be traded, stolen or looted, and have a 40% chance to be destroyed by Zombie hits." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 고유 조합은 거래, 도난, 루팅이 불가능하며 좀비 타격으로 파괴될 확률이 40%입니다.

### C-0500

[C-0500](unknowns.md#c-0500): Ingenuity 페이지: Shield와 Sleeping Bag이 Robot을 막습니다. 피해 페이지: Shield는 robot 피해를 막지 못하며 자고 있는 참가자도 robot 피해에 면역이 아닙니다. 상태: `open`.

- [C-0500](unknowns.md#c-0500) `wiki-sigils-ingenuity-016`: "Shields and Sleeping Bags stop it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
  - 번역: Shield와 Sleeping Bag이 이를 막습니다.
- [C-0500](unknowns.md#c-0500) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Shield는 존 피해, 언세이프 서클 피해, robot 피해를 막지 못합니다.
- [C-0500](unknowns.md#c-0500) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 자신의 Sleeping Bag으로부터 15m(49ft) 이내에서 자고 있는 참가자는 존 피해, 언세이프 서클 피해, robot 피해를 제외한 모든 피해에 면역입니다.

### C-0501

[C-0501](unknowns.md#c-0501): Trolling 페이지: 시청자가 보낸 crate와 보급 상자가 3% 유도 판정을 합니다. 공격 페이지: 보급 상자만 판정하며(착지 거리 5 m), crate는 별개의 아이템입니다. 상태: `open`.

- [C-0501](unknowns.md#c-0501) `wiki-sigils-trolling-020`: "Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 시청자가 보낸 각 crate 또는 보급 상자는 대신 Trolling 참가자 바로 옆에 떨어질 확률이 3%입니다.
- [C-0501](unknowns.md#c-0501) `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([출처](https://iceposeidon.com/safezone/wiki/attacks#care-package))
  - 번역: 대신 Trolling 참가자로부터 5m(16ft) 이내에 떨어질 확률이 3%입니다.
- [C-0501](unknowns.md#c-0501) `wiki-attacks-081`: "A crate holds an item bought by a viewer." ([출처](https://iceposeidon.com/safezone/wiki/attacks#care-package))
  - 번역: crate에는 시청자가 구매한 아이템이 들어 있습니다.

### C-0502

[C-0502](unknowns.md#c-0502): Trolling 페이지: Reality Shield는 언세이프 서클 피해를 막습니다. 언세이프 서클의 피해 표 행에는 Reality Shield가 없습니다(같은 페이지의 참고 사항(notes)에는 포함되어 있습니다). 상태: `open`.

- [C-0502](unknowns.md#c-0502) `wiki-sigils-trolling-027`: "A Guardian angel, a Safety bubble, a Reality Shield or a Death Ward blocks it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: Guardian angel, Safety bubble, Reality Shield, 또는 Death Ward가 이를 막습니다.
- [C-0502](unknowns.md#c-0502) `wiki-damage-006`: "Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (둔화), Body armor (흡수)
- [C-0502](unknowns.md#c-0502) `wiki-damage-059`: "A Safety bubble and a Reality Shield do." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Safety bubble과 Reality Shield는 막습니다.

### C-0503

[C-0503](unknowns.md#c-0503): Trolling 페이지: 한 조항은 방어 아이템 손실이 첫 타격 조건 없이 5초마다 일어난다고 하고, 다른 조항은 첫 타격 이후에 시작되며 면역이 아니어야 한다고 합니다. 상태: `open`.

- [C-0503](unknowns.md#c-0503) `wiki-sigils-trolling-017`: "loses one defense item or unique craft every five seconds, equipped Body Armor included" ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 5초마다 방어 아이템 또는 고유 조합 1개를 잃으며, 장착한 Body Armor도 포함됩니다
- [C-0503](unknowns.md#c-0503) `wiki-sigils-trolling-024`: "After your first hit, you lose one random defense item or unique craft every five seconds while you stay inside and are not immune." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: 첫 타격 이후, 안에 머물러 있고 면역이 아닌 동안 5초마다 무작위 방어 아이템 또는 고유 조합 1개를 잃습니다.

### C-0600

[C-0600](unknowns.md#c-0600): Death ward: 시길 페이지는 서클 밖 또는 언세이프 서클에서 오는 첫 타격을 막고 둘 모두에 2min 동안 면역을 주지만, 피해 페이지 본문은 서클 밖에서 오는 피해만 언급합니다(피해 표는 두 행 모두에 Death Ward를 나열합니다). 상태: `open`.

- [C-0600](unknowns.md#c-0600) `wiki-sigils-death-013`: "Death ward: the first hit from outside the circle or from an unsafe circle is blocked and you are immune to both for 2min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
  - 번역: Death ward: 서클 밖 또는 언세이프 서클에서 오는 첫 타격이 차단되며, 둘 모두에 대해 2min 동안 면역입니다.
- [C-0600](unknowns.md#c-0600) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Death Ward: Death 참가자가 서클 밖에서 받는 첫 타격은 차단되며, 서클 밖에서 오는 피해는 2min 동안 차단됩니다.
- [C-0600](unknowns.md#c-0600) `wiki-damage-006`: "| Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (둔화), Body armor (흡수)

### C-0601

[C-0601](unknowns.md#c-0601): Protection 면역: 능력치 카드는 독, drone, 미사일, C4, landmine, 공습, 건십을 나열하지만, 규칙 문장과 피해 표는 trapped gift, 공습의 불, Protection 보복을 추가합니다. 상태: `open`.

- [C-0601](unknowns.md#c-0601) `wiki-sigils-protection-007`: "Poison, drones, missiles, C4, landmines, airstrikes, gunships" ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection))
  - 번역: 독, drone, 미사일, C4, landmine, 공습, 건십
- [C-0601](unknowns.md#c-0601) `wiki-sigils-protection-008`: "Immune to poison, drones, missiles, C4, landmines, trapped gifts, airstrikes and their fire, gunship bombs and Protection retribution." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 독, drone, 미사일, C4, landmine, trapped gift, 공습과 그 불, 건십 폭탄, Protection 보복에 면역입니다.
- [C-0601](unknowns.md#c-0601) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (반사)

### C-0602

[C-0602](unknowns.md#c-0602): Protection 전략 조언은 '대부분의 시청자 공격'에 면역이라고 하지만, 시길 페이지와 공격 페이지는 시청자 공격 8종 중 미사일, 공습, 건십에만 Protection이 면역이라고 합니다(nuke는 절반). 상태: `open`.

- [C-0602](unknowns.md#c-0602) `wiki-strategy-006`: "If you are unpopular with viewers, consider picking the Protection sigil, so you are immune from most viewer attacks." ([출처](https://iceposeidon.com/safezone/wiki/strategy#sigils))
  - 번역: 시청자에게 인기가 없다면 Protection 시길을 고르는 것을 고려해 보십시오. 그러면 대부분의 시청자 공격에 면역이 됩니다.
- [C-0602](unknowns.md#c-0602) `wiki-sigils-protection-008`: "Immune to poison, drones, missiles, C4, landmines, trapped gifts, airstrikes and their fire, gunship bombs and Protection retribution." ([출처](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
  - 번역: 독, drone, 미사일, C4, landmine, trapped gift, 공습과 그 불, 건십 폭탄, Protection 보복에 면역입니다.
- [C-0602](unknowns.md#c-0602) `wiki-attacks-001`: "While a contestant's EMP is active, viewers cannot send missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes or bounties." ([출처](https://iceposeidon.com/safezone/wiki/attacks#emp))
  - 번역: 참가자의 EMP가 활성화된 동안 시청자는 미사일, 핵, 호드, 최루 가스, 공습, 건십, 사이클롭스, 현상금을 보낼 수 없습니다.
