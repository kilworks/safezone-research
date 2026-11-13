# 규칙: 아이템(items)

## 요약

`items` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.

### 쉬운 말로

아이템 계열은 도구 상자입니다. 무엇을 들 수 있는지, 각 아이템이 무엇을 하는지, 얼마나 오래 지속되는지를 다룹니다. 대부분은 방어이고, 몇 가지 요령이 더해집니다.

먼저 공간입니다. 아이템은 최대 3개까지 들 수 있고, C4, Landmine, Arrow처럼 중첩되는 것도 있습니다 ([M-0200](../rules/items.md#m-0200), [M-0201](../rules/items.md#m-0201)). 동시에 활성화할 수 있는 아이템 효과는 최대 3개이며, 한계에 이르면 아이템은 거부되고 그대로 보유합니다 ([M-0203](../rules/items.md#m-0203), [M-0204](../rules/items.md#m-0204)). Shield, Guardian angel, Mirror forcefield, Anti poison 면역, Flak jacket, Gas mask, Zombie repellent, 소지 중인 Hazmat suit가 이 상한에 포함되고 ([M-0205](../rules/items.md#m-0205)), Safety bubble, 연막탄, 붕대, 조합품, 상인 업그레이드는 포함되지 않습니다 ([M-0206](../rules/items.md#m-0206)).

방어 수단마다 전문 분야가 있습니다. Shield는 20분 동안 면역을 주지만 취약한 동안에는 사용할 수 없습니다 ([M-0215](../rules/items.md#m-0215)). Safety bubble은 안에 있는 모든 사람을 피해와 좀비에 면역으로 만들며 존 피해도 포함되고 ([M-0213](../rules/items.md#m-0213)), 지속 시간은 10분입니다 ([M-0212](../rules/items.md#m-0212)). Guardian angel은 10분 동안 존 피해에 대한 면역을 줍니다 ([M-0210](../rules/items.md#m-0210)). Mirror forcefield는 다음 공격을 공격자에게 반사하며 ([M-0235](../rules/items.md#m-0235)), 그것으로 소모됩니다 ([M-0134](../rules/items.md#m-0134)). Flak jacket은 다음 미사일, 핵, 공습 충격, 건십 폭탄을 막고 ([M-0130](../rules/items.md#m-0130)), Gas mask는 최루 가스를 막습니다 ([M-0131](../rules/items.md#m-0131)). Body armor는 일정량의 피해를 흡수합니다 ([M-0217](../rules/items.md#m-0217)). Sleeping Bag은 그 주변 15 m 이내에서 자는 사람을 보호합니다 ([M-0132](../rules/items.md#m-0132)).

요령: 섬광탄은 30 m 이내의 다른 모든 참가자를 30초 동안 눈멀게 하고 ([M-0244](../rules/items.md#m-0244)), 연막탄은 지도를 가리고 50 m 이내의 공격을 20분 동안 막습니다 ([M-0226](../rules/items.md#m-0226)). 열화상 고글은 연기를 투시하고 ([M-0231](../rules/items.md#m-0231)) 환영 복제본을 복제본으로 보여 줍니다 ([M-0232](../rules/items.md#m-0232)).

효과적인 대상: 폭발물에는 Flak jacket ([M-0130](../rules/items.md#m-0130)), 최루 가스에는 Gas mask ([M-0131](../rules/items.md#m-0131)), 무기 타격에는 Mirror ([M-0235](../rules/items.md#m-0235))입니다.

가장 약한 점: Mirror는 목록에 있는 것만 반사하며 시청자나 관리자의 공격, 존, 좀비는 절대 반사하지 않습니다 ([M-0241](../rules/items.md#m-0241)).

알 수 없는 것과 위키가 모순되는 부분: Shield 제외 대상 ([M-0216](../rules/items.md#m-0216), [C-0202](../unknowns.md#c-0202)), 함정 선물이 Body armor를 무시하는지 ([M-0218](../rules/items.md#m-0218), [C-0201](../unknowns.md#c-0201)), Mirror의 목록 ([M-0237](../rules/items.md#m-0237), [C-0200](../unknowns.md#c-0200)), 자는 동안의 섬광탄 면역 ([M-0246](../rules/items.md#m-0246), [C-0203](../unknowns.md#c-0203)), 취약한 플레이어에 대한 Safety bubble ([M-0214](../rules/items.md#m-0214), [C-0204](../unknowns.md#c-0204)), Zombie repellent가 하는 일 ([M-0220](../rules/items.md#m-0220), [C-0205](../unknowns.md#c-0205))입니다. 미해결: 여러 Mirror가 어떻게 동작하는지 ([U-0215](../unknowns.md#u-0215)), Body armor 풀이 소진되는지 ([U-0209](../unknowns.md#u-0209)), 두 번째 방어구가 하는 일 ([U-0210](../unknowns.md#u-0210))입니다. 또한 미해결: Safety bubble의 10 m가 반지름인지 지름인지 ([U-0208](../unknowns.md#u-0208))와 어떤 다른 아이템이 중첩되는지 ([U-0200](../unknowns.md#u-0200))입니다.

이 페이지는 규칙 67개(21 `DOCUMENTED`, 40 `CONDITIONAL`, 6 `CONTRADICTED`)를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.

## 규칙

<a id="m-0126"></a>

### M-0126: Body armor의 적용 범위: 모든 종류의 피해, 한 개만 소지 가능

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0126](../rules/items.md#m-0126) `wiki-damage-071`: "Body Armor works on every kind of damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Body Armor는 모든 종류의 피해에 적용됩니다.
- [M-0126](../rules/items.md#m-0126) `wiki-damage-072`: "You can carry only one." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 한 개만 소지할 수 있습니다.

**형식 모델:**

- [M-0126](../rules/items.md#m-0126) 해석 A: `armor는 표에 '(absorbs)'로 표시된 모든 피해 원천에 적용됨`
- [M-0126](../rules/items.md#m-0126) 해석 B: `armor는 예외 없이 모든 원천에 적용됨 (문자 그대로)`
- [M-0126](../rules/items.md#m-0126) 매개변수 `max_carried`: 1

**미해결 질문:**

- [U-0122](../unknowns.md#u-0122) (보통): Wiki-damage-002는 'Reality Shield block every kind of damage. absorbs every kind of damage.'(뒤섞임)로 되어 있습니다: 어느 문장이 어느 아이템의 것입니까(Reality Shield는 모든 종류를 막고, Body armor는 모든 종류를 흡수)?

**모순:** [C-0102](../unknowns.md#c-0102)

메모 ([M-0126](../rules/items.md#m-0126)): 표의 Trapped gift 행에는 'Body armor' 항목이 없고, 아이템 페이지에는 'A trapped gift ignores it'라고 되어 있습니다: [C-0102](../unknowns.md#c-0102).

<a id="m-0127"></a>

### M-0127: Reality Shield와 Body armor 페이지 첫머리 문장 (뒤섞임)

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0127](../rules/items.md#m-0127) `wiki-damage-002`: "Reality Shield block every kind of damage. absorbs every kind of damage." ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: Reality Shield 모든 종류의 피해를 막습니다. 모든 종류의 피해를 흡수합니다.

**형식 모델:**

- [M-0127](../rules/items.md#m-0127) 해석 A: `Reality Shield: 모든 종류의 피해를 막음; Body armor: 모든 종류의 피해를 흡수함`

**미해결 질문:**

- [U-0122](../unknowns.md#u-0122) (보통): Wiki-damage-002는 'Reality Shield block every kind of damage. absorbs every kind of damage.'(뒤섞임)로 되어 있습니다: 어느 문장이 어느 아이템의 것입니까(Reality Shield는 모든 종류를 막고, Body armor는 모든 종류를 흡수)?

메모 ([M-0127](../rules/items.md#m-0127)): 이 문장은 스냅샷에서 깨져 있습니다 ('Reality Shield block every kind of damage. absorbs every kind of damage.'). 표에는 Reality Shield 열이 없습니다.

<a id="m-0130"></a>

### M-0130: Flak jacket은 다음 미사일, 핵, 공습 충격, 건십 폭탄을 막고 소모됨

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0130](../rules/items.md#m-0130) `wiki-damage-063`: "A Flak jacket blocks the next missile, nuke, airstrike impact or gunship bomb, then is used up." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Flak jacket은 다음 미사일, 핵, 공습 충격 또는 건십 폭탄을 막고 소모됩니다.
- [M-0130](../rules/items.md#m-0130) `wiki-damage-064`: "It does not block airstrike fire." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 공습 화재는 막지 못합니다.
- [M-0130](../rules/items.md#m-0130) `wiki-damage-065`: "A hit already blocked by something else does not use it up." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 이미 다른 것에 의해 막힌 타격은 이를 소모시키지 않습니다.

**형식 모델:**

- [M-0130](../rules/items.md#m-0130) 해석 A: `source in {missile, nuke, airstrike impact, gunship bomb}이고 jacket 보유 중이며 다른 차단 수단이 적용되지 않았으면: d := 0 이고 jacket 소모됨; 공습 화재는 막지 못함`

**상호작용:** [M-0118](../rules/damage.md#m-0118)

**미해결 질문:**

- [U-0120](../unknowns.md#u-0120) (높음): 한 번의 타격에 여러 방어 수단(Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection)이 적용될 때, 어느 것이 'blocker'이고 어떤 아이템이 소모됩니까? 명시된 유일한 규칙은 'a hit already blocked by something else does not use [the Flak jacket] up'입니다.

메모 ([M-0130](../rules/items.md#m-0130)): 표의 행과 일치합니다 (미사일, 핵, 공습 충격, 건십 폭탄에는 Flak jacket이 있고, 공습 화재에는 없음).

<a id="m-0131"></a>

### M-0131: Gas mask는 최루 가스를 막음

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0131](../rules/items.md#m-0131) `wiki-damage-066`: "A Gas mask blocks tear gas." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Gas mask는 최루 가스를 막습니다.

**형식 모델:**

- [M-0131](../rules/items.md#m-0131) 해석 A: `blocks(Gas mask)는 최루 가스를 포함함`

메모 ([M-0131](../rules/items.md#m-0131)): 최루 가스 행과 일치합니다.

<a id="m-0132"></a>

### M-0132: Sleeping Bag 면역: 자신의 Sleeping Bag에서 15 m 이내이면 존, 언세이프 서클(unsafe circle), robot을 제외한 모든 피해에 면역

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0132](../rules/items.md#m-0132) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: 자신의 Sleeping Bag에서 15m (49ft) 이내에서 자고 있는 참가자는 존, 언세이프 서클(unsafe circle), robot 피해를 제외한 모든 피해에 면역입니다.

**형식 모델:**

- [M-0132](../rules/items.md#m-0132) 해석 A: `asleep이고 dist(self, own_bag) <= 15 m이면: {outside circle, unsafe circle, robot}을 제외한 모든 원천에 면역`
- [M-0132](../rules/items.md#m-0132) 정의역: dist는 미터 단위
- [M-0132](../rules/items.md#m-0132) 매개변수 `radius_m`: 15

**미해결 질문:**

- [U-0120](../unknowns.md#u-0120) (높음): 한 번의 타격에 여러 방어 수단(Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection)이 적용될 때, 어느 것이 'blocker'이고 어떤 아이템이 소모됩니까? 명시된 유일한 규칙은 'a hit already blocked by something else does not use [the Flak jacket] up'입니다.

**모순:** [C-0104](../unknowns.md#c-0104)

메모 ([M-0132](../rules/items.md#m-0132)): 상인 페이지에는 65 s 지연과 flashbang이 추가되어 있고 존과 언세이프 서클(unsafe circle)만 제외합니다 (robot 없음): [C-0105](../unknowns.md#c-0105). 해당 세 원천의 피해 표 행에는 명시된 대로 면역이 없습니다.

<a id="m-0134"></a>

### M-0134: Mirror forcefield는 처음 반사한 공격에서 소모됨

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0134](../rules/items.md#m-0134) `wiki-damage-069`: "A Mirror Forcefield is used up by the first attack it reflects." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Mirror Forcefield는 처음 반사한 공격에서 소모됩니다.

**형식 모델:**

- [M-0134](../rules/items.md#m-0134) 해석 A: `mirror는 첫 반사에서 소모됨; 막힌 공격이나 반사할 수 없는 공격은 이를 소모시키지 않음`

**상호작용:** [M-0120](../rules/damage.md#m-0120)

<a id="m-0200"></a>

### M-0200: 아이템 3개의 인벤토리 용량

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0200](../rules/items.md#m-0200) `wiki-items-002`: "You can carry up to 3 items, some items can stack (such as C4/Landmines/Arrows)." ([출처](https://iceposeidon.com/safezone/wiki/items#inventory))
  - 번역: 아이템을 최대 3개까지 휴대할 수 있으며, 일부 아이템은 중첩할 수 있습니다(C4/Landmines/Arrows 등).

**형식 모델:**

- [M-0200](../rules/items.md#m-0200) 해석 A: `slots_used <= 3 (기본 용량)`
- [M-0200](../rules/items.md#m-0200) 정의역: slots_used 정수 0..3
- [M-0200](../rules/items.md#m-0200) 매개변수 `capacity`: 3

**상호작용:** [M-0201](../rules/items.md#m-0201), [M-0219](../rules/items.md#m-0219)

메모 ([M-0200](../rules/items.md#m-0200)): 아이템 페이지의 기본값입니다. 다른 페이지는 일부 시길에 다른 용량을 제시하며(Endurance 10, Ingenuity 2에 조합 칸 5), 이는 각 시길 계열에 속합니다.

<a id="m-0201"></a>

### M-0201: 한 칸에 중첩되는 아이템

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0201](../rules/items.md#m-0201) `wiki-items-002`: "You can carry up to 3 items, some items can stack (such as C4/Landmines/Arrows)." ([출처](https://iceposeidon.com/safezone/wiki/items#inventory))
  - 번역: 아이템을 최대 3개까지 휴대할 수 있으며, 일부 아이템은 중첩할 수 있습니다(C4/Landmines/Arrows 등).

**형식 모델:**

- [M-0201](../rules/items.md#m-0201) 해석 A: `중첩 가능 = {C4, Landmines, Arrows}만 해당. 그 외 모든 아이템은 개당 한 칸을 차지함`
- [M-0201](../rules/items.md#m-0201) 해석 B: `목록은 열려 있음('등'): 다른 아이템(mirror forcefield, Piety가 아닌 경우의 포션 등)도 중첩될 수 있음`
- [M-0201](../rules/items.md#m-0201) 정의역: 아이템 종류. 중첩 크기: 무기 페이지에 따르면 C4/landmines는 5, arrows는 10

**상호작용:** [M-0200](../rules/items.md#m-0200), [M-0202](../rules/items.md#m-0202), [M-0236](../rules/items.md#m-0236)

**미해결 질문:**

- [U-0200](../unknowns.md#u-0200) (보통): C4, landmine, 화살 외에 어떤 아이템이 한 슬롯에 중첩됩니까(Piety가 아닌 체력 포션, mirror forcefield, 기타)?

메모 ([M-0201](../rules/items.md#m-0201)): 중첩 크기는 아이템 페이지에 없습니다. 무기 페이지는 C4와 landmines에 5, 화살 묶음당 10을 제시합니다.

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

<a id="m-0203"></a>

### M-0203: 활성 아이템 효과 3개 상한

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0203](../rules/items.md#m-0203) `wiki-items-004`: "You can have at most 3 active item effects at once." ([출처](https://iceposeidon.com/safezone/wiki/items#effects))
  - 번역: 활성 아이템 효과는 한 번에 최대 3개까지 가질 수 있습니다.

**형식 모델:**

- [M-0203](../rules/items.md#m-0203) 해석 A: `count(참가자의 활성 아이템 효과) <= 3 (항상)`
- [M-0203](../rules/items.md#m-0203) 정의역: 정수 0..3
- [M-0203](../rules/items.md#m-0203) 매개변수 `cap`: 3

**상호작용:** [M-0204](../rules/items.md#m-0204), [M-0205](../rules/items.md#m-0205), [M-0206](../rules/items.md#m-0206)

<a id="m-0204"></a>

### M-0204: 효과 상한에서 아이템 사용 거부

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0204](../rules/items.md#m-0204) `wiki-items-005`: "At the limit, the item is refused and you keep it." ([출처](https://iceposeidon.com/safezone/wiki/items#effects))
  - 번역: 상한에 도달하면 아이템은 거부되고 그대로 보유합니다.

**형식 모델:**

- [M-0204](../rules/items.md#m-0204) 해석 A: `count == 3일 때 효과를 추가하는 아이템을 사용: 사용이 거부되고, 아이템은 인벤토리에 남으며, 상태는 변하지 않음`
- [M-0204](../rules/items.md#m-0204) 정의역: count 0..3. 아이템 사용 이벤트

**상호작용:** [M-0203](../rules/items.md#m-0203), [M-0205](../rules/items.md#m-0205)

**미해결 질문:**

- [U-0202](../unknowns.md#u-0202) (보통): 상한 목록에 명시되지 않은 효과는 어떻게 동작합니까: EMP(10min), Thermal goggles(소지), Body armor, Sleeping Bag, 체력 포션? 그리고 상한 상태에서 Hazmat suit을 주우면 어떻게 됩니까?

메모 ([M-0204](../rules/items.md#m-0204)): Hazmat suit는 '휴대하는 동안' 효과로 계산되므로(사용 행동 없음), 상한에서 주웠을 때 어떻게 되는지는 페이지에 나와 있지 않습니다([U-0202](../unknowns.md#u-0202)).

<a id="m-0205"></a>

### M-0205: 상한에 포함되는 효과

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0205](../rules/items.md#m-0205) `wiki-items-006`: "These count: a Shield, a Guardian angel, a Mirror forcefield, Anti poison immunity, a Flak jacket, a Gas mask, Zombie repellent, and a Hazmat suit while you carry it." ([출처](https://iceposeidon.com/safezone/wiki/items#effects))
  - 번역: 다음은 포함됩니다: Shield, Guardian angel, Mirror forcefield, Anti poison 면역, Flak jacket, Gas mask, Zombie repellent, 그리고 휴대하는 동안의 Hazmat suit.

**형식 모델:**

- [M-0205](../rules/items.md#m-0205) 해석 A: `계산 대상 = Shield, Guardian angel, Mirror forcefield, Anti poison 면역, Flak jacket, Gas mask, Zombie repellent, Hazmat suit(휴대 중). 그 외는 없음`
- [M-0205](../rules/items.md#m-0205) 해석 B: `같은 목록이지만 각 Mirror forcefield를 따로 계산함(여러 개가 중첩될 수 있음)`
- [M-0205](../rules/items.md#m-0205) 해석 C: `같은 목록이지만 모든 Mirror forcefield를 합쳐 한 번만 계산함`
- [M-0205](../rules/items.md#m-0205) 정의역: 효과 종류의 집합. mirror의 중복 계산 여부는 미해결

**상호작용:** [M-0203](../rules/items.md#m-0203), [M-0206](../rules/items.md#m-0206)

**미해결 질문:**

- [U-0201](../unknowns.md#u-0201) (보통): 여러 mirror forcefield는 하나의 효과로 셉니까, 아니면 각각 효과 3개 상한에 하나씩 산입됩니까?
- [U-0202](../unknowns.md#u-0202) (보통): 상한 목록에 명시되지 않은 효과는 어떻게 동작합니까: EMP(10min), Thermal goggles(소지), Body armor, Sleeping Bag, 체력 포션? 그리고 상한 상태에서 Hazmat suit을 주우면 어떻게 됩니까?

메모 ([M-0205](../rules/items.md#m-0205)): 어느 목록에도 언급되지 않은 것: EMP(10min 시간제), Thermal goggles(역시 '휴대하는 동안'), Body armor, Sleeping Bag, 체력 포션. [U-0202](../unknowns.md#u-0202) 참조.

<a id="m-0206"></a>

### M-0206: 상한에 포함되지 않는 효과

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0206](../rules/items.md#m-0206) `wiki-items-007`: "These do not count: Safety Bubbles, smoke bombs, bandages, crafts, merchant upgrades, and effects that do not come from using an item, such as a Greed chest shield." ([출처](https://iceposeidon.com/safezone/wiki/items#effects))
  - 번역: 다음은 포함되지 않습니다: Safety Bubbles, smoke bombs, bandages, 조합 아이템, 상인 업그레이드, 그리고 Greed chest shield처럼 아이템 사용에서 비롯되지 않은 효과.

**형식 모델:**

- [M-0206](../rules/items.md#m-0206) 해석 A: `계산 제외 = Safety Bubbles, smoke bombs, bandages, 조합 아이템, 상인 업그레이드, 그리고 아이템 사용에서 비롯되지 않은 효과(예: Greed chest shield)`
- [M-0206](../rules/items.md#m-0206) 정의역: 효과 종류의 집합

**상호작용:** [M-0203](../rules/items.md#m-0203), [M-0205](../rules/items.md#m-0205)

메모 ([M-0206](../rules/items.md#m-0206)): Greed chest shield는 Shield 아이템과 별개의 효과입니다. Shield처럼 막는지는 Greed 페이지에 속합니다.

<a id="m-0209"></a>

### M-0209: Hazmat suit가 존 피해 간격을 늘림

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0209](../rules/items.md#m-0209) `wiki-items-013`: "While you carry it, each zone damage interval is 2s longer." ([출처](https://iceposeidon.com/safezone/wiki/items#hazmat_suit))
  - 번역: 휴대하는 동안 각 존 피해 간격이 2s 길어집니다.

**형식 모델:**

- [M-0209](../rules/items.md#m-0209) 해석 A: `휴대 중: 존 밖 피해 간격 = 2s + 2s = 4s, 유예/첫 틱은 변하지 않음`
- [M-0209](../rules/items.md#m-0209) 해석 B: `휴대 중: 모든 간격이 4s이고 첫 틱도 2s 지연됨`
- [M-0209](../rules/items.md#m-0209) 해석 C: `휴대 중: +2s가 언세이프 서클(unsafe circle) 및 robot 피해 간격에도 적용됨(피해 페이지는 서클 밖, 언세이프 서클, robot에 대해 Hazmat suit (slows)를 나열함)`
- [M-0209](../rules/items.md#m-0209) 정의역: 휴대 상태 불리언; 간격 s는 초 단위
- [M-0209](../rules/items.md#m-0209) 매개변수 `added_interval`: 2s
- [M-0209](../rules/items.md#m-0209) 매개변수 `base_interval`: 2s (존 페이지: 2s마다 1 HP)

**따름 결과:** [T-0008](../theorems/T-0008.md), [T-0305](../theorems/T-0305.md)

**상호작용:** [M-0205](../rules/items.md#m-0205)

**미해결 질문:**

- [U-0205](../unknowns.md#u-0205) (높음): Hazmat suit의 '간격당 +2s'는 어떤 피해 원인과 어떤 타이밍(첫 틱, 유예)을 늘립니까?
- [U-0003](../unknowns.md#u-0003) (보통): 존 피해: 세이프 존을 벗어난 뒤 첫 틱은 5 s입니까, 7 s입니까?

메모 ([M-0209](../rules/items.md#m-0209)): 틱당 피해는 변하지 않으므로, 단순한 해석에서는 존 소모 속도가 절반이 됩니다(4s마다 1 HP). Hazmat은 휴대하는 동안 효과 3개 상한에 포함됩니다.

<a id="m-0210"></a>

### M-0210: Guardian angel의 존 면역

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0210](../rules/items.md#m-0210) `wiki-items-014`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#guardian_angel))
  - 번역: 사용 가능
- [M-0210](../rules/items.md#m-0210) `wiki-items-015`: "Immune to zone damage for 10min." ([출처](https://iceposeidon.com/safezone/wiki/items#guardian_angel))
  - 번역: 10min 동안 존 피해에 면역입니다.

**형식 모델:**

- [M-0210](../rules/items.md#m-0210) 해석 A: `사용 후 10min 동안 세이프 존 밖에 있어서 받는 피해 = 0`
- [M-0210](../rules/items.md#m-0210) 해석 B: `위와 같고, 언세이프 서클(unsafe circle) 피해도 0`
- [M-0210](../rules/items.md#m-0210) 정의역: 사용 후 t in [0, 600)초
- [M-0210](../rules/items.md#m-0210) 매개변수 `duration`: 10min

**상호작용:** [M-0205](../rules/items.md#m-0205), [M-0211](../rules/items.md#m-0211)

**미해결 질문:**

- [U-0206](../unknowns.md#u-0206) (보통): Guardian angel의 '존 피해'에 언세이프 서클 피해가 포함됩니까?

메모 ([M-0210](../rules/items.md#m-0210)): 피해 페이지의 표는 Guardian angel을 '서클 밖'과 '언세이프 서클' 모두에 나열하지만, 아이템 페이지는 '존 피해'만 말합니다. 같은 페이지의 Shield 문장은 존과 언세이프 서클을 따로 명시합니다.

<a id="m-0211"></a>

### M-0211: Guardian angel의 종료 조건

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0211](../rules/items.md#m-0211) `wiki-items-016`: "Ends when another contestant attacks you, even if a shield or bubble blocks the hit." ([출처](https://iceposeidon.com/safezone/wiki/items#guardian_angel))
  - 번역: 다른 참가자가 당신을 공격하면, shield나 bubble이 타격을 막더라도 종료됩니다.

**형식 모델:**

- [M-0211](../rules/items.md#m-0211) 해석 A: `대상이 자신인 다른 참가자의 첫 공격에서, Shield나 Safety bubble에 막혔는지와 상관없이 종료됨. 시청자와 관리자의 공격은 제외`
- [M-0211](../rules/items.md#m-0211) 해석 B: `A에 더해, 피해를 주지 않는 적대 행동(steal, Vulnerability Dart, flashbang)과 자신이 설치한 함정을 다른 참가자가 발동시킨 경우에도 종료됨`
- [M-0211](../rules/items.md#m-0211) 해석 C: `막기 전에 실제로 피해를 입혔을 공격일 때만 종료됨. 즉 더 앞서 무력화된 공격(빗나감, smoke, mirror)은 종료시키지 않음`
- [M-0211](../rules/items.md#m-0211) 정의역: 이벤트: attack(attacker!=you, target=you)

**상호작용:** [M-0210](../rules/items.md#m-0210)

**미해결 질문:**

- [U-0207](../unknowns.md#u-0207) (높음): Guardian angel을 끝내는 '당신을 공격한다'는 무엇을 뜻합니까?

메모 ([M-0211](../rules/items.md#m-0211)): 명시된 내용: 막힌 타격도 종료시킵니다. 미해결: 범위 효과, 함정, 독 틱, drone, 반사된 공격에서 '당신을 공격한다'가 무엇을 뜻하는지.

<a id="m-0212"></a>

### M-0212: Safety bubble의 생성, 크기, 지속 시간

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0212](../rules/items.md#m-0212) `wiki-items-017`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
  - 번역: 사용 가능
- [M-0212](../rules/items.md#m-0212) `wiki-items-018`: "Creates a 10m (33ft) bubble where you stand for 10min." ([출처](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
  - 번역: 서 있는 곳에 10m(33ft) bubble을 10min 동안 만듭니다.

**형식 모델:**

- [M-0212](../rules/items.md#m-0212) 해석 A: `bubble = 사용 지점의 사용자를 중심으로 한 반지름 10 m의 원판, 600 s 지속`
- [M-0212](../rules/items.md#m-0212) 해석 B: `bubble = 지름 10 m, 반지름 5 m의 원판`
- [M-0212](../rules/items.md#m-0212) 정의역: 위치는 추상적; t in [0, 600)
- [M-0212](../rules/items.md#m-0212) 매개변수 `size`: 10 m (33 ft)
- [M-0212](../rules/items.md#m-0212) 매개변수 `duration`: 10min

**상호작용:** [M-0213](../rules/items.md#m-0213), [M-0214](../rules/items.md#m-0214)

**미해결 질문:**

- [U-0208](../unknowns.md#u-0208) (보통): Safety bubble의 '10m'는 반지름입니까, 지름입니까?

<a id="m-0213"></a>

### M-0213: Safety bubble의 면역

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0213](../rules/items.md#m-0213) `wiki-items-019`: "Everyone inside is immune to damage and zombies, zone damage included." ([출처](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
  - 번역: 안에 있는 모든 사람은 존 피해를 포함해 피해와 좀비에 면역입니다.
- [M-0213](../rules/items.md#m-0213) `wiki-items-020`: "A trapped gift still hurts the holder." ([출처](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
  - 번역: 함정이 설치된 선물은 여전히 소지자에게 피해를 줍니다.

**형식 모델:**

- [M-0213](../rules/items.md#m-0213) 해석 A: `안에 있는 모든 참가자: 피해 = 0이며 좀비가 해칠 수 없음(존 피해 포함). 예외: 함정이 설치된 선물은 여전히 소지자에게 피해를 줌`
- [M-0213](../rules/items.md#m-0213) 정의역: inside(position, bubble) 불리언

**따름 결과:** [T-0402](../theorems/T-0402.md), [T-0702](../theorems/T-0702.md), [T-0706](../theorems/T-0706.md)

**상호작용:** [M-0212](../rules/items.md#m-0212), [M-0214](../rules/items.md#m-0214), [M-0247](../rules/items.md#m-0247)

메모 ([M-0213](../rules/items.md#m-0213)): 피해 페이지: Safety bubble은 독이 걸리는 것을 막지는 않지만 독의 각 단계를 막습니다. Flashbang은 Safety bubble로 막지 못합니다(flashbang 절). 경계 포함 여부는 명시되어 있지 않습니다.

<a id="m-0214"></a>

### M-0214: Safety bubble과 취약한 참가자

라벨: `CONTRADICTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0214](../rules/items.md#m-0214) `wiki-items-021`: "It does not protect a vulnerable contestant, and you cannot use it while vulnerable." ([출처](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
  - 번역: 취약한 참가자는 보호하지 않으며, 취약한 동안에는 사용할 수 없습니다.

**형식 모델:**

- [M-0214](../rules/items.md#m-0214) 해석 A: `취약한 참가자는 bubble 보호를 받지 못하고 bubble을 사용할 수 없음. bubble 자체는 다른 사람들에게 남음`
- [M-0214](../rules/items.md#m-0214) 해석 B: `Vulnerability Dart는 그들이 소유하거나 그 안에 서 있는 모든 bubble을 터뜨림(상인 페이지). bubble은 모두에게서 사라짐`
- [M-0214](../rules/items.md#m-0214) 정의역: vulnerable 불리언

**상호작용:** [M-0212](../rules/items.md#m-0212), [M-0213](../rules/items.md#m-0213), [M-0216](../rules/items.md#m-0216)

**모순:** [C-0204](../unknowns.md#c-0204)

메모 ([M-0214](../rules/items.md#m-0214)): [C-0204](../unknowns.md#c-0204) 참조. 아이템 페이지는 취약한 참가자가 보호받지 못한다고만 말하고, 상인 페이지는 다트가 bubble을 터뜨린다고 말합니다.

<a id="m-0215"></a>

### M-0215: Shield의 지속 시간과 취약 상태

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0215](../rules/items.md#m-0215) `wiki-items-022`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#shield))
  - 번역: 사용 가능
- [M-0215](../rules/items.md#m-0215) `wiki-items-024`: "You cannot use it while vulnerable, and a Vulnerability Dart removes it." ([출처](https://iceposeidon.com/safezone/wiki/items#shield))
  - 번역: 취약한 동안에는 사용할 수 없으며, Vulnerability Dart가 이를 제거합니다.

**형식 모델:**

- [M-0215](../rules/items.md#m-0215) 해석 A: `Shield는 20min 지속. 취약한 동안 사용 불가. Vulnerability Dart가 제거함`
- [M-0215](../rules/items.md#m-0215) 정의역: t in [0, 1200)초
- [M-0215](../rules/items.md#m-0215) 매개변수 `duration`: 20min

**따름 결과:** [T-0408](../theorems/T-0408.md)

**상호작용:** [M-0205](../rules/items.md#m-0205), [M-0216](../rules/items.md#m-0216)

<a id="m-0216"></a>

### M-0216: Shield의 피해 제외 항목

라벨: `CONTRADICTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0216](../rules/items.md#m-0216) `wiki-items-023`: "Immune to damage for 20min, except zone damage and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/items#shield))
  - 번역: 존 피해와 언세이프 서클 피해를 제외한 피해에 20min 동안 면역입니다.
- [M-0216](../rules/items.md#m-0216) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Shield는 존, 언세이프 서클, robot 피해를 막지 않습니다.

**형식 모델:**

- [M-0216](../rules/items.md#m-0216) 해석 A: `Shield는 존 피해와 언세이프 서클 피해를 제외한 모든 피해를 막음`
- [M-0216](../rules/items.md#m-0216) 해석 B: `Shield는 존, 언세이프 서클, robot 피해를 제외한 모든 피해를 막음(피해 페이지)`
- [M-0216](../rules/items.md#m-0216) 정의역: 피해 원인의 종류

**상호작용:** [M-0215](../rules/items.md#m-0215)

**모순:** [C-0202](../unknowns.md#c-0202)

메모 ([M-0216](../rules/items.md#m-0216)): [C-0202](../unknowns.md#c-0202) 참조. 독: Shield는 독이 걸리는 것을 막지는 않지만 각 단계를 막습니다(피해 페이지). Flashbang은 Shield가 막지 못합니다.

<a id="m-0217"></a>

### M-0217: Body armor의 흡수 풀

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0217](../rules/items.md#m-0217) `wiki-items-025`: "Equippable" ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: 장착 가능
- [M-0217](../rules/items.md#m-0217) `wiki-items-026`: "Absorbs up to 15 HP of damage." ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: 최대 15 HP의 피해를 흡수합니다.
- [M-0217](../rules/items.md#m-0217) `wiki-damage-055`: "Body armor absorbs what is left, until it breaks." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Body armor는 남은 피해를 부서질 때까지 흡수합니다.

**형식 모델:**

- [M-0217](../rules/items.md#m-0217) 해석 A: `armor는 15 HP의 풀을 가짐: 타격마다 풀에서 min(pool, damage_left) HP를 잃고, 이후 pool-=absorbed. 0이 되면 파괴됨`
- [M-0217](../rules/items.md#m-0217) 해석 B: `armor는 타격당 최대 15 HP를 흡수하며 소진되지 않음`
- [M-0217](../rules/items.md#m-0217) 정의역: 풀 정수 0..15
- [M-0217](../rules/items.md#m-0217) 매개변수 `capacity`: 15 HP

**따름 결과:** [T-0007](../theorems/T-0007.md), [T-0305](../theorems/T-0305.md), [T-0402](../theorems/T-0402.md)

**상호작용:** [M-0218](../rules/items.md#m-0218), [M-0219](../rules/items.md#m-0219)

**미해결 질문:**

- [U-0101](../unknowns.md#u-0101) (높음): Body armor가 'absorbs what is left, until it breaks'일 때, 남은 내구도보다 큰 타격은 초과분을 통과시킵니까(A), 아니면 타격 전체가 흡수되고 armor만 부서집니까(B)? 내구도는 흡수한 HP 1당 1씩 줄어듭니까?

메모 ([M-0217](../rules/items.md#m-0217)): 피해 페이지의 '부서질 때까지'와 상인 인챈트의 내구도는 소모되는 풀을 확정합니다. 해석 B는 반박되었습니다([U-0209](../unknowns.md#u-0209), 해결됨). 일부만 흡수된 타격은 명시되어 있지 않습니다: [U-0101](../unknowns.md#u-0101). 파이프라인 순서는 피해 페이지에 속합니다.

<a id="m-0218"></a>

### M-0218: 함정이 설치된 선물은 Body armor를 무시함

라벨: `CONTRADICTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0218](../rules/items.md#m-0218) `wiki-items-027`: "A trapped gift ignores it." ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: 함정이 설치된 선물은 이를 무시합니다.
- [M-0218](../rules/items.md#m-0218) `wiki-damage-071`: "Body Armor works on every kind of damage." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Body Armor는 모든 종류의 피해에 작동합니다.

**형식 모델:**

- [M-0218](../rules/items.md#m-0218) 해석 A: `함정이 설치된 선물의 피해는 Body armor를 우회함`
- [M-0218](../rules/items.md#m-0218) 해석 B: `Body armor는 함정이 설치된 선물을 포함해 모든 종류의 피해에 작동함`
- [M-0218](../rules/items.md#m-0218) 정의역: 피해 원인의 종류

**상호작용:** [M-0217](../rules/items.md#m-0217)

**모순:** [C-0201](../unknowns.md#c-0201)

메모 ([M-0218](../rules/items.md#m-0218)): [C-0201](../unknowns.md#c-0201) 참조. 피해 페이지 표의 Trapped gift 행도 Safety bubble과 Body armor를 생략하며, 이는 A와 일치합니다.

<a id="m-0219"></a>

### M-0219: Body armor 장착 칸과 휴대 한도

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0219](../rules/items.md#m-0219) `wiki-items-028`: "It goes into your armor slot when you get it." ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: 얻으면 armor 칸에 들어갑니다.
- [M-0219](../rules/items.md#m-0219) `wiki-items-029`: "Carry at most one, including equipped armor." ([출처](https://iceposeidon.com/safezone/wiki/items#body_armor))
  - 번역: 장착한 armor를 포함해 최대 하나만 휴대합니다.
- [M-0219](../rules/items.md#m-0219) `wiki-merchant-040`: "Weapon and worn equipment slots do not use inventory space." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: 무기와 착용 장비 칸은 인벤토리 공간을 사용하지 않습니다.
- [M-0219](../rules/items.md#m-0219) `wiki-merchant-041`: "Carry at most one Body Armor." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Body Armor는 최대 하나만 휴대합니다.

**형식 모델:**

- [M-0219](../rules/items.md#m-0219) 해석 A: `armor는 획득 시 인벤토리 칸이 아니라 armor 칸으로 들어감. 장착한 것을 포함해 armor는 총 1개까지. 추가 armor는 거부됨`
- [M-0219](../rules/items.md#m-0219) 해석 B: `두 번째 armor는 장착한 것을 대체하거나 그것과 맞바뀜`
- [M-0219](../rules/items.md#m-0219) 정의역: armor 개수 0..1

**상호작용:** [M-0200](../rules/items.md#m-0200), [M-0217](../rules/items.md#m-0217)

**미해결 질문:**

- [U-0210](../unknowns.md#u-0210) (낮음): Body armor를 착용 중이거나 소지 중일 때 두 번째 Body armor를 얻으면 어떻게 됩니까?

<a id="m-0220"></a>

### M-0220: Zombie repellent

라벨: `CONTRADICTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0220](../rules/items.md#m-0220) `wiki-items-030`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
  - 번역: 사용 가능
- [M-0220](../rules/items.md#m-0220) `wiki-items-031`: "Use it to stop zombies hurting you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
  - 번역: 20min 동안 좀비가 당신을 해치지 못하게 하려면 사용하십시오.
- [M-0220](../rules/items.md#m-0220) `wiki-items-032`: "It only protects you." ([출처](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
  - 번역: 사용자 본인만 보호합니다.
- [M-0220](../rules/items.md#m-0220) `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/zombies#defence))
  - 번역: Zombie repellent: 사용하면 20min 동안 좀비가 당신을 무시합니다.

**형식 모델:**

- [M-0220](../rules/items.md#m-0220) 해석 A: `사용 후 20min 동안: 당신에 대한 좀비 피해 = 0. 좀비는 여전히 당신을 표적으로 삼고 쫓음`
- [M-0220](../rules/items.md#m-0220) 해석 B: `사용 후 20min 동안: 좀비가 당신을 완전히 무시함(유효한 표적이 아님). 다른 사람들을 쫓음`
- [M-0220](../rules/items.md#m-0220) 해석 C: `사용자 본인에게만 적용되며, 근처의 다른 사람에게는 적용되지 않음`
- [M-0220](../rules/items.md#m-0220) 정의역: t in [0, 1200)초
- [M-0220](../rules/items.md#m-0220) 매개변수 `duration`: 20min

**상호작용:** [M-0205](../rules/items.md#m-0205)

**모순:** [C-0205](../unknowns.md#c-0205)

메모 ([M-0220](../rules/items.md#m-0220)): [C-0205](../unknowns.md#c-0205) 참조. '좀비가 당신을 해치지 못하게 한다'(아이템 페이지)와 '좀비가 당신을 무시한다'(좀비 페이지)가 다릅니다. '사용자 본인만 보호합니다'는 모든 해석에서 성립합니다.

<a id="m-0226"></a>

### M-0226: Smoke bomb의 범위, 지속 시간, 다른 참가자에 대한 효과

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0226](../rules/items.md#m-0226) `wiki-items-040`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: 사용 가능
- [M-0226](../rules/items.md#m-0226) `wiki-items-041`: "Blacks out the map and blocks attacks for other contestants within 50m (164ft) of you for 20min." ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: 당신으로부터 50m (164ft) 이내에 있는 다른 참가자에 대해 20min 동안 지도를 가리고 공격을 막습니다.
- [M-0226](../rules/items.md#m-0226) `wiki-items-042`: "Any other contestant inside it cannot attack at all: no targeted attacks, staff areas, C4, landmines or flashbangs." ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: 그 안에 있는 다른 참가자는 전혀 공격할 수 없습니다: 대상 지정 공격, 스태프 구역, C4, landmine, flashbang 모두 불가합니다.

**형식 모델:**

- [M-0226](../rules/items.md#m-0226) 해석 A: `구름 = 터뜨린 위치에 고정된 반지름 50 m의 원판, 20min. 안에 있는 다른 참가자는 지도가 차단되고 공격할 수 없음 (대상 지정 공격, 스태프 구역, C4, landmine, flashbang)`
- [M-0226](../rules/items.md#m-0226) 해석 B: `동일하나 중심이 사용자를 따라 이동함`
- [M-0226](../rules/items.md#m-0226) 정의역: 위치는 추상화, t in [0, 1200) 초
- [M-0226](../rules/items.md#m-0226) 매개변수 `radius`: 50 m
- [M-0226](../rules/items.md#m-0226) 매개변수 `duration`: 20min

**상호작용:** [M-0227](../rules/items.md#m-0227), [M-0228](../rules/items.md#m-0228), [M-0229](../rules/items.md#m-0229), [M-0231](../rules/items.md#m-0231)

**미해결 질문:**

- [U-0211](../unknowns.md#u-0211) (보통): smoke bomb 구름은 터뜨린 위치에 고정됩니까, 사용자를 따라갑니까?

<a id="m-0227"></a>

### M-0227: Smoke bomb 내부에서의 제한

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0227](../rules/items.md#m-0227) `wiki-items-043`: "From inside it you also cannot heal or steal from other contestants, send a trade request, throw a Vulnerability Dart, fire a merchant missile or give a robot a target." ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: 그 안에서는 또한 다른 참가자를 회복하거나 훔칠 수 없고, 거래 요청을 보낼 수 없으며, Vulnerability Dart를 던질 수 없고, 상인 미사일을 발사할 수 없으며, robot에게 목표를 줄 수 없습니다.

**형식 모델:**

- [M-0227](../rules/items.md#m-0227) 해석 A: `구름 안의 다른 참가자는 다음도 할 수 없음: 다른 참가자 회복 또는 훔치기, 거래 요청 보내기, Vulnerability Dart 던지기, 상인 미사일 발사, robot에게 목표 부여`
- [M-0227](../rules/items.md#m-0227) 정의역: 행동 집합

**따름 결과:** [T-0305](../theorems/T-0305.md)

**상호작용:** [M-0226](../rules/items.md#m-0226)

<a id="m-0228"></a>

### M-0228: Smoke bomb 외부의 대상 지정 차단

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0228](../rules/items.md#m-0228) `wiki-items-044`: "Nobody outside can target anyone inside it either, drones included." ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: 밖에 있는 누구도 그 안에 있는 사람을 대상으로 지정할 수 없으며, drone도 마찬가지입니다.

**형식 모델:**

- [M-0228](../rules/items.md#m-0228) 해석 A: `밖에 있는 누구도 구름 안의 사람을 대상으로 지정할 수 없으며, drone도 마찬가지이며 터뜨린 사람도 포함됨`
- [M-0228](../rules/items.md#m-0228) 해석 B: `터뜨린 사람은 밖에서 여전히 대상으로 지정될 수 있음`
- [M-0228](../rules/items.md#m-0228) 정의역: 구름 안의 대상 위치

**상호작용:** [M-0226](../rules/items.md#m-0226)

**미해결 질문:**

- [U-0212](../unknowns.md#u-0212) (보통): smoke bomb을 터뜨린 참가자를 구름 밖에서 대상으로 삼을 수 있습니까?

<a id="m-0229"></a>

### M-0229: Smoke bomb을 터뜨린 사람의 예외

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0229](../rules/items.md#m-0229) `wiki-items-045`: "The contestant who set it off is not affected and can still attack from inside it, including others inside." ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: 이를 터뜨린 참가자는 영향을 받지 않으며, 안에 있는 다른 참가자를 포함해 그 안에서 여전히 공격할 수 있습니다.

**형식 모델:**

- [M-0229](../rules/items.md#m-0229) 해석 A: `이를 터뜨린 참가자는 영향을 받지 않으며 안에서 공격할 수 있고, 안에 있는 다른 참가자도 공격 대상에 포함됨`
- [M-0229](../rules/items.md#m-0229) 정의역: 터뜨린 사람 여부 불리언

**상호작용:** [M-0226](../rules/items.md#m-0226), [M-0228](../rules/items.md#m-0228)

<a id="m-0231"></a>

### M-0231: Thermal goggles 대 Smoke bomb

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0231](../rules/items.md#m-0231) `wiki-items-046`: "Thermal goggles see through it." ([출처](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
  - 번역: Thermal goggles는 이를 투과해 봅니다.
- [M-0231](../rules/items.md#m-0231) `wiki-items-067`: "While you carry them, smoke bombs do not black out your map or block your attacks." ([출처](https://iceposeidon.com/safezone/wiki/items#thermal_goggles))
  - 번역: 소지하고 있는 동안 smoke bomb은 당신의 지도를 가리지 않고 당신의 공격도 막지 않습니다.

**형식 모델:**

- [M-0231](../rules/items.md#m-0231) 해석 A: `goggles 소지: 소지자에게 smoke로 인한 지도 차단과 공격 차단 없음. [M-0227](../rules/items.md#m-0227)의 제한은 여전히 적용됨`
- [M-0231](../rules/items.md#m-0231) 해석 B: `goggles 소지: 소지자에게 [M-0227](../rules/items.md#m-0227)의 제한을 포함해 어떤 종류의 smoke 제한도 없음`
- [M-0231](../rules/items.md#m-0231) 정의역: 소지 불리언

**상호작용:** [M-0226](../rules/items.md#m-0226), [M-0227](../rules/items.md#m-0227)

**미해결 질문:**

- [U-0213](../unknowns.md#u-0213) (보통): Thermal goggles의 예외는 smoke의 공격 차단과 블랙아웃에만 적용됩니까, 아니면 구름 안에서의 회복, 도둑질, 거래 제한에도 적용됩니까?
- [U-0202](../unknowns.md#u-0202) (보통): 상한 목록에 명시되지 않은 효과는 어떻게 동작합니까: EMP(10min), Thermal goggles(소지), Body armor, Sleeping Bag, 체력 포션? 그리고 상한 상태에서 Hazmat suit을 주우면 어떻게 됩니까?

메모 ([M-0231](../rules/items.md#m-0231)): 공격 페이지 (사이클롭스): 구름 안에서는 Thermal goggles를 갖고 있지 않으면 무기와 drone이 그것을 맞힐 수 없습니다.

<a id="m-0232"></a>

### M-0232: Thermal goggles는 환영 복사본을 간파함

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0232](../rules/items.md#m-0232) `wiki-items-068`: "You also see through illusions: copies of contestants show as copies, not as real contestants." ([출처](https://iceposeidon.com/safezone/wiki/items#thermal_goggles))
  - 번역: 환영도 간파합니다: 참가자의 복사본은 실제 참가자가 아니라 복사본으로 보입니다.
- [M-0232](../rules/items.md#m-0232) `wiki-attacks-052`: "Thermal goggles show them as copies." ([출처](https://iceposeidon.com/safezone/wiki/attacks#illusion))
  - 번역: Thermal goggles는 이를 복사본으로 보여 줍니다.

**형식 모델:**

- [M-0232](../rules/items.md#m-0232) 해석 A: `소지하는 동안 환영 복사본은 실제 참가자가 아니라 복사본으로 보임`
- [M-0232](../rules/items.md#m-0232) 정의역: 소지 불리언

<a id="m-0235"></a>

### M-0235: Mirror forcefield는 다음 공격을 반사함

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0235](../rules/items.md#m-0235) `wiki-items-052`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 사용 가능
- [M-0235](../rules/items.md#m-0235) `wiki-items-053`: "Reflects the next attack back at the attacker." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 다음 공격을 공격자에게 되돌립니다.
- [M-0235](../rules/items.md#m-0235) `wiki-damage-041`: "A Mirror forcefield sends the whole hit back to the attacker instead, before any reduction." ([출처](https://iceposeidon.com/safezone/wiki/damage#order))
  - 번역: Mirror forcefield는 대신 타격 전체를 어떤 감소도 적용되기 전에 공격자에게 되돌려 보냅니다.

**형식 모델:**

- [M-0235](../rules/items.md#m-0235) 해석 A: `자신에게 오는 다음 반사 가능한 공격이 타격 전체로, 어떤 감소도 적용되기 전에 공격자에게 되돌아감. 공격자 자신의 파이프라인이 적용됨`
- [M-0235](../rules/items.md#m-0235) 해석 B: `반사된 타격은 공격자의 방어를 건너뛰고 그 파이프라인을 우회함`
- [M-0235](../rules/items.md#m-0235) 정의역: 공격 이벤트

**상호작용:** [M-0236](../rules/items.md#m-0236), [M-0237](../rules/items.md#m-0237), [M-0239](../rules/items.md#m-0239), [M-0240](../rules/items.md#m-0240), [M-0241](../rules/items.md#m-0241)

**미해결 질문:**

- [U-0005](../unknowns.md#u-0005) (높음): 반사된 타격은 공격자 자신의 파이프라인(면역, 감소, armor)을 거칩니까?

<a id="m-0236"></a>

### M-0236: Mirror forcefield는 중첩됨

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0236](../rules/items.md#m-0236) `wiki-items-054`: "Several stack." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 여러 개가 중첩됩니다.
- [M-0236](../rules/items.md#m-0236) `wiki-damage-069`: "A Mirror Forcefield is used up by the first attack it reflects." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Mirror Forcefield는 처음으로 반사하는 공격에 소모됩니다.

**형식 모델:**

- [M-0236](../rules/items.md#m-0236) 해석 A: `여러 개의 mirror를 보유할 수 있으며, 반사 1회가 정확히 1개를 소모함`
- [M-0236](../rules/items.md#m-0236) 해석 B: `여러 개의 mirror를 보유할 수 있으며, 첫 반사가 전부 소모함`
- [M-0236](../rules/items.md#m-0236) 해석 C: `여러 개의 mirror가 연속된 여러 번의 반사를 제공함`
- [M-0236](../rules/items.md#m-0236) 정의역: mirror 수 n >= 0

**상호작용:** [M-0201](../rules/items.md#m-0201), [M-0205](../rules/items.md#m-0205), [M-0247](../rules/items.md#m-0247)

**미해결 질문:**

- [U-0201](../unknowns.md#u-0201) (보통): 여러 mirror forcefield는 하나의 효과로 셉니까, 아니면 각각 효과 3개 상한에 하나씩 산입됩니까?
- [U-0215](../unknowns.md#u-0215) (보통): mirror forcefield를 여러 개 가지고 있을 때, 한 번의 반사는 하나를 소모합니까, 전부를 소모합니까, 아니면 여러 번 반사합니까?
- [U-0200](../unknowns.md#u-0200) (보통): C4, landmine, 화살 외에 어떤 아이템이 한 슬롯에 중첩됩니까(Piety가 아닌 체력 포션, mirror forcefield, 기타)?

메모 ([M-0236](../rules/items.md#m-0236)): 명시된 경우는 Flashbang뿐입니다: 여러 forcefield가 모두 소모됩니다 ([M-0247](../rules/items.md#m-0247)).

<a id="m-0237"></a>

### M-0237: Mirror 반사 목록

라벨: `CONTRADICTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0237](../rules/items.md#m-0237) `wiki-items-055`: "Only reflects Poison Darts, fake gravestones, knives, Zarok's axes, long swords, machetes, bows, staffs, drones, C4, landmines, flashbangs and fake chests." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: Poison Dart, fake gravestone, knife, Zarok's axe, long sword, machete, bow, staff, drone, C4, landmine, flashbang, 가짜 상자만 반사합니다.
- [M-0237](../rules/items.md#m-0237) `wiki-damage-070`: "It only reflects Poison Darts, fake gravestones, bows, wizard staffs, knives, long swords, Zarok's axes, machetes, drones, C4, landmines, flashbangs and fake chests, and never your own explosives." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Poison Dart, fake gravestone, bow, wizard staff, knife, long sword, Zarok's axe, machete, drone, C4, landmine, flashbang, 가짜 상자만 반사하며, 자신의 폭발물은 절대 반사하지 않습니다.
- [M-0237](../rules/items.md#m-0237) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([출처](https://iceposeidon.com/safezone/wiki/damage))
  - 번역: | Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (반사)

**형식 모델:**

- [M-0237](../rules/items.md#m-0237) 해석 A: `반사 대상 = Poison Dart, fake gravestone, knife, Zarok's axe, long sword, machete, bow, staff, drone, C4, landmine, flashbang, 가짜 상자`
- [M-0237](../rules/items.md#m-0237) 해석 B: `A에 trapped gift를 더함 (피해 페이지 표의 Trapped gift 행에 Mirror forcefield (반사)가 있음)`
- [M-0237](../rules/items.md#m-0237) 정의역: A의 공격 종류 13가지. trapped gift 여부는 미해결

**상호작용:** [M-0235](../rules/items.md#m-0235)

**모순:** [C-0200](../unknowns.md#c-0200)

메모 ([M-0237](../rules/items.md#m-0237)): 아이템 목록과 피해 페이지 문장은 13가지에서 일치하지만, 피해 페이지 표에는 trapped gift가 추가되어 있습니다. [C-0200](../unknowns.md#c-0200) 참조. 피해 페이지에는 또한 자신의 폭발물은 절대 반사하지 않는다고 되어 있습니다.

<a id="m-0238"></a>

### M-0238: Mirror는 가짜 상자를 반사함

라벨: `DOCUMENTED`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0238](../rules/items.md#m-0238) `wiki-items-056`: "A reflected fake chest also locks the troll out of chests instead of you." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 반사된 가짜 상자는 또한 당신 대신 트롤이 상자를 열지 못하도록 잠급니다.

**형식 모델:**

- [M-0238](../rules/items.md#m-0238) 해석 A: `반사된 가짜 상자는 대상이 아니라 트롤이 상자를 열지 못하도록 잠금`
- [M-0238](../rules/items.md#m-0238) 정의역: 가짜 상자 이벤트

**상호작용:** [M-0237](../rules/items.md#m-0237)

<a id="m-0239"></a>

### M-0239: Mirror 대 공격자의 mirror

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0239](../rules/items.md#m-0239) `wiki-items-057`: "If the attacker also has one, the attack does nothing and both are used up, except a reflected Poison Dart or fake gravestone: it still poisons the attacker and their own mirror stays." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 공격자도 mirror를 갖고 있으면 공격은 아무 효과가 없고 둘 다 소모됩니다. 단 반사된 Poison Dart 또는 fake gravestone은 예외로, 여전히 공격자를 중독시키며 공격자 자신의 mirror는 남습니다.

**형식 모델:**

- [M-0239](../rules/items.md#m-0239) 해석 A: `공격자도 mirror를 가진 경우: 공격은 아무 효과가 없고 두 mirror 모두 소모됨. 예외로 반사된 Poison Dart 또는 fake gravestone은 공격자를 중독시키며 그 mirror는 남음 (방어자의 mirror는 사용됨)`
- [M-0239](../rules/items.md#m-0239) 해석 B: `예외 변형: 공격자의 mirror는 남고 방어자의 mirror도 유지됨`
- [M-0239](../rules/items.md#m-0239) 정의역: 양측 모두 mirror를 1개 이상 보유

**상호작용:** [M-0235](../rules/items.md#m-0235), [M-0247](../rules/items.md#m-0247)

**미해결 질문:**

- [U-0217](../unknowns.md#u-0217) (낮음): Mirror 대 mirror와 flashbang: 던진 사람도 mirror를 가지고 있다면 던진 사람이 실명합니까?
- [U-0215](../unknowns.md#u-0215) (보통): mirror forcefield를 여러 개 가지고 있을 때, 한 번의 반사는 하나를 소모합니까, 전부를 소모합니까, 아니면 여러 번 반사합니까?

<a id="m-0240"></a>

### M-0240: Mirror의 지속 시간과 종료

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0240](../rules/items.md#m-0240) `wiki-items-058`: "No time limit." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 시간 제한 없음.
- [M-0240](../rules/items.md#m-0240) `wiki-items-059`: "Ends when it reflects an attack or when you die." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 공격을 반사하거나 사망하면 끝납니다.

**형식 모델:**

- [M-0240](../rules/items.md#m-0240) 해석 A: `타이머 없음. 공격을 반사하거나 사망하면 끝남`
- [M-0240](../rules/items.md#m-0240) 정의역: mirror 상태

**상호작용:** [M-0235](../rules/items.md#m-0235), [M-0241](../rules/items.md#m-0241)

<a id="m-0241"></a>

### M-0241: Mirror는 시청자, 관리자, 존, 좀비 피해를 무시함

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0241](../rules/items.md#m-0241) `wiki-items-060`: "Never reflects viewer or admin attacks, such as missiles, nukes and gas, or the zone and zombies." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 미사일, 핵, 가스 같은 시청자 또는 관리자 공격과 존 및 좀비는 절대 반사하지 않습니다.
- [M-0241](../rules/items.md#m-0241) `wiki-items-061`: "These do not use it up." ([출처](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
  - 번역: 이들은 mirror를 소모시키지 않습니다.

**형식 모델:**

- [M-0241](../rules/items.md#m-0241) 해석 A: `시청자 또는 관리자 공격 (미사일, 핵, 가스), 존 피해, 좀비는 절대 반사하지 않으며, 이들은 mirror를 소모시키지 않음`
- [M-0241](../rules/items.md#m-0241) 정의역: 피해 출처 종류

**상호작용:** [M-0235](../rules/items.md#m-0235)

<a id="m-0242"></a>

### M-0242: Flak jacket은 폭발 타격 1회를 막음

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0242](../rules/items.md#m-0242) `wiki-items-062`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#flak_jacket))
  - 번역: 사용 가능
- [M-0242](../rules/items.md#m-0242) `wiki-items-063`: "Use it to block the next missile, nuke, airstrike or gunship hit on you." ([출처](https://iceposeidon.com/safezone/wiki/items#flak_jacket))
  - 번역: 자신에게 오는 다음 미사일, 핵, 공습 또는 건십 타격을 막는 데 사용합니다.
- [M-0242](../rules/items.md#m-0242) `wiki-items-064`: "It stays active until a hit uses it up." ([출처](https://iceposeidon.com/safezone/wiki/items#flak_jacket))
  - 번역: 타격으로 소모될 때까지 활성 상태로 유지됩니다.
- [M-0242](../rules/items.md#m-0242) `wiki-damage-063`: "A Flak jacket blocks the next missile, nuke, airstrike impact or gunship bomb, then is used up." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Flak jacket은 다음 미사일, 핵, 공습 충격 또는 건십 폭탄을 막고, 그다음 소모됩니다.
- [M-0242](../rules/items.md#m-0242) `wiki-attacks-034`: "A Flak jacket blocks the strike, but not the fire." ([출처](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
  - 번역: Flak jacket은 타격은 막지만 불은 막지 못합니다.
- [M-0242](../rules/items.md#m-0242) `wiki-attacks-041`: "A Flak jacket blocks one bomb." ([출처](https://iceposeidon.com/safezone/wiki/attacks#gunship))
  - 번역: Flak jacket은 폭탄 1개를 막습니다.

**형식 모델:**

- [M-0242](../rules/items.md#m-0242) 해석 A: `보유자에게 닿는 다음 미사일, 핵, 공습 충격 또는 건십 폭탄을 막고, 그 타격으로 소모됨. 공습의 불은 막지 못함`
- [M-0242](../rules/items.md#m-0242) 해석 B: `A와 같으나, Shield/Safety bubble/Sleeping Bag이 이미 막은 타격도 이를 소모함`
- [M-0242](../rules/items.md#m-0242) 해석 C: `A와 같으나, 앞서 이미 막힌 타격은 이를 소모하지 않음`
- [M-0242](../rules/items.md#m-0242) 정의역: 나열된 종류의 타격 이벤트

**상호작용:** [M-0205](../rules/items.md#m-0205)

**미해결 질문:**

- [U-0216](../unknowns.md#u-0216) (보통): 다른 방어(Shield, Safety bubble, Sleeping Bag)가 이미 막은 타격으로 Flak jacket이 소모됩니까?

메모 ([M-0242](../rules/items.md#m-0242)): 아이템 페이지는 '공습 또는 건십 타격'이라고 하고, 공격 페이지는 이를 타격과 폭탄 1개로 좁힙니다 (불은 제외).

<a id="m-0243"></a>

### M-0243: Gas mask

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0243](../rules/items.md#m-0243) `wiki-items-065`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#gas_mask))
  - 번역: 사용 가능
- [M-0243](../rules/items.md#m-0243) `wiki-items-066`: "Use it to become immune to tear gas for 10min." ([출처](https://iceposeidon.com/safezone/wiki/items#gas_mask))
  - 번역: 사용하면 10min 동안 최루 가스에 면역이 됩니다.
- [M-0243](../rules/items.md#m-0243) `wiki-damage-066`: "A Gas mask blocks tear gas." ([출처](https://iceposeidon.com/safezone/wiki/damage#notes))
  - 번역: Gas mask는 최루 가스를 막습니다.

**형식 모델:**

- [M-0243](../rules/items.md#m-0243) 해석 A: `사용 후 10min 동안 최루 가스는 사용자에게 아무 영향이 없음`
- [M-0243](../rules/items.md#m-0243) 정의역: t in [0, 600) 초
- [M-0243](../rules/items.md#m-0243) 매개변수 `duration`: 10min

**상호작용:** [M-0205](../rules/items.md#m-0205)

<a id="m-0244"></a>

### M-0244: Flashbang은 주변 참가자를 실명시킴

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0244](../rules/items.md#m-0244) `wiki-items-069`: "Usable" ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 사용 가능
- [M-0244](../rules/items.md#m-0244) `wiki-items-070`: "Blinds every other contestant within 30m (98ft) of you for 30s." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 당신으로부터 30m (98ft) 이내의 다른 모든 참가자를 30s 동안 실명시킵니다.

**형식 모델:**

- [M-0244](../rules/items.md#m-0244) 해석 A: `사용 시: 사용자로부터 30 m 이내의 다른 모든 참가자가 30 s 동안 실명됨. 실명 중 재타격: 연장 없음`
- [M-0244](../rules/items.md#m-0244) 해석 B: `실명 중 재타격하면 타이머가 30 s로 초기화됨`
- [M-0244](../rules/items.md#m-0244) 해석 C: `실명 중 재타격하면 30 s가 추가됨`
- [M-0244](../rules/items.md#m-0244) 정의역: 거리 d <= 30 m (경계 포함 여부는 미해결)
- [M-0244](../rules/items.md#m-0244) 매개변수 `radius`: 30 m
- [M-0244](../rules/items.md#m-0244) 매개변수 `duration`: 30s

**상호작용:** [M-0245](../rules/items.md#m-0245), [M-0246](../rules/items.md#m-0246), [M-0247](../rules/items.md#m-0247)

**미해결 질문:**

- [U-0218](../unknowns.md#u-0218) (낮음): 실명한 참가자가 또 다른 flashbang에 맞으면 실명이 연장됩니까, 초기화됩니까, 무시됩니까?

<a id="m-0245"></a>

### M-0245: 실명 제한

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0245](../rules/items.md#m-0245) `wiki-items-071`: "Blinded contestants can only move: they cannot see the map, use, place or aim items, attack, steal, loot, claim, craft or start a trade." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 실명된 참가자는 이동만 할 수 있습니다: 지도를 볼 수 없고, 아이템을 사용, 설치, 조준할 수 없으며, 공격, 훔치기, 루팅, 수령, 조합을 하거나 거래를 시작할 수 없습니다.
- [M-0245](../rules/items.md#m-0245) `wiki-items-072`: "They can still close a trade." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 거래를 닫는 것은 여전히 가능합니다.
- [M-0245](../rules/items.md#m-0245) `wiki-items-073`: "Effects already active keep working." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 이미 활성화된 효과는 계속 작동합니다.

**형식 모델:**

- [M-0245](../rules/items.md#m-0245) 해석 A: `실명: 이동만 가능. 지도 보기, 아이템 사용/설치/조준, 공격, 훔치기, 루팅, 수령, 조합, 거래 시작은 불가. 거래 닫기는 가능. 이미 활성화된 효과는 계속 작동함`
- [M-0245](../rules/items.md#m-0245) 정의역: 실명 불리언

**상호작용:** [M-0244](../rules/items.md#m-0244)

<a id="m-0246"></a>

### M-0246: Flashbang 면역과 막지 못하는 것

라벨: `CONTRADICTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0246](../rules/items.md#m-0246) `wiki-items-074`: "Shields and safety bubbles do not stop it." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: Shield와 Safety bubble은 이를 막지 못합니다.
- [M-0246](../rules/items.md#m-0246) `wiki-items-075`: "Sleeping contestants are immune." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 잠든 참가자는 면역입니다.
- [M-0246](../rules/items.md#m-0246) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 65초 동안 잠을 자면 flashbang에 면역이 되고, 존 피해와 언세이프 서클(unsafe circle) 피해를 제외한 모든 피해에도 면역이 됩니다.

**형식 모델:**

- [M-0246](../rules/items.md#m-0246) 해석 A: `Shield와 Safety bubble은 이를 막지 못함. 잠든 참가자는 면역`
- [M-0246](../rules/items.md#m-0246) 해석 B: `자신의 Sleeping Bag에서 65 s 동안 잠을 잔 뒤에만 면역 (상인 페이지)`
- [M-0246](../rules/items.md#m-0246) 정의역: 수면 상태, 수면 시간

**상호작용:** [M-0244](../rules/items.md#m-0244)

**모순:** [C-0203](../unknowns.md#c-0203)

메모 ([M-0246](../rules/items.md#m-0246)): [C-0203](../unknowns.md#c-0203) 참조. '잠든 참가자는 면역입니다' 대 '65초 동안 잠을 자면 flashbang에 면역이 됩니다'.

<a id="m-0247"></a>

### M-0247: Flashbang 대 mirror forcefield

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0247](../rules/items.md#m-0247) `wiki-items-076`: "A mirror forcefield is used up and blinds you instead." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: mirror forcefield는 소모되고 대신 당신을 실명시킵니다.
- [M-0247](../rules/items.md#m-0247) `wiki-items-077`: "Several forcefields are all used up, but you are blinded only once." ([출처](https://iceposeidon.com/safezone/wiki/items#flashbang))
  - 번역: 여러 forcefield는 모두 소모되지만, 실명은 한 번만 됩니다.

**형식 모델:**

- [M-0247](../rules/items.md#m-0247) 해석 A: `mirror가 소모되고 던진 사람을 실명시킴. 피해자들의 여러 mirror는 모두 소모됨. 던진 사람은 한 번만 실명됨`
- [M-0247](../rules/items.md#m-0247) 해석 B: `A와 같고, mirror를 가진 던진 사람은 실명되지 않음 (공격자 mirror 규칙 [M-0239](../rules/items.md#m-0239)가 우선)`
- [M-0247](../rules/items.md#m-0247) 해석 C: `A와 같고, mirror를 가진 던진 사람은 실명됨 (flashbang 규칙이 우선)`
- [M-0247](../rules/items.md#m-0247) 정의역: mirror를 가진 피해자 m >= 0

**상호작용:** [M-0236](../rules/items.md#m-0236), [M-0239](../rules/items.md#m-0239), [M-0244](../rules/items.md#m-0244)

**미해결 질문:**

- [U-0217](../unknowns.md#u-0217) (낮음): Mirror 대 mirror와 flashbang: 던진 사람도 mirror를 가지고 있다면 던진 사람이 실명합니까?
- [U-0201](../unknowns.md#u-0201) (보통): 여러 mirror forcefield는 하나의 효과로 셉니까, 아니면 각각 효과 3개 상한에 하나씩 산입됩니까?
- [U-0215](../unknowns.md#u-0215) (보통): mirror forcefield를 여러 개 가지고 있을 때, 한 번의 반사는 하나를 소모합니까, 전부를 소모합니까, 아니면 여러 번 반사합니까?

<a id="m-0326"></a>

### M-0326: Vulnerability Dart

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0326](../rules/items.md#m-0326) `wiki-merchant-015`: "Vulnerability Dart: 25 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Vulnerability Dart: 블러드 토큰 25개.
- [M-0326](../rules/items.md#m-0326) `wiki-merchant-016`: "Throw it at a contestant within 10m." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 10m 이내의 참가자에게 던집니다.
- [M-0326](../rules/items.md#m-0326) `wiki-merchant-017`: "It removes their Shield and pops every Safety Bubble they own or stand in, and stops Shields and Safety Bubbles protecting them for 10 minutes." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 대상의 Shield를 제거하고, 대상이 소유했거나 안에 서 있는 모든 Safety Bubble을 터뜨리며, 10분 동안 Shield와 Safety Bubble이 대상을 보호하지 못하게 합니다.
- [M-0326](../rules/items.md#m-0326) `wiki-merchant-018`: "They cannot use a Shield or a Safety Bubble while vulnerable." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 취약한 상태에서는 Shield나 Safety Bubble을 사용할 수 없습니다.

**형식 모델:**

- [M-0326](../rules/items.md#m-0326) 해석 A: `거리 <= 10 m의 참가자에게 던짐. 대상의 Shield를 제거하고, 대상이 소유했거나 안에 서 있는 모든 Safety Bubble을 터뜨리며, 10 min 동안 Shield와 Safety Bubble이 대상을 보호하지 못하고 대상은 이를 사용할 수 없음`
- [M-0326](../rules/items.md#m-0326) 정의역: 미터, 분
- [M-0326](../rules/items.md#m-0326) 매개변수 `dart_cost_tokens`: 25
- [M-0326](../rules/items.md#m-0326) 매개변수 `dart_range_m`: 10
- [M-0326](../rules/items.md#m-0326) 매개변수 `vulnerable_duration_min`: 10

**따름 결과:** [T-0402](../theorems/T-0402.md)

**미해결 질문:**

- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?
- [U-0324](../unknowns.md#u-0324) (보통): Vulnerability Dart: 이미 취약한 참가자에게 두 번째 다트를 쓰면 초기화됩니까, 연장됩니까, 아무 일도 없습니까? 10분은 던진 시점부터입니까, 명중한 시점부터입니까?

메모 ([M-0326](../rules/items.md#m-0326)): 터뜨려지는 Safety Bubble에는 다른 참가자도 함께 서 있는 것이 포함됩니다. Safety Bubble 안에 있는 상태에서는 Safety Bubble을 던질 수 없습니다 (Safety Bubble 페이지).

<a id="m-0327"></a>

### M-0327: Sleeping Bag 소유권

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0327](../rules/items.md#m-0327) `wiki-merchant-020`: "Sleeping Bag: 30 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag: 블러드 토큰 30개.
- [M-0327](../rules/items.md#m-0327) `wiki-merchant-025`: "Only you can pick up your bag." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 본인만 자신의 Sleeping Bag을 집어 들 수 있습니다.
- [M-0327](../rules/items.md#m-0327) `wiki-merchant-026`: "You can have only one Sleeping Bag, held or placed." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag은 들고 있든 설치했든 하나만 가질 수 있습니다.
- [M-0327](../rules/items.md#m-0327) `wiki-merchant-027`: "It cannot be dropped or stolen, only destroyed by you." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 떨어뜨리거나 도난당할 수 없으며, 본인만 파괴할 수 있습니다.
- [M-0327](../rules/items.md#m-0327) `wiki-merchant-028`: "Greed can still steal your other items while you sleep." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 당신이 자는 동안에도 Greed는 당신의 다른 아이템을 훔칠 수 있습니다.

**형식 모델:**

- [M-0327](../rules/items.md#m-0327) 해석 A: `토큰 30개. 소유자만 Sleeping Bag을 집어 들 수 있음. 들고 있거나 설치한 Sleeping Bag은 최대 1개. 떨어뜨리거나 도난당할 수 없고 소유자만 파괴할 수 있음. Greed는 잠든 참가자의 다른 아이템을 여전히 훔칠 수 있음`
- [M-0327](../rules/items.md#m-0327) 매개변수 `sleeping_bag_cost_tokens`: 30

메모 ([M-0327](../rules/items.md#m-0327)): Greed 페이지('Sleeping Bags cannot be stolen, but you can steal from a sleeping contestant')와 일치합니다.

<a id="m-0328"></a>

### M-0328: Sleeping Bag 수면 시간대와 행동 불능

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0328](../rules/items.md#m-0328) `wiki-merchant-021`: "Place it and sleep from 18:00 to 06:00 local solar time, for eight hours of sleep in total." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag을 설치하고 현지 태양시 18:00부터 06:00 사이에 자며, 수면 시간은 총 8시간입니다.
- [M-0328](../rules/items.md#m-0328) `wiki-merchant-022`: "While you sleep within 15m of your bag, you cannot act." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag에서 15m 이내에서 자는 동안에는 행동할 수 없습니다.
- [M-0328](../rules/items.md#m-0328) `wiki-merchant-024`: "Wake up to act." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 행동하려면 일어나야 합니다.

**형식 모델:**

- [M-0328](../rules/items.md#m-0328) 해석 A: `Sleeping Bag을 설치하고 현지 태양시 18:00부터 06:00까지 수면, 총 8시간의 수면. Sleeping Bag에서 15 m 이내에서 자는 동안 행동할 수 없음. 행동하려면 일어나야 함`
- [M-0328](../rules/items.md#m-0328) 정의역: 시간, 미터
- [M-0328](../rules/items.md#m-0328) 매개변수 `sleep_window`: 현지 태양시 18:00부터 06:00까지
- [M-0328](../rules/items.md#m-0328) 매개변수 `sleep_total_h`: 8
- [M-0328](../rules/items.md#m-0328) 매개변수 `sleep_radius_m`: 15

**미해결 질문:**

- [U-0325](../unknowns.md#u-0325) (높음): Sleeping Bag: 'sleep from 18:00 to 06:00 ... for eight hours of sleep in total' 규칙은 무엇입니까?
- [U-0326](../unknowns.md#u-0326) (낮음): 'Local solar time'(지역 태양시): 무엇에 대한 지역입니까(참가자의 위치, 이벤트 장소, 기준 도시 하나)?
- [U-0327](../unknowns.md#u-0327) (높음): Sleeping Bag: 65 s의 수면은 연속이어야 합니까? 잠든 사람이 15m 반경을 벗어나거나 깨어나거나 맞으면 어떻게 됩니까? 깨어나면 면역이 즉시 끝납니까?
- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?

<a id="m-0329"></a>

### M-0329: Sleeping Bag 면역

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0329](../rules/items.md#m-0329) `wiki-merchant-019`: "A contestant who has slept in their Sleeping Bag for 65 seconds cannot be targeted." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag에서 65초 동안 잔 참가자는 대상으로 지정될 수 없습니다.
- [M-0329](../rules/items.md#m-0329) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 65초 동안 자고 나면 섬광탄과, 존 피해 및 언세이프 서클(unsafe circle) 피해를 제외한 모든 피해에 면역입니다.

**형식 모델:**

- [M-0329](../rules/items.md#m-0329) 해석 A: `65 s 동안 잔 뒤: 대상으로 지정될 수 없고, 섬광탄과, 존 피해 및 언세이프 서클 피해를 제외한 모든 피해에 면역`
- [M-0329](../rules/items.md#m-0329) 정의역: 초
- [M-0329](../rules/items.md#m-0329) 매개변수 `sleep_immunity_delay_s`: 65

**미해결 질문:**

- [U-0327](../unknowns.md#u-0327) (높음): Sleeping Bag: 65 s의 수면은 연속이어야 합니까? 잠든 사람이 15m 반경을 벗어나거나 깨어나거나 맞으면 어떻게 됩니까? 깨어나면 면역이 즉시 끝납니까?
- [U-0300](../unknowns.md#u-0300) (보통): 무기, 함정, 상인, sleeping bag의 범위 경계(10m, 20m, 50m, 15m)는 포함입니까 미포함입니까? 거리는 지면상의 유클리드 거리입니까?

**모순:** [C-0300](../unknowns.md#c-0300), [C-0301](../unknowns.md#c-0301)

메모 ([M-0329](../rules/items.md#m-0329)): 다른 페이지와 충돌합니다. robot 피해 예외([C-0300](../unknowns.md#c-0300)), 그리고 65 s 지연과 즉시 면역의 차이([C-0301](../unknowns.md#c-0301)).

<a id="m-0330"></a>

### M-0330: Sleeping Bag 재사용 제한

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0330](../rules/items.md#m-0330) `wiki-merchant-029`: "After your bag protects you, you cannot sleep in a bag again for 20 minutes, even if you pick it up and place it again." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: Sleeping Bag이 당신을 보호한 뒤에는, 다시 집어 들어 설치하더라도 20분 동안 어떤 Sleeping Bag에서도 다시 잘 수 없습니다.

**형식 모델:**

- [M-0330](../rules/items.md#m-0330) 해석 A: `Sleeping Bag이 보호한 뒤 20 min 동안 어떤 Sleeping Bag에서도 잘 수 없음. 다시 집어 들어 설치해도 마찬가지`
- [M-0330](../rules/items.md#m-0330) 정의역: 분
- [M-0330](../rules/items.md#m-0330) 매개변수 `sleep_lockout_min`: 20

**미해결 질문:**

- [U-0328](../unknowns.md#u-0328) (높음): Sleeping Bag: 20분의 '다시 잠들 수 없음(cannot sleep again)' 제한은 언제 시작됩니까(bag이 처음 보호하는 순간, 깨어날 때, 마지막으로 막은 피해 시점 중)?

<a id="m-0331"></a>

### M-0331: 상인 미사일

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0331](../rules/items.md#m-0331) `wiki-merchant-030`: "Missile: 10 blood tokens." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 미사일: 블러드 토큰 10개.
- [M-0331](../rules/items.md#m-0331) `wiki-merchant-031`: "Launch a standard missile at an exact map location." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 지도상의 정확한 위치에 표준 미사일을 발사합니다.
- [M-0331](../rules/items.md#m-0331) `wiki-merchant-032`: "It lands 30 seconds after launch." ([출처](https://iceposeidon.com/safezone/wiki/merchant#items))
  - 번역: 발사 30초 후에 떨어집니다.

**형식 모델:**

- [M-0331](../rules/items.md#m-0331) 해석 A: `토큰 10개. 지도상의 정확한 위치에 표준 미사일을 발사. 발사 30 s 후에 떨어짐`
- [M-0331](../rules/items.md#m-0331) 정의역: 토큰, 초
- [M-0331](../rules/items.md#m-0331) 매개변수 `missile_cost_tokens`: 10
- [M-0331](../rules/items.md#m-0331) 매개변수 `missile_delay_s`: 30
- [M-0331](../rules/items.md#m-0331) 매개변수 `missile_damage_hp`: UNKNOWN, [U-0340](../unknowns.md#u-0340) 참조

**미해결 질문:**

- [U-0340](../unknowns.md#u-0340) (높음): 정확한 위치에 30 s 후 떨어진다고 할 때, 상인의 'standard missile'은 피해와 반경이 얼마입니까?
- [U-0321](../unknowns.md#u-0321) (보통): 어떤 상인 구매에 빈 인벤토리 슬롯이 필요합니까('Items need a free inventory slot')?

메모 ([M-0331](../rules/items.md#m-0331)): Smoke bomb은 그 폭탄 안에서 발사하는 것을 막습니다 (Smoke bomb 페이지).

<a id="m-0335"></a>

### M-0335: Body armor 소지 제한

라벨: `DOCUMENTED`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0335](../rules/items.md#m-0335) `wiki-merchant-041`: "Carry at most one Body Armor." ([출처](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
  - 번역: Body Armor는 최대 하나만 소지할 수 있습니다.

**형식 모델:**

- [M-0335](../rules/items.md#m-0335) 해석 A: `소지하는 Body Armor는 최대 1개`

메모 ([M-0335](../rules/items.md#m-0335)): Body Armor 페이지에도 'Carry at most one, including equipped armor'라고 되어 있어 같은 규칙입니다.

<a id="m-0339"></a>

### M-0339: 방어구 인챈트와 감소

라벨: `CONDITIONAL`. 시길: all.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0339](../rules/items.md#m-0339) `wiki-merchant-057`: "Armor enchantment: 30 blood tokens. +10 durability, up to 45." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: Armor enchantment: 블러드 토큰 30개. 내구도 +10, 최대 45까지.
- [M-0339](../rules/items.md#m-0339) `wiki-merchant-058`: "It then loses one durability every twenty minutes, down to 15." ([출처](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
  - 번역: 이후 20분마다 내구도가 1씩 줄어 15까지 내려갑니다.

**형식 모델:**

- [M-0339](../rules/items.md#m-0339) 해석 A: `토큰 30개. 내구도 +10, 최대 45까지. 이후 20 min마다 내구도 1씩 감소, 15까지`
- [M-0339](../rules/items.md#m-0339) 정의역: 내구도는 정수, 분
- [M-0339](../rules/items.md#m-0339) 매개변수 `armor_enchant_cost_tokens`: 30
- [M-0339](../rules/items.md#m-0339) 매개변수 `armor_enchant_bonus`: 10
- [M-0339](../rules/items.md#m-0339) 매개변수 `armor_cap`: 45
- [M-0339](../rules/items.md#m-0339) 매개변수 `armor_decay_interval_min`: 20
- [M-0339](../rules/items.md#m-0339) 매개변수 `armor_decay_floor`: 15

**따름 결과:** [T-0012](../theorems/T-0012.md), [T-0402](../theorems/T-0402.md)

**미해결 질문:**

- [U-0338](../unknowns.md#u-0338) (보통): 방어구 인챈트 '+10 durability, up to 45': 반복 구매할 수 있습니까, 45는 인챈트 후 내구도의 상한입니까, 그리고 어떤 기준값에서 시작합니까?
- [U-0339](../unknowns.md#u-0339) (보통): 인챈트된 방어구 감쇠 'loses one durability every twenty minutes, down to 15': 시계는 언제 시작하고, 피해로 15보다 낮아졌어도 감쇠가 15에서 멈추며, 재인챈트하면 다시 시작합니까?

메모 ([M-0339](../rules/items.md#m-0339)): 기본 방어구 내구도는 이 페이지가 아니라 Body Armor 페이지에 있습니다(거기에는 'Absorbs up to 15 HP of damage'라고 되어 있습니다).

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

<a id="m-0513"></a>

### M-0513: Greed 상자 Shield 확률

라벨: `CONDITIONAL`. 시길: greed.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0513](../rules/items.md#m-0513) `wiki-sigils-greed-010`: "Each real chest you claim has a 25% chance to give you a Shield for 20min." ([출처](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
  - 번역: 획득하는 진짜 상자마다 25% 확률로 20min 동안 Shield를 얻습니다.
- [M-0513](../rules/items.md#m-0513) `wiki-sigils-greed-011`: "No roll while you are vulnerable." ([출처](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
  - 번역: 취약한 상태에서는 확률 판정이 없습니다.
- [M-0513](../rules/items.md#m-0513) `wiki-items-007`: "a Greed chest shield" ([출처](https://iceposeidon.com/safezone/wiki/items#effects))
  - 번역: Greed 상자 shield

**형식 모델:**

- [M-0513](../rules/items.md#m-0513) 해석 A: `취약하지 않은 상태에서 claim(real chest)하면 확률 0.25로 1200 s 동안 Shield를 부여함. 취약한 동안에는 판정이 없음. 이 Shield는 활성 아이템 효과 3개 제한에 포함되지 않음`
- [M-0513](../rules/items.md#m-0513) 해석 B: `기존 Shield와 겹칠 때의 규칙이 정의되어 있지 않음`
- [M-0513](../rules/items.md#m-0513) 정의역: 진짜 상자 획득 1회당. 20 min = 1200 s
- [M-0513](../rules/items.md#m-0513) 매개변수 `p`: 0.25
- [M-0513](../rules/items.md#m-0513) 매개변수 `duration_s`: 1200
- [M-0513](../rules/items.md#m-0513) 매개변수 `stack_rule`: UNKNOWN, see [U-0511](../unknowns.md#u-0511)

**상호작용:** [M-0512](../rules/sigil.md#m-0512)

**미해결 질문:**

- [U-0511](../unknowns.md#u-0511) (보통): Greed 상자 Shield: 참가자가 이미 활성 Shield(아이템 또는 이전 상자 Shield)를 가지고 있으면 어떻게 됩니까?

메모 ([M-0513](../rules/items.md#m-0513)): 아이템 페이지는 Greed 상자 shield가 3개 제한에 포함되는 활성 아이템 효과가 아니라고 명시하므로, 아이템 사용이 아닙니다. 가짜 상자는 판정하지 않습니다 ('real chest'). Shield를 제거하는 Vulnerability Dart가 이 Shield도 제거하는지는 적혀 있지 않으며, Shield 아이템 문구는 Vulnerability Dart가 이를 제거한다고 말합니다.

<a id="m-0518"></a>

### M-0518: Ingenuity 포션 합치기

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0518](../rules/items.md#m-0518) `wiki-sigils-ingenuity-009`: "Combine two matching potions into the next size, up to gigantic." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 같은 포션 두 개를 합쳐 다음 크기로 만들며, gigantic까지 가능합니다.

**형식 모델:**

- [M-0518](../rules/items.md#m-0518) 해석 A: `tier(p1) = tier(p2) < gigantic인 combine(p1, p2) -> 다음 등급의 포션 하나`
- [M-0518](../rules/items.md#m-0518) 해석 B: `같은 종류의 같은 포션 두 개는 무엇이든 합쳐짐`
- [M-0518](../rules/items.md#m-0518) 정의역: 등급 small < medium < large < gigantic. 회복량 5, 10, 20, 40 (아이템 페이지)이므로 합쳐도 손실 없음
- [M-0518](../rules/items.md#m-0518) 매개변수 `results`: small+small=medium; medium+medium=large; large+large=gigantic (합치기 결과)

**상호작용:** [M-0525](../rules/healing.md#m-0525), [M-0526](../rules/healing.md#m-0526)

**미해결 질문:**

- [U-0515](../unknowns.md#u-0515) (낮음): Ingenuity 포션 합치기: "two matching potions"는 무슨 뜻이며, 비용이나 제한이 있습니까?

메모 ([M-0518](../rules/items.md#m-0518)): 비용이나 쿨다운은 명시되어 있지 않습니다. Campfire와 Everything potion의 재료로 쓰입니다. 합친 포션이 풀 또는 회복량을 정합니다.

<a id="m-0519"></a>

### M-0519: Ingenuity 함정 선물

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0519](../rules/items.md#m-0519) `wiki-sigils-ingenuity-010`: "Attach a landmine or C4 to an item to make a trapped gift, once every 16h." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 아이템에 landmine 또는 C4를 붙여 함정 선물을 만듭니다. 16h에 한 번 가능합니다.
- [M-0519](../rules/items.md#m-0519) `wiki-sigils-ingenuity-011`: "Only you can see it is trapped." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 함정이라는 것은 본인만 볼 수 있습니다.

**형식 모델:**

- [M-0519](../rules/items.md#m-0519) 해석 A: `attach(trap in {landmine, C4}, item) -> 함정 선물. 공유 쿨다운 하나 16 h = 57600 s. 소유자만 함정임을 볼 수 있음`
- [M-0519](../rules/items.md#m-0519) 해석 B: `landmine과 C4에 각각 별도의 16 h 쿨다운이 있음`
- [M-0519](../rules/items.md#m-0519) 해석 C: `다른 Ingenuity 참가자도 이를 볼 수 있음`
- [M-0519](../rules/items.md#m-0519) 정의역: 초 단위 시간
- [M-0519](../rules/items.md#m-0519) 매개변수 `cooldown_s`: 57600
- [M-0519](../rules/items.md#m-0519) 매개변수 `trap_types`: landmine, C4

**상호작용:** [M-0517](../rules/sigil.md#m-0517)

**미해결 질문:**

- [U-0516](../unknowns.md#u-0516) (보통): Trapped gift: 16 h 제한은 landmine과 C4 부착이 공유합니까, 그리고 누가 함정을 볼 수 있습니까(소유자만, 아니면 다른 Ingenuity 참가자도)?

메모 ([M-0519](../rules/items.md#m-0519)): C4 페이지는 C4가 '보유한 다른 아이템'에 붙는다고 말하고, Landmine 페이지는 '자신에게 사용하는 아이템'에 붙는다고 말하며, 각각 16h에 한 번을 반복합니다. 피해량(C4 23 HP, landmine 11 HP)은 무기 페이지에 있으며 여기에는 기록하지 않았습니다. 함정 선물은 Body armor를 무시하고 Safety bubble을 통해서도 소지자에게 피해를 줍니다 (아이템 페이지).

<a id="m-0520"></a>

### M-0520: Ingenuity 고유 조합품 제한과 좀비에 의한 파괴

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0520](../rules/items.md#m-0520) `wiki-sigils-ingenuity-012`: "Unique crafts cannot be traded, stolen or looted, and have a 40% chance to be destroyed by Zombie hits." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
  - 번역: 고유 조합품은 거래, 훔치기, 루팅이 불가능하며 좀비 타격으로 파괴될 확률이 40%입니다.
- [M-0520](../rules/items.md#m-0520) `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([출처](https://iceposeidon.com/safezone/wiki/zombies))
  - 번역: 조합한 아이템이 파괴될 확률 40%

**형식 모델:**

- [M-0520](../rules/items.md#m-0520) 해석 A: `조합품 c: 거래 불가, 훔치기 불가, 루팅 불가. 좀비의 흡수 타격마다 모든 조합품에 대해 확률 0.40으로 파괴`
- [M-0520](../rules/items.md#m-0520) 해석 B: `좀비 타격마다 한 번 판정하며 확률 0.40으로 무작위 조합품 하나를 파괴`
- [M-0520](../rules/items.md#m-0520) 해석 C: `좀비와의 접촉 1회당 0.40 판정 한 번`
- [M-0520](../rules/items.md#m-0520) 정의역: 판정당 확률 0.4. 좀비당 타격 빈도는 10 s에 흡수 1회 (가드 좀비는 5 s에 2 HP)
- [M-0520](../rules/items.md#m-0520) 매개변수 `p_destroy`: 0.4
- [M-0520](../rules/items.md#m-0520) 매개변수 `roll_unit`: UNKNOWN, see [U-0518](../unknowns.md#u-0518)

**상호작용:** [M-0522](../rules/items.md#m-0522), [M-0527](../rules/zombies.md#m-0527)

**미해결 질문:**

- [U-0518](../unknowns.md#u-0518) (높음): 고유 조합의 "40% chance to be destroyed by Zombie hits": 굴림은 흡수 타격마다, 좀비마다, 아니면 조합마다 이루어지며, 막힌 타격도 굴립니까?

메모 ([M-0520](../rules/items.md#m-0520)): Ingenuity 페이지와 좀비 페이지는 40%에서 일치합니다 ('unique crafts'와 'crafted items'는 같은 집합). Greed는 이를 훔칠 수 없으며, Black hole과 Fortress도 조합품입니다. 'looted'는 조합품이 묘비 루팅에 들어가지 않음을 암시하지만, 사망 시 운명은 명시되어 있지 않습니다.

<a id="m-0522"></a>

### M-0522: Ingenuity 조합 레시피

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-014`: "Made from Landmine Drone" ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
  - 번역: Landmine Drone으로 만듭니다
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-018`: "Made from Guardian angel Health potion" ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
  - 번역: Guardian angel Health potion으로 만듭니다
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-022`: "Made from Anti poison Health potion" ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-everything_potion))
  - 번역: Anti poison Health potion으로 만듭니다
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-024`: "Made from Safety bubble Zombie repellent" ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
  - 번역: Safety bubble Zombie repellent로 만듭니다
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-027`: "Made from EMP Mirror forcefield" ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-black_hole))
  - 번역: EMP Mirror forcefield로 만듭니다
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-029`: "Made from Shield Body armor" ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))
  - 번역: Shield Body armor로 만듭니다

**형식 모델:**

- [M-0522](../rules/items.md#m-0522) 해석 A: `craft(Robot) = Landmine + Drone; craft(Campfire) = Guardian angel + Health potion; craft(Everything potion) = Anti poison + Health potion; craft(Zombie killer) = Safety bubble + Zombie repellent; craft(Black hole) = EMP + Mirror forcefield; craft(Fortress) = Shield + Body armor; 재료 둘 다 소모됨`
- [M-0522](../rules/items.md#m-0522) 해석 B: `재료 하나만 소모됨`
- [M-0522](../rules/items.md#m-0522) 정의역: 레시피는 라벨에서 읽은 아이템 이름의 순서 없는 쌍
- [M-0522](../rules/items.md#m-0522) 매개변수 `robot`: Landmine,Drone
- [M-0522](../rules/items.md#m-0522) 매개변수 `campfire`: Guardian angel,Health potion (재료)
- [M-0522](../rules/items.md#m-0522) 매개변수 `everything_potion`: Anti poison,Health potion (재료)
- [M-0522](../rules/items.md#m-0522) 매개변수 `zombie_killer`: Safety bubble,Zombie repellent (재료)
- [M-0522](../rules/items.md#m-0522) 매개변수 `black_hole`: EMP,Mirror forcefield
- [M-0522](../rules/items.md#m-0522) 매개변수 `fortress`: Shield,Body armor

**상호작용:** [M-0515](../rules/sigil.md#m-0515), [M-0520](../rules/items.md#m-0520), [M-0521](../rules/economy.md#m-0521)

**미해결 질문:**

- [U-0517](../unknowns.md#u-0517) (높음): Ingenuity 조합: 명시된 재료 두 개가 모두 소모됩니까, 조합 하나가 5개 조합 칸 중 하나를 차지합니까, 그리고 레시피 6개가 5칸에 어떻게 맞습니까?

메모 ([M-0522](../rules/items.md#m-0522)): 라벨은 두 재료 이름을 구분자 없이 이어서 나열하므로, 알려진 아이템 이름(Guardian angel, Health potion, Anti poison, Safety bubble, Zombie repellent, Mirror forcefield, Body armor, Landmine, Drone, EMP, Shield)으로 나눕니다. 합친 포션 크기는 Campfire와 Everything potion에 쓰입니다. 조합품은 3개 효과 아이템 제한에 포함되지 않습니다 (아이템 페이지).

<a id="m-0528"></a>

### M-0528: Black hole 조합품

라벨: `CONDITIONAL`. 시길: ingenuity.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0528](../rules/items.md#m-0528) `wiki-sigils-ingenuity-028`: "Destroys every chest and crate within 200m (656ft), including care packages, airdrops and fake chests." ([출처](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-black_hole))
  - 번역: 200m (656ft) 이내의 모든 상자와 crate를 파괴하며, 보급 상자, 에어드롭, 가짜 상자도 포함합니다.

**형식 모델:**

- [M-0528](../rules/items.md#m-0528) 해석 A: `위치 x에서 사용 -> dist(x, c) <= 200 m인 모든 상자와 crate(보급 상자, 에어드롭, 가짜 상자 포함)를 사용 순간에 파괴함`
- [M-0528](../rules/items.md#m-0528) 해석 B: `명시되지 않은 시간 동안 지속되는 필드`
- [M-0528](../rules/items.md#m-0528) 정의역: 미터 단위 dist 0..200
- [M-0528](../rules/items.md#m-0528) 매개변수 `radius_m`: 200
- [M-0528](../rules/items.md#m-0528) 매개변수 `duration_s`: UNKNOWN, see [U-0523](../unknowns.md#u-0523)

**상호작용:** [M-0521](../rules/economy.md#m-0521), [M-0531](../rules/economy.md#m-0531)

**미해결 질문:**

- [U-0523](../unknowns.md#u-0523) (보통): Black hole: 즉시 발동입니까, 지속됩니까, 어디를 중심으로 하며, 누가 이득을 얻습니까?
- [U-0015](../unknowns.md#u-0015) (높음): 상자 규칙(종류, 획득 범위, 생성 빈도, 내용물)은 무엇입니까? 상자 페이지는 삭제되었습니다(RE-0004).

메모 ([M-0528](../rules/items.md#m-0528)): 어떤 수단으로든 crate를 파괴하면 Trolling에게 지급(누가 생성했든 파괴한 crate당 토큰 1개)될 수 있고, 상자에 대해서는 Ingenuity 토큰도 지급될 수 있습니다 ([M-0521](../rules/economy.md#m-0521)).

<a id="m-0532"></a>

### M-0532: 가짜 상자 설치

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0532](../rules/items.md#m-0532) `wiki-sigils-trolling-007`: "Fake chest: place up to 2 per rolling hour." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 가짜 상자: 롤링 1시간당 최대 2개까지 설치합니다.
- [M-0532](../rules/items.md#m-0532) `wiki-sigils-trolling-008`: "It looks like a care package." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 보급 상자처럼 보입니다.
- [M-0532](../rules/items.md#m-0532) `wiki-sigils-trolling-011`: "It vanishes after 1h." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 1h 후에 사라집니다.

**형식 모델:**

- [M-0532](../rules/items.md#m-0532) 해석 A: `직전 3600 s 동안 설치가 2회 미만일 때에 한해 place(fake chest) 허용. 보급 상자처럼 보임. 설치 3600 s 후에 사라짐`
- [M-0532](../rules/items.md#m-0532) 해석 B: `충전 2개가 1800 s마다 하나씩 회복됨`
- [M-0532](../rules/items.md#m-0532) 해석 C: `시계 기준 1시간당 2개`
- [M-0532](../rules/items.md#m-0532) 정의역: 초 단위 시간
- [M-0532](../rules/items.md#m-0532) 매개변수 `limit`: 2
- [M-0532](../rules/items.md#m-0532) 매개변수 `window_s`: 3600
- [M-0532](../rules/items.md#m-0532) 매개변수 `lifetime_s`: 3600
- [M-0532](../rules/items.md#m-0532) 매개변수 `limit_semantics`: UNKNOWN, see [U-0530](../unknowns.md#u-0530)

**상호작용:** [M-0517](../rules/sigil.md#m-0517), [M-0533](../rules/damage.md#m-0533)

**미해결 질문:**

- [U-0530](../unknowns.md#u-0530) (보통): 가짜 상자 "롤링 1시간당 최대 2개": 설치 시각에 대한 슬라이딩 윈도입니까, 아니면 충전되는 2회분입니까?

메모 ([M-0532](../rules/items.md#m-0532)): 1 h 동안 지속되므로 해석 A에서 활성 개수는 최대 2입니다. 가짜는 Ingenuity만 알아봅니다 ([M-0517](../rules/sigil.md#m-0517)). 위치 제약과 표시되는 아이템은 명시되어 있지 않습니다.

<a id="m-0534"></a>

### M-0534: Fake gravestone

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0534](../rules/items.md#m-0534) `wiki-sigils-trolling-013`: "Fake gravestone: place one, then wait 2h before the next." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: Fake gravestone: 하나를 설치한 뒤 다음 설치까지 2h를 기다립니다.
- [M-0534](../rules/items.md#m-0534) `wiki-sigils-trolling-014`: "It copies the gravestone of an eliminated contestant, or of a random living one while nobody is eliminated." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 탈락한 참가자의 묘비를 복제하며, 탈락자가 없는 동안에는 살아 있는 임의의 참가자의 묘비를 복제합니다.
- [M-0534](../rules/items.md#m-0534) `wiki-sigils-trolling-015`: "Each contestant who tries to loot it is poisoned once." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 이를 루팅하려는 각 참가자는 1회 중독됩니다.

**형식 모델:**

- [M-0534](../rules/items.md#m-0534) 해석 A: `최대 1개 설치. 다음 설치는 설치 후 7200 s 뒤부터 허용. 복제 대상은 트롤이 고른 탈락 참가자의 묘비이며, 탈락자가 없으면 살아 있는 임의의 참가자의 묘비. 이를 루팅하려는 각 참가자는 1회 중독됨(첫 시도에 한함)`
- [M-0534](../rules/items.md#m-0534) 해석 B: `2 h 대기는 이전 fake가 사라지는 시점부터 계산`
- [M-0534](../rules/items.md#m-0534) 해석 C: `복제 대상은 탈락 참가자 중에서 무작위로 선택`
- [M-0534](../rules/items.md#m-0534) 정의역: 시간(초 단위)
- [M-0534](../rules/items.md#m-0534) 매개변수 `cooldown_s`: 7200
- [M-0534](../rules/items.md#m-0534) 매개변수 `lifetime_s`: UNKNOWN, [U-0533](../unknowns.md#u-0533) 참조
- [M-0534](../rules/items.md#m-0534) 매개변수 `copy_source`: UNKNOWN, [U-0534](../unknowns.md#u-0534) 참조
- [M-0534](../rules/items.md#m-0534) 매개변수 `poison`: 참가자당 1회

**상호작용:** [M-0517](../rules/sigil.md#m-0517)

**미해결 질문:**

- [U-0533](../unknowns.md#u-0533) (보통): Fake gravestone: 얼마나 지속되며, 2 h 대기는 설치 시점에 시작됩니까 이전 것이 사라질 때 시작됩니까?
- [U-0534](../unknowns.md#u-0534) (낮음): Fake gravestone 복사 원본: 누군가 탈락했을 때, 탈락한 참가자 중 누구를 복사할지 누가 정합니까?

메모 ([M-0534](../rules/items.md#m-0534)): 독의 세부 사항(1 min 30 s마다 HP 1, 초기화됨, 중첩되지 않음)은 독 페이지에 있으며, fake gravestone은 그곳의 두 가지 중독 원천 중 하나입니다. Mirror forcefield는 이를 공격자에게 되돌립니다. Ingenuity는 fake를 알아봅니다. Death 시길이 fake gravestone을 약탈하는 경우는 기술되어 있지 않습니다.

<a id="m-0537"></a>

### M-0537: 언세이프 서클 방어 아이템 상실

라벨: `CONDITIONAL`. 시길: trolling.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-017`: "loses one defense item or unique craft every five seconds, equipped Body Armor included" ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
  - 번역: 5초마다 방어 아이템 또는 고유 조합 아이템 1개를 잃으며, 장착한 Body Armor도 포함됩니다
- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-024`: "After your first hit, you lose one random defense item or unique craft every five seconds while you stay inside and are not immune." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: 첫 타격 이후, 서클 안에 머무르고 면역이 아닌 동안 5초마다 무작위 방어 아이템 또는 고유 조합 아이템 1개를 잃습니다.
- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-025`: "Defense items are Shields, Safety Bubbles, Guardian Angels, Hazmat Suits, Body Armor, Mirror Forcefields, Flak Jackets, Gas Masks, Zombie Repellents, Anti Poisons and Sleeping Bags." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: 방어 아이템은 Shields, Safety Bubbles, Guardian Angels, Hazmat Suits, Body Armor, Mirror Forcefields, Flak Jackets, Gas Masks, Zombie Repellents, Anti Poisons, Sleeping Bags입니다.
- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-026`: "Equipped Body Armor is not safe." ([출처](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
  - 번역: 장착한 Body Armor도 안전하지 않습니다.

**형식 모델:**

- [M-0537](../rules/items.md#m-0537) 해석 A: `첫 타격부터 서클 안에 있고 면역이 아닌 동안 5 s마다 {Shield, Safety Bubble, Guardian Angel, Hazmat Suit, Body Armor, Mirror Forcefield, Flak Jacket, Gas Mask, Zombie Repellent, Anti Poison, Sleeping Bag} 중 무작위 아이템 1개 또는 고유 조합 아이템 1개를 제거. 첫 상실은 t_hit + 5 s`
- [M-0537](../rules/items.md#m-0537) 해석 B: `첫 상실은 첫 타격 시점`
- [M-0537](../rules/items.md#m-0537) 해석 C: `시계는 진입 시점부터`
- [M-0537](../rules/items.md#m-0537) 정의역: 5 s 주기. 보유한 해당 아이템 중에서 균등 무작위(분포는 명시되지 않음)
- [M-0537](../rules/items.md#m-0537) 매개변수 `period_s`: 5
- [M-0537](../rules/items.md#m-0537) 매개변수 `defense_item_types`: 11
- [M-0537](../rules/items.md#m-0537) 매개변수 `fate`: UNKNOWN, [U-0539](../unknowns.md#u-0539) 참조
- [M-0537](../rules/items.md#m-0537) 매개변수 `clock_start`: UNKNOWN, [U-0538](../unknowns.md#u-0538) 참조

**상호작용:** [M-0536](../rules/damage.md#m-0536)

**미해결 질문:**

- [U-0538](../unknowns.md#u-0538) (높음): 언세이프 서클(unsafe circle) 아이템 손실: 첫 손실은 진입과 첫 타격에 대해 언제 발생합니까?
- [U-0539](../unknowns.md#u-0539) (보통): 언세이프 서클(unsafe circle) 아이템 손실: 잃은 아이템은 파괴됩니까 떨어집니까, "면역 아님" 조건은 시계를 멈춥니까 손실만 건너뜁니까, 그리고 활성 효과(인벤토리가 아닌 것)도 영향을 받습니까?

**모순:** [C-0503](../unknowns.md#c-0503)

메모 ([M-0537](../rules/items.md#m-0537)): 장착한 Body Armor는 명시적으로 안전하지 않습니다. 방어 목록에는 시길 능력인 Reality Shield와 Death Ward가 포함되지 않습니다. 무작위 선택이 균등한지는 명시되어 있지 않습니다.

<a id="m-0620"></a>

### M-0620: Endurance 인벤토리: 3 대신 10슬롯

라벨: `DOCUMENTED`. 시길: endurance.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0620](../rules/items.md#m-0620) `wiki-sigils-endurance-008`: "You have 10 inventory slots instead of 3." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 인벤토리 슬롯이 3개가 아니라 10개입니다.

**형식 모델:**

- [M-0620](../rules/items.md#m-0620) 해석 A: `slots = 10`
- [M-0620](../rules/items.md#m-0620) 매개변수 `inventory_slots`: 10

메모 ([M-0620](../rules/items.md#m-0620)): Slots 라벨([M-0603](../rules/sigil.md#m-0603))과 같은 값입니다. 상인 페이지는 구매를 통해 Endurance에 최대 20까지 허용합니다.

<a id="m-0621"></a>

### M-0621: Endurance 보급 상자 일정

라벨: `CONDITIONAL`. 시길: endurance.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-009`: "Every 2h 30min, a care package falls within 10m (33ft) of you." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 2h 30min마다 보급 상자가 당신으로부터 10m (33ft) 이내에 떨어집니다.
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-013`: "Every 2h 30min, a care package falls within 10m (33ft) of each Endurance contestant." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
  - 번역: 2h 30min마다 각 Endurance 참가자로부터 10m (33ft) 이내에 보급 상자가 떨어집니다.
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-014`: "It lands after 30s." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
  - 번역: 30s 뒤에 착지합니다.
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-010`: "Anyone can claim it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 누구나 가져갈 수 있습니다.
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-015`: "After it lands it is a normal care package: any contestant can claim it." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
  - 번역: 착지한 뒤에는 일반 보급 상자이며, 어떤 참가자든 가져갈 수 있습니다.
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-016`: "It never holds a health potion or drone." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
  - 번역: health potion이나 drone은 절대 들어 있지 않습니다.

**형식 모델:**

- [M-0621](../rules/items.md#m-0621) 해석 A: `t_k = t0 + k*9000 s의 고정 시계. 착지는 t_k + 30 s. 위치는 참가자로부터 10 m 이내`
- [M-0621](../rules/items.md#m-0621) 해석 B: `이전 상자가 수령될 때 타이머가 다시 시작`
- [M-0621](../rules/items.md#m-0621) 정의역: 초 단위
- [M-0621](../rules/items.md#m-0621) 매개변수 `period_s`: 9000
- [M-0621](../rules/items.md#m-0621) 매개변수 `landing_delay_s`: 30
- [M-0621](../rules/items.md#m-0621) 매개변수 `t0`: UNKNOWN, [U-0607](../unknowns.md#u-0607) 참조

**미해결 질문:**

- [U-0607](../unknowns.md#u-0607) (높음): Endurance 보급 상자 "2h 30min마다": 첫 투하는 이벤트 시작 2h30 후입니까, 시길 선택 후입니까, 이전 수령 후입니까, 그리고 어떤 상자가 "자신의 것"입니까?

메모 ([M-0621](../rules/items.md#m-0621)): 낙하 시점과 착지 시점 중 어느 때의 위치인지는 명시되어 있지 않습니다(10m는 상자가 떨어질 때 참가자로부터의 거리입니다). 내용물은 health potion과 drone을 제외한 무작위 아이템입니다.

<a id="m-0624"></a>

### M-0624: Endurance 제한: 거래, 묘비 루팅, 버리기, 줍기 불가

라벨: `CONDITIONAL`. 시길: endurance.

**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):

- [M-0624](../rules/items.md#m-0624) `wiki-sigils-endurance-011`: "You cannot trade, loot gravestones, drop items or pick up dropped items." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 거래하거나, 묘비를 루팅하거나, 아이템을 버리거나, 버려진 아이템을 주울 수 없습니다.
- [M-0624](../rules/items.md#m-0624) `wiki-sigils-endurance-012`: "You can still destroy items, claim chests and take crates." ([출처](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
  - 번역: 아이템 파괴, 상자 수령, 크레이트 획득은 여전히 할 수 있습니다.

**형식 모델:**

- [M-0624](../rules/items.md#m-0624) 해석 A: `행동 {trade, loot_gravestone, drop_item, pickup_dropped_item}은 비활성. {destroy_item, claim_chest, take_crate, claim_care_package}는 활성`
- [M-0624](../rules/items.md#m-0624) 해석 B: `A에 더해, 다른 사람에게서 오는 거래 제안도 거부됨`

**미해결 질문:**

- [U-0610](../unknowns.md#u-0610) (보통): Endurance의 "cannot trade, loot gravestones, drop items or pick up dropped items": 거래 금지는 다른 사람의 제안 수신, 선물 주기, 부활로 돌려받는 아이템도 포함합니까?

메모 ([M-0624](../rules/items.md#m-0624)): 묘비 루팅이 비활성이므로 Endurance 참가자는 무덤을 약탈하거나 거기서 아이템을 얻을 수 없습니다. 보급 상자 수령은 토큰 획득 규칙에 의해 허용됩니다.

## 시뮬레이션 검증

`sim/tests/`에 테스트가 있는 정리: [T-0007](../theorems/T-0007.md), [T-0008](../theorems/T-0008.md), [T-0012](../theorems/T-0012.md), [T-0302](../theorems/T-0302.md), [T-0305](../theorems/T-0305.md), [T-0402](../theorems/T-0402.md), [T-0407](../theorems/T-0407.md), [T-0408](../theorems/T-0408.md), [T-0702](../theorems/T-0702.md), [T-0706](../theorems/T-0706.md)

## 미해결 질문

[U-0003](../unknowns.md#u-0003), [U-0005](../unknowns.md#u-0005), [U-0015](../unknowns.md#u-0015), [U-0101](../unknowns.md#u-0101), [U-0120](../unknowns.md#u-0120), [U-0122](../unknowns.md#u-0122), [U-0200](../unknowns.md#u-0200), [U-0201](../unknowns.md#u-0201), [U-0202](../unknowns.md#u-0202), [U-0205](../unknowns.md#u-0205), [U-0206](../unknowns.md#u-0206), [U-0207](../unknowns.md#u-0207), [U-0208](../unknowns.md#u-0208), [U-0210](../unknowns.md#u-0210), [U-0211](../unknowns.md#u-0211), [U-0212](../unknowns.md#u-0212), [U-0213](../unknowns.md#u-0213), [U-0215](../unknowns.md#u-0215), [U-0216](../unknowns.md#u-0216), [U-0217](../unknowns.md#u-0217), [U-0218](../unknowns.md#u-0218), [U-0300](../unknowns.md#u-0300), [U-0321](../unknowns.md#u-0321), [U-0324](../unknowns.md#u-0324), [U-0325](../unknowns.md#u-0325), [U-0326](../unknowns.md#u-0326), [U-0327](../unknowns.md#u-0327), [U-0328](../unknowns.md#u-0328), [U-0338](../unknowns.md#u-0338), [U-0339](../unknowns.md#u-0339), [U-0340](../unknowns.md#u-0340), [U-0504](../unknowns.md#u-0504), [U-0505](../unknowns.md#u-0505), [U-0506](../unknowns.md#u-0506), [U-0511](../unknowns.md#u-0511), [U-0515](../unknowns.md#u-0515), [U-0516](../unknowns.md#u-0516), [U-0517](../unknowns.md#u-0517), [U-0518](../unknowns.md#u-0518), [U-0523](../unknowns.md#u-0523), [U-0530](../unknowns.md#u-0530), [U-0533](../unknowns.md#u-0533), [U-0534](../unknowns.md#u-0534), [U-0538](../unknowns.md#u-0538), [U-0539](../unknowns.md#u-0539), [U-0607](../unknowns.md#u-0607), [U-0610](../unknowns.md#u-0610)

## 신뢰도

`CONTRADICTED`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.
