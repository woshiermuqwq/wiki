创建生物时可用的全部选项。大部分选项放在 `Options` 区块下，示例如下：
```yml
Dummy:
  Type: skeleton
  Options:
    MovementSpeed: 0.3
    PreventSunburn: true
```

##
- [通用选项](/Mobs/Options#通用选项)
- [按群体分类的选项](/Mobs/Options#按群体分类的选项)
- [按生物类型分类的选项](/Mobs/Options#按生物类型分类的选项)
##

# 通用选项

以下选项为通用选项，对所有生物类型都有效。

#### AlwaysShowName
名称标签是否始终显示。
等效于 NBT 标签 `CustomNameVisible`。
默认为 `false`。
```yml
  Options:
    AlwaysShowName: false
```

#### AttackSpeed
生物的攻击速度。
默认为各生物的原版攻击速度。
```yaml
  Options:
    AttackSpeed: 1
```

#### VisibleByDefault
设置生物在生成或加载时是否默认可见。
默认为 `true`。
```yml
  Options:
    VisibleByDefault: true
```

#### Invisible
为生物施加永久隐身效果；无需通过 `~onSpawn` 触发器施加隐身药水。
默认为 `false`。
```yml
  Options:
    Invisible: true
```

#### Collidable
生物是否具有碰撞体积。Minecraft 中的碰撞是双向的，因此需要将碰撞双方的此项都设为 `false` 才能确保不发生碰撞，同时也能阻止玩家推动生物。默认为 `true`。
```yml
  Options:
    Collidable: true
```

#### DigOutOfGround
当生物受到窒息伤害时，将其向上传送两格。默认为 `false`。
```yml
  Options:
    DigOutOfGround: false
```

#### Despawn
决定生物的消失方式。
如果你使用了大量刷怪点、实体会压垮服务器，或者你制作的实体需要特殊的消失策略（如 NPC、Boss 等），建议开启此选项。
默认为 `true`。

| 模式            | 别名                    | 说明                                                                 |
|-----------------|------------------------|----------------------------------------------------------------------|
| NORMAL          | TRUE, YES              | - 周围没有玩家时消失<br>- 服务器重启时消失<br>- 区块卸载时消失<br>- 可被 MythicMobs 普通击杀命令杀死 |
| CHUNK           |                        | - 服务器重启时消失<br>- 区块卸载时消失<br>- 可被 MythicMobs 普通击杀命令杀死 |
| NEVER           | FALSE, NO              | - 可被 MythicMobs 普通击杀命令杀死 |
| PERSISTENT      |                        | - 区块卸载时将生物保存到世界文件中<br>- 服务器重启后仍然存在<br>- 持久化生物在未加载的区块中不会触发技能 |
| NPC             |                        | - 服务器重启时消失<br>- 区块卸载时消失 |

> 对于 PERSISTENT 消失模式：要移除一个持久化生物，你必须使用 kill 命令（`/mm m kill <类型>`）或在 killall 命令后追加 `-p` 参数（`/mm m killall -p`）。更多信息详见[这里](/Commands-and-Permissions#mob-commands)。

```yml
  Options:
    Despawn: true
```

#### FollowRange
生物锁定目标进行攻击或追踪的范围（格）。
默认为原版追踪范围——`32`。
```yml
  Options:
    FollowRange: 32
```

#### Glowing
设置生物是否永久发光。默认为 `false`。
```yml
  Options:
    Glowing: false
```

#### HealOnReload
允许不会消失的生物在其所在区块重新加载时恢复生命值。默认为 `false`。
```yml
  Options:
    HealOnReload: false
```

#### Invincible
使生物对所有类型的伤害完全免疫。此选项无法通过命令技能更改。
默认为 `false`。
```yml
  Options:
    Invincible: false
```

#### Interactable
设置生物是否可以被交互。如果生物是盔甲架，则会拒绝一切与其装备的交互。
默认为 `false`。
```yml
  Options:
    Interactable: false
```

#### LockPitch
阻止生物的头部上下转动。
默认为 `false`。
```yml
  Options:
    LockPitch: false
```

#### KnockbackResistance
攻击击退抗性的百分比。此选项的取值范围为 `0` 到 `1`。
但拥有 100% 击退抗性的生物仍然会被弓的附魔 `ARROW_KNOCKBACK`（冲击附魔）击退。
如需真正的击退免疫，请参考[速度](/Skills/mechanics/velocity)技能页面。默认为 `0`。
```yml
  Options:
    KnockbackResistance: 0.5
```

#### MaxCombatDistance
阻止距离超过指定格数的玩家对该生物造成伤害。
将此选项设置为小于生物某技能或攻击距离的值，可以确保生物能攻击到玩家，且不容易被利用。
默认为 `256`。
```yml
  Options:
    MaxCombatDistance: 256 
```

#### MovementSpeed
生物的移动速度。
大多数生物的默认移动速度为 `0.2`，任何高于 `1` 的值通常会让生物变得难以对抗或根本无法对抗。
```yml
  Options:
    MovementSpeed: 0.2
```

#### NoAI
生物是否禁用 AI。此选项会覆盖 [AIGoalSelectors](/Mobs/Mobs#aigoalselectors) 中指定的所有 AI 目标。
与 AIGoalSelectors 不同，此选项对硬编码 AI 的实体也有效。且如果设为 `true`，该生物将永远不会施放任何技能。
默认为 `false`。
```yml
  Options:
    NoAI: false
```

#### NoDamageTicks
定义生物受到伤害后无敌的时长（刻）。
如果为该生物启用了[免疫表](/Mobs/ImmunityTables)，则 `NoDamageTicks` 将按每个玩家分别计算，而非全局共用。
默认为 `10`。
```yml
  Options:
    NoDamageTicks: 20
```

#### NoGravity
生物是否不受重力影响。如果设为 `true`，该生物**无法**使用[速度](/Skills/mechanics/velocity)技能。
默认为 `false`。
```yml
  Options:
    NoGravity: false
```

#### PassthroughDamage
将生物受到的所有伤害传递给其父实体（如果存在）。生物的父实体是最初召唤该生物的那个实体。
默认为 `false`。
```yml
  Options:
    PassthroughDamage: false
```

#### PreventItemPickup
阻止生物捡起物品。
默认为 `true`。
```yml
  Options:
    PreventItemPickup: false
```

#### PreventLeashing
是否阻止给生物拴上拴绳。
默认为 `true`。
```yml
  Options:
    PreventLeashing: false
```

#### PreventMobKillDrops
阻止被 MythicMob 击杀的目标掉落战利品。
默认为 `false`。
```yml
  Options:
    PreventMobKillDrops: false
```

#### PreventOtherDrops
阻止生物掉落其原版战利品表。
默认为 `false`。
```yml
  Options:
    PreventOtherDrops: false
```

#### PreventRandomEquipment
阻止生物生成时携带随机装备。
默认为 `false`。
```yml
  Options:
    PreventRandomEquipment: false
```

#### PreventRenaming
阻止使用命名牌给生物重命名。
默认为 `true`。
```yml
  Options:
    PreventRenaming: false
```

#### PreventSunburn
阻止生物在阳光下燃烧。
默认为 `false`。
```yml
  Options:
    PreventSunburn: true
```

#### PreventTransformation
设置是否阻止生物转换为其他实体。
默认为 `true`。
```yaml
  Options:
    PreventTransformation: false
```

#### PreventVanillaDamage
取消生物造成的所有"常规"原版伤害。
触发 `onAttack` 的技能仍然会执行。
默认为 `false`。
```yml
  Options:
    PreventVanillaDamage: true
```

#### RepeatAllSkills
当生物的生命值恢复到高于某个基于生命值的技能阈值时，是否重新触发该技能。
默认为 `false`。
```yml
  Options:
    RepeatAllSkills: false
```

#### ReviveHealth
当生物的死亡事件被取消时（通过 [Cancelevent](/skills/mechanics/cancelevent) 技能配合 [~onDeath](/Skills/Triggers/onDeath)），该值指定生物将恢复到的生命值。如果值为 `-1`，则生物会恢复到自身的最大生命值。
```yaml
# 此生物每次死亡事件被取消时都会恢复到 50 点生命值
ExampleMob:
  Type: COW
  Health: 100
  Options:
    ReviveHealth: 50
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```
```yaml
# 此生物每次死亡事件被取消时都会恢复到最大生命值（100）
ExampleMob:
  Type: COW
  Health: 100  
  Options:
    ReviveHealth: -1
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```

#### Scale
生物的缩放比例。
如果设为 `-1`，则忽略此选项。
默认为 `-1`。
```yaml
  Options:
    Scale: 2
```

#### ShowHealth
通过广播消息显示生物的生命值，广播半径由 `/plugins/MythicMobs/config.yml` 中的 `Mobs.ShowHealth.Radius` 决定，格式由 `Mobs.ShowHealth.Formatting` 决定。
默认为 `false`。
```yml
  Options:
    ShowHealth: false
```

#### Silent
生物是否使用原版音效。
默认为 `false`。
```yml
  Options:
    Silent: false
```

#### UseThreatTable
生物是否启用[仇恨表](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Mobs/ThreatTables)
```yaml
  Options:
    UseThreatTable: true
```

#### RandomizeProperties
RandomizeProperties 是原版为生物生成时提供随机变体的功能，包括随机装备、僵尸领袖状态、动物变体、僵尸/蜘蛛骑士、生物大小、生成幼体的概率等。
当你高度自定义了实体行为且不希望出现原版随机化时，此选项非常有用。
默认为 `true`。
```yaml
  Options:
    RandomizeProperties: false
```

# 按群体分类的选项

## 船与箱子船

#### Type
船实体的[类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Boat.Type.html)。
别名：`BoatType`。
默认为 `OAK`。
```yaml
  Options:
    BoatType: MANGROVE
```

## 可繁殖生物

#### Age
生物的年龄。`-1` 表示幼体，`1` 表示成年。
适用于所有可以长大的生物，例如：羊、猪、牛……
当大于 0 时，表示该生物可以再次繁殖前还需等待的刻数。
等效于 NBT 中的 `Age`。
可以使用极小的负数来扭曲生物的模型（不受支持）。
在某些情况下可能无法正常工作。
默认为 `1`。
```yml
  Options:
    Age: -1
```

#### AgeLock
是否锁定生物的年龄。
用于防止幼年生物随时间长大。
如果你希望 Age 选项随时间推移持续生效，必须启用此选项。
默认为 `false`。
```yml
  Options:
    AgeLock: true
```

#### Adult
设置生物的成年状态。
在 `Age` 不生效时使用。
```yml
  Options:
    Adult: true
```

#### Baby
设置生物的幼年/成年状态。
在 `Age` 不生效时使用。
```yml
  Options:
    Baby: true
```

## 可染色生物

适用于马、羊驼、流浪商人羊驼、鹦鹉、羊、潜影贝、热带鱼和狼。
### Color
设置生物的颜色（羊的羊毛颜色或狼的项圈颜色）。
取值可以是任意一种[颜色](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)。
默认为 `WHITE`。
```yml
  Options:
    Color: RED
```

## 中立实体

例如适用于狼和僵尸猪人。

#### Angry
生物生成时是否处于愤怒状态。
> 注意：由于 Bukkit/Spigot 的 bug，狼无法以此选项生成愤怒状态。
> 如果你需要生成愤怒的狼，请使用 AIGoalSelectors 和 AITargetSelectors。
默认为 `false`。
```yaml
  Options:
    Angry: true
```

## 史莱姆与岩浆怪

#### PreventSlimeSplit
阻止史莱姆和岩浆怪分裂。
默认为 `false`。
```yaml
  Options:
    PreventSlimeSplit: true
```

## 可变大小的实体

#### Size
设置史莱姆、岩浆怪和幻翼的大小。
可以设置得非常大，且每次增大都会让体型呈指数级增长。
极高的值会导致服务器卡顿甚至崩溃。
默认为 `1to8`（幻翼默认为 `1`）。
```yaml
  Options:
    Size: 10
```

## 袭击者

#### CanJoinRaid
实体是否可以加入袭击。
默认为 `true`。
```yaml
  Options:
    CanJoinRaid: false
```

#### PatrolLeader
实体是否为巡逻队队长。
默认为 `false`。
```yaml
  Options:
    PatrolLeader: true
```

#### PatrolSpawnPoint
默认为 `false`。
```yaml
  Options:
    PatrolSpawnPoint: true
```

## 可驯服生物

#### Tameable
玩家是否可以驯服该生物。用于狼、猫和马。
默认为 `false`。
```yaml
  Options:
    Tameable: true
```

## 僵尸（所有变种）

#### PreventJockeyMounts
设置是否阻止僵尸生成时成为骑士。
仅对僵尸有效。
默认为 `false`。
```yaml
  Options:
    PreventJockeyMounts: true
```

#### PreventConversion
阻止僵尸转换为其他类型的僵尸。
默认为 `false`。
```yaml
  Options:
    PreventConversion: true
```

#### ReinforcementsChance
僵尸受到伤害时召唤增援的概率。
取值范围为 0 到 1（对应 0% 到 100% 的概率）。
仅对僵尸有效。
默认为 `0`。
```yaml
  Options:
    ReinforcementsChance: 0.38
```

# 按生物类型分类的选项

以下选项仅针对特定生物类型，用在其他生物类型上不会产生效果。

## 盔甲架

#### CanMove
设置盔甲架是否可以移动。默认为 `true`，需要 PaperSpigot。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanMove: true
```

#### CanTick
设置盔甲架是否可以 tick。默认为 `true`，需要 PaperSpigot。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanTick: true
```

#### HasArms
设置盔甲架是否有手臂。默认为 `false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasArms: true
```

#### HasBasePlate
设置盔甲架是否有底座。默认为 `true`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasBasePlate: false
```

#### HasGravity
设置盔甲架是否受重力影响。默认为 `true`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasGravity: true
```

#### Invisible
设置盔甲架是否隐身。默认为 `false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Invisible: true
```

#### ItemBody
指定放入盔甲架身体/胸甲槽位的 [Mythic 物品](/Items/Items)。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemBody: AN_EXAMPLE_CHESTPLATE
```

#### ItemFeet
指定放入盔甲架脚部槽位的 [Mythic 物品](/Items/Items)。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemFeet: AN_EXAMPLE_BOOTS
```

#### ItemHand
指定放入盔甲架主手槽位的 [Mythic 物品](/Items/Items)。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHand: AN_EXAMPLE_SWORD
```

#### ItemOffhand
指定放入盔甲架副手槽位的 [Mythic 物品](/Items/Items)。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemOffhand: AN_EXAMPLE_STICK
```

#### ItemHead
指定放入盔甲架头盔槽位的 [Mythic 物品](/Items/Items)。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHead: AN_EXAMPLE_HELMET
```

#### ItemLegs
指定放入盔甲架护腿槽位的 [Mythic 物品](/Items/Items)。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemLegs: AN_EXAMPLE_PANTS
```

#### Marker
将盔甲架设为标记。此选项可阻止盔甲架在游戏中被破坏，使其完全不可交互。默认为 `false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Marker: false
```

#### Small
将盔甲架设为小型变体。默认为 `false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Small: true
```

#### Pose
设置身体各部位的当前姿态。
默认值为 `0,0,0`，支持使用 `#to#` 的随机范围格式。
这些配置放在 `Pose` 区块下，而非 `Options` 区块。
###### 头部
```yml
Mob:
  Type: armor_stand
  Pose:
    Head: 0,50,0
```
###### 身体
```yml
Mob:
  Type: armor_stand
  Pose:
    Body: 0,10,10
```
###### 左臂
```yml
Mob:
  Type: armor_stand
  Pose:
    LeftArm: 0to360,0,0
```
###### 右臂
```yml
Mob:
  Type: armor_stand
  Pose:
    RightArm: 0to90,0,0
```
###### 左腿
```yml
Mob:
  Type: armor_stand
  Pose:
    LegLeg: 0,0to80,0
```
###### 右腿
```yml
Mob:
  Type: armor_stand
  Pose:
    RightLeg: 20,25,0
```

## 蜜蜂

#### Anger
设置蜜蜂愤怒状态持续的刻数。
设为 0 表示蜜蜂不会愤怒。
默认为 `0`。
```yaml
  Options:
    Anger: 200
```

#### HasNectar
蜜蜂是否携带花粉。
默认为 `false`。
```yaml
  Options:
    HasNectar: true
```

#### HasStung
蜜蜂是否已经蜇过实体。
默认为 `false`。
```yaml
  Options:
    HasStung: true
```

#### PreventStingerLoss
是否阻止蜜蜂在攻击实体后失去螫针。
默认为 `false`。
```yaml
  Options:
    PreventStingerLoss: true
```

## 骆驼

#### Saddled
实体是否已装上鞍。
默认为 `false`。
```yaml
  Options:
    Saddled: true
```

#### Tamed
实体是否已被驯服。
默认为 `false`。
```yaml
  Options:
    Tamed: true
```

## 猫

#### CatType
设置猫的种类。
可选种类：ALL_BLACK、BLACK、BRITISH_SHORTHAIR、CALICO、PERSIAN、JELLIE、RAGDOLL、RED、SIAMESE、TABBY、WHITE。
```yaml
  Options:
    CatType: BLACK
```

#### CollarColor
设置猫项圈的颜色。
可选颜色：BLACK、BLUE、BROWN、CYAN、GRAY、GREEN、LIGHT_BLUE、LIGHT_GRAY、LIME、MAGENTA、ORANGE、PINK、PURPLE、RED、WHITE、YELLOW。
```yaml
  Options:
    CollarColor: GREEN
```

#### Tamed
实体是否已被驯服。
默认为 `false`。
```yaml
  Options:
    Tamed: true
```

## 鸡

#### Jockey
鸡是否将 NBT 标签 `IsChickenJockey` 设置为 1。
如果为 true，则鸡可以自然消失，死亡时掉落 10 点经验（而非 1-3 点），且不能下蛋。
默认为 `false`。
```yaml
  Options:
    Jockey: true
```

## 苦力怕

#### ExplosionRadius
设置苦力怕爆炸的半径/威力。
负值将被忽略，爆炸半径保持苦力怕的默认值。
默认为 `-1`。
```yaml
  Options:
    ExplosionRadius: 5
```

#### FuseTicks
设置苦力怕引爆所需的刻数。
负值将被忽略，引爆时间保持苦力怕的默认值。
默认为 `-1`。
```yaml
  Options:
    FuseTicks: 60
```

#### SuperCharged
苦力怕是否以超级充能形态生成。
默认为 `false`。
```yaml
  Options:
    SuperCharged: true
```

#### PreventSuicide
阻止苦力怕在爆炸后死亡。需要将游戏规则 `mobGriefing` 设为 true 才能使此选项生效。
默认为 `false`。
```yaml
  Options:
    PreventSuicide: true
```

## 末影人

#### PreventTeleport
主要针对末影人，但可能对其他生物也有效。可能会破坏传送技能！
默认为 `false`。
```yaml
  Options:
    PreventTeleport: true
```

#### HeldBlock
设置末影人手持的方块。
默认为 `AIR`。
```yaml
  Options:
    HeldBlock: STONE
```

## 经验球

#### Experience
设置经验球生物给予的经验值。
默认为 `1`。
```yaml
  Options:
    Experience: 10
```

## 掉落方块

#### Block
决定方块的[类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。
默认为 `STONE`。
```yaml
  Options:
    Block: BIRCH_WOOD
```

#### BlockData
输入方块数据的附加字段。
默认为 `0`。

#### DropsItem
实体是否应该掉落该掉落方块的物品形式。
默认为 `true`。
```yaml
  Options:
    DropsItem: false
```

#### HurtsEntities
撞击时是否对实体造成伤害。
默认为 `true`。
```yaml
  Options:
    HurtsEntities: false
```

#### ReplaceSpawnLocationBlock
实体是否应替换其生成位置的方块。
默认为 `false`。
```yaml
  Options:
    ReplaceSpawnLocationBlock: true
```

#### UseSpawnLocationType
掉落方块的类型是否应使用生成位置的方块类型。
默认为 `false`。
```yaml
  Options:
    UseSpawnLocationType: true
```

## 狐狸

#### FoxType
决定狐狸的种类。
可选值：`RED` 或 `SNOW`。
默认为 `RED`。
```yaml
  Options:
    FoxType: SNOW
```

## 青蛙

#### Type
决定青蛙的种类。
别名：`Variant`。
可选值：`WARM`、`COLD` 或 `TEMPERATE`。
默认为 `WARM`。
```yaml
  Options:
    Type: COLD
```

## 山羊

#### Screaming
设置此山羊是否为尖叫山羊。尖叫山羊会发出尖叫声且冲撞更频繁。
默认为 `false`。
```yaml
  Options:
    Screaming: true
```

## 疣猪兽

#### ImmuneToZombification
疣猪兽是否免疫僵尸化。
默认为 `false`。
```yaml
  Options:
    ImmuneToZombification: true
```

#### Huntable
疣猪兽是否可以被猪灵猎杀。
默认为 `true`。
```yaml
  Options:
    Huntable: true
```

## 马、驴和骡

#### HorseArmor
用于设置马身上护甲的类型。
可选值：`iron`、`gold`、`diamond`。
[护甲类型]必须为小写。
```yaml
  Options:
    HorseArmor: gold
```

#### CarryingChest
用于设置驴是否携带箱子。
默认为 `false`。
```yaml
  Options:
    CarryingChest: true
```

#### HorseColor
设置马的颜色。
颜色必须大写，可以是任意一种 [Spigot 马的颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Color.html)。
```yaml
  Options:
    HorseColor: CREAMY
```

#### Saddled
用于设置马是否已装上鞍。
如果设置了 [HorseArmor](#horsearmor) 则默认为 `true`，否则默认为 `false`。
```yaml
  Options:
    Saddled: true
```

#### HorseStyle
设置马的斑纹样式。
样式可以是任意一种 [Spigot 马样式](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Style.html)。
```yaml
  Options:
    HorseStyle: WHITE_DOTS
```

#### Tamed
用于设置马是否已被驯服。
默认为 `false`。
```yaml
  Options:
    Tamed: true
```

#### HorseType
定义马的种类。
可以是任意一种 [Spigot 马变体](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Variant.html)。
默认为 `HORSE`。
**在 MC 1.11+ 中已移除，请改用 [Type](/Mobs/Mobs#type)。**

## 交互实体
#### Height
交互实体的高度。
默认为 `1`。
```yaml
  Options:
    Height: 2
```

#### Width
交互实体的宽度。
默认为 `Height` 选项的值。
```yaml
  Options:
    Width: 3
```

#### Responsive
交互实体是否可响应。
默认为 `true`。
```yaml
  Options:
    Responsive: false
```

## 铁傀儡
#### PlayerCreated
表现得像是玩家建造了该生物。
默认为 `false`。
```yaml
  Options:
    PlayerCreated: true
```

## 物品实体

#### Item
物品实体的材质。
默认为 `STONE`。
```yaml
  Options:
    Item: BRICK
```

#### Amount
物品堆中的物品数量。
默认为 `1`。
```yaml
  Options:
    Amount: 10
```

#### CanPickup
物品堆是否可以被捡起。
默认为 `true`。
```yaml
  Options:
    CanPickup: false
```

## 羊驼

#### CarryingChest
设置实体是否携带箱子。
默认为 `false`。
```yaml
  Options:
    CarryingChest: true
```

#### Tamed
设置实体是否已被驯服。
默认为 `false`。
```yaml
  Options:
    Tamed: true
```

#### Color
设置羊驼的颜色。
颜色必须大写，可以是任意一种 [Spigot 羊驼颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Llama.Color.html)。
```yaml
  Options:
    Color: CREAMY
```

## 箱子矿车

#### ChestContents
将放入箱子内的[掉落表]。
```yaml
  Options:
    ChestContents: example_droptable
```

## 熊猫

#### MainGene
设置熊猫可以遗传给后代的[主基因](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Panda.Gene.html)。
可选值：NORMAL、AGGRESSIVE、LAZY、WORRIED、PLAYFUL、WEAK、BROWN。
默认为 `NORMAL`。
```yaml
  Options:
    MainGene: LAZY
```

#### HiddenGene
设置熊猫可以遗传给后代的[隐性基因](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Panda.Gene.html)。
可选值：NORMAL、AGGRESSIVE、LAZY、WORRIED、PLAYFUL、WEAK、BROWN。
默认为 `NORMAL`。
```yaml
  Options:
    HiddenGene: WORRIED
```

## 鹦鹉

#### Variant
鹦鹉的[变体](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Parrot.Variant.html)。
```yaml
  Options:
    Variant: GRAY
```

#### FlyingSpeed
鹦鹉的飞行速度。
默认为 `-1`（不应用此选项）。
```yml
  Options:
    FlyingSpeed: 0.2
```

## 猪

#### Saddled
猪是否已装上鞍。
默认为 `false`。
```yaml
  Options:
    Saddled: true
```

## 猪灵

#### AbleToHunt
猪灵是否能够猎杀。
默认为 `true`。
```yaml
  Options:
    AbleToHunt: false
```

#### ImmuneToZombification
猪灵是否免疫僵尸化。
默认为 `true`。
```yaml
  Options:
    ImmuneToZombification: false
```

## 猪灵蛮兵

#### ImmuneToZombification
猪灵是否免疫僵尸化。
默认为 `true`。
```yaml
  Options:
    ImmuneToZombification: false
```

## 兔子

#### IsKillerBunny
别名：`Angry`。
将兔子设为杀手兔。
默认为 `false`。
```yaml
  Options:
    IsKillerBunny: true
```

#### RabbitType
设置兔子的[种类](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Rabbit.Type.html)。
可选种类：BLACK、BLACK_AND_WHITE、BROWN、GOLD、SALT_AND_PEPPER、THE_KILLER_BUNNY、WHITE。
```yaml
  Options:
    RabbitType: SALT_AND_PEPPER
```

## 羊

#### Sheared
羊是否已被剪毛。
默认为 `false`。
```yaml
  Options:
    Sheared: true
```

## 蠹虫

#### PreventBlockInfection
阻止蠹虫感染方块。
默认为 `false`。
```yaml
  Options:
    PreventBlockInfection: true
```

## 骷髅

#### PreventConversion
阻止骷髅转换为其他类型的骷髅。
默认为 `false`。
```yaml
  Options:
    PreventConversion: true
```

## 雪傀儡

#### Derp
雪傀儡的南瓜是否已被剪掉。
默认为 `false`。
```yaml
  Options:
    Derp: true
```

#### PreventSnowFormation
阻止雪傀儡制造雪。
默认为 `false`。
```yaml
  Options:
    PreventSnowFormation: true
```

## TNT

#### FuseTicks
TNT 爆炸所需的刻数。
默认为 `-1`（立即爆炸）。
```yaml
  Options:
    FuseTicks: 100
```

#### ExplosionYield
决定爆炸的强度。
默认为 `-1`（使用普通 TNT 的爆炸威力）。
```yaml
  Options:
    ExplosionYield: 2
```

#### Incendiary
爆炸是否能够引发火焰。
默认为 `false`。
```yaml
  Options:
    Incendiary: true
```

## 热带鱼

#### Pattern
设置鱼的[形状/花纹](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/TropicalFish.Pattern.html)。
```yaml
  Options:
    Pattern: GLITTER
```

#### BodyColor
设置鱼的[主色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。
```yaml
  Options:
    BodyColor: GRAY
```

## PatternColor
设置鱼的[副色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。
```yaml
  Options:
    BodyColor: LIME
```

## 村民

#### HasTrades
村民是否可以交易。
默认为 `false`。
> 详见 [Trades](/Mobs/Mobs#trades)
```yaml
  Options:
    HasTrades: true
```

#### Profession
指定村民的[职业](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Profession.html)。
未设置此选项的村民在初始生成时会随机分配一个职业。
```yaml
  Options:
    Profession: MASON
```

#### Type
表示[村民类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Type.html)，通常对应其生成所在的生物群系。
默认为 PLAINS。
```yaml
  Options:
    Type: DESERT
```

#### Level
村民的职业等级，等级 1 到 5。
等级 1 的村民可能会更换职业。如果你希望村民固定职业，请将其等级设为 2 或更高。
设置村民职业时必需。
```yaml
  Options:
    Level: 3
```

## 狼

#### Variant
设置[狼的变体](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Wolf.Variant.html)。
```yaml
  Options:
    Variant: black
```

#### Color
设置狼项圈的[颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。
```yaml
  Options:
    Color: RED
```

## 僵尸村民

#### Profession
指定僵尸村民的[职业](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Profession.html)。
此选项还会使僵尸村民在被药水治愈后转换为对应类型的村民。
默认为 `FARMER`。
```yaml
  Options:
    Profession: MASON
```

[掉落表]: /drops/Drops#drop-tables
