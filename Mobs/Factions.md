# 自定义生物 AI

MythicMobs 提供了在生物中编写自定义 AI 的能力，让你可以大量定制生物如何攻击、选择什么目标进行攻击以及其他行为。

在接下来的部分中，我将提供一些示例来说明如何配置几个常见的场景，这些场景可能正是你希望在自己的服务器上实现的。

**关于玩家的说明：**
默认情况下，MythicMobs 使用权限系统来判断玩家是否属于某个阵营。如果玩家拥有权限 `faction.(阵营名)`，他们就会被视为该阵营的成员。

此行为可以通过 API 注册自定义阵营提供者来覆盖。

## AI 目标、攻击目标和阵营

- 自定义 AI 通常需要配置两个部分才能工作。
  你需要**AI 目标（AI Goals）**，告诉生物应该如何行动；还需要**AI 攻击目标（AI Targets）**，告诉生物如何选择目标。
- **阵营（Factions）**用于将生物划分为不同的群组，稍后会用于更高级的配置。
- 默认情况下，大多数（不是全部）Minecraft 生物都有某种内部的 AI 目标列表，告诉它们的 AI 应该如何运作。例如，骷髅的 AI 规定了它应该以玩家为目标，并且在攻击玩家时应该使用射箭的方式。
- 要使用 MythicMobs 重新编写 AI，我们必须首先清空 AI 目标和攻击目标，然后在其中添加新的指令。
- 自定义 AI 并非适用于所有生物。有些生物（如末影龙）是硬编码的，无法更改。**试图更改这些生物的 AI 甚至可能导致服务器崩溃，所以请务必小心，使用测试环境！**

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&a一具腐朽的骷髅'
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

- 这个例子展示了骷髅 AI 如何进行攻击的基本原理（去掉了随机走动等额外行为）。

      * **AIGoalSelectors** 部分告诉骷髅生物在执行日常目标时使用 **arrowattack**（射箭）动作。
      * **AITargetSelectors** 部分告诉骷髅生物应该以玩家为目标来执行 **arrowattack** 动作。
      * 如你所见，**clear** 总是排在最前面，它会清空生物原有的 AI，让你有一个干净的基础开始配置。这很重要，否则你的 AI 可能不会按预期的方式运行。

- 现在假设我们想让骷髅攻击其他生物，并且使用近战攻击而不是远程攻击。下面是实现方式：

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&a一具腐朽的骷髅'
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

- 现在这个骷髅 AI 被编程为攻击其他生物，以及攻击任何先动手攻击它的实体。此外，它将使用近战攻击而不是远程攻击。

      * **AIGoalSelectors** 部分现在加入了 **meleeattack**（近战攻击）目标，表示使用近战方式进行攻击。需要注意的是，你必须给骷髅装备一把剑才能使用近战攻击，因为你不能用弓（骷髅的默认武器）进行近战。不过对于僵尸来说就不需要额外的装备。
      * **AITargetSelectors** 部分现在移除了 **players** 目标，所以骷髅不会主动攻击玩家。取而代之的是 **otherfactionmonsters** 目标，告诉它攻击不属于自己阵营的任何怪物（在本例中为 Undead）。还有优先级为 1 的 **hurtbytarget** 选择器，表示如果任何其他实体先攻击了骷髅（比如玩家），它会进行反击。这个目标选择器很常用，应该设置为较高的优先级，这样生物就不会被玩家卡 Bug 利用。如果没有它，玩家就可以在骷髅不还手的情况下击杀它，这通常不是想要的效果。

- 所有目标选择器和 AI 目标列表请参见[生物自定义 AI](/Mobs/Custom-AI)

- 在接下来的两个部分中，我将提供两个常见场景的 AI 配置示例，你可能希望在自己的服务器上实现。

## 示例 1：守卫攻击附近的怪物

- 在这个场景中，我们想在城门口设置一些守卫来击退靠得太近的怪物。你可以用铁傀儡伪装成村民来实现这个功能，但铁傀儡的 AI 更难控制，而且它们有特殊的击飞攻击，对怪物来说不公平。所以我们将使用 MythicMobs 的自定义 AI 来以更好的方式实现同样的效果。
- 首先我们需要一个强壮的守卫生物来保护我们的城镇。让我们创建一个伪装成村民的骷髅，并给他装备一把剑。

```yaml
SummonedGuard1:
  Type: skeleton
  Display: '&E城镇守卫'
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

- 如果我们把这个生物绑定到城门处的刷怪笼，它会去攻击我们城镇里的所有玩家，所以我们需要做一些调整让它变得友好。

```yaml
SummonedGuard1:
  Type: skeleton
  Display: '&E城镇守卫'
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

- 现在这个生物会以自己阵营之外的其他含有怪物的阵营为目标，也会攻击任何伤害它的实体（这可以防止一些不道德的玩家为了好玩而击杀我们的守卫）。它还会在路径上打开任何门以到达目标。
- 这只是问题的一半。接下来我们需要确保在城外游荡的怪物会对我们的守卫进行还击。
- 下面我们拿出之前的腐朽骷髅生物，进行如下配置。

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&a一具腐朽的骷髅'
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

- 我们的腐朽骷髅现在属于 Undead 阵营（与 Guard 阵营不同），所以它会被守卫攻击。同时，通过添加 **hurtbytarget** 目标选择器，我们的腐朽骷髅在被守卫攻击时会进行反击（并最终被消灭）。
- 对于我们在城镇附近生成的其他任何生物，我们需要添加与上面骷髅相同的 AI 目标和攻击目标配置，确保生物所属的阵营与守卫不同。

- 现在，当我们在城门口设置城镇守卫的刷怪笼时，他会击退怪物但忽略玩家（只要玩家不去招惹守卫）。
- 在这种情况下，我们可能还需要设置一些额外的选项，比如守卫的跟随距离较短（本例中为 5），以及刷怪笼的牵引范围较短。这可以确保守卫不会四处乱跑把所有怪物都杀了——那些怪物是我们希望玩家能击杀以获取经验和战利品的。我们还需要确保守卫的 **PreventMobKillDrops** 设置为 true，这样它的击杀不会给玩家掉落经验/战利品。

## 示例 2：兽人和地精互相攻击

- 在我们的世界里有两个阵营：地精和兽人，他们彼此不太友好。我们设置了一个战场，他们处于持续的战争中，但眼下他们都使用默认 AI 的骷髅生物类型，几乎没有在打架。
- 我们想使用 MythicMobs 自定义 AI 配置它们，让它们在附近时互相攻击，同时也会攻击进入战场的玩家。
- 让我们创建一个兽人生和一个地精生物。

```yaml
OrcCenturion:
  Type: villagezombie
  Display: '&a兽人百夫长'
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
  Display: '&a地精战斗大师'
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

- 这里有几点需要注意的配置。

      * 首先，我们把兽人生设置为 **Orcs 阵营**，把地精生物设置为 **Goblin 阵营**。这在逻辑上把两种生物类型区分开来。
      * 接下来，我们为两个生物都配置了标准的 **clear、opendoors 和 meleeattack** 动作，这对于大多数近战型生物来说是常见的设置。
      * 最后我们清空 AI，然后设置了三个 AI 攻击目标选择器。
          * 第一个是 **hurtbytarget** 选择器，如前所述，这是一个很好的后备选项，防止生物被其他生物或玩家攻击时无法还击而被卡 Bug 利用。
          * 第二个是 **specificfactionmonsters** 选择器，填入了对立阵营的名称。这个优先级设为 2，所以地精和兽人在没有进入战斗状态时会优先选择对方作为目标。
          * 最后一个是 **players** 目标选择器，告诉生物在附近没有地精/兽人时攻击玩家。
      * 最后，记得将 **PreventMobKillDrops** 设置为 true，这样交战的 NPC 阵营不会给路过的玩家掉落经验和战利品。
      * 如果我们还有其他地精或兽人的生物类型，只需要将这些 AI 配置复制粘贴到它们的生物设置中，它们就会表现出与以上两个生物相似的行为。
