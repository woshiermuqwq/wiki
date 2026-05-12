Customizing 生物 AI
==================

MythicMobs 提供 the ability to program 自定义 生物 AI in your 生物
which 允许 for a huge 数量 of additional customization as to how
生物 攻击, what targets they choose to 攻击, and 其他 动作.

In the following sections I will provide some 示例 on how to
configure a couple common scenarios that you may want to use on your
服务器.

**注意 on 玩家:**
By 默认, MythicMobs uses a 权限 system for 玩家 to be considered part of a 阵营. If a 玩家 has the 权限 `faction.(factionname)`, 它们将 be considered in the 阵营.

This 行为 can be overridden using the API by registering a 自定义 阵营 provider.

AI 目标, Targets, and 阵营
-------------------------------

- 自定义 AI 通常 需要 two things configured 为了 work.
    You need **AI 目标**, which tell the 生物 how it should act, and you
    need **AI Targets** which tells the 生物 how it should 目标 things.
- **阵营** 用于 separate 生物 into groups and 将 used
    later for more advanced configurations.
- By 默认, most (并非所有) Minecraft 生物 have some sort of internal
    列表 of AI 目标 that tells them how their AI should work. As an
    示例, the Skeleton AI says that it should 目标 玩家 and that
    it should use the arrow 攻击 选项 when attacking said 玩家.
- In order to re-program AI using MythicMobs we must first clear its
    AI 目标 and targets and then 添加 new objectives to these areas.
- 自定义 AI 不 work with all 生物. Some 生物, 例如 the
    Enderdragon, are hard-coded and 不能 be changed. **Attempting to
    change the AI on these may even crash your 服务器, so be wary and
    use test environments!**

<!-- -->
```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&aa decaying skeleton'
  Health: 15
  Damage: 1
  Faction: Undead
  AIGoalSelectors:
  - clear
  - arrowattack
  AITargetSelectors:
  - clear
  - players
  Options:
    FollowRange: 10
    MovementSpeed: 0.2
    PreventOtherDrops: true
```
- This 示例 shows how the Skeleton AI 通常 works for
    attacking. (minus all the fluff, 例如 randomly walking around).

<!-- -->

        * The **AIGoalSelectors** section tells the Skeleton 生物 to use the **arrowattack** 动作 when 它是 going about its day to day AI 目标.
        * The **AITargetSelectors** section tells the Skeleton 生物 that it should look to 目标 玩家 to use the **arrowattack** 动作 on.
        * As you see **clear** is 总是 first, which 在此情况下 wipes the 生物 AI so you have a clean slate to work with. This is important 否则 your AI 可能不 function the way you would expect.
    * Now lets say we want the skeleton to 攻击 其他 生物 instead and we want him to use a melee 攻击 而不是 a ranged 攻击. See below for how we accomplish this.

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&aa decaying skeleton'
  Health: 15
  Damage: 1
  Faction: Undead
  AIGoalSelectors:
  - clear
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - otherfactionmonsters
  Equipment:
  - COS_WoodSword HAND
  Options:
    FollowRange: 10
    MovementSpeed: 0.2
    PreventOtherDrops: true
```

- The skeleton AI now is programmed to 攻击 其他 生物, and any 生物
    that 攻击 it first. In addition, it将usethe melee 攻击。
    而不是 ranged 攻击.

<!-- -->

        * The **AIGoalSelectors** section now has the **meleeattack** AI 目标 which says to 攻击 using melee. It 应为 noted that you must equip the skeleton with a sword now so he can use the melee 攻击 自从 you 不能 melee with a bow equipped (the skeletons 默认 weapon) This would not be 必需 但是 for a zombie.
        * The **AITargetSelectors** section now has the **玩家** 目标 removed so the skeleton 不会 actively engage 玩家. Instead 它有 the **其他factionmonsters** 目标, which tells it that it should 攻击 any monsters 即 not in its own 阵营 (在此情况下 Undead). There is 也 **hurtbytarget** selector with a priority of 1 which says that if any 其他 实体 攻击 the skeleton first (例如 a 玩家) then 它将 retaliate. This 目标 selector is a common one that 应为 set as a higher priority so that 生物 不要 end up being exploitable. Without this here, the 玩家 could kill the skeleton 没有 it attacking back which 通常 不是 wanted.

- For 一系列 all the 目标 and AI 目标 selectors please see [生物 自定义 AI](/生物/自定义-AI)

<!-- -->

- In the next two sections I will provide some 示例 for AI
    configuration for two common scenarios you may wish to implement on
    your 服务器.

示例 1: Guards 攻击 nearby monsters
----------------------------------------

- In this scenario we want to setup some guards at the entrance to our
    city which should repel monsters that wander 也 close. You could
    use an Iron Golem for this function disguised as a villager, but
    their AI harder to control and 它们有 special knock-up 攻击
    that make it unfair 对于 生物, so 我们是 going to use MythicMobs'
    自定义 AI to accomplish the same thing in a better way.
- The first thing we need is a beefy guard 生物 to protect our town.
    Lets create a skeleton disguised as a villager, and equip him with a
    sword.

<!-- -->

```yaml
SummonedGuard1:
  Type: skeleton
  Display: '&Ea town guard'
  Health: 500
  Damage: 5
  Equipment:
  - COS_StoneSword HAND
  Options:
    Despawn: true
    FollowRange: 5
    AlwaysShowName: false
    MovementSpeed: 0.35
    PreventOtherDrops: true
    KnockbackResistance: 1
    PreventMobKillDrops: true
  Disguise: villager
```

- So if we tie this 生物 to a 生物 生成器 at our gates, he going to
    go 攻击 all of our 玩家 in the town so we need to make some
    ad仅ments to make him friendly.

<!-- -->

```yaml
SummonedGuard1:
  Type: skeleton
  Display: '&Ea town guard'
  Health: 500
  Damage: 5
  Equipment:
  - COS_StoneSword HAND
  Faction: Guard
  AIGoalSelectors:
  - clear
  - opendoors
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - otherfactionmonsters
  Options:
    Despawn: true
    FollowRange: 5
    AlwaysShowName: false
    MovementSpeed: 0.35
    PreventOtherDrops: true
    KnockbackResistance: 1
    PreventMobKillDrops: true
  Disguise: Villager
```

- Now the 生物 will 目标 其他 阵营 containing monsters 除此之外
    his own and will 目标 任何人 that hurts him (this will keep some
    of our less ethical 玩家 from killing our guards 对于 hell of
    it) He 还将 open any doors in his way to get to his 目标.
- So 这是 the first half of the problem. Next we need to ensure
    that our monsters 即 roaming outside our walls will 攻击
    back 再次st our guards.
- Below we will grab our Decaying Skeleton 生物 and configure him as
    such.

<!-- -->

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&aa decaying skeleton'
  Health: 15
  Damage: 1
  Faction: Undead
  AIGoalSelectors:
  - clear
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - players
  Equipment:
  - COS_RawHead HEAD
  - COS_WoodSword HAND
  Options:
    Despawn: true
    FollowRange: 10
    AlwaysShowName: false
    MovementSpeed: 0.2
    PreventOtherDrops: true
```

- Our decaying skeleton is now in the Undead 阵营 (different then
    the Guard 阵营) and so he 将 attacked by the guard. Also, by
    adding the **hurtbytarget** 目标 selector, our decaying skeleton
    will now fight back if engaged with a guard (and ultimately die)
- For any 其他 生物 we have that 生成 near the town, we would want
    to 添加 the same AI 目标 and Targets as configured above 对于
    skeleton making sure that the 生物 has a different 阵营 then the
    guard.

<!-- -->

- Now when we setup our 生物 生成器 for our town guard at the gates,
    he will repel monsters but 忽略 玩家 (只要y leave the
    guard alone)
- Some additional 设置 that we would 可能 want to set in this
    case are a short follow 范围 对于 guard (5 在此情况下) and a
    short leash 范围 对于 生物 生成器. This will ensure that the
    guard 不 go off on a rampage and kill all the monsters that we
    want our 玩家 to be able to kill for experience and loots. We
    也 want to ensure that the guard has the **PreventMobKillDrops**
    设为 true so that his kills 不要 掉落 exp/loot for our 玩家.

示例 2: Orcs and Goblins 攻击 彼此
---------------------------------------------

- So in our 世界 we have two 阵营, the goblins and the orcs and
    它们会n't like 彼此 much. We have a battlefield setup where
    它们是 at constant war 除了 现在 它们是 两者都 using the
    skeleton 生物 类型 with its 默认 AI and 它们是n't doing much
    fighting.
- We want to configure them using Mythic 生物 自定义 AI so that they
    fight 彼此 when nearby in addition to any 玩家 that wander
    到 battlefield.
- Lets create an Orc 生物 and a Goblin 生物.

<!-- -->

```yaml
OrcCenturion:
  Type: villagezombie
  Display: '&aan orc centurion'
  Health: 50
  Damage: 4
  Faction: Orcs
  AIGoalSelectors:
  - clear
  - opendoors
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - specificfactionmonsters Goblin
  - players
  Equipment:
  - C_DeathfistSkullcap HEAD
  - C_DeathfistTunic CHEST
  - C_DeathfistLeggings LEGS
  - C_DeathfistBoots FEET
  - COS_WoodSword HAND
  Options:
    Despawn: true
    FollowRange: 10
    AlwaysShowName: false
    MovementSpeed: 0.25
    PreventOtherDrops: true
    PreventItemPickup: true
    KnockbackResistance: 0.25
    PreventMobKillDrops: true
```
```yaml
GoblinBattlemaster:
  Type: zombie
  Display: '&aa goblin battlemaster'
  Health: 80
  Damage: 4
  Faction: Goblin
  AIGoalSelectors:
  - clear
  - opendoors
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - specificfactionmonsters Orcs
  - players
  Equipment:
  - COS_BronzeHead HEAD
  - COS_BronzeChest CHEST
  - COS_BronzeLegs LEGS
  - COS_BronzeFeet FEET
  - COS_WoodAxe HAND
  Skills:
  - skill{s=BashI} ~onAttack >0 0.25
  Options:
    Despawn: true
    FollowRange: 10
    AlwaysShowName: false
    MovementSpeed: 0.25
    PreventOtherDrops: true
    PreventItemPickup: true
    KnockbackResistance: 0.4    
    PreventMobKillDrops: true
```
- So 有 few things we've configured here of 注意.

<!-- -->

        * First we have set the orc 生物 on the **Orc 阵营** and the Goblin 生物 on the **Goblin 阵营**. This will logically separate the two 生物 类型.
        * Next we configure 两者都 of the 生物 与 standard **clear, opendoors, and meleeattack** 动作 即 common for most melee 类型 生物.
        ** Lastly we clear our AI then setup three AI 目标选择器.

            * First is the **hurtbytarget** selector which as mentioned 之前 is a good fall back 选项 so that 生物 can not be exploited by 其他 生物 or 玩家 that 它们将 not retaliate 再次st.
        ** Next is the **specifictargetfaction** selector 与 opposing 阵营 in it. This is set to priority 2 so the goblins and orcs will 目标 彼此 first when 它们是n't 已经 in 战斗
            * Last is the **玩家** 目标 selector which tells that 生物 to 攻击 玩家 if 没有 goblins/orcs nearby.
    * Lastly remember to set the **PreventMobKillDrops** to true so that warring npc 阵营 不要 掉落 exp / loots for 玩家 that happen to wander by.
    * If we have 其他 goblin or orc 生物 类型, we need 仅 copy and paste these AI configurations 到ir 生物 setups and they should react similarly to the two 生物 above.