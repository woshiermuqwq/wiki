[[_TOC_]]

## 概述

条件用于决定某个动作是否可以执行。

条件可在以下位置使用[1]：
-   [技能](/skills/mechanics/skill)
-   [掉落表](/drops/Drops#drop-tables)
-   [生成器](/Spawners)
-   [随机生成](/Random%20Spawns)

当应用多个条件时，必须全部满足，技能才会执行。部分条件支持以逗号分隔的数组，此类条件只需数组中的任意一个字符串匹配即可。

要了解如何使用内联条件，[请点此查看！](/skills/Inline-Conditions)


## 类型

条件可分为四类：

1. 实体条件：检查某个实体的条件。
2. 位置条件：检查某个位置的条件。如果以实体为目标时使用了位置条件，则检查该实体所在位置的条件。
3. 比较条件：检查两个不同「事物」之间的某些条件。例如 "Cuboid"（长方体）会在目标位于以两个坐标为顶点的长方体内部时返回 true。
4. 元条件：它们不一定会直接检查施法者或目标对象的任何内在属性。例如 "StringEquals" 会根据两个字符串是否匹配来返回 true 或 false。这些字符串*可以*是通过占位符获取的施法者或目标值，但那只是其中一种应用方式。

## 用法
条件还可以在元技能内部的三个不同位置使用：

#### 普通条件（Conditions）
此部分的条件检查施法者或其所在位置。
```yaml
  Conditions:
  - health{h=>10}
```
> 检查施法者生命值是否高于 10 点。

```yaml
  Conditions:
  - globalscore{objective=Test;v=>10}
```
> 在上面的例子中，globalscore 条件会检查施法者的全局计分板值。

##
#### 目标条件（TargetConditions）
此部分的条件检查元技能的[继承目标](/Skills/Metaskills#inheritance)。

```yaml
  TargetConditions:
  - health{h=>10}
```
> 检查继承到的目标实体生命值是否高于 10 点，只有满足这一条件的实体才会作为继承目标被元技能继续使用。如果没有任何实体满足，默认情况下元技能将不会执行。

```yaml
  TargetConditions:
  - globalscore{objective=Test;v=>10}
```
> 在上面的例子中，globalscore 条件会检查继承目标的全局计分板值。由于 globalscore 是实体条件，只有在目标是实体时才会生效。

##
#### 触发者条件（TriggerConditions）
此部分的条件检查元技能的触发者。
```yaml
  TriggerConditions:
  - health{h=>10}
```
> 检查元技能的触发者生命值是否高于 10 点。

## 范围值
范围值使用 **#to#** 或 **#-#** 格式。若想使用负数范围，须用 "to" 代替 "-"。例如：
```yaml
YourMagnificentSkill:
  Conditions:
    - altitude{a=1-5}
  TargetConditions:
    - distance{d=1to10} true
  TriggerConditions:
    - distance{d=1to10} true
```

## 条件操作

条件操作让你可以根据条件的结果做出额外的行为。默认条件操作是 **true**。

| 操作                          | 描述                                                               |
|------------------------------|-------------------------------------------------------------------|
| `true`                       | 条件满足时该技能会执行                                               |
| `false`                      | 条件满足时该技能*不会*执行                                           |
| `power` [乘数]               | 将技能的强度乘以 `乘数` 的值（例如 power 2.0 会使技能强度翻倍）         |
| `cast` [技能名]              | 条件满足时额外施放一个技能，不影响原技能的执行                           |
| `castinstead` [技能名]       | 条件满足时改为施放另一个技能                                          |
| `orElseCast` [技能名]        | 条件不满足时改为施放另一个技能                                        |

<!--
| `level`        |                                                                                       |
-->

```yaml
  Conditions:
  - day true
  Skills:
  - message{m="It's day!"} @self
```
> 仅在施法者所在世界为白天时执行。

```yaml
  Conditions:
  - day false
  Skills:
  - message{m="It's *not* day!"} @self
```
> 仅在施法者所在世界*不是*白天时执行。
> 与 `true` 相反的行为。

```yaml
ExampleSkill:
  Conditions:
  - day true
  - sunny orElseCast OtherSkill
  Skills:
  - message{m="It's day and sunny!"} @self

OtherSkill:
  Skills:
  - message{m="It's day and not sunny!"} @self
```
> 如果某条条件未达成*（条件满足但条件操作为 false，或反之）*，[后续条件将不再检查](https://en.wikipedia.org/wiki/Short-circuit_evaluation)。
> 因此，即使 OtherSkill 是由于 `sunny` 条件被执行，我们也能确保 `day` 条件一定已经满足了，否则整个技能一开始就不会执行——
> 因为 `day true`
> 在 `sunny orElseCast OtherSkill`
> 之前被检查。

```yaml
YourAwesomeSkill:
  Conditions:
  - day true
  TargetConditions:
  - stance{s=defensive} power 0.5
  TriggerConditions:
  - stance{stance=defensive} power 0.5
  - score{objective=test;value=>20} false
  - haspotioneffect{type=POISON;level=>0;duration=0to100} true
```


## 复合条件
条件还可以用小括号分组，并通过**与**（`&&`）和**或**（`||`）布尔运算符进行组合评估。
这样使用的条件仍然可以带有条件操作。
```yaml
  Conditions:
  - ((day false || raining true) && onBlock{material=LIME_CONCRETE}) true
```
> 当正在下雨或不是白天时，并且施法者站在 LIME_CONCRETE（浅绿色混凝土）方块上时，条件满足。

> day 和 raining 显式声明了条件操作，而 onBlock 使用默认的 `true`。


## 通用属性
每个条件都共享并可使用以下属性：

| 属性       | 别名     | 描述                                           | 默认值 |
|-----------|---------|------------------------------------------------|--------|
| onFailSkill | onFail | 此条件未通过时调用的元技能                        |<!--type:Metaskill-->|
| onPassSkill | onPass | 此条件通过时调用的元技能                          |<!--type:Metaskill-->|


# 扩展条件
以下是扩展插件提供的条件链接。如果没有安装对应的插件，这些条件不会生效。

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Conditions)
- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Conditions)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Conditions)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#conditions)

# 条件列表

| 条件                                                                           | 类型     | 描述                                                                                     |
|--------------------------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------|
| [Altitude（海拔）](/skills/conditions/altitude)                                 | 实体     | 检测目标实体离地面的高度                                                                     |
| [Biome（生物群系）](/skills/conditions/biome)                                   | 位置     | 检测目标是否位于指定的生物群系列表中                                                          |
| [BiomeType（生物群系类型）](/skills/conditions/biometype)                       | 位置     | 检测某位置的生物群系类别                                                                     |
| [BlockType（方块类型）](/skills/conditions/blocktype)                           | 位置     | 检测目标位置处的材质类型                                                                     |
| [BlockTypeInRadius（半径内方块类型）](/skills/conditions/BlockTypeInRadius)     | 位置     | 检查目标位置周围半径内指定方块的数量                                                           |
| [Blocking（格挡中）](/skills/conditions/blocking)                               | 实体     | 检测目标玩家是否正在用盾牌格挡                                                                |
| [BoundingBoxesOverlap（碰撞箱重叠）](/skills/conditions/BoundingBoxesOverlap)   | 比较     | 检查施法者的碰撞箱是否与目标碰撞箱重叠                                                          |
| [BowTension（弓弦张力）](/skills/conditions/bowtension)                          | 元       | 检查实体射箭时的弓弦张力                                                                     |
| [Burning（着火）](/skills/conditions/burning)                                   | 实体     | 目标实体是否着火                                                                            |
| [Chance（概率）](/skills/conditions/chance)                                     | 元       | 元技能被执行的概率                                                                         |
| [Charged（带电）](/skills/conditions/charged)                                   | 实体     | 检查目标爬行者是否带电                                                                      |
| [Children（子实体）](/skills/conditions/children)                               | 实体     | 检测施法者有多少个子实体                                                                     |
| [Color（颜色）](/skills/conditions/color)                                       | 实体     | 检测实体的颜色                                                                             |
| [CompareValues（比较值）](/skills/conditions/CompareValues)                     | 元       | 根据指定运算比较两个值                                                                      |
| [Crouching（潜行中）](/skills/conditions/crouching)                             | 实体     | 目标实体是否在潜行                                                                          |
| [Cuboid（长方体）](/skills/conditions/cuboid)                                    | 比较     | 目标是否位于给定两个坐标点之间的长方体内                                                        |
| [DamageAmount（伤害数值）](/skills/conditions/DamageAmount)                      | 元       | 检查受到的伤害数值范围                                                                      |
| [DamageCause（伤害原因）](/skills/conditions/DamageCause)                        | 元       | 检查伤害原因的类型                                                                         |
| [DamageTag（伤害标签）](/skills/conditions/damagetag)                            | 元       | 检查伤害原因的标签                                                                         |
| [Dawn（黎明）](/skills/conditions/dawn)                                         | 位置     | 是否处于黎明，即游戏时间 22000 到 2000                                                        |
| [Day（白天）](/skills/conditions/day)                                            | 位置     | 是否处于白天，即游戏时间 2000 到 10000                                                        |
| [Dimension（维度）](/skills/conditions/dimension)                               | 位置     | 目标位置是否处于某维度                                                                      |
| [DirectionalVelocity（有向速度向量）](/skills/conditions/directionalvelocity)   | 实体     | 目标是否具有符合给定参数的速度向量                                                              |
| [Distance（距离）](/skills/conditions/distance)                                 | 比较     | 施法者与目标之间的距离是否在给定范围内                                                          |
| [DistanceFromLocation（与指定位置的距离）](/skills/conditions/DistanceFromLocation) | 实体  | 目标与指定位置之间的距离是否在某个范围内                                                         |
| [DistanceFromPin（与标记点的距离）](/skills/conditions/DistanceFromPin)          | 位置     | 检查目标是否在指定标记点的某个距离范围内                                                         |
| [DistanceFromSpawn（与出生点的距离）](/skills/conditions/distancefromspawn)      | 位置     | 目标与世界出生点之间的距离是否在给定范围内                                                        |
| [DistanceFromTrackedLocation（与追踪位置的距离）](/skills/conditions/distancefromtrackedlocation) | 位置 | 追踪位置与施法者之间的距离是否在给定范围内                                                   |
| [Dusk（黄昏）](/skills/conditions/dusk)                                         | 位置     | 是否处于黄昏，即游戏时间 14000 到 18000                                                        |
| [EnchantingExperience（附魔经验值）](/skills/conditions/EnchantingExperience)   | 实体     | 检查目标玩家的经验点数                                                                      |
| [EnchantingLevel（附魔等级）](/skills/conditions/enchantingLevel)                | 实体     | 检查目标玩家的经验等级                                                                      |
| [EnderDragonAlive（末影龙存活）](/skills/conditions/EnderDragonAlive)           | 位置     | 检查目标位置所在世界中是否至少有一只末影龙存活                                                    |
| [EnderDragonPhase（末影龙阶段）](/skills/conditions/EnderDragonPhase)           | 实体     | 检查末影龙是否处于某个或某些阶段                                                               |
| [EntityItemIsSimilar（物品实体相似）](/skills/conditions/EntityItemIsSimilar)  | 实体     | 检测目标物品实体是否与另一个物品相似                                                            |
| [EntityItemType（物品实体类型）](/skills/conditions/EntityItemType)             | 实体     | 检测目标物品实体的类型                                                                      |
| [EntityMaterialType（实体材质类型）](/skills/conditions/EntityMaterialType)     | 实体     | 检测目标物品实体的材质                                                                      |
| [EntityType（实体类型）](/skills/conditions/entitytype)                         | 实体     | 检测目标的实体类型                                                                         |
| [Faction（阵营）](/skills/conditions/faction)                                   | 实体     | 检测目标的阵营                                                                             |
| [FallSpeed（下落速度）](/skills/conditions/fallspeed)                           | 实体     | 目标的下落速度是否在给定范围内                                                                |
| [FieldOfView（视野角）](/skills/conditions/fieldofview)                          | 比较     | 检测目标是否在施法者视线方向的给定角度内                                                         |
| [FoodLevel（饥饿值）](/skills/conditions/FoodLevel)                              | 实体     | 检查目标的饥饿值是否在给定范围内                                                               |
| [FoodSaturation（饱和值）](/skills/conditions/FoodSaturation)                    | 实体     | 检查目标的饱和值是否在给定范围内                                                               |
| [Gamemode（游戏模式）](/skills/conditions/Gamemode)                              | 实体     | 检查目标玩家的游戏模式是否为指定的模式                                                          |
| [Gliding（滑翔中）](/skills/conditions/gliding)                                  | 实体     | 目标是否在滑翔                                                                            |
| [GlobalScore（全局计分板）](/skills/conditions/globalscore)                       | 实体     | 检查全局计分板的值                                                                         |
| [HasAI（有AI）](/skills/conditions/hasai)                                        | 实体     | 检查目标实体是否启用了 AI                                                                   |
| [HasAura（有光环）](/skills/conditions/hasaura)                                   | 实体     | 检查目标实体是否有指定光环                                                                   |
| [HasAuraStacks（有光环层数）](/skills/conditions/hasaurastacks)                   | 实体     | 检测目标的某光环层数是否在给定范围内                                                            |
| [HasAuraType（有光环类型）](/skills/conditions/HasAuraType)                       | 实体     | 检查目标实体是否有指定类型的光环                                                               |
| [HasCurrency（有金钱）](/skills/conditions/hascurrency)                           | 实体     | 目标是否拥有指定数量的 Vault 金钱                                                            |
| [HasEnchantment（有附魔）](/skills/conditions/HasEnchantment)                     | 实体     | 检查目标实体装备物品上是否有某项附魔                                                            |
| [HasFreeInventorySlot（有空背包槽）](/skills/conditions/HasFreeInventorySlot)   | 实体     | 检查被评估实体是否有空闲的背包槽                                                               |
| [HasGravity（有重力）](/skills/conditions/hasgravity)                             | 实体     | 检测目标生物是否受重力影响                                                                   |
| [HasItem（有物品）](/skills/conditions/hasItem)                                   | 实体     | 检测目标玩家是否拥有指定数量和材质的物品                                                         |
| [HasOffhand（副手有物品）](/skills/conditions/HasOffhand)                         | 实体     | 检查目标实体副手是否有物品                                                                   |
| [HasOwner（有拥有者）](/skills/conditions/hasowner)                               | 实体     | 检测目标生物是否有拥有者                                                                     |
| [HasParent（有父实体）](/skills/conditions/hasparent)                              | 实体     | 检测目标生物是否有父实体                                                                     |
| [HasPassenger（有骑乘者）](/skills/conditions/hasPassenger)                        | 实体     | 检查目标实体是否有骑乘者                                                                     |
| [HasPermission（有权限）](/skills/conditions/haspermission)                        | 实体     | 检测目标玩家是否有某权限                                                                     |
| [HasPotionEffect（有药水效果）](/skills/conditions/haspotioneffect)               | 实体     | 检测目标实体是否有某药水效果                                                                  |
| [HasTag（有标签）](/skills/conditions/hastag)                                     | 实体     | 检测目标是否有某个计分板标签                                                                  |
| [Health（生命值）](/skills/conditions/health)                                    | 实体     | 匹配目标的当前生命值                                                                        |
| [HealthPercent（生命值百分比）](/skills/conditions/HealthPercent)                 | 实体     | 匹配目标的生命值百分比或倍数                                                                  |
| [Height（高度）](/skills/conditions/height)                                       | 位置     | 检查目标的 Y 坐标是否在某个范围内                                                              |
| [HeightAbove（高于指定高度）](/skills/conditions/heightabove)                      | 位置     | 检查目标的 Y 坐标是否高于指定值                                                               |
| [HeightBelow（低于指定高度）](/skills/conditions/heightbelow)                      | 位置     | 检查目标的 Y 坐标是否低于指定值                                                               |
| [Holding（手持）](/skills/conditions/holding)                                     | 实体     | 检查目标是否手持指定材质（支持 MythicMobs 和 MMOItems）                                        |
| [inClaim（在领地内）](/skills/conditions/inClaim)                                   | 位置     | 检查目标位置是否在某领地内                                                                   |
| [InCombat（战斗中）](/skills/conditions/incombat)                                  | 实体     | 检查目标生物是否被视为处于战斗中                                                               |
| [InPinRegion（在标记区域内）](/skills/conditions/InPinRegion)                      | 位置     | 检查目标位置是否在两个标记点界定的区域内                                                          |
| [IsInvulnerable（无敌）](/skills/conditions/IsInvulnerable)                       | 实体     | 检查目标实体是否处于无敌状态                                                                  |
| [IsInSurvivalMode（生存模式）](/skills/conditions/IsInSurvivalMode)               | 实体     | 检查目标玩家是否处于生存模式                                                                  |
| [Inside（室内）](/skills/conditions/inside)                                      | 位置     | 检查目标头顶是否有方块                                                                      |
| [isBaby（幼体）](/skills/conditions/isbaby)                                      | 实体     | 检查目标实体是否为幼体                                                                      |
| [isCaster（是施法者）](/skills/conditions/iscaster)                                 | 实体     | 检查目标是否为施法者本身                                                                     |
| [isChild（是子实体）](/skills/conditions/ischild)                                   | 实体     | 检查目标是否为施法者的子实体                                                                  |
| [isClimbing（攀爬中）](/skills/conditions/isClimbing)                              | 实体     | 检查目标实体是否在攀爬                                                                      |
| [IsCreeperPrimed（爬行者点燃）](/skills/conditions/IsCreeperPrimed)                | 实体     | 检查目标爬行者是否已点燃准备爆炸                                                               |
| [isFlying（飞行中）](/skills/conditions/isflying)                                  | 实体     | 检查目标玩家是否在飞行                                                                      |
| [isFrozen（冻结中）](/skills/conditions/isfrozen)                                  | 实体     | 检查目标实体是否被冻结                                                                      |
| [isLeashed（拴绳中）](/skills/conditions/isleashed)                                | 实体     | 检查目标是否被拴绳牵引                                                                      |
| [isLiving（是活物）](/skills/conditions/isliving)                                  | 实体     | 检查目标是否为活物实体                                                                      |
| [isMonster（是怪物）](/skills/conditions/ismonster)                                | 实体     | 检查目标是否为怪物                                                                         |
| [isMythicMob（是MythicMob）](/skills/conditions/ismythicmob)                        | 实体     | 检查目标是否为 MythicMob                                                                    |
| [IsParentAlive（父实体存活）](/skills/conditions/IsParentAlive)                    | 实体     | 检查目标实体的父实体是否仍存活                                                                 |
| [IsParent（是父实体）](/skills/conditions/IsParent)                                 | 比较     | 检查目标实体是否为施法者的父实体                                                               |
| [isPlayer（是玩家）](/skills/conditions/isplayer)                                  | 实体     | 检查目标是否为玩家                                                                         |
| [isRaiderPatrolLeader（是掠夺者队长）](/skills/conditions/isRaiderPatrolLeader)    | 实体     | 检查目标实体是否为掠夺者巡逻队的队长                                                            |
| [isSaddled（已装鞍）](/skills/conditions/issaddled)                                | 实体     | 检查目标实体是否已装鞍                                                                      |
| [isSkill（技能存在）](/skills/conditions/IsSkill)                                   | 元       | 检查指定的元技能是否存在                                                                     |
| [isTamed（已驯服）](/skills/conditions/IsTamed)                                    | 实体     | 检查目标实体是否已被驯服                                                                     |
| [IsUsingSpyglass（使用望远镜）](/skills/conditions/IsUsingSpyglass)               | 实体     | 检查目标玩家是否在使用望远镜                                                                  |
| [ItemGroupOnCooldown（物品组冷却中）](/skills/conditions/ItemGroupOnCooldown)      | 实体     | 检查目标玩家的指定物品组是否处于冷却中                                                           |
| [ItemIsSimilar（物品相似）](/skills/conditions/itemissimilar)                     | 实体     | 检查目标玩家的背包槽物品是否与某一物品相似                                                        |
| [ItemRecharging（物品蓄力中）](/skills/conditions/itemrecharging)                  | 实体     | 检查目标的武器是否在蓄力                                                                     |
| [ItemType（物品类型）](/skills/conditions/ItemType)                                | 元       | 检查触发技能物品的材质                                                                      |
| [LastDamageCause（上次受伤原因）](/skills/conditions/lastdamagecause)             | 实体     | 检查目标最后一次受伤的原因                                                                   |
| [LastSignal（上次信号）](/skills/conditions/lastsignal)                          | 实体     | 匹配目标生物收到的上一个信号                                                                  |
| [Level（等级）](/skills/conditions/level)                                        | 实体     | 检查目标 MythicMob 的等级                                                                   |
| [LightLevel（光照等级）](/skills/conditions/lightlevel)                          | 位置     | 检测目标位置的光照等级                                                                      |
| [LightLevelFromBlocks（方块光照等级）](/skills/conditions/lightlevelfromblocks)  | 位置     | 检测目标位置源自发光方块的光照等级                                                              |
| [LineOfSight（视线无阻）](/skills/conditions/lineofsight)                       | 比较     | 检测目标是否在施法者的视线内                                                                  |
| [LineOfSightFromOrigin（原点到目标的视线）](/skills/conditions/lineofsightfromorigin) | 比较 | 检测目标是否在原点的视线内                                                                   |
| [LivingInRadius（半径内活物数）](/skills/conditions/LivingInRadius)              | 位置     | 匹配指定半径内活物实体的数量范围                                                               |
| [LocalDifficulty（区域难度）](/skills/conditions/localdifficulty)                | 位置     | 检测目标位置的难度系数                                                                      |
| [LookingAt（正在注视）](/Skills/Conditions/LookingAt)                            | 实体     | 检查玩家是否在注视某物                                                                      |
| [LunarPhase（月相）](/skills/conditions/lunarphase)                              | 位置     | 检查目标世界的月相                                                                         |
| [MaterialisOnCooldown（材质冷却中）](/skills/conditions/MaterialIsOnCooldown)    | 实体     | 检查目标玩家的指定材质是否处于冷却中                                                             |
| [MetaskillCondition（元技能条件）](/skills/conditions/MetaskillCondition)         | 元       | 施放一个元技能来决定该条件是否通过                                                               |
| [MobsInChunk（区块内生物数）](/skills/conditions/mobsinchunk)                    | 位置     | 匹配目标位置所在区块内的生物数量范围                                                             |
| [MobsInRadius（半径内生物数）](/skills/conditions/mobsinradius)                  | 位置     | 检查给定半径内有多少生物                                                                     |
| [MobsInWorld（世界内生物数）](/skills/conditions/mobsinworld)                     | 位置     | 匹配目标世界中的生物数量范围                                                                  |
| [MobsNearOrigin（原点附近生物数）](/skills/conditions/MobsNearOrigin)            | 元       | 匹配原点周围给定半径内的生物数量范围                                                             |
| [MobSize（生物大小）](/skills/conditions/mobsize)                                 | 实体     | 检查可改变大小的实体的尺寸                                                                   |
| [Moist（湿润度）](/skills/conditions/Moist)                                       | 位置     | 检查目标耕地方块是否有水分                                                                   |
| [MoistureLevel（湿润等级）](/skills/conditions/moisturelevel)                     | 位置     | 检查目标耕地方块是否具有指定的湿润等级                                                           |
| [MotionX（X轴动量）](/skills/conditions/motionx)                                  | 实体     | 检查目标实体 X 轴动量是否在给定范围内                                                            |
| [MotionY（Y轴动量）](/skills/conditions/motiony)                                  | 实体     | 检查目标实体 Y 轴动量是否在给定范围内                                                            |
| [MotionZ（Z轴动量）](/skills/conditions/motionz)                                  | 实体     | 检查目标实体 Z 轴动量是否在给定范围内                                                            |
| [Mounted（骑乘中）](/skills/conditions/mounted)                                  | 实体     | 目标实体是否正在骑乘/驾驶某物                                                                  |
| [Moving（移动中）](/skills/conditions/moving)                                    | 实体     | 目标的速度是否大于零                                                                        |
| [MythicMobType（MythicMob类型）](/skills/conditions/mythicmobtype)               | 实体     | 检查目标生物的 MythicMob 类型                                                                |
| [MythicPack（数据包存在）](/skills/conditions/mythicpack)                          | 元       | 检查数据包是否存在                                                                         |
| [MythicPackVersion（数据包版本）](/skills/conditions/MythicPackVersion)            | 元       | 检查数据包是否为指定版本                                                                     |
| [MythicPackVersionGreater（数据包版本不低于）](/skills/conditions/MythicPackVersionGreater) | 元 | 检查数据包版本是否大于或等于指定版本                                                        |
| [Name（名称）](/skills/conditions/name)                                           | 实体     | 检查实体名称                                                                              |
| [NearClaim（附近有领地）](/skills/conditions/nearclaim)                            | 位置     | 目标位置是否靠近 GriefPrevention 领地                                                         |
| [Night（夜晚）](/skills/conditions/night)                                         | 位置     | 是否处于夜晚，即游戏时间 14000 到 22000                                                        |
| [NotInRegion（不在区域中）](/skills/conditions/notinregion)                        | 位置     | 目标位置是否不在指定的 WorldGuard 区域内                                                         |
| [OffGCD（不在全局冷却中）](/skills/conditions/offgcd)                               | 实体     | 检查目标生物是否没有活跃的全局冷却                                                               |
| [OnBlock（站在方块上）](/skills/conditions/onblock)                               | 位置     | 匹配目标实体所站的方块                                                                      |
| [OnGround（在地面）](/skills/conditions/onground)                                | 实体     | 目标实体是否站在实心地面上                                                                   |
| [OriginDistanceFromPin（原点与标记点距离）](/skills/conditions/OriginDistanceFromPin) | 位置 | 检查原点是否在指定标记点的某个距离范围内                                                       |
| [OriginLocation（原点位置）](/skills/conditions/OriginLocation)                   | 元       | 检查原点是否在给定位置                                                                      |
| [Outside（室外）](/skills/conditions/outside)                                     | 位置     | 目标头顶是否有开阔天空                                                                      |
| [Owner（拥有者）](/skills/conditions/owner)                                       | 比较     | 检查目标实体是否为施法者的拥有者                                                               |
| [OwnerIsOnline（拥有者在线）](/skills/conditions/ownerisonline)                   | 实体     | 检查目标生物的拥有者是否在线（若拥有者为玩家）                                                     |
| [Pitch（俯仰角）](/skills/conditions/pitch)                                      | 实体     | 检查目标实体的俯仰角是否在某个范围内                                                             |
| [PlayerKills（玩家击杀数）](/skills/conditions/playerkills)                      | 实体     | 匹配目标生物击杀的玩家数量                                                                   |
| [PlayerNotWithin（玩家不在内）](/skills/conditions/playernotwithin)              | 位置     | 检查目标半径范围内是否没有玩家                                                                 |
| [PlayerWithin（玩家在内）](/skills/conditions/playerwithin)                      | 位置     | 检查目标半径范围内是否有玩家                                                                  |
| [PlayersInRadius（半径内玩家数）](/skills/conditions/playersinradius)            | 实体     | 检查半径内有多少玩家                                                                        |
| [PlayersInWorld（世界内玩家数）](/skills/conditions/playersinworld)               | 元       | 匹配施法者所在世界中的玩家数量                                                                 |
| [PlayersOnline（在线玩家数）](/skills/conditions/playersonline)                  | 元       | 匹配在线玩家数量                                                                           |
| [Plugin（插件）](/skills/conditions/plugin)                                       | 元       | 检查指定插件是否在服务器上运行                                                                 |
| [Premium（高级版）](/skills/conditions/premium)                                   | 元       | 检查 MythicMobs 高级版是否在运行时                                                             |
| [ProjectileHasEnded（弹射物已结束）](/skills/conditions/ProjectileHasEnded)       | 元       | 检查调用弹射物是否已结束                                                                     |
| [Raining（下雨）](/skills/conditions/raining)                                    | 位置     | 目标世界是否在下雨                                                                         |
| [Region（区域）](/skills/conditions/region)                                       | 位置     | 目标是否在指定 WorldGuard 区域内                                                               |
| [SameFaction（相同阵营）](/skills/conditions/samefaction)                         | 实体     | 检测施法者和目标是否处于同一阵营                                                               |
| [Score（计分板）](/skills/conditions/score)                                      | 实体     | 检查目标实体的计分板值                                                                      |
| [ServerIsPaper（服务器为Paper）](/skills/conditions/ServerIsPaper)               | 元       | 检查服务器是否运行 Paper 分支                                                                |
| [ServerNmsVersion（服务器NMS版本）](/skills/conditions/servernmsversion)          | 元       | 检查服务器是否运行指定 Minecraft NMS 版本                                                       |
| [ServerVersion（服务器版本）](/skills/conditions/serverversion)                  | 元       | 检查服务器是否运行指定 Minecraft 版本                                                           |
| [ServerVersionAfterOrEqual（服务器版本不低于）](/skills/conditions/ServerVersionAfterOrEqual) | 元 | 检查服务器版本是否不低于指定版本                                                           |
| [ServerVersionBefore（服务器版本早于）](/skills/conditions/ServerVersionBefore)   | 元       | 检查服务器版本是否早于指定版本                                                                |
| [Size（大小）](/skills/conditions/Size)                                           | 实体     | 检查目标实体的大小                                                                         |
| [SkillOnCooldown（技能冷却中）](/skills/conditions/skilloncooldown)               | 实体     | 检查目标指定技能是否在冷却中                                                                  |
| [SpawnReason（生成原因）](/skills/conditions/SpawnReason)                         | 实体     | 检查目标的生成原因                                                                         |
| [Sprinting（疾跑中）](/skills/conditions/Sprinting)                               | 实体     | 检查目标**玩家**是否在疾跑                                                                    |
| [Stance（形态）](/skills/conditions/stance)                                       | 实体     | 检查目标生物的当前形态                                                                      |
| [StringEmpty（字符串为空）](/skills/conditions/StringEmpty)                        | 元       | 检查提供的字符串是否为空                                                                     |
| [StringNotEmpty（字符串非空）](/skills/conditions/StringNotEmpty)                  | 元       | 检查提供的字符串是否非空                                                                     |
| [StringEquals（字符串相等）](/skills/conditions/stringequals)                     | 元       | 检查 value1 是否等于 value2。两者均可使用变量和占位符。                                           |
| [Structure（结构中）](/skills/conditions/structure)                               | 位置     | 匹配目标位置是否在某结构内部                                                                  |
| [Sunny（晴天）](/skills/conditions/sunny)                                         | 位置     | 目标世界是否晴天                                                                           |
| [TargetInLineOfSight（猎物在视线内）](/skills/conditions/targetinlineofsight)     | 实体     | 检测目标是否能看到它的目标                                                                   |
| [TargetNotInLineOfSight（猎物不在视线内）](/skills/conditions/targetnotinlineofsight) | 实体 | 检测目标是否看不到它的目标                                                                  |
| [TargetWithin（猎物在范围内）](/skills/conditions/targetwithin)                    | 实体     | 检测目标的目标是否在某距离内                                                                  |
| [TargetNotWithin（猎物不在范围内）](/skills/conditions/targetnotwithin)            | 实体     | 检测目标的目标是否在某距离外                                                                  |
| [Targets（目标数量）](/skills/conditions/targets)                                  | 元       | 检测从父级技能树继承的目标数量是否匹配给定范围                                                    |
| [TemplateType（模板类型）](/skills/conditions/TemplateType)                        | 实体     | 检查目标生物是否继承了指定模板                                                                |
| [Thundering（雷暴）](/skills/conditions/thundering)                                | 位置     | 目标世界是否有雷暴                                                                         |
| [TriggerBlockType（触发方块类型）](/skills/conditions/TriggerBlockType)           | 元       | 检查触发技能的方块材质类型                                                                   |
| [TriggerItemType（触发物品类型）](/skills/conditions/TriggerItemType)              | 元       | 检查触发技能的物品材质类型                                                                   |
| [VariableContains（变量包含）](/skills/conditions/VariableContains)                | 元       | 检查指定变量是否包含某个值                                                                   |
| [VariableEquals（变量相等）](/skills/conditions/variableequals)                   | 元       | 检查指定变量是否等于某个值                                                                   |
| [VariableInRange（变量在范围内）](/skills/conditions/variableinrange)             | 元       | 检查指定数值变量是否在某个范围内                                                               |
| [VariableIsSet（变量已设置）](/skills/conditions/variableisset)                   | 元       | 检查指定变量是否已设置                                                                      |
| [VehicleIsDead（载具已死亡）](/skills/conditions/vehicleisdead)                    | 实体     | 检查施法者骑乘的载具是否已死亡                                                                 |
| [Velocity（速度向量）](/skills/conditions/Velocity)                                | 实体     | 检查目标实体的速度向量是否在给定范围内                                                           |
| [Wearing（穿戴）](/skills/conditions/wearing)                                     | 实体     | 检测目标实体装备了什么                                                                      |
| [World（世界）](/skills/conditions/world)                                         | 位置     | 检查目标世界的名称                                                                         |
| [WorldTime（世界时间）](/skills/conditions/worldtime)                              | 位置     | 匹配目标位置所在世界的时间范围                                                                 |
| [Yaw（水平朝向）](/skills/conditions/yaw)                                         | 实体     | 检查目标实体的水平朝向是否在给定范围内                                                           |
| [xDiff（X差）](/skills/conditions/xdiff)                                          | 实体     | 检查目标实体与施法者之间的 X 差                                                              |
| [yDiff（Y差）](/skills/conditions/ydiff)                                          | 实体     | 检查目标实体与施法者之间的 Y 差                                                              |
| [zDiff（Z差）](/skills/conditions/zdiff)                                          | 实体     | 检查目标实体与施法者之间的 Z 差                                                              |

更多示例
-------------
```yaml
FlameShock:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - incombat
  - stance aggressive
  - onblock GRASS
  - offgcd
  Skills:
  - gcd{t=60}
  - message{m="<mob.name> begins casting a spell"}
  - potion{t=SLOW;d=60;l=7}
  - delay 60
  - message{m="<target.name> &ecombusts"}
  - effect:particles{p=flame;a=20;hS=3;vS=1;s=0;y=2}
  - potion{t=HARM;d=1;l=1}
```
[1] 并非所有条件在所有场合都适用。