![](http://fs5.directupload.net/images/160325/wrovw3y5.jpg)

技能 战力 is an 属性 available to all 技能 that increases the
potency of 技能. Base 属性 set in the 生物 configuration 不会
be affected by 战力 等级. It is primarily used as a way to increase
技能 战力 with a 生物 等级, and can 仅 be applied using [等级
Modifiers](/生物/等级). Some 技能 have certain
属性 that can be multiplied by 战力 等级.

Future builds will allow you to define a scaling factor on it. In
current builds 它是 not possible to turn off the affection of 战力
等级 when using 技能 除了 对于
[弹射物](/技能/技能/弹射物) and
[制导弹射物](/技能/技能/制导弹射物) 技能. If you 不要 wish to
utilize 战力 等级 仅仅 不要 use them in the 等级 modifiers.

**技能 受 战力 等级 + formulas:**

- [basedamage](/技能/技能/basedamage){multiplier=M} - 伤害 =
    M \* 战力
- [consume](/技能/技能/consume){伤害=D} - 伤害 = D \* 战力
- [consume](/技能/技能/consume){heal=H} - heal = H \* 战力
- [伤害](/技能/技能/伤害){数量=A} - 伤害 = A \* 战力
- [leap](/技能/技能/leap){速度向量=V} - 速度向量 = V \* ( 1 +
    战力 \* 0.1 )
- [弹射物](/技能/技能/弹射物){速度向量=V} - 速度向量 =
    V \* 战力
- [弹射物](/技能/技能/弹射物){maxrange=MR} - maxrange =
    MR \* 战力
- [制导弹射物](/技能/技能/制导弹射物){速度向量=V} - 速度向量 = V \*
    战力
- [制导弹射物](/技能/技能/制导弹射物){maxrange=MR} - maxrange = MR \*
    战力

示例
--------

In this 示例, a 等级 2 ThornySkeleton would do 10 伤害 而不是
5 因为 it gains +1 战力 per 等级 (base 战力 of 1 + 1 per 等级 =
2, 5\*2 = 10). A 等级 3 ThornySkeleton would do 15 伤害, and so on.

    ThornySkeleton:
      Type: SKELETON
      Health: 20
      LevelModifiers:
        Health: 10
        Power: 1
      Skills:
      - 伤害{a=5} @触发器 ~onDamaged