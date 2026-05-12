[[_TOC_]]

## 简介

条件用于决定某个动作是否可以执行。

条件可以在以下位置使用 [1]：
-   [技能机制](/skills/mechanics/skill)
-   [掉落表](/drops/Drops#drop-tables)
-   [生成器](/Spawners)
-   [随机生成](/Random%20Spawns)

当应用多个条件时，全部条件都必须满足技能才会执行。某些条件支持用逗号分隔的数组，这种情况下只需数组中有一个字符串匹配即可。

要查看如何内联使用条件，[请点击这里！](/skills/Inline-Conditions)


## 类型
  
条件可以分为四种类型：

1. 实体条件：检查实体的状态。
2. 位置条件：检查某个位置的状态。如果位置条件的目标是实体，则会检查该实体所在位置的状态。
3. 比较条件：检查两个不同「事物」之间的某种关系。例如，「Cuboid」会在目标位于两个坐标构成的立方体内时返回 true。
4. 元条件：它们不一定检查施法者或目标的任何固有属性。例如，「StringEquals」会根据两个字符串是否匹配返回 true 或 false。这些字符串*可以*是从施法者或目标获取值的占位符，但这只是一种可能的应用。

## 用法
条件还可以在元技能中的三个不同位置使用：
#### Conditions
此部分的条件针对施法者或其位置进行检查。
```yaml
  Conditions:
  - health{h=>10}
```
> 检查施法者是否拥有超过 10 点生命值

```yaml
  Conditions:
  - globalscore{objective=Test;v=>10}
```
> 在上面的示例中，globalscore 条件将检查施法者的全局计分板值。

##
#### TargetConditions
此部分的条件针对元技能的[继承目标](/Skills/Metaskills#inheritance)进行检查

```yaml
  TargetConditions:
  - health{h=>10}
```
> 检查继承的目标实体是否拥有超过 10 点生命值，只有那些满足条件的实体才会被元技能作为继承目标。如果没有目标满足条件，则默认情况下元技能不会执行。

```yaml
  TargetConditions:
  - globalscore{objective=Test;v=>10}
```
> 上面的示例中 globalscore 条件将检查继承目标的全局计分板值。由于 globalscore 是实体条件，只有目标是实体时才会生效。

##
#### TriggerConditions
此部分的条件针对元技能的触发器进行检查
```yaml
  TriggerConditions:
  - health{h=>10}
```
> 检查元技能的触发者是否拥有超过 10 点生命值

## 范围值  
范围值使用 **#to#** 或 **#-#** 的格式。如果要在范围中使用负数，必须使用 "to" 而不是 "-"。例如：
```yaml
YourMagnificentSkill:
  Conditions:
    - altitude{a=1-5}
  TargetConditions:
    - distance{d=1to10} true
  TriggerConditions:
    - distance{d=1to10} true
```

## 条件动作

条件动作让你可以根据条件执行额外的操作。默认的条件动作是 **true**

| 动作         | 描述                                                                           |
|----------------|---------------------------------------------------------------------------------------|
| `true`         | 满足此条件时技能将运行                                           |
| `false`        | 满足此条件时技能将*不会*运行                                     |
| `power` [multiplier] | 将技能的 power 乘以 `multiplier` 的值（例如 power 2.0 会使技能威力翻倍） |
| `cast` [skill] | 满足条件时施放一个额外技能，不影响原始技能的执行 |
| `castinstead` [skill] | 满足条件时改为施放一个不同的技能                        |
| `orElseCast` [skill] | 不满足条件时改为施放一个不同的技能                     |

<!--
| `level`        |                                                                                       |
-->

```yaml
  Conditions:
  - day true
  Skills:
  - message{m="现在是白天！"} @self
```
> 只有在施法者所在世界是白天时才会运行  

```yaml
  Conditions:
  - day false
  Skills:
  - message{m="现在*不是*白天！"} @self
```
> 只有在施法者所在世界*不是*白天时才会运行  
> 与 `true` 的行为相反  

```yaml
ExampleSkill:
  Conditions:
  - day true
  - sunny orElseCast OtherSkill
  Skills:
  - message{m="是白天而且阳光明媚！"} @self

OtherSkill:
  Skills:
  - message{m="是白天但天气不好！"} @self
```
> 如果条件行未被满足*（满足条件但条件动作为 false，或不满足条件但条件动作为 true）*，[则不再检查后续条件](https://en.wikipedia.org/wiki/Short-circuit_evaluation)  
> 因此即使因为 `sunny` 条件而执行了 OtherSkill，我们也可以确定 `day` 条件也已经满足，否则因为  
> `day true`  
> 在  
> `sunny orElseCast OtherSkill`  
> 之前检查，根本不会有技能运行  

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
条件还可以通过括号分组，并使用 **AND**（`&&`）和 **OR**（`||`）布尔运算符进行求值。
以这种方式使用的条件仍然可以带有条件动作。
```yaml
  Conditions:
  - ((day false || raining true) && onBlock{material=LIME_CONCRETE}) true
```
> 当下雨或不是白天时，条件被满足，此外，只有在施法者站在 LIME_CONCRETE 方块上时条件才被满足  

> day 和 raining 声明了它们的条件动作，而 onBlock 使用默认的 `true`


## 通用属性
每个条件都共享并可以使用以下属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onFailSkill | onFail  | 条件未通过时调用的元技能   |<!--type:Metaskill-->|
| onPassSkill | onPass  | 条件通过时调用的元技能     |<!--type:Metaskill-->|


# 附加条件
由附加插件添加的条件链接。以下链接中的任何条件都需要安装对应插件才能使用。

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Conditions)
- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Conditions)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Conditions)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#conditions)

# 条件列表

| 条件                                                                     | 类型     | 描述                                                                                 |
|-------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------|
| [Altitude](/skills/conditions/altitude)                                       | 实体   | 测试目标实体离地面的高度                                           |
| [Biome](/skills/conditions/biome)                                             | 位置 | 测试目标是否在给定的生物群系列表中                                       |
| [BiomeType](/skills/conditions/biometype)                                     | 位置 | 测试某个位置的生物群系类别。                                                   |
| [BlockType](/skills/conditions/blocktype)                                     | 位置 | 测试目标位置存在的方块类型                                    |
| [BlockTypeInRadius](/skills/conditions/BlockTypeInRadius)                     | 位置 | 检查目标位置周围半径内指定方块的数量   |
| [Blocking](/skills/conditions/blocking)                                       | 实体   | 测试目标玩家是否正在用盾牌格挡                                       |
| [BoundingBoxesOverlap](/skills/conditions/BoundingBoxesOverlap)               | 比较  | 检查施法者的包围盒是否与目标的包围盒重叠                                 |
| [BowTension](/skills/conditions/bowtension)                                   | 元     | 检查实体射箭时的蓄力程度                                 |
| [Burning](/skills/conditions/burning)                                         | 实体   | 目标实体是否着火                                                |
| [Chance](/skills/conditions/chance)                                           | 元     | 元技能执行的概率                                           |
| [Charged](/skills/conditions/charged)                                         | 实体   | 检查目标苦力怕是否被充能                                                       |
| [Children](/skills/conditions/children)                                       | 实体   | 测试施法者有多少个子级                                                    |
| [Color](/skills/conditions/color)                                             | 实体   | 测试实体的颜色                                                                 |
| [CompareValues](/skills/conditions/CompareValues)                             | 元     | 基于指定操作比较两个值                                           |
| [Crouching](/skills/conditions/crouching)                                     | 实体   | 目标实体是否在潜行                                              |
| [Cuboid](/skills/conditions/cuboid)                                           | 比较  | 目标是否在 location1 x location2 之间的长方体内                 |
| [DamageAmount](/skills/conditions/DamageAmount)                               | 元     | 检查所受伤害的范围                                                           |
| [DamageCause](/skills/conditions/DamageCause)                                 | 元     | 检查伤害原因的类型                                                        |
| [DamageTag](/skills/conditions/damagetag)                                     | 元     | 检查伤害原因的标签                                                        |
| [Dawn](/skills/conditions/dawn)                                               | 位置 | 如果游戏时间是黎明，即 22000 到 2000                                        |
| [Day](/skills/conditions/day)                                                 | 位置 | 如果游戏时间是白天，即 2000 到 10000                                         |
| [Dimension](/skills/conditions/dimension)                                     | 位置 | 如果目标位置在某个维度内                                          |
| [DirectionalVelocity](/skills/conditions/directionalvelocity)                 | 实体 | 如果目标的速度向量匹配给定参数                                    |
| [Distance](/skills/conditions/distance)                                       | 比较  | 施法者与目标之间的距离是否在给定范围内                |
| [DistanceFromLocation](/skills/conditions/DistanceFromLocation)               | 实体   | 目标与指定位置之间的距离是否在给定范围内  |
| [DistanceFromPin](/skills/conditions/DistanceFromPin)                         | 位置 | 检查目标是否在指定钉点的特定距离内                          |
| [DistanceFromSpawn](/skills/conditions/distancefromspawn)                     | 位置 | 世界出生点到目标的距离是否在给定范围内   |
| [DistanceFromTrackedLocation](/skills/conditions/distancefromtrackedlocation) | 位置 | 跟踪位置到施法者的距离是否在给定范围内      |
| [Dusk](/skills/conditions/dusk)                                               | 位置 | 如果游戏时间是黄昏，即 14000 到 18000。                                      |
| [EnchantingExperience](/skills/conditions/EnchantingExperience)               | 实体   | 检查目标玩家的附魔经验点数                                               |
| [EnchantingLevel](/skills/conditions/enchantingLevel)                         | 实体   | 检查目标玩家的附魔等级                                                |
| [EnderDragonAlive](/skills/conditions/EnderDragonAlive)                       | 位置 | 检查目标位置所在世界是否至少有一只末影龙存活   |
| [EnderDragonPhase](/skills/conditions/EnderDragonPhase)                       | 实体   | 检查末影龙是否处于某个阶段                                            |
| [EntityItemIsSimilar](/skills/conditions/EntityItemIsSimilar)                 | 实体   | 测试目标物品实体是否与另一个物品相似                                   |
| [EntityItemType](/skills/conditions/EntityItemType)                           | 实体   | 测试目标物品实体的类型                                                  |
| [EntityMaterialType](/skills/conditions/EntityMaterialType)                   | 实体   | 测试目标物品实体的材质                                              |
| [EntityType](/skills/conditions/entitytype)                                   | 实体   | 测试目标的实体类型                                                       |
| [Faction](/skills/conditions/faction)                                         | 实体   | 测试目标的阵营                                                                 |
| [FallSpeed](/skills/conditions/fallspeed)                                     | 实体   | 目标的坠落速度是否在给定范围内                                   |
| [FieldOfView](/skills/conditions/fieldofview)                                 | 比较  | 测试目标是否在施法者视角的给定角度内               |
| [FoodLevel](/skills/conditions/FoodLevel)                                     | 实体   | 检查目标的饥饿值是否在范围内                                                |
| [FoodSaturation](/skills/conditions/FoodSaturation)                           | 实体   | 检查目标的饱和度是否在范围内                                                |
| [Gamemode](/skills/conditions/Gamemode)                                       | 实体   | 检查目标玩家的游戏模式是否为指定模式                                   |
| [Gliding](/skills/conditions/gliding)                                         | 实体   | 目标是否在滑翔                                                                      |
| [GlobalScore](/skills/conditions/globalscore)                                 | 实体   | 检查全局计分板值                                                         |
| [HasAI](/skills/conditions/hasai)                                             | 实体   | 检查目标实体是否启用了 AI                                                |
| [HasAura](/skills/conditions/hasaura)                                         | 实体   | 检查目标实体是否拥有指定的光环                                                |
| [HasAuraStacks](/skills/conditions/hasaurastacks)                             | 实体   | 测试目标的光环层叠数是否在给定范围内                               |
| [HasAuraType](/skills/conditions/HasAuraType)                                 | 实体   | 检查目标实体是否拥有指定类型的光环                                           |
| [HasCurrency](/skills/conditions/hascurrency)                                 | 实体   | 目标是否拥有指定数量的 Vault 货币                                          |
| [HasEnchantment](/skills/conditions/HasEnchantment)                           | 实体   | 检查目标实体装备的物品是否拥有某种附魔                                |
| [HasFreeInventorySlot](/skills/conditions/HasFreeInventorySlot)               | 实体   | 检查被评估实体是否有空闲背包槽位                                      |
| [HasGravity](/skills/conditions/hasgravity)                                   | 实体   | 测试目标生物是否具有重力                                                          |
| [HasItem](/skills/conditions/hasItem)                                         | 实体   | 测试目标玩家是否拥有指定数量的指定材料                            |
| [HasOffhand](/skills/conditions/HasOffhand)                                   | 实体   | 检查目标实体的副手上是否有物品                                      |
| [HasOwner](/skills/conditions/hasowner)                                       | 实体   | 测试目标生物是否有主人                                                         |
| [HasParent](/skills/conditions/hasparent)                                     | 实体   | 测试目标生物是否有父级                                                         |
| [HasPassenger](/skills/conditions/hasPassenger)                               | 实体   | 检查目标实体是否有乘客                                                   |
| [HasPermission](/skills/conditions/haspermission)                             | 实体   | 测试目标玩家是否拥有某个权限                                                  |
| [HasPotionEffect](/skills/conditions/haspotioneffect)                         | 实体   | 测试目标实体是否拥有某种药水效果                                               |
| [HasTag](/skills/conditions/hastag)                                           | 实体   | 测试目标是否拥有计分板标签                                                     |
| [Health](/skills/conditions/health)                                           | 实体   | 匹配目标的生命值                                                                 |
| [HealthPercent](/skills/conditions/HealthPercent)                             | 实体   | 匹配目标的生命值百分比或倍数                                        |
| [Height](/skills/conditions/height)                                           | 位置 | 检查目标的 Y 坐标是否在范围内                                           |
| [HeightAbove](/skills/conditions/heightabove)                                 | 位置 | 检查目标的 Y 坐标是否高于某个值                                            |
| [HeightBelow](/skills/conditions/heightbelow)                                 | 位置 | 检查目标的 Y 坐标是否低于某个值                                      |
| [Holding](/skills/conditions/holding)                                         | 实体   | 检查目标是否手持给定物品（支持 MythicMobs 和 MMOItems）             |
| [inClaim](/skills/conditions/inClaim)                                         | 位置 | 检查目标位置是否在领地内                                               |
| [InCombat](/skills/conditions/incombat)                                       | 实体   | 检查目标生物是否被视为处于战斗中                                              |
| [InPinRegion](/skills/conditions/InPinRegion)                                 | 位置 | 检查目标位置是否在由两个钉点界定的区域内                        |
| [IsInvulnerable](/skills/conditions/IsInvulnerable)                           | 实体   | 检查目标实体是否处于无敌状态                                       |
| [IsInSurvivalMode](/skills/conditions/IsInSurvivalMode)                       | 实体   | 检查目标玩家是否处于生存模式                                               |
| [Inside](/skills/conditions/inside)                                           | 位置 | 检查目标头上是否有方块                                              |
| [isBaby](/skills/conditions/isbaby)                                           | 实体   | 检查目标实体是否为幼体                                                         |
| [isCaster](/skills/conditions/iscaster)                                       | 实体   | 检查目标是否为施法者                                                            |
| [isChild](/skills/conditions/ischild)                                         | 实体   | 检查目标是否为施法者的子级                                                 |
| [isClimbing](/skills/conditions/isClimbing)                                   | 实体   | 检查目标实体是否在攀爬                                                       |
| [IsCreeperPrimed](/skills/conditions/IsCreeperPrimed)                         | 实体   | 检查目标苦力怕是否准备爆炸                                             |
| [isFlying](/skills/conditions/isflying)                                       | 实体   | 检查目标玩家是否在飞行                                                         |
| [isFrozen](/skills/conditions/isfrozen)                                       | 实体   | 检查目标实体是否被冰冻                                                         |
| [isLeashed](/skills/conditions/isleashed)                                     | 实体   | 检查目标是否被拴绳拴住                                                         |
| [isLiving](/skills/conditions/isliving)                                       | 实体   | 检查目标是否为活体实体                                                       |
| [isMonster](/skills/conditions/ismonster)                                     | 实体   | 检查目标是否为怪物                                                             |
| [isMythicMob](/skills/conditions/ismythicmob)                                 | 实体   | 检查目标是否为 MythicMob                                                           |
| [IsParentAlive](/skills/conditions/IsParentAlive)                             | 实体   | 检查目标实体的父级是否还活着                                      |
| [IsParent](/skills/conditions/IsParent)                                       | 比较  | 检查目标实体是否为施法者的父级                                       |
| [isPlayer](/skills/conditions/isplayer)                                       | 实体   | 检查目标是否为玩家                                                              |
| [isRaiderPatrolLeader](/skills/conditions/isRaiderPatrolLeader)               | 实体   | 检查目标实体是否为掠夺者巡逻队的队长                                |
| [isSaddled](/skills/conditions/issaddled)                                     | 实体   | 检查目标实体是否被装上鞍                                                        |
| [isSkill](/skills/conditions/IsSkill)                                         | 元     | 检查指定的元技能是否存在                                                  |
| [isTamed](/skills/conditions/IsTamed)                                         | 实体   | 检查目标实体是否已被驯服                                                          |
| [IsUsingSpyglass](/skills/conditions/IsUsingSpyglass)                         | 实体   | 检查目标玩家是否正在使用望远镜                                               |
| [ItemGroupOnCooldown](/skills/conditions/ItemGroupOnCooldown)                 | 实体   | 检查目标玩家的指定物品组是否处于冷却中              |
| [ItemIsSimilar](/skills/conditions/itemissimilar)                             | 实体   | 检查目标玩家的背包槽位中是否有与指定物品相似的物品                     |
| [ItemRecharging](/skills/conditions/itemrecharging)                           | 实体   | 检查目标的武器是否在充能                                                   |
| [ItemType](/skills/conditions/ItemType)                                       | 元     | 检查触发技能的物品材质                       |
| [LastDamageCause](/skills/conditions/lastdamagecause)                         | 实体   | 检查目标最近一次受到的伤害原因                                                      |
| [LastSignal](/skills/conditions/lastsignal)                                   | 实体   | 匹配目标生物最近接收到的信号                                          |
| [Level](/skills/conditions/level)                                             | 实体   | 检查目标 MythicMob 的等级                                                        |
| [LightLevel](/skills/conditions/lightlevel)                                   | 位置 | 测试目标位置的光照等级                                              |
| [LightLevelFromBlocks](/skills/conditions/lightlevelfromblocks)               | 位置 | 测试目标位置发光方块产生的光照等级       |
| [LineOfSight](/skills/conditions/lineofsight)                                 | 比较  | 测试目标是否在施法者的视线范围内                                    |
| [LineOfSightFromOrigin](/skills/conditions/lineofsightfromorigin)             | 比较  | 测试目标是否在起效点的视线范围内                                    |
| [LivingInRadius](/skills/conditions/LivingInRadius)                           | 位置 | 匹配区域内活体实体数量的范围                       |
| [LocalDifficulty](/skills/conditions/localdifficulty)                         | 位置 | 测试目标位置的难度等级                                         |
| [LookingAt](/Skills/Conditions/LookingAt)                                     | 实体   | 检查玩家是否在看向某物                                                  |
| [LunarPhase](/skills/conditions/lunarphase)                                   | 位置 | 检查目标世界的月相                                                      |
| [MaterialisOnCooldown](/skills/conditions/MaterialIsOnCooldown)               | 实体   | 检查目标玩家的指定材料是否处于冷却中                               |
| [MetaskillCondition](/skills/conditions/MetaskillCondition)                   | 元     | 施放一个元技能来判断条件是否通过              |
| [MobsInChunk](/skills/conditions/mobsinchunk)                                 | 位置 | 匹配目标位置所在区块中的生物数量范围                       |
| [MobsInRadius](/skills/conditions/mobsinradius)                               | 位置 | 检查给定半径内的生物数量                                                 |
| [MobsInWorld](/skills/conditions/mobsinworld)                                 | 位置 | 匹配目标世界中的生物数量范围                                  |
| [MobsNearOrigin](/skills/conditions/MobsNearOrigin)                           | 元     | 匹配起效点周围给定半径内的生物数量范围                |
| [MobSize](/skills/conditions/mobsize)                                         | 实体   | 检查可改变大小的实体的大小                                |
| [Moist](/skills/conditions/Moist)                                             | 位置 | 检查目标耕地方块是否被湿润                                            |
| [MoistureLevel](/skills/conditions/moisturelevel)                             | 位置 | 检查目标耕地方块是否具有指定湿润等级                 |
| [MotionX](/skills/conditions/motionx)                                         | 实体   | 检查目标实体 X 轴运动量的范围。                                    |
| [MotionY](/skills/conditions/motiony)                                         | 实体   | 检查目标实体 Y 轴运动量的范围。                                    |
| [MotionZ](/skills/conditions/motionz)                                         | 实体   | 检查目标实体 Z 轴运动量的范围。                                    |
| [Mounted](/skills/conditions/mounted)                                         | 实体   | 目标实体是否在骑乘坐骑/载具                                                |
| [Moving](/skills/conditions/moving)                                           | 实体   | 目标的速度向量是否大于零                                                |
| [MythicMobType](/skills/conditions/mythicmobtype)                             | 实体   | 检查目标生物的 MythicMob 类型                                                |
| [MythicPack](/skills/conditions/mythicpack)                                   | 元     | 检查 Pack 是否存在                                                            |
| [MythicPackVersion](/skills/conditions/MythicPackVersion)                     | 元     | 检查 Pack 是否具有指定版本                                                    |
| [MythicPackVersionGreater](/skills/conditions/MythicPackVersionGreater)       | 元     | 检查 Pack 的版本是否大于或等于指定版本                           |
| [Name](/skills/conditions/name)                                               | 实体   | 检查实体的名称                                                       |
| [NearClaim](/skills/conditions/nearclaim)                                     | 位置 | 目标位置是否靠近任何 GriefPrevention 领地                                     |
| [Night](/skills/conditions/night)                                             | 位置 | 如果游戏时间是夜晚，即 14000 到 22000                                      |
| [NotInRegion](/skills/conditions/notinregion)                                 | 位置 | 目标位置是否不在给定的 WorldGuard 区域内                              |
| [OffGCD](/skills/conditions/offgcd)                                           | 实体   | 检查目标生物是否处于全局冷却中                                        |
| [OnBlock](/skills/conditions/onblock)                                         | 位置 | 匹配目标实体站立的方块                                          |
| [OnGround](/skills/conditions/onground)                                       | 实体   | 目标实体是否站在实体地面上                                              |
| [OriginDistanceFromPin](/skills/conditions/OriginDistanceFromPin)             | 位置 | 检查起效点是否在指定钉点的特定距离内                          |
| [OriginLocation](/skills/conditions/OriginLocation)                           | 元     | 检查起效点是否在给定位置                                                   |
| [Outside](/skills/conditions/outside)                                         | 位置 | 目标头顶是否有开阔天空                                                         |
| [Owner](/skills/conditions/owner)                                             | 比较  | 检查目标实体是否为施法者的主人                                        |
| [OwnerIsOnline](/skills/conditions/ownerisonline)                             | 实体   | 检查目标生物的主人是否在线（如果主人是玩家）                     |
| [Pitch](/skills/conditions/pitch)                                             | 实体   | 检查目标实体的俯仰角是否在范围内                                    |
| [PlayerKills](/skills/conditions/playerkills)                                 | 实体   | 匹配目标生物击杀玩家的数量                                          |
| [PlayerNotWithin](/skills/conditions/playernotwithin)                         | 位置 | 检查目标半径范围内是否有玩家                                       |
| [PlayerWithin](/skills/conditions/playerwithin)                               | 位置 | 检查目标半径范围内是否有玩家                                       |
| [PlayersInRadius](/skills/conditions/playersinradius)                         | 实体   | 检查半径内的玩家数量                                                    |
| [PlayersInWorld](/skills/conditions/playersinworld)                            | 元     | 匹配施法者所在世界中的玩家数量                                         |
| [PlayersOnline](/skills/conditions/playersonline)                             | 元     | 匹配服务器在线玩家的数量                                                        |
| [Plugin](/skills/conditions/plugin)                                           | 元     | 检查指定插件是否在服务器上运行                                       |
| [Premium](/skills/conditions/premium)                                         | 元     | 检查服务器是否运行 MythicMobs Premium                                     |
| [ProjectileHasEnded](/skills/conditions/ProjectileHasEnded)                   | 元     | 检查调用的弹射物是否已结束                                                    |
| [Raining](/skills/conditions/raining)                                         | 位置 | 目标世界是否在下雨                                                     |
| [Region](/skills/conditions/region)                                           | 位置 | 目标是否在给定的 WorldGuard 区域内                                           |
| [SameFaction](/skills/conditions/samefaction)                                 | 实体   | 测试施法者和目标是否处于相同阵营                                       |
| [Score](/skills/conditions/score)                                             | 实体   | 检查目标实体的计分板值                                           |
| [ServerIsPaper](/skills/conditions/ServerIsPaper)                             | 元     | 检查服务器是否运行 Paper 分支。                                  |
| [ServerNmsVersion](/skills/conditions/servernmsversion)                       | 元     | 检查服务器是否运行指定的 Minecraft NMS 版本。                          |
| [ServerVersion](/skills/conditions/serverversion)                             | 元     | 检查服务器是否运行指定的 Minecraft 版本。                              |
| [ServerVersionAfterOrEqual](/skills/conditions/ServerVersionAfterOrEqual)     | 元     | 检查服务器版本是否在指定版本之后或与之相同                      |
| [ServerVersionBefore](/skills/conditions/ServerVersionBefore)                 | 元     | 检查服务器版本是否在指定版本之前                                 |
| [Size](/skills/conditions/Size)                                               | 实体   | 检查目标实体的大小                                                       |
| [SkillOnCooldown](/skills/conditions/skilloncooldown)                         | 实体   | 检查给定技能是否对目标处于冷却中                                       |
| [SpawnReason](/skills/conditions/SpawnReason)                                 | 实体   | 检查目标的生成原因                                          |
| [Sprinting](/skills/conditions/Sprinting)                                     | 实体   | 检查目标**玩家**是否在冲刺                                                  |
| [Stance](/skills/conditions/stance)                                           | 实体   | 检查目标生物的 stance                                                        |
| [StringEmpty](/skills/conditions/StringEmpty)                                 | 元     | 检查提供的字符串是否为空                                                        |
| [StringNotEmpty](/skills/conditions/StringNotEmpty)                           | 元     | 检查提供的字符串是否非空                                                    |
| [StringEquals](/skills/conditions/stringequals)                               | 元     | 检查 value1 是否等于 value2。两个值都可以使用变量和占位符。           |
| [Structure](/skills/conditions/structure)                                     | 位置 | 匹配目标位置是否在结构内部                                    |
| [Sunny](/skills/conditions/sunny)                                             | 位置 | 目标世界的天气是否为晴天。                                           |
| [TargetInLineOfSight](/skills/conditions/targetinlineofsight)                 | 实体   | 测试目标是否对其目标拥有视线                                        |
| [TargetNotInLineOfSight](/skills/conditions/targetnotinlineofsight)           | 实体   | 测试目标是否对其目标没有视线                               |
| [TargetWithin](/skills/conditions/targetwithin)                               | 实体   | 测试目标的目标是否在特定距离内                                    |
| [TargetNotWithin](/skills/conditions/targetnotwithin)                         | 实体   | 测试目标的目标是否不在特定距离内                                |
| [Targets](/skills/conditions/targets)                                         | 元     | 测试从父级技能树继承的目标数量是否匹配给定范围。  |
| [TemplateType](/skills/conditions/TemplateType)                               | 实体   | 检查目标生物是否继承自指定模板                                       |
| [Thundering](/skills/conditions/thundering)                                   | 位置 | 目标世界是否在雷暴                                                  |
| [TriggerBlockType](/skills/conditions/TriggerBlockType)                       | 元     | 检查触发技能的方块类型                              |
| [TriggerItemType](/skills/conditions/TriggerItemType)                         | 元     | 检查触发技能的物品材料类型                         |
| [VariableContains](/skills/conditions/VariableContains)                       | 元     | 检查给定变量是否包含特定值                                         |
| [VariableEquals](/skills/conditions/variableequals)                           | 元     | 检查给定变量是否具有某个特定值。                                          |
| [VariableInRange](/skills/conditions/variableinrange)                         | 元     | 检查给定数值变量是否在特定范围内。                               |
| [VariableIsSet](/skills/conditions/variableisset)                             | 元     | 检查给定变量是否已设置。                                                          |
| [VehicleIsDead](/skills/conditions/vehicleisdead)                             | 实体   | 检查施法者的骑乘载具是否已死亡。                                                |
| [Velocity](/skills/conditions/Velocity)                                       | 实体   | 检查目标实体的速度向量范围。                                  |
| [Wearing](/skills/conditions/wearing)                                         | 实体   | 测试目标实体装备了什么。                                                 |
| [World](/skills/conditions/world)                                             | 位置 | 检查目标世界的名称。                                                       |
| [WorldTime](/skills/conditions/worldtime)                                     | 位置 | 匹配目标位置所在世界的时间范围。                               |
| [Yaw](/skills/conditions/yaw)                                                 | 实体   | 检查目标实体的偏航角范围。                                       |
| [xDiff](/skills/conditions/xdiff)                                             | 实体   | 检查目标实体与施法者之间的 X 坐标差值。                     |
| [yDiff](/skills/conditions/ydiff)                                             | 实体   | 检查目标实体与施法者之间的 Y 坐标差值。                     |
| [zDiff](/skills/conditions/zdiff)                                             | 实体   | 检查目标实体与施法者之间的 Z 坐标差值。                     |

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
  - message{m="<mob.name> 开始施法"}
  - potion{t=SLOW;d=60;l=7}
  - delay 60
  - message{m="<target.name> &e燃烧了"}
  - effect:particles{p=flame;a=20;hS=3;vS=1;s=0;y=2}
  - potion{t=HARM;d=1;l=1}
```
[1] 并非所有条件在任何地方都适用。