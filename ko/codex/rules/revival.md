# 규칙: 부활(revival)

## 요약

`revival` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

부활 계열은 참가자가 죽을 때 어떤 일이 일어나는지, 그리고 돌아올 수 있는지를 다룹니다. 여기서 죽음이 항상 끝은 아니지만, 시간은 짧고 몇 가지가 그것을 영구히 닫을 수 있습니다.

죽으면 마지막으로 확인된 위치에 아이템이 담긴 묘비가 나타납니다 ([M-0107](../rules/revival.md#m-0107)). 다른 참가자는 이를 루팅하거나, 죽은 지 10분 이내에 당신을 부활시킬 수 있습니다 ([M-0108](../rules/revival.md#m-0108)). 무덤 안의 블러드 토큰은 부활이 가능한 동안 잠겨 있습니다 ([M-0109](../rules/revival.md#m-0109)). 부활이 일어나면 부활한 참가자는 묘비에 아직 남은 아이템을 돌려받고 ([M-0114](../rules/revival.md#m-0114)), 들어가지 않는 아이템은 묘비에 남습니다 ([M-0115](../rules/revival.md#m-0115)).

누가 부활시킬 수 있는지는 Healing 시길과 연결되어 있습니다. Healing 참가자는 어떤 시길의 참가자든 최대 10회까지 부활시킬 수 있습니다 ([M-0113](../rules/revival.md#m-0113), [M-0654](../rules/revival.md#m-0654)). 이는 죽은 지 10분 이내에 이루어져야 하며 ([M-0655](../rules/revival.md#m-0655)), 부활시키는 사람은 5 HP를 소모하고 부활한 참가자는 5 HP로 돌아옵니다 ([M-0656](../rules/revival.md#m-0656)). 반대로, Healing 참가자의 묘비에서 10 m (33 ft) 이내에 있는 살아 있는 참가자는 누구나 그를 최대 2회까지 부활시킬 수 있습니다 ([M-0112](../rules/revival.md#m-0112), [M-0653](../rules/revival.md#m-0653)).

이를 끝내는 것: Death 시길 플레이어가 당신의 묘비를 약탈하거나 가장 먼저 루팅하면, 당신은 다시는 부활할 수 없습니다 ([M-0116](../rules/revival.md#m-0116)). 각 묘비는 한 번만 약탈할 수 있고, 약탈당한 묘비는 영영 부활시킬 수 없습니다 ([M-0612](../rules/revival.md#m-0612)). 따라서 플레이어의 관점에서 10분의 시간은 Death 플레이어에 의해 단축될 수 있으며, 그가 도착하기 전에 부활하는 것이 희망입니다 ([M-0116](../rules/revival.md#m-0116)).

기재된 바에 따른 가장 강한 점: Healing 시길의 부활자는 어떤 시길이든 되살릴 수 있습니다 ([M-0113](../rules/revival.md#m-0113)). 가장 약한 점: 부활시키는 사람의 비용 ([M-0656](../rules/revival.md#m-0656)), 짧은 시간 ([M-0655](../rules/revival.md#m-0655)), Death에 의한 영구 차단 ([M-0116](../rules/revival.md#m-0116))입니다.

알 수 없는 것: 누구의 죽음이 10분의 시간을 시작하는지 ([U-0011](../unknowns.md#u-0011)), 그리고 Healing 참가자가 아닌 사람이 Healing이 아닌 참가자를 부활시킬 수 있는지 ([U-0108](../unknowns.md#u-0108))입니다. 2회와 10회의 제한이 무엇에 붙어 있는지도 미해결입니다 ([U-0107](../unknowns.md#u-0107), [U-0624](../unknowns.md#u-0624)). 위키는 Healing 부활 제한도 두 페이지에서 다르게 서술합니다 ([C-0105](../unknowns.md#c-0105)). 잠긴 토큰이 얼마나 오래 잠겨 있는지, 잠금이 끝나면 어떻게 되는지도 미해결입니다 ([U-0105](../unknowns.md#u-0105)). 아이템이 돌아올 때의 용량 규칙이 무엇인지 ([U-0109](../unknowns.md#u-0109)), 무덤이 죽은 장소인지 마지막 GPS 위치인지 ([U-0124](../unknowns.md#u-0124)), 5 HP 비용이 부활시키는 사람을 죽일 수 있는지 ([U-0625](../unknowns.md#u-0625))도 미해결입니다.

이 페이지는 규칙 13개(2 `DOCUMENTED`, 11 `CONDITIONAL`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0107"></a>

### M-0107: 사망 시 묘비 생성

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0107](../rules/revival.md#m-0107) `wiki-007`: "When you die, a gravestone with your items appears where you were last seen." ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 죽으면 마지막으로 목격된 위치에 아이템이 담긴 묘비가 나타납니다.
- [M-0107](../rules/revival.md#m-0107) `wiki-011`: "When you die, you leave behind a gravestone containing any items you had." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 죽으면 가지고 있던 모든 아이템이 담긴 묘비를 남깁니다.

**형식 모델:**

- [M-0107](../rules/revival.md#m-0107) 해석 A: `사망 시: gravestone(pos = 사망 시점의 위치, items = 소지한 모든 아이템)`
- [M-0107](../rules/revival.md#m-0107) 해석 B: `gravestone(pos = 사망 전 마지막 GPS 측위)`
- [M-0107](../rules/revival.md#m-0107) 정의역: 모든 참가자

**미해결 질문:**

- [U-0124](../unknowns.md#u-0124) (낮음): 묘비 위치 'where you were last seen': 사망 순간의 위치입니까, 마지막으로 수신된 GPS 위치입니까?

메모 ([M-0107](../rules/revival.md#m-0107)): 두 문장은 같은 규칙입니다 (소개 부분과 Death/Revival 절). 묘비 속 블러드 토큰은 [M-0109](../rules/revival.md#m-0109)에서 다룹니다.

<a id="m-0108"></a>

### M-0108: 10 min 이내에 묘비를 루팅하거나 부활시킴

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0108](../rules/revival.md#m-0108) `wiki-008`: "Other contestants can loot it, or revive you within 10min of their death." ([출처](https://iceposeidon.com/safezone/wiki#damage))
  - 번역: 다른 참가자는 이를 루팅하거나, 그들의 사망 후 10min 이내에 당신을 부활시킬 수 있습니다.

**형식 모델:**

- [M-0108](../rules/revival.md#m-0108) 해석 A: `t - t_death <= 600 s인 동안 부활 가능 (t_death는 사망한 참가자의 사망 시각)`
- [M-0108](../rules/revival.md#m-0108) 해석 B: `시간 창을 부활시키는 쪽의 사망 시점부터 계산 (대명사를 문자 그대로 읽은 경우)`
- [M-0108](../rules/revival.md#m-0108) 정의역: t, t_death는 초 단위
- [M-0108](../rules/revival.md#m-0108) 매개변수 `revive_window_s`: 600

**미해결 질문:**

- [U-0011](../unknowns.md#u-0011) (보통): 부활 제한 시간: 소개 페이지의 'within 10min of their death'와 Healing 페이지의 'within 10min of the death' 중, 누구의 사망이 제한 시간을 시작시킵니까?
- [U-0108](../unknowns.md#u-0108) (보통): 비Healing 참가자는 누가 부활시킬 수 있습니까? 두 규칙에서 암시되는 대로 Healing 참가자만입니까, 아니면 다른 규칙에 따라 누구든 가능합니까?

메모 ([M-0108](../rules/revival.md#m-0108)): Healing 페이지에는 '사망 후 10min 이내'라고 되어 있으며 같은 600 s입니다. 시길별 부활 규칙(5 HP 비용, 10 m 범위)은 Healing 페이지에 있으며 여기에 중복 기록하지 않았습니다.

<a id="m-0109"></a>

### M-0109: 묘비 속 블러드 토큰은 부활이 가능한 동안 잠김

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0109](../rules/revival.md#m-0109) `wiki-012`: "Blood tokens in the grave stay locked while revival is possible." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 묘비 속 블러드 토큰은 부활이 가능한 동안 잠긴 상태로 유지됩니다.

**형식 모델:**

- [M-0109](../rules/revival.md#m-0109) 해석 A: `locked(tokens) = revival_possible(grave); 그 이후에는 잠금 해제`
- [M-0109](../rules/revival.md#m-0109) 해석 B: `부활될 때까지 잠김, 상한 기준으로 부활이 여전히 가능하면 600 s가 지나도 유지`

**미해결 질문:**

- [U-0105](../unknowns.md#u-0105) (보통): 'Blood tokens in the grave stay locked while revival is possible': 누구의 토큰이며, 얼마 동안이고, 잠금이 끝나면 어떻게 됩니까?
- [U-0011](../unknowns.md#u-0011) (보통): 부활 제한 시간: 소개 페이지의 'within 10min of their death'와 Healing 페이지의 'within 10min of the death' 중, 누구의 사망이 제한 시간을 시작시킵니까?
- [U-0107](../unknowns.md#u-0107) (높음): 부활 횟수 제한 '2 times'(Healing 참가자에게)와 '10 times'(Healing 참가자에 의한)는 무엇에 붙는 카운터입니까?

메모 ([M-0109](../rules/revival.md#m-0109)): '부활 가능'은 시간 창, 부활 횟수 상한, Death 시길의 약탈 규칙([M-0116](../rules/revival.md#m-0116))에 따라 달라집니다.

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

메모 ([M-0112](../rules/revival.md#m-0112)): Healing 페이지는 '당신의 묘비로부터 10m 이내의 살아 있는 참가자'를 덧붙이고 '... 최대 10회까지 부활시킬 수 있다'고 하므로 [C-0104](../unknowns.md#c-0104)를 참조하십시오. 시길별 세부 사항은 비교만 하고 중복 기록하지 않았습니다.

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

<a id="m-0114"></a>

### M-0114: 부활한 참가자는 묘비에 남아 있는 아이템을 되돌려 받음

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0114](../rules/revival.md#m-0114) `wiki-017`: "The revived contestant gets back the items still in their gravestone." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 부활한 참가자는 묘비에 아직 남아 있는 아이템을 되돌려 받습니다.

**형식 모델:**

- [M-0114](../rules/revival.md#m-0114) 해석 A: `부활 시: inventory := items(grave), 수용량 한도 적용 ([M-0115](../rules/revival.md#m-0115)); 묘비의 아이템은 제거됨`

**상호작용:** [M-0107](../rules/revival.md#m-0107)

**미해결 질문:**

- [U-0109](../unknowns.md#u-0109) (낮음): 'Items that do not fit stay in the gravestone': 부활 시 용량 규칙은 무엇이며, 묘비에 남은 아이템은 이후 어떻게 됩니까?
- [U-0105](../unknowns.md#u-0105) (보통): 'Blood tokens in the grave stay locked while revival is possible': 누구의 토큰이며, 얼마 동안이고, 잠금이 끝나면 어떻게 됩니까?

메모 ([M-0114](../rules/revival.md#m-0114)): 남아 있는 아이템만 반환됩니다. 부활 전에 루팅한 쪽이 가져간 아이템은 사라집니다.

<a id="m-0115"></a>

### M-0115: 들어가지 않는 아이템은 묘비에 남음

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0115](../rules/revival.md#m-0115) `wiki-018`: "Items that do not fit stay in the gravestone." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: 들어가지 않는 아이템은 묘비에 남습니다.

**형식 모델:**

- [M-0115](../rules/revival.md#m-0115) 해석 A: `leftover = items(grave) 중 들어가는 부분집합을 뺀 나머지; leftover는 묘비에 남음`
- [M-0115](../rules/revival.md#m-0115) 해석 B: `leftover는 바닥에 떨어짐`
- [M-0115](../rules/revival.md#m-0115) 매개변수 `inventory_capacity`: UNKNOWN, [U-0109](../unknowns.md#u-0109) 참조

**상호작용:** [M-0114](../rules/revival.md#m-0114)

**미해결 질문:**

- [U-0109](../unknowns.md#u-0109) (낮음): 'Items that do not fit stay in the gravestone': 부활 시 용량 규칙은 무엇이며, 묘비에 남은 아이템은 이후 어떻게 됩니까?

<a id="m-0116"></a>

### M-0116: Death 시길이 묘비를 약탈하거나 처음 루팅하면 부활 불가

라벨: `DOCUMENTED`. 시길: death.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0116](../rules/revival.md#m-0116) `wiki-019`: "If a Sigil of death player robs your gravestone, or is the first to loot it, you can never be revived." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: Sigil of death 플레이어가 당신의 묘비를 약탈하거나 처음으로 루팅하면, 당신은 영영 부활할 수 없습니다.

**형식 모델:**

- [M-0116](../rules/revival.md#m-0116) 해석 A: `Death 참가자가 묘비를 약탈하거나 그 첫 루팅자가 되면 revivable(grave) = false가 영구히 성립`

메모 ([M-0116](../rules/revival.md#m-0116)): Death 시길 페이지('각 묘비는 한 번 약탈될 수 있으며, 약탈된 묘비는 영영 부활할 수 없다', '묘비에서 아이템이나 블러드 토큰을 처음 루팅하면 그 묘비도 약탈한 것이 된다')와 대조했으며, 같은 규칙이고 불일치는 발견되지 않았습니다. 시길별 세부 사항은 중복 기록하지 않았습니다.

<a id="m-0612"></a>

### M-0612: 약탈된 묘비: 1회뿐이며 부활 불가

라벨: `DOCUMENTED`. 시길: death.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0612](../rules/revival.md#m-0612) `wiki-sigils-death-010`: "Each gravestone can be robbed once, and a robbed gravestone can never be revived." ([출처](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
  - 번역: 각 묘비는 한 번만 약탈할 수 있으며, 약탈된 묘비는 다시는 부활시킬 수 없습니다.
- [M-0612](../rules/revival.md#m-0612) `wiki-019`: "If a Sigil of death player robs your gravestone, or is the first to loot it, you can never be revived." ([출처](https://iceposeidon.com/safezone/wiki#death))
  - 번역: Sigil of death 플레이어가 당신의 묘비를 약탈하거나 가장 먼저 루팅하면, 당신은 다시는 부활할 수 없습니다.

**형식 모델:**

- [M-0612](../rules/revival.md#m-0612) 해석 A: `robbed(g)는 되돌릴 수 없는 플래그. robbed(g)이면 revivable(g)은 영구히 거짓`
- [M-0612](../rules/revival.md#m-0612) 정의역: 묘비 g

**상호작용:** [M-0611](../rules/sigil.md#m-0611)

메모 ([M-0612](../rules/revival.md#m-0612)): 개요 페이지와 Death 페이지는 일치합니다. 소개 페이지는 '약탈하거나 ... 가장 먼저 루팅'이라고 하고, Death 페이지는 아이템이나 토큰을 처음 루팅하면 약탈로 친다고 합니다.

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
  - 번역: 그들의 사망 후 10min 이내에 당신을 부활시킬 수 있습니다.

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
- [U-0002](../unknowns.md#u-0002) (치명적): 어떤 피해 원천이 7단계 타격 파이프라인을 거칩니까(존 틱, 독, 출혈, 좀비 드레인(drain), 가드 좀비, 로봇, 언세이프 서클(unsafe circle), Eddie의 손실, 부활 비용, Retribution)?

메모 ([M-0656](../rules/revival.md#m-0656)): 부활한 참가자는 묘비에서 아이템도 되찾습니다(소개 페이지). 비용이 피해 파이프라인을 거치는지는 [U-0002](../unknowns.md#u-0002)입니다.

## 시뮬레이션 검증

아직 이 페이지를 다루는 정리나 시뮬레이션이 없습니다.

## 미해결 질문

[U-0002](../unknowns.md#u-0002), [U-0011](../unknowns.md#u-0011), [U-0105](../unknowns.md#u-0105), [U-0107](../unknowns.md#u-0107), [U-0108](../unknowns.md#u-0108), [U-0109](../unknowns.md#u-0109), [U-0124](../unknowns.md#u-0124), [U-0624](../unknowns.md#u-0624), [U-0625](../unknowns.md#u-0625), [U-0626](../unknowns.md#u-0626)

## 신뢰도

`CONDITIONAL`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
