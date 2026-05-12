目标选择器用于决定技能施放时瞄准的目标。

虽然目标选择器在技术上不是必填的（默认目标选择器通常为 @trigger），但忘记写目标选择器大概是 MythicMobs 新手最容易犯的错误之一。

当在 Skill 元技能上使用了目标选择器后，元技能内部的所有技能都会继承这个初始目标选择器。你仍然可以通过给元技能内部的单条技能指定自己的目标选择器，来覆盖父级目标选择器。

如果实体目标被传递给了一个以位置为目标的技能，该技能会使用实体的当前坐标。

[[_TOC_]]

# 扩展目标选择器
以下是扩展插件提供的目标选择器链接。如果没有安装对应的插件，这些目标选择器不会生效。

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Targeters)
- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Targeters)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Targeters)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#targeters)

# 目标选择器

## 实体目标选择器

### 单体实体目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[Self] | @Caster<br>@Boss<br>@Mob | 以技能的施法者为目标 |
| @[Target] | @T | 以施法者当前锁定的目标为目标 |
| @[Trigger] | | 以触发该技能的实体为目标 |
| @[NearestPlayer] | | 以半径内最近的玩家为目标 |
| @[WolfOwner] | | 以狼的拥有者为目标 |
| @[Owner] | | 以生物的[拥有者](/skills/mechanics/setowner)为目标 |
| @[Parent] | @summoner | 以生物的[父实体](/skills/mechanics/setparent)为目标 |
| @[Mount] | | 以施法者的原始[坐骑](/Mobs/Mobs#mount)为目标 |
| @[Father] | @dad<br>@daddy | 以施法者生物的父亲为目标 |
| @[Mother] | @mom<br>@mommy | 以施法者生物的母亲为目标 |
| @[Passenger] | | 以施法者生物的骑乘者为目标 |
| @[PlayerByName] | @specificplayer | 以指定名称的玩家为目标，支持占位符 |
| @[UniqueIdentifier] | @UUID | 以指定 UUID 的实体为目标，支持占位符 |
| @[Vehicle] | | 以施法者的载具为目标 |
| @[InteractionLastAttacker] | @lastAttacker | 以上次攻击该 `INTERACTION` 实体的实体为目标 |
| @[InteractionLastInteract] | @lastInteract | 以上次与该 `INTERACTION` 实体交互的实体为目标 |
| @[OwnerLocation] | | 以生物拥有者的位置为目标 |
| @[ParentLocation] | @summonerlocation | 以生物父实体的位置为目标 |

### 多实体目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[LivingInCone] | @entitiesInCone<br>@livingEntitiesInCone<br>@LEIC<br>@EIC | 以相对于施法者面向方向的指定角度、长度和旋转角的锥形区域内所有活物为目标 |
| @[LivingInWorld] | @EIW | 以施法者所在世界中的所有活物为目标 |
| @[NotLivingNearOrigin] | @nonLivingNearOrigin<br>@NLNO | 以原点附近半径内的所有非活物实体为目标 |
| @[PlayersInRadius] | @PIR | 以给定半径内的所有玩家为目标 |
| @[MobsInRadius] | @MIR | 以半径内所有指定类型的 MythicMob 或原版覆写生物为目标 |
| @[EntitiesInRadius] | @livingEntitiesInRadius<br>@livingInRadius<br>@allInRadius<br>@EIR | 以给定半径内的所有实体为目标 |
| @[EntitiesInRing] | @EIRR | 以给定环状区域内的所有实体为目标 |
| @[EntitiesInRingNearOrigin] | @ERNO | 以原点周围给定环状区域内的所有实体为目标 |
| @[PlayersInWorld] | @World | 以当前世界中的所有玩家为目标 |
| @[PlayersOnServer] | @Server<br>@Everyone | 以服务器中的所有玩家为目标 |
| @[PlayersInRing] | | 以指定最小和最大半径之间的所有玩家为目标 |
| @[PlayersNearOrigin] | @PNO | 以元技能[原点](/skills/targeters/origin)附近的玩家为目标 |
| @[TrackedPlayers] | @tracked | 以施法者渲染距离范围之内的玩家为目标 |
| @[MobsNearOrigin] | | 以原点周围半径内所有指定类型的 MythicMob 或原版覆写生物为目标 |
| @[EntitiesNearOrigin] | @ENO | 以元技能[原点](/skills/targeters/origin)附近的所有实体为目标 |
| @[Children] | @child<br>@summons | 以施法者召唤的任何子实体为目标 |
| @[Siblings] | @sibling<br>@brothers<br>@sisters | 以与施法者共享同一父实体的任何生物为目标 |
| @[ItemsNearOrigin] | | 以元技能[原点](/skills/targeters/origin)附近的掉落物品为目标 |
| @[ItemsInRadius] | @IIR | 以给定半径内的所有掉落物品为目标 |

### 仇恨表目标选择器

以下目标选择器仅在生物启用了[仇恨表](/Mobs/ThreatTables)时才有效。

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[ThreatTable] | @TT | 以施法者生物仇恨表中的所有实体为目标 |
| @[ThreatTablePlayers] | | 以施法者生物仇恨表中的所有玩家为目标 |
| @[RandomThreatTarget] | @RTT | 以施法者生物仇恨表中的随机一个实体为目标 |
| @[RandomThreatTargetLocation] | @RTTL | 以施法者生物仇恨表中随机一个实体的位置为目标 |

## 位置目标选择器

### 单体位置目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[SelfLocation] | @casterLocation<br>@bossLocation<br>@mobLocation | 以施法者的坐标为标 |
| @[SelfEyeLocation] | @eyeDirection<br>@casterEyeLocation<br>@bossEyeLocation<br>@mobEyeLocation | 以施法者的眼部坐标为标 |
| @[Forward] | | 以施法者面向前方的某个位置为目标 |
| @[ProjectileForward] | | 以施法弹射物面向前方（相对于其方向）的某个位置为目标 |
| @[TargetLocation] | @targetloc<br>@TL | 以施法者当前目标的坐标为目标 |
| @[TargetPredictedLocation] | @targetPredictedLoc<br>@TPL<br>@PredictedTargetLocation | 基于当前移动速度，预测施法者最高仇恨目标在指定刻数之后的位置，以该位置为目标 |
| @[TriggerLocation] | | 以触发该技能的实体的坐标为目标 |
| @[SpawnLocation] | | 以世界的出生点坐标为目标 |
| @[CasterSpawnLocation] | | 以施法者生成时的坐标为目标 |
| @[Location] | | 以施法者所在世界中的指定坐标为目标 |
| @[Origin] | @source | 以元技能的「原点」或「起效点」坐标为目标。虽然原点通常是施法者生物，但有些特殊情况下并非如此（例如在弹射物技能中，「原点」是弹射物的坐标） |
| @[ObstructingBlock] | | 尝试以施法者正前方遮挡其视线的方块为目标 |
| @[TargetBlock] | | 以施法者玩家正在注视的方块为目标 |
| @[TrackedLocation] | | 以生物的追踪位置为目标 |
| @[NearestStructure] | | 以施法者所在世界中指定类型且在半径内最近的结构为目标 |
| @[VariableLocation] | @varLocation | 以存储在指定变量中的位置为目标 |
| @[HighestBlock] | | 以技能原点处最高的方块为目标 |
| @[PlayerLocationByName] | | 以指定名称玩家的坐标为目标 |

### 多位置目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[ForwardWall] | | 以施法者正前方的一个平面为目标 |
| @[PlayerLocationsInRadius] | @PLIR | 以给定半径内所有玩家的坐标为目标 |
| @[Pin] | | 以一个[标记点](/Pins)的坐标为目标 |
| @[Ring] | | 以排成环状的一组坐标点为目标 |
| @[RandomRingPoint] | | 以施法者周围环上的随机点为目标 |
| @[Cone] | | 返回组成锥形的多个坐标点（注意：Cone 固定在 Y 轴上，不能上下旋转） |
| @[Sphere] | | 以施法者周围的球体中的点为目标 |
| @[Rectangle] | @cube<br>@cuboid | 返回组成矩形的多个坐标点 |
| @[RandomLocationsNearCaster] | @randomLocations<br>@RLNC | 以施法者附近的随机位置为目标 |
| @[RandomLocationsNearOrigin] | @RLO<br>@randomLocationsOrigin<br>@RLNO | 以技能原点附近的随机位置为目标 |
| @[BlocksNearOrigin] | @BNO | 以元技能原点周围半径内的所有方块为目标 |
| @[RingAroundOrigin] | @ringOrigin<br>@RAO | 以原点周围指定环状区域内的位置为目标 |
| @[Spawners] | | 以指定生成器的坐标为目标 |
| @[BlocksInPinRegion] | | 以两个标记点界定的区域中的方块为目标 |
| @[ChunksInWERegion] | @chunksInWGRegion | 以指定 WorldGuard 区域内各个区块的 (0,0) 角坐标为目标 |

## 元目标选择器

元目标选择器以[继承目标](/Skills/Metaskills#inheritance)为参照。例如：

```yaml
# 生物文件
Laser:
  Type: CREEPER
  Display: 'Laser'
  Health: 12
  AITargetSelectors:
  - 0 clear
  - 1 players
  Skills:
  - skill{s=Laser} @target
```
```yaml
# 技能文件
Laser:
  Skills:
  - ignite @EntitiesInLine{r=1}
```
在上面的技能示例中，`ignite` 技能会以施法者与 `- skill{s=Laser} @target` 中指定的目标选择器所选中的目标之间的实体为目标——即施法者与其目标之间连线上的实体。

部分元目标选择器还允许技能「从原点」施放。这将把元目标选择器的起始位置从施法者改为 @Origin，从而实现一些复杂效果，尤其在与弹射物结合使用时。


### 元实体目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[LivingInLine] | @entitiesInLine<br>@livingEntitiesInLine<br>@LEIL<br>@EIL | 以继承目标与施法者生物之间连线上的所有实体为目标 |
| @[LivingNearTargetLocation] | @LNTL<br>@ENTL<br>@ENT | 以继承目标附近的所有活物为目标 |
| @[PlayersNearTargetLocations] | @playersNearTargetLocation<br>@PNTL | 以继承目标附近的所有玩家为目标 |
| @[TargetedTarget] | @Targeted | 以继承到的目标实体为目标 |

### 元位置目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[Line] | | 以生物与继承目标之间的位置为目标 |
| @[RandomLocationsNearTargets] | @randomLocationsNearTarget<br>@randomLocationsNearTargetEntities<br>@randomLocationsNearTargetLocations<br>@RLNT<br>@RLNTE<br>@RLNTL | 以继承目标周围的随机位置为目标 |
| @[FloorOfTargets] | @FOT<br>@floorsOfTarget | 以被继承目标脚下方块的位置为目标 |
| @[LocationsOfTargets] | @locationOfTarget<br>@LOT | 以被继承目标实体的坐标为目标 |
| @[TargetedLocation] | @targetedLocations<br>@targetedLoc | 以被继承目标位置的坐标为目标 |
| @[BlocksInRadius] | @BIR | 以被继承目标周围半径内的所有方块为目标 |
| @[BlocksInChunk] | @BIC | 以相对于继承目标的区块内所有方块为目标 |
| @[BlockVein] | @vein<br>@bv | 以从技能原点开始、材质匹配的所有相邻方块为目标 |

## 特殊目标选择器

| 目标选择器 | 简写 | 描述 |
|----------|-----------|---------------------------------------------------------------------------------|
| @[None]  | | 不提供任何目标（适用于不需要目标输入的技能） |
| @[Region]| | 以区域为目标的特殊目标选择器，仅适用于特定技能 |

# 通用属性
以下是一些大多数目标选择器都能使用的通用属性，具体取决于目标选择器的返回值类型。

## 所有目标选择器通用

| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| targetconditions | conditions, cond, c | [内联目标条件](/Skills/Inline-Conditions#targetconditions) |<!--type:Conditions-->|
| fallback  | fb | 当此目标选择器没有返回目标时使用的回退目标选择器 |<!--type:Targeter-->|

### 以…身份执行属性
| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| sudoparent | fromparent, ofparent, asparent, parent, ofparent | 若设为 `true`，此目标选择器将以执行该技能的施法者实体的[父实体][Parent]身份来解析 | |
| sudoowner | fromowner, ofowner, asowner, owner, ofowner | 若设为 `true`，此目标选择器将以执行该技能的施法者实体的[拥有者][Owner]身份来解析 | |
| sudotrigger | fromtrigger, oftrigger, astrigger, trigger, oftrigger | 若设为 `true`，此目标选择器将以执行该技能的技能树的[触发者][Trigger]身份来解析 | |

以下示例中，[生物将持续被传送到其拥有者面前](https://cdn.discordapp.com/attachments/523443579574681600/1101186712174088253/a.gif)，因为 `Forward` 目标选择器使用了 `sudoowner` 属性，因此会以生物拥有者的身份进行解析：
```yaml
TestOwner:
  Type: Wolf
  Skills:
  - setOwner @NearestPlayer{r=99} ~onSpawn
  - tp @Forward{f=5;y=1;sudoowner=true} ~onTimer:1
```

## 实体目标选择器通用属性
| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| useboundingbox | bb | 若目标选择器在进行距离检查，此选项允许基于目标的包围盒而非碰撞箱中心进行检查 | |
| unique | u | 一个实体最多能被选为目标的次数。默认值为 1，设为 0 则无限制。主要用于具有多个碰撞箱的 MEG 模型 | |
| nomegbb | nmb | 是否过滤掉 MEG 子碰撞箱 | |

## 位置目标选择器通用属性
| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| xoffset | xo, x | X 轴上的偏移量 | |
| yoffset | yo, y | Y 轴上的偏移量 | |
| zoffset | zo, z | Z 轴上的偏移量 | |
| forwardOffset | foffset, fo | 基于施法者视角的前后偏移 | 0 |
| sideOffset | soffset, so | 基于施法者视角的左右偏移 | 0 |
| upoffset | uoffset, uo | 基于施法者视角的上下偏移 | 0 |
| rotatex | rotx | X 轴旋转 | |
| rotatey | roty | Y 轴旋转 | |
| rotatez | rotz | Z 轴旋转 | |
| coordinatex | cx | 设置 X 轴坐标 | |
| coordinatey | cy | 设置 Y 轴坐标 | |
| coordinatez | cz | 设置 Z 轴坐标 | |
| length | | 将方向向量乘以指定数值 | |
| blocktypes | blocktype, bt | 仅选定指定类型的方块。多个方块可用 `,` 分隔<br>可在类型前加 `#` 表示方块只需部分匹配该类型，加 `@` 表示方块只需以该类型开头<br>可在类型前加 `*` 表示指定的是[方块标签](https://minecraft.wiki/w/Tag#Block_tags_2)而非方块类型（例如 `blocktype=*sculk_replaceable`） | |
| blockignores | blockignore, bi | 从目标选择器中排除指定类型的方块。多个方块可用 `,` 分隔<br>可使用 `blocktype` 中注明的特殊语法 | |
| coordinateyaw | cyaw | 设置 yaw 值 | |
| coordinatepitch | cpitch | 设置 pitch 值 | |
| blockcentered | centered | 布尔值。若设为 true，则以目标位置处方块的中心点为目标，而非目标位置本身 | |
| faulty | | 是否使用旧版矢量公式 | false |

# 目标选择器选项

## 目标过滤器

目标过滤器允许你筛选掉某些目标，使目标选择器更加灵活。

通过以下两个属性使用（适用于任何实体目标选择器）：

| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| target | | 要纳入目标的实体类型 | |
| ignore | | 不纳入目标的实体类型 | |

例如，要创建一个忽略所有玩家和非敌对生物的目标选择器，可以这样写：

```yaml
  - damage{a=20} @EntitiesInRadius{r=10;ignore=players,animals}
```
要创建一个只以玩家为目标的目标选择器，可以这样写：

```yaml
  - skill{s=ASkill} @EntitiesInRadius{r=5;target=players}
```

> 你可以在 MythicMobs/config/config-skills.yml 中设置默认目标过滤器。

### Target 属性可用的过滤器
| 过滤器 | 别名 | 描述 |
|-----------|-----------|--------------------------------------------------------------------------------|
| ground    | | 是否以地面实体为目标。若使用，将忽略飞行和水生实体 |
| water     | | 是否以水生实体为目标。若使用，将忽略飞行和地面实体 |
| flying    | | 是否以飞行实体为目标。若使用，将忽略地面和水生实体 |
| self      | caster | 技能的施法者是否可被选为目标 |
| player    | | 玩家是否可被选为目标 |
| creative  | | 创造模式玩家是否可被选为目标 |
| spectator | | 旁观模式玩家是否可被选为目标 |
| armorstand| armor_stand | 盔甲架是否可被选为目标 |
| marker    | | 标记实体是否可被选为目标 |
| npc       | | Citizens NPC 是否可被选为目标 |
| animal    | | 动物是否可被选为目标 |
| creature  | | 生物是否可被选为目标 |
| monster   | | 怪物是否可被选为目标 |
| villager  | | 村民是否可被选为目标 |

> 如果没有使用 `ground`、`water` 和 `flying` 中任意一项，且默认过滤器也不包含它们，那么 `Players`、`ArmorStands`、`Markers`、`Creative`、`Spectator`、`CitizensNPCs`、`Animals`、`Creatures`、`Monsters` 和 `Villagers` 也会被忽略。

### Ignore 属性可用的过滤器
| 过滤器 | 别名 | 描述 |
|-----------|-----------|--------------------------------------------------------------------------------|
| player    | | 玩家是否不应被选为目标 |
| creative  | | 创造模式玩家是否不应被选为目标 |
| spectator | | 旁观模式玩家是否不应被选为目标 |
| armorstand| armor_stand | 盔甲架是否不应被选为目标 |
| marker    | | 标记实体是否不应被选为目标 |
| npc       | | Citizens NPC 是否不应被选为目标 |
| animal    | | 动物是否不应被选为目标 |
| creature  | | 生物是否不应被选为目标 |
| monster   | | 怪物是否不应被选为目标 |
| villager  | | 村民是否不应被选为目标 |
| faction   | | 同阵营实体是否不应被选为目标 |
| owner     | | 施法者的拥有者是否不应被选为目标 |
| vanilla   | | 原版实体是否不应被选为目标 |

### 专用过滤器
你也可以通过以下属性专门设定是否以某类实体为目标。这些属性的效果会覆盖通用的 target/ignore 属性对该特定实体类型的设置。

| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| targetself| | 是否以技能的施法者为目标 | |
| targetplayers| | 是否以玩家为目标 | |
| targetcreative| | 是否以创造模式玩家为目标 | |
| targetspectator| | 是否以旁观模式玩家为目标 | |
| targetarmorstands| | 是否以盔甲架为目标 | |
| targetmarkers| | 是否以标记实体为目标 | |
| targetnpcs| | 是否以 Citizens NPC 为目标 | |
| targetanimals| | 是否以动物为目标 | |
| targetcreatures| | 是否以生物为目标 | |
| targetsamefaction| | 是否以同阵营实体为目标 | |
| targetowner| | 是否以施法者的拥有者为目标 | |
| targetvanilla| targetnonmythic | 是否以非 Mythic 实体为目标 | |
| targetvillagers| | 是否以村民为目标 | |
| targetall | | 是否以所有实体为目标。若为 true，将忽略所有过滤条件 | false |

```yaml
  - damage{a=20} @EntitiesInRadius{r=10;targetplayers=true;targetsamefaction=true;targetowner=false}
```
> 使用此方式可明确以玩家和同阵营实体为目标（与其他任何有效目标一起），同时排除施法者的拥有者。

## 目标数量限制

所有实体和位置目标选择器也支持目标数量限制（从 v5.0.4 起）。通过此功能，你可以限制目标实体/位置的数量，包括它们被选中的顺序。

通过以下属性实现：

| 属性 | 别名 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| sort | sortby | 目标实体/位置的排序方式。基于距离的排序以技能原点为参照 |<!--type:NONE,RANDOM,NEAREST,FURTHEST,HIGHEST_HEALTH,LOWEST_HEALTH,HIGHEST_THREAT,LOWEST_THREAT-->|
| skipTargetsUpToIndex | stuti | 排序后跳过前 n 个目标（若 >0） |0|
| limit | | 跳过操作后限制目标实体/位置的数量（若 >0） |0|

假设你想让技能只以 30 格内最近的 2 名玩家为目标，只需设置 limit 为 2 并按最近排序：

```yaml
  - mechanic @PlayersInRadius{r=30;limit=2;sort=NEAREST}
```

目前 sort 支持以下值：

**通用排序方式：**
- NONE *（通常按实体存在的时间排序）*
- RANDOM
- NEAREST *（距技能原点最近）*
- FURTHEST *（距技能原点最远）*

**仅适用于实体的排序方式**
- HIGHEST_HEALTH
- LOWEST_HEALTH
- HIGHEST_THREAT
- LOWEST_THREAT

因此目标选择器将按以下顺序操作：
- 根据提供的 sort 属性（如果有）对目标排序（仅在 limit 和 skipTargetsUpToIndex >0 时执行）
- 根据 skipTargetsUpToIndex 属性值跳过前 n 个目标（若 >0）
- 根据 limit 属性值返回前 n 个目标（若 >0）

所以，你可以通过同时使用 limit 和 skipTargetsUpToIndex 来获取特定索引位置的目标：
```yaml
GiveRewards:
  Skills:
  - message{m="You are first!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1} # 以最高仇恨的玩家为目标
  - message{m="You are second!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1;stuti=1} # 以第二高的玩家为目标
  - message{m="You are third!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1;stuti=2} # 以第三高的玩家为目标
  - message{m="You aren't on the podium!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;stuti=3} # 以其他人所有人为目标
```

<!-- LINKS -->
<!-- Single Entity Targeters -->
  [InteractionLastAttacker]: /Skills/Targeters/InteractionLastAttacker
  [InteractionLastInteract]: /Skills/Targeters/InteractionLastInteract
  [Father]: /Skills/Targeters/Father
  [Mother]: /Skills/Targeters/Mother
  [Mount]: /Skills/Targeters/Mount
  [NearestPlayer]: /Skills/Targeters/NearestPlayer
  [Owner]: /Skills/Targeters/Owner
  [Parent]: /Skills/Targeters/Parent
  [Passenger]: /Skills/Targeters/Passenger
  [PlayerByName]: /Skills/Targeters/PlayerByName
  [Self]: /Skills/Targeters/Self
  [Target]: /Skills/Targeters/Target
  [Trigger]: /Skills/Targeters/Trigger
  [UniqueIdentifier]: /Skills/Targeters/UniqueIdentifier
  [Vehicle]: /Skills/Targeters/Vehicle
  [WolfOwner]: /Skills/Targeters/WolfOwner
<!-- Multi Entity Targeters -->
  [Children]: /Skills/Targeters/Children
  [EntitiesInRadius]: /Skills/Targeters/EntitiesInRadius
  [EntitiesInRing]: /Skills/Targeters/EntitiesInRing
  [EntitiesInRingNearOrigin]: /Skills/Targeters/EntitiesInRingNearOrigin
  [EntitiesNearOrigin]: /Skills/Targeters/EntitiesNearOrigin
  [ItemsInRadius]: /Skills/Targeters/ItemsInRadius
  [ItemsNearOrigin]: /Skills/Targeters/ItemsNearOrigin
  [LivingInCone]: /Skills/Targeters/LivingInCone
  [LivingInWorld]: /Skills/Targeters/LivingInWorld
  [MobsInRadius]: /Skills/Targeters/MobsInRadius
  [MobsNearOrigin]: /Skills/Targeters/MobsNearOrigin
  [NotLivingNearOrigin]: /Skills/Targeters/NotLivingNearOrigin
  [PlayerLocationsInRadius]: /Skills/Targeters/PlayerLocationsInRadius
  [PlayersInRadius]: /Skills/Targeters/PlayersInRadius
  [PlayersInRing]: /Skills/Targeters/PlayersInRing
  [PlayersInWorld]: /Skills/Targeters/PlayersInWorld
  [PlayersNearOrigin]: /Skills/Targeters/PlayersNearOrigin
  [PlayersOnServer]: /Skills/Targeters/PlayersOnServer
  [Siblings]: /Skills/Targeters/Siblings
  [TrackedPlayers]: /Skills/Targeters/TrackedPlayers
<!-- ThreatTable Targeters -->
  [ThreatTable]: /Skills/Targeters/ThreatTable
  [ThreatTablePlayers]: /Skills/Targeters/ThreatTablePlayers
  [RandomThreatTarget]: /Skills/Targeters/RandomThreatTarget
  [RandomThreatTargetLocation]: /Skills/Targeters/RandomThreatTargetLocation
<!-- Single Location Targeters -->
  [CasterSpawnLocation]: /Skills/Targeters/CasterSpawnLocation
  [Forward]: /Skills/Targeters/Forward
  [HighestBlock]: /Skills/Targeters/HighestBlock
  [Location]: /Skills/Targeters/Location
  [NearestStructure]: /Skills/Targeters/NearestStructure
  [ObstructingBlock]: /Skills/Targeters/ObstructingBlock
  [Origin]: /Skills/Targeters/Origin
  [Ownerlocation]: /Skills/Targeters/Ownerlocation
  [ParentLocation]: /Skills/Targeters/ParentLocation
  [PlayerLocationByName]: /Skills/Targeters/PlayerLocationByName
  [ProjectileForward]: /Skills/Targeters/ProjectileForward
  [SelfEyeLocation]: /Skills/Targeters/SelfEyeLocation
  [SelfLocation]: /Skills/Targeters/SelfLocation
  [SpawnLocation]: /Skills/Targeters/SpawnLocation
  [VariableLocation]: /Skills/Targeters/VariableLocation
  [TargetBlock]: /Skills/Targeters/TargetBlock
  [TargetLocation]: /Skills/Targeters/TargetLocation
  [TargetPredictedLocation]: /Skills/Targeters/TargetPredictedLocation
  [TrackedLocation]: /Skills/Targeters/TrackedLocation
  [TriggerLocation]: /Skills/Targeters/TriggerLocation
<!-- Multi Location Targeters -->
  [BlocksInPinRegion]: /Skills/Targeters/BlocksInPinRegion
  [BlocksNearOrigin]: /Skills/Targeters/BlocksNearOrigin
  [ChunksInWERegion]: /Skills/Targeters/ChunksInWERegion
  [Cone]: /Skills/Targeters/Cone
  [ForwardWall]: /Skills/Targeters/ForwardWall
  [Pin]: /Skills/Targeters/Pin
  [RandomLocationsNearOrigin]: /Skills/Targeters/RandomLocationsNearOrigin
  [RandomLocationsNearCaster]: /Skills/Targeters/RandomLocationsNearCaster
  [Rectangle]: /Skills/Targeters/Rectangle
  [RandomRingPoint]: /Skills/Targeters/RandomRingPoint
  [RingAroundOrigin]: /Skills/Targeters/RingAroundOrigin
  [Ring]: /Skills/Targeters/Ring
  [Spawners]: /Skills/Targeters/Spawners
  [Sphere]: /Skills/Targeters/Sphere
<!-- Meta Targeters -->
  [BlocksInRadius]: /Skills/Targeters/BlocksInRadius
  [BlocksInChunk]: /Skills/Targeters/BlocksInChunk
  [BlockVein]: /Skills/Targeters/BlockVein
  [FloorOfTargets]: /Skills/Targeters/FloorOfTargets
  [Line]: /Skills/Targeters/Line
  [LivingInLine]: /Skills/Targeters/LivingInLine
  [LivingNearTargetLocation]: /Skills/Targeters/LivingNearTargetLocation
  [LocationsOfTargets]: /Skills/Targeters/LocationsOfTargets
  [PlayersNearTargetLocations]: /Skills/Targeters/PlayersNearTargetLocations
  [RandomLocationsNearTargets]: /Skills/Targeters/RandomLocationsNearTargets
  [TargetedLocation]: /Skills/Targeters/TargetedLocation
  [TargetedTarget]: /Skills/Targeters/TargetedTarget
<!-- Special Targeters -->
  [None]: /Skills/Targeters/None
  [Region]: /Skills/Targeters/Region