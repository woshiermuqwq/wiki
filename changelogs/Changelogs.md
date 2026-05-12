[[_TOC_]]

# 5.10.0（正式版）

## 通用
- 新增 **1.21.7** 和 **1.21.8** 支持
- 新增 `HAPPY_GHAST`（快乐恶魂）实体类型
- 性能：更快的二次处理流程，优化了实体查找缓存和重载时的物品解析
- 默认配置：添加了若干缺失的选项

## API 与事件
- 新增：`MythicReloadCompleteEvent`
- 新增（核心）：`ReloadEvent`
- 新增：`MythicPlayerVariableSetEvent`、`MythicPlayerVariableRemoveEvent`
- `MythicHealMechanicEvent` 现在也会调用 `EntityRegainHealthEvent`
- 为 `DamageMetadata` 添加了元数据访问
- 在 `SkillTriggerMetadata` 中恢复了旧的元数据访问
- 为 RPG 交叉兼容性奠定了 API 基础

## 占位符
- 新增 `<target.armor>`、`<&lt>`、`<&gt>`、`<^dot>`、`<^dot2>`
- 新增 `PlaceholderAngle`
- 占位符现在支持更多位置（如物品浏览器解析）
- 修复了泛型 `int`、`float` 和 `double` 占位符不解析变量的问题
- 修复了复杂情况下 PlaceholderVector 不工作的问题
- 修复了带物品 NBT（string/int/float/double）的占位符不解析的问题

## 变量
- 新变量类型：`Set`、`List`、`Map`、`Boolean`、`Vector`、`Time`、**Item**、**MetaSkill**
- [元变量占位符](/Skills/Placeholders#meta-variable-placeholders)：`<[scope].var.[name].keyword>` 支持关键词链式调用
- 更新了 `Variable.ofType`；新增 `PolymorphicPlaceholder`
- 生物变量可以设置所有已注册的变量类型
- 内部：迁移了默认变量处理器供 Crucible 使用

## 技能
- **新增**：[`ForEach`](/Skills/Mechanics/ForEach) 和 [`ForEachValue`](/Skills/Mechanics/ForEachValue)
- **新增**：`ClearTarget` 技能
- 更新：`variableadd` / `variablesubtract` 支持新变量类型
- 弹射物系列：
  - 添加了许多缺失的弹射物选项
  - 为 `shoot` 和 `volley` 添加了 `startYOffset`、`startForwardOffset`、`startSideOffset`
- 环绕系列：
  - 为 `ParticleOrbital` 半径添加了占位符支持
  - 新增 `immuneDelay`；修复了多重命中免疫
  - 移除了 `hugSurface` 的 `hs` 别名
  - 改进了环绕物的目标定位逻辑
- Aura：`sync=true` 现在强制使用同步调度器
- Look 技能：细微行为调整
- Summon：修复了 `useTargetYaw`/`useTargetPitch`
- Stun：修复了 `freezeFacing` 反转问题；修复了较新版本的问题

## 传送（仅 Paper）
- **新增**了所有传送技能的选项（Paper）：
  - 传送原因
  - 保留载具
  - 支持 Paper 的 `TeleportFlag`
- 修复：解决了导致传送技能失效的回归问题；对新选项进行了额外优化

## 目标选择器与触发器
- 目标选择器：
  - 为 `@EntitiesInRadius` 和 `@EntitiesNearOrigin` 添加了 `shape`
  - 添加了通用 `upoffset` 位置属性
- 触发器：
  - 潜影贝现在支持 `onShoot` 和 `onBowHit`
  - 修复了掉落方块生物的 `onDeath`

## 条件
- **新增**：[`VariableContains`](/Skills/Conditions/VariableContains)
- **新增**：`projectileHasEnded`
- **新增**：`isSkill{name=...}`
- `mythicMobType` 条件：`exactmatch=false` 选项
- 添加了 `xdiff` 和 `zdiff` 条件
- 修复了健康条件解析触发器的问题

## 物品与装备
- 物品标志：允许在 `Hide` 字段中使用完整标志（如 `HIDE_ATTRIBUTES`）
- 兼容性：在 1.20.5 以上版本中丢弃不支持的 `HIDE_POTION_EFFECTS`
- 物品系统：
  - 重载时更快的物品缓存（也能解析占位符/变量）
  - 修复了工具规则
  - 修复了物品技能可能失败的情况
  - 尝试修复 `ItemMatcher` 中 `vanillaonly=true` 的问题

## 生物与生成
- 选项：
  - `Options.Aware: false`
  - `Options.PreventKnockback`
  - `Hidden: true`（阻止生物出现在列表中），并修复了使其无用的继承问题
- 数据包：修复了数据包生成生物时生成位置不正确的问题

## 全息图与显示
- 全息图：修复了之前构建版本中的多个回归问题
- 文本显示子弹：
  - 新增 `bulletRotation`
  - 修复了 1.20_R1 上的旋转代码

## Bug 修复与其他
- 为生成半径属性添加了占位符支持
- 修复 NPE：启动时、`MythicConfig`、`ForEach`、`Summon`、带 `DisplayItem` 图腾的向量、目标设置
- 修复了 1.21.4+ 上 recoil 技能的问题
- 修复了其他插件在加载前调用某些方法时的错误
- 修复了开发构建版本中引入的 aura `IllegalStateException`
- 修复了极少数情况下的等级修正器错误
- 修复了 `Log` 技能的消息解析
- 修复了目标变量不存在时 `variableequals` 的警告
- 修复了 `onShoot` aura 不设置 `<skill.var.bow-tension>` 的问题
- 修复了各种导弹 `verticalOffset` 问题
- 修复了 1.21.8 上发光效果的不可变列表错误
- 修复了所有可驯服类型的 `setOwner`/`removeOwner`

# 5.9.5

Bug 修复
---------
- 更新了一些依赖
- 修复了带属性的物品在应该堆叠时不堆叠的问题
- 修复了某些耐久度相关问题不使用新耐久度组件数据的问题
- 修复了等级修正器的一些错误
- 修复了较新版本上 recoil 效果的若干问题
- 修复了 stun 技能的 freezeFacing 选项反转问题

# 5.9.4

Bug 修复
---------
- 为 raytraceTo 技能添加了 `ignoreEntities`
- 修复了射线追踪技能中 `ignorePassable=false` 穿透屏障方块的问题

# 5.9.3

Bug 修复
---------
- 修复了 ignoreSameFaction 目标过滤器的若干问题

# 5.9.2

通用
-------
- 为 `GoToOwner/Parent` AI 目标添加了 `teleportToWorld=true/false`。
- 为 runaitargetselector 添加"goal/g"别名以匹配错误消息
- 添加了 `%mythic_stat_...%` PAPI 占位符
- 添加了 `<target.distanceSq>` 和 `<trigger.distanceSq>` 占位符

条件
----------
### 新增：CompareValues

Bug 修复
---------
- 修复了 suicide 技能不计入生物伤害自身的问题（关闭 #1584）
- 修复了较新版本上对话气泡 yaw/pitch 反转的问题
- 可能修复了 MountMe 技能
- 修复了配置物品 NBT 的 MapList 元素不工作的问题
- 修复了原版战利品表掉落的 IllegalArgumentException（关闭 #1949）
- 修复了复制生物生成器时生物类型的错误（关闭 #1951）
- 修复了 shield 技能的错误（关闭 #1955）
- 修复了 `<skill.targets>` 占位符中的 NPE（关闭 #1961）
- 修复了 1.21.4 上的 ClientboundSetEntityDataPacket 错误
- 修复了 PermissionFactionProvider 中将 OP 放入每个阵营的问题
- 修复了非英文服务器上的 StackOverflowError
- 修复了菜单图标配置错误时插件无法加载的问题

# 5.9.1

Bug 修复
---------
- 修复了 VariableMath 技能不支持 double 变量
- 修复了 ItemMatcher 的一些 bug
- 修复了 moveTowardsTargetConditional AI 目标
- 修复了弹射物弹跳问题
- 修复了弹射物的其他若干问题
- 优化了没有命中技能的弹射物
- 修复了 `Options.Color` 在药水上不生效的问题
- 修复了极高速度向量的弹射物可能导致服务器崩溃的错误
- 修复了 1.21.5 上的射线追踪错误
- 修复了自定义伤害属性不触发 onDamaged aura 的问题
- 修复了弹射物上 `hitself` 不工作的问题

# 5.9.0

通用
-------
- 新增 `/pins regionRedefine` 指令。
- 将包图标改为使用 Mythic 物品语法。
- 缩放方程和 `LevelModifiers` 现在可以与任何属性配合使用。
- 为所有数值占位符添加了 step 和 lerp 函数

```
step(e, x) { 0, x < e; 1, x >= e
lerp(a, b, r)
```

技能
---------
### 新增：swingOffhand
- 添加了 `swingOffhand` 技能（副手挥动）。

### 新增：setEntityPose
- 添加了 `setEntityPose{pose=X}` 技能。

### 新增：setItemGroupCooldown
- 添加了 `setItemGroupCooldown{group=namespace:key;ticks=20}` 技能。

### Hit
- 为 hit 技能添加了 `scaleByAttackCooldown`（基于武器攻击冷却缩放伤害）。

### Leap
- Leap 技能的 Noise 现在默认为 `0`。

### MetaSkill
- 为 `MetaSkill` 技能添加了 `snapshotStats=true`。

### Missile
- 为 `missile` 技能添加了 `startWithParentVelocity` 选项。

### 弹射物
- 为弹射物类型技能添加了 HitTargeter

hitTarget/htr 接受一个实体目标选择器。由 htr 定位的实体将通过 onHit 处理并获取免疫延迟。

### Slash
- 为 SlashMechanic 添加了 `specificStep/ss`

### Totem
- 为 Totem 技能添加了 `faceAwayFromCaster=true` 选项。
- 为 Totem 技能添加了 `hugSurface=true` 选项。

### Wait
- 新增特殊关键词技能 `wait`
- 将暂停技能树直到条件满足

条件
----------

### 新增：itemGroupOnCooldown
- 添加了 `itemGroupOnCooldown{group=namespace:key}` 条件。

### 新增：服务器版本条件
- 添加了 `serverAfter{version=1.21.4;inclusive=true}`、`serverBefore{version=1.21.4;inclusive=false}` 和 `serverIsPaper` 条件。

### Stance
- 将 `stance` 条件的默认 `strict` 值改为 `true`。

目标选择器
---------
- 修复了 `@FloorOfTarget` 目标选择器的若干 bug。
- 将位置选择器选项的默认 `faulty` 值改为 `false`。
- 为 `@RingAroundOrigin` 目标选择器添加了 `relative=true/false`。

### 新增：`@PlayerLocationByName`
### 新增：`@PredictedTargetLocation`
`@PredictedTargetLocation{ticks=X}`
- 基于速度向量定位施法者目标在未来 X ticks 的预测位置

触发器
---------
- 将 `onTridentHit` 重命名为 `onProjectileHit`，`onTridentThrow` 重命名为 `onProjectileThrow`。
- 添加了 `onProjectileLand` 触发器。

占位符
------------
### 新增：距离占位符
- 添加了 `<target.distance>` 和 `<trigger.distance>` 占位符。

### 新增：时间戳占位符
- 添加了 `<utils.epoch>`、`<utils.epoch.millis>` 和 `<utils.epoch.ticks>` 占位符。

物品
-----

### 原版战利品表掉落
- 新增掉落类型 `- vanillaLootTable minecraft:table_name`，从原版战利品表和数据包中掉落物品。

### BlockStates 组件
- 添加了 `BlockStates` 组件支持，用于指定物品的方块状态：
  ```yaml
  TestBlockStates:
    Material: OAK_SLAB
    Display: '含水的台阶'
    Options.Placeable: true
    BlockStates:
    - type top
    - waterlogged true
  ```

### 滑翔翼组件
- 为物品添加了 `Glider: true` 选项以实现滑翔翼组件。

### UUID 和时间戳选项
- 添加了 `Options.GenerateUUID: true/false` 和 `Options.GenerateTimestamp: true/false`，在生成时给物品分配 UUID 或时间戳。

API
---
### 新增：事件方法
- 暴露了事件方法。
- 添加了技能调用时的 `MythicSkillEvent`。

### 新增：Crucible 与 RPG API
- 暴露了 Crucible 和 RPG 功能的 API。

### 新增：数据包显示实体 API
- 暴露了更多基于数据包的显示实体 API 方法。

### 新增：仇恨表 API
- 暴露了仇恨表映射。

### 移除：已弃用的装备槽位方法
- 移除了非常旧的按编号引用装备槽位的弃用方法。

### AI 目标
- 升级了 `ownerTarget` 和 `ownerAttacker` AI 目标，可被任何生物使用；添加了 `parentAttacker` 和 `parentTarget` AI 目标。
- 重构了主人接口以提高一致性。

Bug 修复与优化
-------------------------
- 通用重构和内部清理。
- 修复了某些情况下可终止技能的 `onTerminate` 不工作的问题。
- 修复了弹射物目标过滤器的逻辑 bug。
- 修复了重构后各种生物选项不应用的问题。
- 修复了属性重构导致的若干 bug。
- 修复了 API `get` 方法获取最大堆叠数的 bug。
- 修复了 `ItemMatcher` 中的 `IllegalArgumentException`。
- 修复了 1.21.5 上弹射物的 `NoSuchMethodError`。
- 修复了新宠物 AI 功能的 bug。
- 修复了 `MythicSkillEvent` 的异步错误。
- 修复了初始显示数据包子弹旋转在旋转时不使用的问题。
- 修复了 1.21.5 上玩家加入时发生的错误。
- 修复了图腾上的 MEG 子弹不随生成实体旋转的问题。
- 修复了最近引入的掉落 NPE。
- 修复了掉落权重的异常。
- 修复了上一个构建版本破坏装备的问题。
- 修复了 Nexo 掉落不用于装备的问题。
- 修复了可装备组件在 1.21.3 之前版本也应用的问题。
- 修复了某些方块不适用于基于方块的子弹的问题。
- 修复了较新版本上的 `swingArm` 技能。
- 修复了加载自定义技能时的多个错误。
- 修复了某些情况下 `MythicProvider` 注册过晚的问题。
- 修复了 `PreventStingerLoss` 选项的拼写错误。
- 修复了命中多个目标时 `scaleByAttackCooldown` 的问题。
- 修复了 `@FloorOfTarget` 目标选择器的若干 bug。


# 5.8.2
## Bug 修复 / 其他

- 优化了数据包实体
- 优化了弹射物
- TargetSelf 现在将忽略所有其他过滤器
- 移除了一些次要的错误日志记录
- 修复了 targetself = true 时 ENO（实体近原点）无视条件包含施法者的问题
- 修复了弹射物上的 HitTargeter
- 修复了一些自定义 AI 目标自几个版本前起无法加载的问题
- 修复了物品匹配器及相关技能的一些问题
- 修复了粒子在 1.20.X 版本上抛出错误的问题
- 修复了物品工具规则中的 ClassCastException
- 修复了较新版本上 MountTarget 技能失效的问题
- 修复了 StatExecutor 中的 NPE
- 修复了仇恨表即使伤害取消仍追踪仇恨的问题
- 修复了仇恨不使用属性、伤害修正器之后最终伤害量的问题
- 修复了 FancyDrops 伤害追踪不追踪弹射物或技能伤害的问题
- 修复了 FancyDrops 计算贡献时不使用属性、伤害修正器之后最终伤害量的问题
- 修复了 FancyDrops 伤害计算和排行榜计入已取消伤害的问题
- 修复了死亡排行榜不向所有参与玩家显示的问题
- 修复了终止引用始终被克隆的问题
- 修复了 varequal 和 varrange 不使用技能元数据的问题
- 修复了属性在启动时不使用基值的问题
- 修复了 varinRange 条件无法作为目标条件引用技能变量的问题
- 修复了 @ThreatTablePlayers 目标选择器中的 NPE

# 5.8.1

通用
-------
- 添加了缺失的粒子：`infested`、`block_crumble`、`trail`
- 将缺失的原版属性添加为 Stats：`BLOCK_BREAK_SPEED`、`BLOCK_INTERACTION_RANGE`、`ENTITY_INTERACTION_RANGE`
- 为 `dropItem` 技能添加了 `then=` 技能选项
- 为 `remove` 技能添加了 `then=` 技能选项
- 为 `MobsInRadius` 目标选择器的 `radius` 添加了占位符支持
- 允许 message 技能在没有目标的情况下使用

Bug 修复 / 其他
-----------------
- 菜单性能优化
- 重构和清理模板系统
- 移除了一些杂散调试信息
- 修复了生命偷取属性反向的问题
- 修复了生命恢复属性的若干问题
- 修复了 SkillMechanic 中的 ConcurrentModificationException
- 修复了模板的一些 bug
- 修复了分支元技能被可终止技能取消的问题
- 修复了 shoot 技能第一 tick 期间弹射物旋转的问题
- 修复了元数据深拷贝不按值克隆目标的问题
- 修复了关于魔法值的控制台刷屏

# 5.8.0

**注意：此更新包含各种优化、新技能、改进、bug 修复和额外的 API 功能。如发现问题请通过在 Issues 部分创建问题或在相应的 Discord 频道中告知我们来报告。**

通用
-------
- 新增 1.21.3 和 1.21.4 支持
- 大量微优化以提升性能（感谢 Taiyou！）
- 在 `config-general.yml` 中添加了 `Configuration.General.AnnounceOpReload`，设置 Mythic 重载公告是否发送给所有在线 OP。
- 优化了各种弹射物/实体选择技能，在关键区域移除了流的使用。
- 添加了全局选项以自动对所有物品应用 FancyDrops（默认禁用）。
- 添加了 `/mm m spawn [type] [amount] @targeter` 指令。

随机生成
---------------
- **多种生物带权重**：现在可在随机生成器条目中使用加权值指定多种生物，例如：
- **结构支持**：添加了 `Structures:` 列表选项，允许限制随机生成器仅在特定结构中生成生物
- **新配置选项**：
  - `RandomSpawning.MaxGenerationAttempts` 限制集群生成器生成时的尝试次数
  - `RandomSpawning.LocalSpawningLimit` 和随机生成器上的新 `MaxLocalMobs` 选项用于覆盖本地限制
- **重命名**：旧的 `GroupMultiplier` 选项现在在 `config-spawning.yml` 中名为 `LocalGroupMultiplier`
- 对集群生成和结构检测逻辑进行了各种改进。

生物
----
- 精简了变体选项到 `Options.Variant`，适用于狼、猫、青蛙、村民等
- 新增配置**自定义生物生成器物品**的能力，包括设置生成延迟、生成范围等
- 添加了狼专属的 `Options.Variant` 用于自定义狼变体

技能
---------
### 新增：followPath
- 一个 Aura（光环），使目标生物沿定义的路径行走。

### 新增：log
- `log{message="调试到控制台，变量 <caster.var.test>"}` 用于简单日志记录。

### 新增：setTextDisplay
- `setTextDisplay{text="text here"} @Target` 用于显示文本的技能。

### 新增：openTrades
- 为目标玩家打开商人菜单的技能。
  - `realTrade/real` 属性决定交易是否与真正的村民进行。

### 新增：movePin
- `movePin{pin=X}` 重新定位标点的技能。

### 新增：directionalVelocity
- `directionalVelocity{yaw=50}` 基于指定角度向目标施加速度向量。

### 新增：rotateTowards
- 使施法者朝向目标旋转。

### 新增：setChunkForceLoaded
- 强制加载目标位置的区块。

### 新增：resetAI
- 将生物的 AI 恢复为出厂默认值。

### 新增：matchRotation
- `matchRotation{of=@targeter}` 匹配给定目标的旋转角度。

### 新增：clearExperience
- 重置玩家的经验值。

### 新增：setProjectileDirection
- `setProjectileDirection{magnitude=1}` 用于控制弹射物方向。

### 新增：lookAtTarget
- 一个使生物注视其当前目标的 AI 目标。

### 更新：dropItem
- 现在包含一个 `then=` 技能段落，以掉落的物品实体为目标。

### 更新：setSpeed
- 遵循配置的移动速度；如果未设置则默认为生物的基础速度。

### 更新：consumeSlotItem
- 正确移除数量为 `0` 的物品。

### 更新：shoot
- 现在支持 `item=<material>` 用于自定义弹射物（例如 `item=REDSTONE`）。

### 更新：particleOrbital
- 在施法者死亡/消失后终止，并支持 `ticks` 的占位符。

### recoil
- 修复了 1.21+ 上的 recoil；占位符可在 recoil 值中使用。

条件
----------
### 新增：boundingBoxesOverlap
### 新增：distanceFromPin
### 新增：distanceFromLocation
### 新增：PlaceholderBoolean
### 新增：originDistanceFromPin
### 新增：stringEmpty / stringNotEmpty
### lookAt
- 现在有 `distance`/`d` 属性（默认为 5），用于检查生物是否正注视该距离内的目标。

目标选择器
---------
### 新增：@BlocksInPinRegion、@HighestBlock、@TrackedPlayers、@ChunksinWERegion、@PNO、@OwnerLocation、@ParentLocation、@WolfOwner
### skipTargetsUpToIndex
### @ObstructingBlock - 重写以获得更好的性能

物品
-----
- 添加了 `Options.Glint: true` 以添加附魔光泽效果
- 添加了 Mythic 颜色选择器
- 添加了 Fancy Drops 的 `vfxmodel/vfxitemmodel` 支持
- 添加了 `namespace:enchant_name` 支持
- 添加了 `strict=true` 到所有物品条件/技能
- 扩展了 `Equippable` 组件
- 添加了 `#tag` 和 `*wildcard` 支持
- 添加了 `Tool` 和 `UseCooldown` 子组件
### 新增：`TooltipStyle` 组件
### 新增：`Consumable` 组件
### 新增：`Food` 组件

属性（Stats）
-----
- 为最新 Minecraft 属性添加了新的 Mythic 属性：STEP_HEIGHT、ARMOR、ARMOR_TOUGHNESS、BURNING_TIME 等

API
---
- 重构了 `EquipSlots` 以允许自定义槽位
- 添加了 API 方法用于导出物品组件数据
- 增强了 `BukkitItemMatcher` 的物品匹配能力
- 暴露了更多插件触发器和事件调用

## Bug 修复与优化
- 预生成并存储默认生物属性以加快生成速度
- 改进了世界检查以修复一些并发问题
- 改进了占位符的四舍五入
- 修复了随机生成生物偶尔生成在墙内或负坐标的问题
- 修复了为较新版本构建时在较旧版本上加载失败的问题
- 修复了某些情况下占位符 double 值的 NPE
- 修复了苦力怕的 `onPrime` 触发器
- 修复了自定义方块不能用作生物图腾头部的问题
- 粒子效果不再被 Spigot 的默认视图范围错误限制
- 修复了 `look` 技能的 `force=true` 选项
- 修复了弹射物的负重力
- 修复了 1.21+ 上的 recoil
- 修复了生成器不保存及 `Spawners.DisableCommandSaving` 逻辑反转的问题
- 修复了 `onDamaged` aura 不随技能伤害触发的问题
- 修复了 `consumeSlotItem` 数量为 `0` 时失败的问题
- 修复了默认药水等级为 `2` 而不是 `1`
- 修复了烟花颜色加载 `RBG` 而不是 `RGB` 的问题
- 修复了 `teleport{unsafe=false}` 不正确放置玩家的问题
- 修复了 `hasItem`、`holding` 和其他物品条件以支持新物品匹配器
- 修复了生命恢复属性错误治疗死亡玩家的问题
- 修复了无法受伤实体的 MythicDamageEvent
- 修复了 `mobsInRadius` 对某些原版类型失败的问题
- 修复了生成器物品不应用正确生物数据的问题
- 修复了子碰撞箱元数据操作导致栈溢出的问题
- 修复了 `spin` 效果在施法者死亡时不停止的问题
- 修复了 `EnderBeam` 技能中的 IllegalArgumentException
- 修复了 `setDisplayEntityItem` 技能与 Crucible 生成物品不兼容的问题
- 修复了物品显示插值/旋转问题
- 修复了没有 `MovementSpeed` 的生物使用 `setSpeed` 技能卡住的问题
- 修复了鸡骑士选项不工作的问题
- 修复了 1.21.4 上各种船类型失效的问题
- 许多额外的并发和缓存修复

旧版更新日志
================
-   [5.7.X 更新日志](/changelogs/5.7.x_changelogs)
-   [5.6.X 更新日志](/changelogs/5.6.x_changelogs)
-   [5.5.X 更新日志](/changelogs/5.5.x_changelogs)
-   [5.4.X 更新日志](/changelogs/5.4.x_changelogs)
-   [5.3.X 更新日志](/changelogs/5.3.x_changelogs)
-   [5.2.X 更新日志](/changelogs/5.2.x_changelogs)
-   [5.1.X 更新日志](/changelogs/5.1.x_changelogs)
-   [5.0.X 更新日志](/changelogs/5.0.x_changelogs)
-   [4.14.X 更新日志](/changelogs/4.14.x_changelogs)
-   [4.13.X 更新日志](/changelogs/4.13.x_changelogs)
-   [4.12.X 更新日志](/changelogs/4.12.x_changelogs)
-   [4.11.X 更新日志](/changelogs/4.11.x_changelogs)
-   [4.10.X 更新日志](/changelogs/4.10.x_changelogs)
-   [4.9.X 更新日志](/changelogs/4.9.x_changelogs)
-   [4.8.X 更新日志](/changelogs/4.8.x_changelogs)
-   [4.7.X 更新日志](/changelogs/4.7.x_changelogs)
-   [4.6.X 更新日志](/changelogs/4.6.x_changelogs)
-   [4.5.X 更新日志](/changelogs/4.5.x_changelogs)
-   [4.4.X 更新日志](/changelogs/4.4.x_changelogs)
-   [4.3.X 更新日志](/changelogs/4.3.x_changelogs)
-   [4.2.X 更新日志](/changelogs/4.2.x_changelogs)
-   [4.1.X 更新日志](/changelogs/4.1.x_changelogs)
-   [4.0.X 更新日志](/changelogs/4.0.x_changelogs)
-   [2.5.X 更新日志](/changelogs/2.5.x_changelogs)
-   [2.4.X 更新日志](/changelogs/2.4.x_changelogs)
-   [2.3.X 更新日志](/changelogs/2.3.x_changelogs)
-   [2.2.X 更新日志](/changelogs/2.2.x_changelogs)
-   [2.1.X 更新日志](/changelogs/2.1.x_changelogs)
-   [2.0.X 更新日志](/changelogs/2.0.x_changelogs)
-   [Pre-2.0 更新日志](/changelogs/pre-2.0_changelogs)
