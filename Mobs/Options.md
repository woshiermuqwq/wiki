All 选项 available when creating a 生物. 大部分se 选项 go 在...下 `Options` section, like so:
```yml
Dummy:
  Type: skeleton
  Options:
    MovementSpeed: 0.3
    PreventSunburn: true
```

##
- [Universal 选项](/生物/选项#universal-选项)
- [Group Specific 选项](/生物/选项#group-specific-选项)
- [生物 Specific 选项](/生物/选项#生物-specific-选项)
##

# Universal 选项

These 选项 are universal and will work 无论 the 生物 类型.

#### AlwaysShowName
the 名称-tag是否总是 displayed。
Equivalent to the NBT-tag `CustomNameVisible`.
Defaults to `false`.
```yml
  Options:
    AlwaysShowName: false
```

#### AttackSpeed
ThThe 攻击 速度 of the 生物
Defaults to 原版 攻击 速度 of the respective 生物
```yaml
  Options:
    AttackSpeed: 1
```

#### VisibleByDefault
设是否 the 生物 is visible 默认情况下 when the 生物 spawns or when the 生物 gets loaded。
Defaults to `true`.
```yml
  Options:
    VisibleByDefault: true
```

#### Invisible
将permanent invisibility 效果 on the 生物; no need设应用 invisibility 药水 with `~onSpawn` 触发器。
Defaults to `false`.
```yml
  Options:
    Invisible: true
```

#### Collidable
Whether the 生物 has collisions. Collisions in Minecraft are bidirectional, so this would need to be set to `false` on 两者都
the 实体 colliders to ensure that no collisions takes place but 还将 stop the 玩家 from pushing the 生物. Defaults to `true`.
```yml
  Options:
    Collidable: true
```

#### DigOutOfGround
Teleports the 生物 two 方块 up if it takes `SUFFOCATION` 伤害. Defaults to `false`.
```yml
  Options:
    DigOutOfGround: false
```

#### 消失
决定how the 生物 will 消失。
ThThis 选项 应为 turned on if 您是 using a lot of 生物 生成器 or 实体 will overwhelm your 服务器, or the 实体 you are making 需要 some special 行为 regarding its 消失 policy (Npcs, Boss etc.)
DDefaults to `true`.

| 模式 | 别名 | Description |
|-----------------|------------------------|-------------------------------------------------------------|
| NORMAL | TRUE, YES | - Despawns if no 玩家 are nearby<br>- Despawns if the 服务器 is restarted<br>- Despawns if the chunk is unloaded<br>- Is killed by normal mythicmobs kill 指令 |
| CHUNK | | - Despawns if the 服务器 is restarted<br>- Despawns if the chunk is unloaded<br>- Is killed by normal mythicmobs kill 指令 |
| NEVER | FALSE, NO | - Is killed by normal mythicmobs kill 指令 |
| PERSISTENT | | - Saves the 生物 in the 世界 文件 一旦 a chunk unloads.<br>- Persists across 服务器 reboots.<br>- Persistent 生物 不要 触发 技能 in unloaded chunks. |
| NPC | | - Despawns if the 服务器 is restarted<br>- Despawns if the chunk is unloaded |

> For the PERSISTENT 消失 模式: to 移除 a persistent 生物, 您必须 也 use the kill 指令 (`/mm m kill <type>`) or append the `-p` 标志 to the killall one (`/mm m killall -p`). More information on the subject可以found[here](/指令-and-权限#生物-指令)。

```yml
  Options:
    Despawn: true
```

#### FollowRange
The 范围 in 方块 在...内 which a 生物 will 目标 to 攻击 or track an 实体.
Defaults to 原版 follow 范围 - `32`.
```yml
  Options:
    FollowRange: 32
```

#### Glowing
将是否 the 生物 is 永久 glowing. Defaults设`false`。
```yml
  Options:
    Glowing: false
```

#### HealOnReload
Allows non-despawning 生物 to heal 一旦 the chunk 它们是 in gets reloaded. Defaults to `false`.
```yml
  Options:
    HealOnReload: false
```


#### Invincible
使生物完全 invincible to all 类型 of 伤害. This 选项 不能 be changed by 指令 技能。
Defaults to `false`.
```yml
  Options:
    Invincible: false
```

#### Interactable
设是否 the 生物 can be interacted with. If the 生物 is an armor stand, 它将 deny any interaction 与 equipments。
Defaults to `false`.
```yml
  Options:
    Interactable: false
```

#### LockPitch
Keeps the 生物 head from looking up/down.
Defaults to `false`.
```yml
  Options:
    LockPitch: false
```

#### KnockbackResistance
Aknockback resisted from 攻击. This 选项 can be 任何地方 between `0` and `1`的percentage。
But a 生物 with 100% knockback resistance can 仍然 be knocked back by a bow 附魔: `ARROW_KNOCKBACK` (punch 附魔).
For true knockback resistance, see the [速度向量](/技能/机制/速度向量) 机制 page. Defaults to `0`.
```yml
  Options:
    KnockbackResistance: 0.5
```

#### MaxCombatDistance
Prevents 玩家 即 a number of 方块 远离 damaging the 生物.
设置 this 选项 to a number 小于 the 距离 of a certain 生物 技能 or 攻击 will ensure that the 生物 can 伤害 the 玩家 and 不会 be as easy to exploit.
Defaults to `256`.
```yml
  Options:
    MaxCombatDistance: 256 
```

#### MovementSpeed
The 移动 速度 of the 生物.
Most 生物 has a 默认 move 速度 of `0.2` and any 值 higher than `1` tends to make a 生物 difficult or impossible to fight.
```yml
  Options:
    MovementSpeed: 0.2
```

#### NoAI
Whether the 生物 should have AI. This 选项 覆盖 any AI 目标 specified in [AIGoalSelectors](/生物/生物#aigoalselectors).
As opposed to AIGoalSelectors, this will work on 实体 that have hardcoded AI. And if 这是 set to `true`, the 生物 永远不会 cast any 技能.
Defaults to `false`.
```yml
  Options:
    NoAI: false
```

#### NoDamageTicks
Defines how long in ticks the 生物 is invulnerable 之后 taking 伤害.
若[ImmunityTables](/生物/ImmunityTables) is 启用 对于 生物，then `NoDamageTicks`将willbe per 玩家 而不是 global。
Defaults to `10`.
```yml
  Options:
    NoDamageTicks: 20
```

#### NoGravity
Whether the 生物 不应 have gravity. If set to `true`, the 生物 **CANNOT** have the [速度向量](/技能/机制/速度向量) 机制 used on it.
Defaults to `false`.
```yml
  Options:
    NoGravity: false
```

#### Pass通过Damage
使all 伤害 takenbe redirected to the 生物 父级, if one exists. A 生物 父级 is the 实体 that initially summoned the 生物。
Defaults to `false`.
```yml
  Options:
    PassthroughDamage: false
```

#### PreventItemPickup
Prevent 生物 from picking up 物品;
Defaults to `true`.
```yml
  Options:
    PreventItemPickup: false
```

#### PreventLeashing
Whether to prevent a leash from being placed on the 生物.
Defaults to `true`.
```yml
  Options:
    PreventLeashing: false
```

#### PreventMobKillDrops
Prevents a MythicMob 目标 from dropping loot.
Defaults to `false`.
```yml
  Options:
    PreventMobKillDrops: false
```

#### PreventOtherDrops
Prevents the 生物 from dropping its 原版 loot 表.
Defaults to `false`.
```yml
  Options:
    PreventOtherDrops: false
```

#### PreventRandomEquipment
Prevents the 生物 from spawning with random 装备.
Defaults to `false`.
```yml
  Options:
    PreventRandomEquipment: false
```

#### PreventRenaming
Prevents the 生物 from being renamed using a nametag.
Defaults to `true`.
```yml
  Options:
    PreventRenaming: false
```

#### PreventSunburn
Prevents the 生物 from burning in the sun.
Defaults to `false`.
```yml
  Options:
    PreventSunburn: true
```

#### PreventTransformation
Se设是否 the 生物 应为 prevented from being turned into 其他 实体。
DeDefaults to `true`.
```yaml
  Options:
    PreventTransformation: false
```

#### PreventVanillaDamage
CaCancels every instance of the 生物 dealing "regular" 原版 伤害, canceling it.
Sk技能 that 触发器 onAttack 仍会 be executed.
Defaults to `false`.
```yml
  Options:
    PreventVanillaDamage: true
```

#### RepeatAllSkills
Whether to repeat 生命值 based 技能 if a 生物 heals back 在...上方 血量 threshold.
Defaults to `false`.
```yml
  Options:
    RepeatAllSkills: false
```

#### ReviveHealth
When the 生物 death 事件 gets cancelled (via a [Cancelevent](/技能/机制/cancelevent) 机制 [~onDeath](/技能/触发器/onDeath)) the one specified is the 数量 of 血量 the 生物 将 set to. If the 值 is `-1`, the 生物 will heal to its own max 血量 值.
```yaml
#This mob will always return to 50 health every time the death event is cancelled
ExampleMob:
  Type: COW
  Health: 100
  Options:
    ReviveHealth: 50
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```
```yaml
#This mob will always return to its maximum health (100) every time the death event is cancelled
ExampleMob:
  Type: COW
  Health: 100  
  Options:
    ReviveHealth: -1
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```

#### Scale
ThThe scale of the 生物.
If若set to -1，the 选项将isignored。
DeDefaults to `-1`.
```yaml
  Options:
    Scale: 2
```

#### ShowHealth
Displays the 血量 of the 生物 通过 消息 broadcast 在...内 a 半径 and formatting by `Mobs.ShowHealth.Radius` and `Mobs.ShowHealth.Formatting`, 分别, in `/plugins/MythicMobs/config.yml`
Defaults to `false`.
```yml
  Options:
    ShowHealth: false
```

#### Silent
Whether a 生物 should use 原版 sound 效果.
DDefaults to `false`.
```yml
  Options:
    Silent: false
```

#### UseThreatTable
Whether the 生物 should have [仇恨表](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/生物/ThreatTables) 启用
```yaml
  Options:
    UseThreatTable: true
```

#### RandomizeProperties
RaRandomizeProperties is the 原版 feature in 充能 of giving variations to 生物 when they 生成, 例如 装备, zombie leader status, animal variations, zombie/spider jockey, 生物 size, 概率 of spawning as baby, etc
ThThis is ideal if you are heavily overriding 实体 行为 and 不要 want the natural randomization
Defaults to `true`
```yaml
  Options:
    RandomizeProperties: false
```


# Group specific 选项

## Boat & BoatChest

#### 类型
ThThe [类型 of the boat 实体](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Boat.类型.html).
Aliases: `BoatType`.
Defaults to `OAK`
```yaml
  Options:
    BoatType: MANGROVE
```

## Breedable 生物

#### Age
ThThe age of the 生物. Use `-1` for Baby and `1` for Adults.
UsUsable on any 生物 that can age. For 示例: Sheep, Pigs, Cows...
WhWhen above 0, 表示 the number of ticks 之前 this 生物 can breed 再次.
EqEquivalent to the `Age` NBT.
UsUse very low negative numbers to mess 与 生物 model (not 支持).
MaMay not be working properly under some situations.
DeDefaults to `1`.
```yml
  Options:
    Age: -1
```

#### AgeLock
是否应locked in placethe 生物 age。
Useful for keeping a baby 生物 from growing up 随时间.
This is 必需 if 您想要 Age 选项 to work 随时间.
Defaults to `false`.
```yml
  Options:
    AgeLock: true
```

#### Adult
设adult status of 生物。
Use if `Age` 不 work.
```yml
  Options:
    Adult: true
```

#### Baby
设baby/adult status of 生物。
Use if `Age` 不 work.
```yml
  Options:
    Baby: true
```

## Colorable 生物

Used for Horses, Llamas, TraderLlamas, Parrots, Sheeps, Shulkers, TropicalFishes and Wolves
### 颜色
设color of the 生物 (wool color of sheep or the collar color of wolves)。
The 值 can be any of this [Colors](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)
Defaults to `WHITE`.
```yml
  Options:
    Color: RED
```


## Neutral 实体

Used for wolves and zombie pigmen, 例如.

#### Angry
Whether the 生物 will 生成 angry or not.
> 注意: Due to a Bukkit/Spigot bug wolves can not be spawned angry with this 选项.
> Use AIGoalSelectors and AITargetSelectors if 您想要 to 生成 angry wolves.
Defaults to `false`.
```yaml
  Options:
    Angry: true
```

## Slimes & Magma Cubes

#### PreventSlimeSplit
Prevents slimes and magmacubes from splitting.
默认 to `false`.
```yaml
  Options:
    PreventSlimeSplit: true
```

## 实体 with 变量 size

#### Size
设size of slimes, magma cubes, and phantoms。
Can get VERY big and get exponentially larger with each increase.
Extremely high size will cause 服务器 lag and possibly crashes.
默认 to `1to8` (Phantoms is `1`)
```yaml
  Options:
    Size: 10
```


## Raiders

#### CanJoinRaid
Whether the 实体 can join a raid.
Defaults to `true`.
```yaml
  Options:
    CanJoinRaid: false
```

#### PatrolLeader
the 实体是否the leader of a patrol。
Defaults to `false`.
```yaml
  Options:
    PatrolLeader: true
```

#### PatrolSpawnPoint
Defaults to `false`.
```yaml
  Options:
    PatrolSpawnPoint: true
```


## Tameable 生物

#### Tameable
Whether 玩家 are able to tame the 生物. Used for wolves, cats and horses.
Defaults to `false`.
```yaml
  Options:
    Tameable: true
```


## Zombies (all variants)

#### PreventJockeyMounts
Se将是否 the zombie 将 prevented from spawning设a jockey。
OnOnly works for Zombies.
DeDefaults to `false`.
```yaml
  Options:
    PreventJockeyMounts: true
```

#### PreventConversion
PrPrevents the Zombie from being converted into 其他 类型 of zombies.
Defaults to `false`.
```yaml
  Options:
    PreventConversion: true
```


#### ReinforcementsChance
Ch概率 for zombies to 生成 reinforcements on taking 伤害.
ShShould be a number between 0 and 1 (0% and 100% 概率).
OnOnly works for Zombies.
DeDefaults to `0`.
```yaml
  Options:
    ReinforcementsChance: 0.38
```



# 生物 specific 选项

These are specific 生物 选项 and 将有 no 效果 when used on a
didifferent 生物 类型.

## Armor Stand

#### CanMove
Se将是否 an armor stand can move. Defaults设`true` and 需要 PaperSpigot。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanMove: true
```

#### CanTick
Se将是否 an armor stand can tick. Defaults设`true` and 需要 PaperSpigot。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanTick: true
```

#### HasArms
Se将是否 an armor stand has arms. Defaults设`false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasArms: true
```

#### HasBasePlate
Se将是否 an armor stand has a baseplate. Defaults设`true`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasBasePlate: false
```

#### HasGravity
Se将是否 the armor stand is affected by gravity. Defaults设`true`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasGravity: true
```

#### Invisible
Se将是否 the armor stand is invisible. Defaults设`false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Invisible: true
```

#### ItemBody
DeDesignates the [Mythic 物品](/物品/物品) that should go in the body/chest 栏位 of an armor stand.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemBody: AN_EXAMPLE_CHESTPLATE
```

#### ItemFeet
DeDesignates the [Mythic 物品](/物品/物品) that should go in the feet 栏位 of an armor stand.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemFeet: AN_EXAMPLE_BOOTS
```

#### ItemHand
DeDesignates the [Mythic 物品](/物品/物品) that should go in the main hand 栏位 of an armor stand.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHand: AN_EXAMPLE_SWORD
```

#### ItemOffhand
DeDesignates the [Mythic 物品](/物品/物品) that should go in the off hand 栏位 of an armor stand.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemOffhand: AN_EXAMPLE_STICK
```

#### ItemHead
DeDesignates the [Mythic 物品](/物品/物品) that should go in the helmet 栏位 of an armor stand.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHead: AN_EXAMPLE_HELMET
```

#### ItemLegs
DeDesignates the [Mythic 物品](/物品/物品) that should go in the leggings 栏位 of an armor stand.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemLegs: AN_EXAMPLE_PANTS
```

#### Marker
将armor stand设a marker. This 选项 阻止 the armor stand from being destroyed in game,。
mamaking it 完全 non-interactable. Defaults to `false`.
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Marker: false
```

#### Small
Se将armor stand设small variant. Defaults to `false`。
```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Small: true
```

#### Pose
Se设body part current pose。
De默认 值 are `0,0,0` and accepts ranges like `#to#`.
ThThese will go 在...下 `Pose` section 而不是 the `Options` section.
###### Head
```yml
Mob:
  Type: armor_stand
  Pose:
    Head: 0,50,0
```
###### Body
```yml
Mob:
  Type: armor_stand
  Pose:
    Body: 0,10,10
```
###### LeftArm
```yml
Mob:
  Type: armor_stand
  Pose:
    LeftArm: 0to360,0,0
```
###### RightArm
```yml
Mob:
  Type: armor_stand
  Pose:
    RightArm: 0to90,0,0
```
###### LeftLeg
```yml
Mob:
  Type: armor_stand
  Pose:
    LegLeg: 0,0to80,0
```
###### RightLeg
```yml
Mob:
  Type: armor_stand
  Pose:
    RightLeg: 20,25,0
```


## Bee

#### Anger
Se设time in ticks 直到 bee anger ends。
IfIf set to 0 the bee 不会 be angry.
Defaults to `0`.
```yaml
  Options:
    Anger: 200
```

#### HasNectar
Whthe bee是否carrying pollen。
DeDefaults to `false`.
```yaml
  Options:
    HasNectar: true
```


#### HasStung
WhWhether the bee has stung an 实体.
DeDefaults to `false`.
```yaml
  Options:
    HasStung: true
```


#### PreventStingerLoss
WhWhether to prevent the bee from losing its stinger 一旦 it hits an 实体.
DeDefaults to `false`.
```yaml
  Options:
    PreventStingerLoss: true
```


## Camel

#### Saddled
Whthe 实体是否saddled or not。
DeDefaults to `false`.
```yaml
  Options:
    Saddled: true
```

#### Tamed
Whthe 实体是否tamed or not。
DeDefaults to `false`.
```yaml
  Options:
    Tamed: true
```


## Cat

#### CatType
Se设类型 of cat。
Ty类型 can be ALL_BLACK, BLACK, BRITISH_SHORTHAIR, CALICO, PERSIAN, JELLIE, RAGDOLL, RED, SIAMESE, TABBY or WHITE.
```yaml
  Options:
    CatType: BLACK
```

#### CollarColor
Se设color of the cat collar。
AvAvailable colors are: BLACK, BLUE, BROWN, CYAN, GRAY, GREEN, LIGHT_BLUE, LIGHT_GRAY, LIME, MAGENTA, ORANGE, PINK, PURPLE, RED, WHITE, or YELLOW.
```yaml
  Options:
    CollarColor: GREEN
```

#### Tamed
Whthe 实体是否tamed or not。
DeDefaults to `false`.
```yaml
  Options:
    Tamed: true
```


## Chicken

#### Jockey
WhWhether or not the chicken has the `IsChickenJockey` NBT set to 1.
If t若true，the chicken将cannaturally 消失, 掉落 10 experience upon death 而不是 1-3 and 不能 lay eggs。
DeDefaults to `false`.
```yaml
  Options:
    Jockey: true
```


## Creepers

#### ExplosionRadius
Se设半径/战力 of the creepers explosion。
NeNegative 值 are ignored, and the explosion 半径 remains the creeper 默认 one.
DeDefaults to `-1`.
```yaml
  Options:
    ExplosionRadius: 5
```

#### FuseTicks
Se将number of ticks it takes for creepers设explode。
NeNegative 值 are ignored, and the time it takes remains the creeper 默认 one.
DeDefaults to `-1`.
```yaml
  Options:
    FuseTicks: 60
```

#### SuperCharged
WhWhether the creeper should 生成 as a super charged creeper.
DeDefaults to `false`.
```yaml
  Options:
    SuperCharged: true
```

#### PreventSuicide
PrPrevents creepers from dying upon exploding. Set `mobGriefing` gamerule to true for this 选项 to work.
DeDefaults to `false`.
```yaml
  Options:
    PreventSuicide: true
```


## Enderman

#### PreventTeleport
MeMeant for Endermen but //might// work on 其他 生物. May break teleport 技能!
DeDefaults to `false`.
```yaml
  Options:
    PreventTeleport: true
```


#### HeldBlock
Se设方块 that the Enderman is carrying。
DeDefaults to `AIR`.
```yaml
  Options:
    HeldBlock: STONE
```


## Experience_orb

#### Experience
Se设数量 of experience give by the experience orb 生物。
DeDefaults to `1`.
```yaml
  Options:
    Experience: 10
```


## Falling 方块

#### 方块
De决定the [类型 of the 方块](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。
DeDefaults to `STONE`.
```yaml
  Options:
    Block: BIRCH_WOOD
```

#### BlockData
AdAdditional field for inputting blockdata.
DeDefaults to `0`.

#### DropsItem
ShShould the 实体 be able to 掉落 the falling 方块 物品.
DeDefaults to `true`.
```yaml
  Options:
    DropsItem: false
```

#### HurtsEntities
DaDamages 实体 on impact.
DeDefaults to `true`.
```yaml
  Options:
    HurtsEntities: false
```

#### ReplaceSpawnLocationBlock
IfIf the 实体 should replace the 方块 at its 生成 位置.
DeDefaults to `false`.
```yaml
  Options:
    ReplaceSpawnLocationBlock: true
```

#### UseSpawnLocationType
IfIf the 类型 of the falling 方块 应为 the one at the 生成 位置.
DeDefaults to `false`.
```yaml
  Options:
    UseSpawnLocationType: true
```


## Fox

#### FoxType
Det决定the 类型 of the fox。
CaCan be `RED` or `SNOW`.
DeDefaults to `RED`.
```yaml
  Options:
    FoxType: SNOW
```


## Frog

#### 类型
De决定the 类型 of the Frog。
Al别名 is `Variant`.
CaCan be `WARM`, `COLD` or `TEMPERATE`.
DeDefaults to `WARM`.
```yaml
  Options:
    Type: COLD
```


## Goat

#### Screaming
Se设if 这是 a screaming goat. A screaming goat makes screaming sounds and rams more 经常。
DeDefaults to `false`.
```yaml
  Options:
    Screaming: true
```


## Hoglin

#### ImmuneToZombification
Whthe hoglin是否immune to being zombified。
DeDefaults to `false`.
```yaml
  Options:
    ImmuneToZombification: true
```

#### Huntable
Whthe hoglin是否able to be hunted by piglins。
DeDefaults to `true`.
```yaml
  Options:
    Huntable: true
```


## Horses, Donkeys, and Mules

#### HorseArmor
UsUsed for horses to set the 类型 of armor 它们有 on.
CaCan be `iron`, `gold`, or `diamond`
[a[armor_type] 必须为 in lower case
```yaml
  Options:
    HorseArmor: gold
```

#### CarryingChest
UsUsed for donkeys to set 是否 它们是 carrying a chest or not.
DeDefaults to `false`.
```yaml
  Options:
    CarryingChest: true
```


#### HorseColor
Se设color of the horse。
CoColors 必须为 uppercase,can be any of the [Spigot Horse colors](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Horse.Color.html).
```yaml
  Options:
    HorseColor: CREAMY
```


#### Saddled
UsUsed for horses to set 是否 它们是 saddled or not.
Defaults to `true` if [HorseArmor](#horsearmor) is set, or `false` 否则
```yaml
  Options:
    Saddled: true
```

#### HorseStyle
Se设style of the horse。
StStyles can be any of the [Spigot Horse Style](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Horse.Style.html)
```yaml
  Options:
    HorseStyle: WHITE_DOTS
```


#### Tamed
UsUsed for horses to set 是否 它们是 tamed or not.
Defaults to `false`.
```yaml
  Options:
    Tamed: true
```

#### HorseType
Defines the 类型 of horse
Can be any of the [Spigot Horse variants](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Horse.Variant.html)
Defaults to `HORSE`
**Removed in MC 1.11+, use[类型](/生物/生物#类型) instead.**


## Interaction
#### 高度
ThThe 高度 of the Interaction 实体.
DeDefaults to `1`.
```yaml
  Options:
    Height: 2
```

#### 宽度
ThThe 宽度 of the Interaction 实体.
DeDefaults to the 值 of the `Height` 选项.
```yaml
  Options:
    Width: 3
```

#### Responsive
IfIf the Interaction 实体 is responsive.
DeDefaults to `true`.
```yaml
  Options:
    Responsive: false
```


## IronGolem
#### PlayerCreated
AcActs as if the 玩家 built the 生物.
DeDefaults to `false`.
```yaml
  Options:
    PlayerCreated: true
```


## 物品

#### 物品
ThThe material of the 物品 实体.
DeDefaults to `STONE`.
```yaml
  Options:
    Item: BRICK
```

#### 数量
ThThe 数量 of 物品 in the itemstack.
DeDefaults to `1`.
```yaml
  Options:
    Amount: 10
```

#### CanPickup
IfIf the itemstack can be picked up.
DeDefaults to `true`.
```yaml
  Options:
    CanPickup: false
```


## Llama

#### CarryingChest
SeSet 是否 the 实体 is carrying a chest or not.
DeDefaults to `false`.
```yaml
  Options:
    CarryingChest: true
```

#### Tamed
SeSet 是否 the 实体 is tamed or not.
Defaults to `false`.
```yaml
  Options:
    Tamed: true
```

#### 颜色
Se设color of the llama。
CoColors 必须为 uppercase,can be any of the [Spigot Llama colors](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Llama.Color.html).
```yaml
  Options:
    Color: CREAMY
```


## MinecartChest

#### ChestContents
ThThe [droptable] that 将 put 在...内 chest.
```yaml
  Options:
    ChestContents: example_droptable
```


## Panda

#### MainGene
Se将main [gene](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Panda.Gene.html) that the panda can pass on设its offspring。
CaCan be NORMAL, AGGRESSIVE, LAZY, WORRIED, PLAYFUL, WEAK, BROWN.
DeDefaults to `NORMAL`.
```yaml
  Options:
    MainGene: LAZY
```


#### HiddenGene
Se将hidden [gene](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Panda.Gene.html) that the panda can pass on设its offspring。
CaCan be NORMAL, AGGRESSIVE, LAZY, WORRIED, PLAYFUL, WEAK, BROWN.
DeDefaults to `NORMAL`.
```yaml
  Options:
    HiddenGene: WORRIED
```


## Parrot

#### Variant
ThThe [variant](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Parrot.Variant.html) of the parrot.
```yaml
  Options:
    Variant: GRAY
```

#### FlyingSpeed
ThThe flying 速度 of the parrot.
Defaults to `-1` (The 选项 不是 applied)
```yml
  Options:
    FlyingSpeed: 0.2
```


## Pig

#### Saddled
IfIf the pig is saddled.
Defaults to `false`.
```yaml
  Options:
    Saddled: true
```



## Piglin

#### AbleToHunt
Whthe piglin是否able to hunt。
DeDefaults to `true`.
```yaml
  Options:
    AbleToHunt: false
```


#### ImmuneToZombification
Whthe piglin是否immune to being zombified。
DeDefaults to `true`.
```yaml
  Options:
    ImmuneToZombification: false
```


## Piglin Brute

#### ImmuneToZombification
Whthe piglin是否immune to being zombified。
DeDefaults to `true`.
```yaml
  Options:
    ImmuneToZombification: false
```


## Rabbit

#### IsKillerBunny
AlAlias: `Angry`.
Se将rabbit设the Killer Bunny。
Defaults to `false`.
```yaml
  Options:
    IsKillerBunny: true
```


#### RabbitType
Se设[类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Rabbit.类型.html) of rabbit。
类型 can be BLACK, BLACK_AND_WHITE, BROWN, GOLD, SALT_AND_PEPPER, THE_KILLER_BUNNY or WHITE
```yaml
  Options:
    RabbitType: SALT_AND_PEPPER
```


## Sheep

#### Sheared
Whthe Sheep是否已经 sheared。
DeDefaults to `false`.
```yaml
  Options:
    Sheared: true
```


## Silverfish

#### PreventBlockInfection
PrPrevent silverfish from infecting 方块.
Defaults to `false`.
```yaml
  Options:
    PreventBlockInfection: true
```


## Skeleton

#### PreventConversion
PrPrevents the Skeleton from being converted into 其他 类型 of skeletons.
Defaults to `false`.
```yaml
  Options:
    PreventConversion: true
```


## Snow Golem

#### Derp
WhWhether the Snow Golem has its pumpkin 已经 sheared.
Defaults to `false`.
```yaml
  Options:
    Derp: true
```


#### PreventSnowFormation
PrPrevent the Snow Golem from creating snow.
DeDefaults to `false`.
```yaml
  Options:
    PreventSnowFormation: true
```


## TNT

#### FuseTicks
HoHow long the TNT takes to explode.
Defaults to `-1` (instantly).
```yaml
  Options:
    FuseTicks: 100
```


#### ExplosionYield
De决定the strength of the explosion。
Defaults to `-1` (The normal TNT Explosion Yield is used).
```yaml
  Options:
    ExplosionYield: 2
```


#### Incendiary
Whthe explosion是否能够 starting 触发。
Defaults to `false`.
```yaml
  Options:
    Incendiary: true
```


## Tropical Fish

#### Pattern
Se设[形状/Pattern](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/TropicalFish.Pattern.html) of the fish。
```yaml
  Options:
    Pattern: GLITTER
```


#### BodyColor
Se设[Primary Color](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html) of the fish。
```yaml
  Options:
    BodyColor: GRAY
```


## PatternColor
设[Secondary Color](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html) of the fish。
```yaml
  Options:
    BodyColor: LIME
```


## Villagers

#### HasTrades
WhWhether the villager can be traded with.
DeDefaults to `false`.
> 检查 out [Trades](/生物/生物#trades)
```yaml
  Options:
    HasTrades: true
```


#### Profession
SpSpecifies the [Profession](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Villager.Profession.html) of the villager.
ViVillagers 没有 this 选项 will roll a random profession on their initial 生成.
```yaml
  Options:
    Profession: MASON
```


#### 类型
ReRepresents [Villager 类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Villager.类型.html), 通常 corresponding to what 生物群系 they 生成 in.
DeDefaults to PLAINS.
```yaml
  Options:
    Type: DESERT
```


#### 等级
ViVillager profession 等级, 等级 1 - 5.
Le等级 1 villagers might switch professions. If 您想要 a villager to hold its profession, give them a 等级 of 2 or higher.
Re必需 if 设置 villager professions.
```yaml
  Options:
    Level: 3
```


## Wolfs

#### Variant
设[Wolf Variant](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Wolf.Variant.html)。
```yaml
  Options:
    Variant: black
```

#### 颜色
设[Color](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html) of the Wolf Collar。
```yaml
  Options:
    Color: RED
```

## Zombie Villagers

#### Profession
SpSpecifies the [Profession](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/实体/Villager.Profession.html) of the zombie villager.
ThThis 选项 还将 make the zombie turn 到 respective villager 类型 when being cured using 药水.
DeDefaults to `FARMER`.
```yaml
  Options:
    Profession: MASON
```


[droptable]: /掉落/掉落#掉落-tables