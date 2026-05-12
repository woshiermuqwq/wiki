**战力 等级**

技能 战力 is an 属性 available to all 技能 that increases the potency of 技能. Base 属性 set in the 生物 configuration 不会 be affected by 战力 等级. It is primarily used as a way to increase 技能 战力 with a 生物 等级, and can 仅 be applied using [等级 Modifiers](/生物/等级). Some 机制 have certain 属性 that can be multiplied by 战力 等级.

Future builds will allow you to define a scaling factor on it. In current builds 它是 not possible to turn off the affection of 战力 等级 when using 机制 除了 对于 [弹射物](/技能/机制/弹射物) and [制导弹射物](/技能/机制/制导弹射物) 机制. If you 不要 wish to utilize 战力 等级 仅仅 不要 use them in the 等级 modifiers.

机制 即 affected by 战力 等级 + formulas:

| 机制 | 属性 | 战力 等级 效果 |
| ------------- | ----------| ----------------------------------------------------- |
| [basedamage](/技能/机制/basedamage) | {multiplier=M} | 伤害 = M * 战力 |
| [consume](/技能/机制/consume) | {伤害=D} | 伤害 = D * 战力 |
| [consume](/技能/机制/consume) | {heal=H} | heal = H * 战力 |
| [伤害](/技能/机制/伤害) | {数量=A} | 伤害 = A * 战力 |
| [leap](/技能/机制/leap) | {速度向量=V} | 速度向量 = V * ( 1 + 战力 * 0.1 ) |
| [弹射物](/技能/机制/弹射物) | {速度向量=V} | 速度向量 = V * 战力 |
| [弹射物](/技能/机制/弹射物) | {maxrange=MR} | maxrange = MR * 战力 |
| [制导弹射物](/技能/机制/制导弹射物) | {速度向量=V} | 速度向量 = V * 战力 |
| [制导弹射物](/技能/机制/制导弹射物) | {maxrange=MR} | maxrange = MR * 战力 |

**示例**
```
ThornySkeleton:
  Type: SKELETON
  Health: 20
  LevelModifiers:
    Health: 10
    Power: 1
  Skills:
  - damage{amount=5} @trigger ~onDamaged
```
In this 示例, a 等级 2 ThornySkeleton has a 战力 of 2 (base of 1, +1 from its LevelModifiers), so its 技能 would do 10 伤害 自从 the 伤害 数量 属性 is multiplied by its 战力.\
A 等级 3 ThornySkeleton would do 15 伤害 由于 3 战力, and so on.