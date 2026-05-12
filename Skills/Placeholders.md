这里列出了你可以在使用字符串的技能中使用的所有占位符和特殊字符。文末有一些示例供你参考。

__**注意：** 技能中的大部分变量功能需要高级版授权，MMOCore、特殊字符、颜色代码和 `setvariable` 除外。__


[[_TOC_]]

# 特殊字符
| **占位符** | **功能**                                                | 符号    |
|:---------:|--------------------------------------------------------|---------|
|  <&co>   | 返回冒号                                                | `:`     |
|  <&sq>   | 返回单引号                                              | `'`     |
|  <&da>   | 返回破折号                                              | `-`     |
|  <&bs>   | 返回反斜杠                                              | `\`     |
|  <&fs>   | 返回正斜杠                                              | `/`     |
|  <&sp>   | 返回空格                                                | ` `     |
|  <&cm>   | 返回逗号                                                | `,`     |
|  <&sc>   | 返回分号                                                | `;`     |
|  <&eq>   | 返回等号                                                | `=`     |
|  <&dq>   | 返回双引号                                              | `"`     |
|  <&rb>   | 返回右方括号                                            | `]`     |
|  <&lb>   | 返回左方括号                                            | `[`     |
|  <&rc>   | 返回右花括号                                            | `}`     |
|  <&lc>   | 返回左花括号                                            | `{`     |
|  <&nm>   | 返回井号                                                | `#`     |
|  <&nl>   | 强制换行                                                |  <br>    |
| <&heart> | 返回爱心                                                | `❤`    |
| <&skull> | 返回骷髅头                                              | `☠`    |
|  <&lt>   | 返回小于号                                              | `<`     |
|  <&gt>   | 返回大于号                                              | `>`     |
|  <^dot>  | 返回点号                                                | `.`     |
| <^dot2>  | 返回返回点号的占位符。在涉及敏感的占位符解析时很有用。        | `<^dot>` |

# 颜色代码
这些颜色代码在生物配置文件和技能配置文件的任意位置均可用，甚至能在命令技能中正确格式化 tellraw 命令！

旧版颜色代码：

| **代码** |  **颜色**  | **代码** |   **颜色**    |
|:--------:|:---------:|:--------:|:-------------:|
|    &0    |    黑色    |    &B    |      水蓝      |
|    &1    |   深蓝色   |    &C    |      红色      |
|    &2    |   深绿色   |    &D    |     浅紫色     |
|    &3    |   深水蓝   |    &E    |      黄色      |
|    &4    |   深红色   |    &F    |      白色      |
|    &5    |   深紫色   |    &K    |     闪烁       |
|    &6    |    金色    |    &L    |      粗体      |
|    &7    |    灰色    |    &M    |     删除线     |
|    &8    |   深灰色   |    &N    |     下划线     |
|    &9    |    蓝色    |    &O    |      斜体      |
|    &A    |    绿色    |    &R    |      重置      |

建议使用 [MiniMessage 标签](https://docs.adventure.kyori.net/minimessage/format.html#standard-tags)来进行文本样式和装饰。
以下是一个使用 MiniMessage 标签的示例：
```yml
MessageSkill:
  Skills:
    - message{m=<rainbow>This text is a rainbow</rainbow> but <red>this is red</red>!} @target
    - message{m=<#bae5f4>This is a cool color that I picked from</#bae5f4> <red><click:open_url:https://www.color-hex.com/color/bae5f4>color-hex site</click></red>} @target
```
MiniMessage 还有一个[网页预览器](https://webui.adventure.kyori.net/)，可以在线预览文本在游戏中的显示效果。

# 扩展插件的占位符
以下是扩展插件提供的占位符链接。如果没有安装对应的插件，这些占位符不会生效。

- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Placeholders)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#placeholders)

# 占位符

## 施法者占位符
这类占位符返回施法者的对应属性。例如 `<caster.l.y.#>` 返回施法者的 Y 坐标。

|       施法者占位符       | 功能                                                     |
|:------------------------:|---------------------------------------------------------|
|     <caster.damage>      | 返回施法者的 Attack_Damage 属性值                         |
|    <caster.display>      | 返回施法者的显示名称                                       |
|  <caster.mythic_type>    | 返回施法者的内部生物类型                                    |
|     <caster.type>        | 返回 MythicMob 的内部 ID，否则返回实体名称                  |
|   <caster.type.name>     | 返回 MythicMob 的显示名称，否则返回实体名称                  |
|     <caster.uuid>        | 返回施法者的 UUID                                          |
|     <caster.level>       | 返回施法者的等级                                           |
|      <caster.name>       | 返回施法者的名称                                           |
|       <caster.hp>        | 返回施法者的当前生命值                                      |
|      <caster.mhp>        | 返回施法者的最大生命值                                      |
|      <caster.php>        | 返回施法者的生命值百分比                                    |
|      <caster.thp>        | 返回施法者的完整生命值（整数）                               |
|     <caster.tt.top>      | 返回施法者当前最高仇恨者的名称                               |
|      <caster.l.w>        | 返回施法者所在的世界名                                      |
|      <caster.l.x>        | 返回施法者的 X 坐标                                        |
|   <caster.l.x.{Float}>   | 返回施法者的 X 坐标 ± {Float} 范围内的随机数                |
|   <caster.l.x.double>    | 返回施法者精确的 X 坐标                                     |
|      <caster.l.y>        | 返回施法者的 Y 坐标                                        |
|   <caster.l.y.{Float}>   | 返回施法者的 Y 坐标 ± {Float} 范围内的随机数                |
|   <caster.l.y.double>    | 返回施法者精确的 Y 坐标                                     |
|      <caster.l.z>        | 返回施法者的 Z 坐标                                        |
|   <caster.l.z.{Float}>   | 返回施法者的 Z 坐标 ± {Float} 范围内的随机数                |
|   <caster.l.z.double>    | 返回施法者精确的 Z 坐标                                     |
|     <caster.l.yaw>       | 返回施法者的水平朝向                                        |
|    <caster.l.pitch>      | 返回施法者的俯仰角                                         |
|     <caster.stance>      | 返回施法者当前的形态（stance）                              |
|  <caster.stat.{Stat}>    | 返回施法者指定 {Stat} 属性的值                              |
| <caster.heldenchantlevel.{Integer}> | 返回指定附魔 ID {Integer} 的等级                     |
| <caster.skill.{Metaskill}.cooldown> | 返回指定技能的当前冷却时间（浮点数）                 |
| <caster.raytrace.{Float}> | 返回施法者视线方向上 {Float} 格范围内的方块名。如果只写 <caster.raytrace>，默认范围为 4.5。如果未命中方块，返回 `AIR` |
| <caster.children.size>   | 返回该实体的子实体数量                                      |
| <caster.attack_cooldown> | 返回玩家装备物品的攻击冷却值，为 0（满冷却）到 1（无冷却）之间的浮点数 |

## 目标占位符
这类占位符返回所用的目标选择器选中目标的对应属性。例如 `<target.name>` 配合 `@NearestPlayer` 将返回距离施法者最近玩家的名字。以下仅列出了可作用于 `target` 作用域的部分占位符，通常[施法者占位符](#施法者占位符)部分中的所有占位符也同样适用于目标。

|    **目标占位符**    | **功能**                                                  |
|:-------------------:|----------------------------------------------------------|
|    <target.uuid>    | 返回目标的 UUID                                            |
|    <target.name>    | 返回目标的名称                                             |
|     <target.hp>     | 返回目标的当前生命值                                        |
|    <target.mhp>     | 返回目标的最大生命值                                        |
|    <target.php>     | 返回目标的生命值百分比                                      |
|    <target.thp>     | 返回目标的完整生命值（整数）                                 |
|  <target.threat>    | 返回目标的威胁值                                           |
|    <target.l.w>     | 返回目标所在的世界名                                        |
|    <target.l.x>     | 返回目标的 X 坐标                                          |
| <target.l.x.{Float}> | 返回目标的 X 坐标 ± {Float} 范围内的随机数                  |
|    <target.l.y>     | 返回目标的 Y 坐标                                          |
| <target.l.y.{Float}> | 返回目标的 Y 坐标 ± {Float} 范围内的随机数                  |
|    <target.l.z>     | 返回目标的 Z 坐标                                          |
| <target.l.z.{Float}> | 返回目标的 Z 坐标 ± {Float} 范围内的随机数                  |
|   <target.l.yaw>    | 返回目标的水平朝向                                         |
|  <target.l.pitch>   | 返回目标的俯仰角                                           |
|   <target.level>    | 返回目标的等级                                             |
| <target.block.type> | 返回目标方块的类型                                         |
| <target.block.data> | 返回目标方块的数据值                                       |
| <target.entity_type> | 返回目标的实体类型                                         |
| <target.item.type>  | 返回目标物品实体的类型                                      |
| <target.held.item>  | 返回目标手持的物品                                         |
| <target.itemstack_amount> | 返回地面上物品实体的堆叠数量                           |
| <target.stat.{StatName}> | 返回目标指定属性的值                                   |
| <target.raytrace.{Float}> | 返回目标视线方向上 {Float} 格范围内的方块名。如果只写 <target.raytrace>，默认范围为 4.5。如果未命中方块，返回 `AIR` |
| <target.fovoffset{rotation=0;absolute=true}> | 返回施法者视线方向与施法者到目标实体连线方向之间的角度偏差（度）。可用于判断目标偏离施法者视野中心的距离 |
| <target.distance>    | 返回施法者与技能目标之间的距离。如果目标不在施法者所在世界中，返回 Double 最大值 |
| <target.distancesquared> | 返回施法者与技能目标之间距离的平方。如果目标不在施法者所在世界中，返回 Double 最大值 |
| <target.armor>       | 返回目标的护甲值                                           |
| <target.item.itemstack.{EquipSlot}> | 返回目标玩家指定装备槽中物品的 ItemStack。槽位可以是名称（HAND、OFFHAND 等）或数字 |

## 触发者占位符
这类占位符返回触发技能的那个实体的对应属性。例如 `<trigger.name>` 配合 `~onDeath` 触发器，会返回击杀该生物的那个实体的名字。

```yaml
    Skills:
    - message{m="<&b><caster.name><&r> was slain by <&a><trigger.name><&r>."} @PIR{r=20} ~onDeath
```

以下仅列出了可作用于 `trigger` 作用域的部分占位符，通常[施法者占位符](#施法者占位符)部分中的所有占位符也同样适用于触发者。

|    触发者占位符     | 功能                                                          |
|:------------------:|--------------------------------------------------------------|
|   <trigger.uuid>   | 返回触发技能实体的 UUID                                        |
|   <trigger.name>   | 返回触发技能实体的名称                                          |
|    <trigger.hp>    | 返回触发技能实体的当前生命值                                     |
|   <trigger.mhp>    | 返回触发技能实体的最大生命值                                     |
|  <trigger.threat>  | 返回触发技能实体的威胁值                                         |
|   <trigger.l.w>    | 返回触发技能实体所在的世界名                                     |
|   <trigger.l.x>    | 返回触发技能实体的 X 坐标                                       |
| <trigger.l.x.{Float}> | 返回触发技能实体的 X 坐标 ± {Float} 范围内的随机数               |
|   <trigger.l.y>    | 返回触发技能实体的 Y 坐标                                       |
| <trigger.l.y.{Float}> | 返回触发技能实体的 Y 坐标 ± {Float} 范围内的随机数               |
|   <trigger.l.z>    | 返回触发技能实体的 Z 坐标                                       |
| <trigger.l.z.{Float}> | 返回触发技能实体的 Z 坐标 ± {Float} 范围内的随机数               |
|  <trigger.l.yaw>   | 返回触发者的水平朝向                                            |
| <trigger.l.pitch>  | 返回触发者的俯仰角                                              |
| <trigger.held.item>  | 返回触发者手持的物品                                           |
| <trigger.raytrace>   | 返回触发者视线方向的方块名（4.5 格范围）                         |
| <trigger.item.amount> | 返回触发者手持物品的数量                                       |
| <trigger.item.type> | 返回触发者手持物品的类型                                        |
| <trigger.item.model> | 返回触发者手持物品的模型                                        |
| <trigger.stat.{Stat}> | 返回触发者指定属性的值                                         |
| <trigger.raytrace.{Float}> | 返回触发者视线方向上 {Float} 格范围内的方块名。如果只写 <trigger.raytrace>，默认范围为 4.5。如果未命中方块，返回 `AIR` |
| <trigger.distance> | 返回施法者与技能树触发者之间的距离。如果触发者不在施法者所在世界中，返回 Double 最大值 |
| <trigger.distancesquared> | 返回施法者与技能树触发者之间距离的平方。如果触发者不在施法者所在世界中，返回 Double 最大值 |


## 杂项占位符
|    **占位符**              | **功能**                                                  |
|---------------------------|----------------------------------------------------------|
| <drop.amount>             | 在特定掉落类型中使用时，返回掉落数量                          |
| <drops.xp>                | 返回通过特定掉落类型掉落的经验值                              |
| <drops.money>             | 返回通过 Vault 插件掉落的金钱                                |
| <random.#to#>             | 返回指定范围内的随机整数                                    |
| <random.float.#to#>       | 返回指定范围内的随机浮点数                                   |
| <utils.epoch>             | 返回当前的纪元时间戳                                        |
| <utils.epoch.seconds>     | 返回当前的纪元时间戳（秒）                                   |
| <utils.epoch.timestamp>   | 返回自纪元以来的毫秒数                                       |
| <utils.epoch.millis>      | 返回当前纪元时间的毫秒部分                                   |
| <utils.epoch.ticks>       | 返回转换成刻的当前纪元时间。假定服务器始终维持每秒 20 刻。计入毫秒。<br>虽然不太常规，但考虑到 Minecraft（以及 Mythic）内部以刻衡量时间，在大规模处理需要将常规纪元时间转换为刻的场景时，这个占位符可能有助于简化流程 |

## 物品占位符
| **占位符**                                  | **功能**                                    |
|--------------------------------------------|---------------------------------------------|
| <item.amount>                              | 返回触发技能物品的数量                         |
| <mythicitem.{MythicItem}.material>         | 返回指定 Mythic 物品的材质                     |
| <mythicitem.{MythicItem}.model>            | 返回指定 Mythic 物品的自定义模型数据              |
| <mythicitem.{MythicItem}.display>          | 返回指定 Mythic 物品的显示名称                   |
| <mythicitem.{MythicItem}.itemstack>        | 返回指定 Mythic 物品的物品堆                    |

## 计分板占位符
| **占位符**                       | **功能**                                               |
|----------------------------------|-------------------------------------------------------|
| <caster.score.{Objective}>       | 返回施法者在 "{Objective}" 计分项中的分数                |
| <target.score.{Objective}>       | 返回目标在 "{Objective}" 计分项中的分数                  |
| <trigger.score.{Objective}>      | 返回触发者在 "{Objective}" 计分项中的分数                |
| <global.score.{Objective}>       | 返回虚拟玩家 \_\_GLOBAL\_\_ 在 "{Objective}" 计分项中的分数 |
| <score.objective.player>         | 返回指定玩家在 "objective" 计分项中的分数                |
| <score.objective.dummyname>      | 返回 "dummyname"（虚拟玩家）在 "objective" 计分项中的分数 |

```yaml
  - message{m=You have slain <trigger.var.slainmobs> Mobs!} @trigger ~onInteract
```

## 变量占位符
这类占位符返回所调用的变量的值。例如 `<caster.var.\[name\]>` 返回施法者的 `[name]` 变量的值。
部分变量只在特定情况下生成和可用，比如之前在技能树中使用过某些特定的触发器/属性/元技能。

|   变量占位符                                                                               |   由什么生成                                                                                              |  功能                                                                                                   |
|:------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|
| <caster.var.{VariableName}>                                                                |    | 返回施法者变量注册表中 {VariableName} 变量的值                                                                    |
| <target.var.{VariableName}>                                                                |    | 返回技能目标变量注册表中 {VariableName} 变量的值                                                                    |
| <world.var.{VariableName}>                                                                 |    | 返回技能所在世界变量注册表中 {VariableName} 变量的值                                                                  |
| <global.var.{VariableName}>                                                                |    | 返回整个服务器变量注册表中 {VariableName} 变量的值                                                                    |
| <skill.var.{VariableName}>                                                                 |    | 返回当前[技能树](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/SkillTrees)中 {VariableName} 变量的值 |
| <skill.var.damage-amount>                | [~onDamaged] 触发器 <br> [~onAttack] 触发器 <br> [~onBowHit] 触发器 <br> [onDamaged] 技能 <br> [onAttack] 技能 | 返回承受或造成的伤害值                                                                                   |
| <skill.var.damage-type>                  | [~onDamaged] 触发器 <br> [~onAttack] 触发器 <br> [~onBowHit] 触发器 <br> [onDamaged] 技能 <br> [onAttack] 技能 | 返回承受或造成的伤害类型（如果有的话）                                                                     |
| <skill.var.damage-cause>                 | [~onDamaged] 触发器 <br> [~onAttack] 触发器 <br> [~onBowHit] 触发器 <br> [onDamaged] 技能 <br> [onAttack] 技能 | 返回承受或造成的伤害原因                                                                                 |
| <skill.var.aura-name>                    | 所有 [aura] 技能                                                                                           | 返回光环名称                                                                                            |
| <skill.var.aura-type>                    | 所有 [aura] 技能                                                                                           | 返回光环类型                                                                                            |
| <skill.var.aura-charges>                 | 所有 [aura] 技能                                                                                           | 返回光环剩余使用次数                                                                                     |
| <skill.var.aura-duration>                | 所有 [aura] 技能                                                                                           | 返回光环剩余持续时间                                                                                     |
| <skill.var.aura-duration-millis>         | 所有 [aura] 技能                                                                                           | 返回光环剩余持续时间（毫秒）                                                                              |
| <skill.var.aura-stacks>                  | 所有 [aura] 技能                                                                                           | 返回光环剩余层数                                                                                        |
| <skill.var.input>                        | [onChat] 技能                                                                                               | 返回聊天输入内容                                                                                        |
| <skill.targets>                          |    | 返回继承到的目标数量                                                                                     |
| <skill.var.interval>                     | 使用了 `repeat` 和 `repeatInterval` [通用属性]                                                               | 返回当前迭代次数                                                                                        |
| <skill.var.itr>                          | 使用了 `repeat` 和 `repeatInterval` [通用属性]                                                               | 返回当前迭代次数                                                                                        |
| <skill.var.volume>                       | [~onHear] 触发器                                                                                            | 返回一个 1 到 15 之间的浮点数，表示声音强度。与距离成正比（声源越远，值越大）                                |
| <skill.var.sound-type>                   | [~onHear] 触发器                                                                                            | 返回声音类型                                                                                            |
| <skill.var.hit-block-type>               | [raytrace] 技能                                                                                              | 返回命中的方块，未命中则返回 AIR                                                                          |
| <skill.var.bow-tension>                  | [~onShoot] 触发器                                                                                            | 返回弹射物的射出力度                                                                                     |

```yaml
  Skills:
  - setvariable{var=caster.test1;val=1} @self
  - setvariable{var=target.test2;val=2} @self
  - message{m=<caster.var.test1> <caster.var.test2> <target.var.test1> <target.var.test2>} @self
```
> 如果你自己执行这个元技能，它会向你发送一条消息 `1 2 1 2`，因为每条技能的目标都是施法者自身，所以即便使用了 "target" 作用域，实际操作的始终是施法者的变量注册表。

### 元变量占位符

你可以在变量占位符后面追加一些关键词（我们称之为「元关键词」），每种关键词对应特定的变量类型，用来修改变量的返回值和返回类型。

```yaml
<{VariableScope}.var.{VariableName}.{keywords}>
```

每个关键词都有一个
- `输入类型`，即该关键词适用的变量类型
- `输出类型`，即该关键词返回值可被创建为的变量类型

> 变量占位符内部的任意位置均支持占位符，因此每个关键词本身也可以是通过另一个占位符解析而来的值。

##

```yaml
<skill.var.exampleString.capitalize>
```
> 在字符串类型的所有关键词中，我们使用的是 `capitalize`，其输出为字符串类型。这意味着：
> - 它作用于一个字符串变量
> - 它对其值进行某种转换（此处为将字符串的每个字符大写）
> - 它返回一个字符串值


```yaml
<skill.var.exampleString.size>
```
> 在字符串类型的所有关键词中，我们使用的是 `size`，其输出为整数类型。这意味着：
> - 它作用于一个字符串变量
> - 它对其值进行某种转换（此处为返回字符串的长度）
> - 它返回一个整数值

##

由于每个元关键词都有特定的输入和输出类型，因此可以将它们**串联**起来使用，获得复合效果——每个关键词都会转换变量的值，然后将结果传递给下一个关键词。

```yaml
<skill.var.exampleString.substring.0.9.size.add.1>
```
> 在字符串类型的所有关键词中，我们使用的是 `substring`，其输出为字符串类型。这意味着：
> - 它作用于一个字符串变量
> - 它对其值进行某种转换（此处为提取字符串的前 10 个字符）
> - 它返回一个字符串值
>
> 在字符串类型的所有关键词中，我们又使用了 `size`，其输出为整数类型。这意味着：
> - 它作用于一个字符串变量（即 `substring` 关键词刚刚返回的值）
> - 它对其值进行某种转换（此处为返回字符串的长度，我们知道此长度在 0 到 10 之间）
> - 它返回一个整数值
>
> 在整数类型的所有关键词中，我们又使用了 `add`，其输出为整数类型。这意味着：
> - 它作用于一个整数变量（即 `size` 关键词刚刚返回的值）
> - 它对其值进行某种转换（此处为将整数值加上 1）
> - 它返回一个整数值

#### 通用元关键词
|  占位符     | 返回类型 | 返回值说明 |
|-----------|---------|----------|
| .cache    |         | 根据输入值和其后使用的关键词，此关键词会在首次解析时缓存结果，之后的每次解析直接返回缓存值 |
| .formatted | STRING | 返回更易于阅读的输入值版本 |
| .tointeger | INTEGER | 将值转换为整数，不做任何特定操作，允许链接整数元关键词 |
| .tofloat   | FLOAT   | 将值转换为浮点数，不做任何特定操作，允许链接浮点数元关键词 |
| .todouble  | DOUBLE  | 将值转换为双精度浮点，不做任何特定操作，允许链接双精度浮点元关键词 |
| .toboolean | BOOLEAN | 将值转换为布尔值，不做任何特定操作，允许链接布尔元关键词 |
| .tostring  | STRING  | 将值转换为字符串，不做任何特定操作，允许链接字符串元关键词 |
| .tolocation | LOCATION | 将值转换为位置，不做任何特定操作，允许链接位置元关键词 |
| .tovector  | VECTOR  | 将值转换为向量，不做任何特定操作，允许链接向量元关键词 |
| .tolist    | LIST    | 将值转换为列表，不做任何特定操作，允许链接列表元关键词 |
| .toset     | SET     | 将值转换为集合，不做任何特定操作，允许链接集合元关键词 |
| .tomap     | MAP     | 将值转换为映射，不做任何特定操作，允许链接映射元关键词 |
| .totime    | TIME    | 将值转换为时间，不做任何特定操作，允许链接时间元关键词 |
> [跳转至说明>>](#元变量占位符)

#### 整数元关键词
|  占位符       | 返回类型 | 返回值说明 |
|-------------|---------|----------|
| .add.{Integer} | INTEGER | 值与指定整数的加法结果 |
| .sub.{Integer} | INTEGER | 值与指定整数的减法结果 |
| .mul.{Integer} | INTEGER | 值与指定整数的乘法结果 |
| .div.{Integer} | INTEGER | 值与指定整数的除法结果 |
| .abs | INTEGER | 值的绝对值 |
> [跳转至说明>>](#元变量占位符)

#### 浮点数元关键词
|  占位符     | 返回类型 | 返回值说明 |
|-----------|---------|----------|
| .add.{Float} | FLOAT | 值与指定浮点数的加法结果 |
| .sub.{Float} | FLOAT | 值与指定浮点数的减法结果 |
| .mul.{Float} | FLOAT | 值与指定浮点数的乘法结果 |
| .div.{Float} | FLOAT | 值与指定浮点数的除法结果 |
| .abs | FLOAT | 值的绝对值 |
> [跳转至说明>>](#元变量占位符)

#### 双精度浮点元关键词
|  占位符      | 返回类型 | 返回值说明 |
|------------|---------|----------|
| .add.{Double} | DOUBLE | 值与指定双精度浮点数的加法结果 |
| .sub.{Double} | DOUBLE | 值与指定双精度浮点数的减法结果 |
| .mul.{Double} | DOUBLE | 值与指定双精度浮点数的乘法结果 |
| .div.{Double} | DOUBLE | 值与指定双精度浮点数的除法结果 |
| .abs | DOUBLE | 值的绝对值 |
> [跳转至说明>>](#元变量占位符)

#### 布尔元关键词
|  占位符       | 返回类型 | 返回值说明 |
|-------------|---------|----------|
| .inverse    | BOOLEAN | 值的取反 |
| .number     | INTEGER | 值以 0（false）或 1（true）表示 |
| .yesno      | STRING  | 值以 no（false）或 yes（true）表示 |
| .union.{Boolean} | BOOLEAN | 与指定布尔值的逻辑或 |
| .intersection.{Boolean} | BOOLEAN | 与指定布尔值的逻辑与 |
| .difference.{Boolean} | BOOLEAN | 当值为 true 且参数为 false 时返回 true |
> [跳转至说明>>](#元变量占位符)

#### 字符串元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .size | INTEGER | 字符串的长度 |
| .uppercase | STRING | 全部大写 |
| .lowercase | STRING | 全部小写 |
| .capitalize | STRING | 首字母大写 |
| .trim | STRING | 去除首尾空格 |
| .replace.{old}.{new} | STRING | 将所有 `old` 出现替换为 `new` |
| .remove.{text} | STRING | 移除所有 `text` 出现 |
| .contains.{text} | BOOLEAN | 字符串是否包含 `text` |
| .substring.{start}.{end} | STRING | 从索引 `start` 到 `end` 的子串 |
| .shift.{Integer} | STRING | 移除前 `Integer` 个字符 |
| .split.{regex}.{joiner} | STRING | 按 `regex` 分割，再用 `joiner` 连接 |
| .indexof.{text} | INTEGER | 首次出现 `text` 的索引 |
| .lastindexof.{text} | INTEGER | 末次出现 `text` 的索引 |
| .startswith.{text} | BOOLEAN | 字符串是否以 `text` 开头 |
| .endswith.{text} | BOOLEAN | 字符串是否以 `text` 结尾 |
| .append.{text} | STRING | 在末尾追加 `text` |
| .prepend.{text} | STRING | 在开头添加 `text` |
| .insert.{index}.{text} | STRING | 在指定 `index` 处插入 `text` |
| .regex.{pattern} | BOOLEAN | 字符串是否匹配正则表达式 `pattern` |
| .{index} | STRING | 返回指定 `index` 位置的字符 |
> [跳转至说明>>](#元变量占位符)

#### 集合元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .size | INTEGER | 集合中元素的数量 |
| .join.{delimiter} | STRING | 用 `delimiter` 连接所有元素 |
| .contains.{element} | BOOLEAN | 集合是否包含指定的 `element` |
> [跳转至说明>>](#元变量占位符)

#### 位置元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .x | DOUBLE | X 坐标 |
| .y | DOUBLE | Y 坐标 |
| .z | DOUBLE | Z 坐标 |
| .world | STRING | 世界名 |
| .yaw | DOUBLE | 水平朝向 |
| .pitch | DOUBLE | 俯仰角 |
| .coords | LIST | 包含 X、Y、Z 坐标的列表 |
> [跳转至说明>>](#元变量占位符)

#### 向量元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .x | DOUBLE | X 分量 |
| .y | DOUBLE | Y 分量 |
| .z | DOUBLE | Z 分量 |
| .normalized | VECTOR | 单位化后的向量 |
| .length | DOUBLE | 向量的长度（模） |
| .mul.{vector} | VECTOR | 与另一向量相乘 |
| .div.{vector} | VECTOR | 除以另一向量 |
| .add.{vector} | VECTOR | 加上另一向量 |
| .sub.{vector} | VECTOR | 减去另一向量 |
| .rotate.{axis}.{angle} | VECTOR | 绕指定 `axis` 旋转 `angle` 弧度 |
> [跳转至说明>>](#元变量占位符)

#### 列表元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .size | INTEGER | 列表中元素的数量 |
| .first | STRING | 列表的第一个元素 |
| .last | STRING | 列表的最后一个元素 |
| .reverse | LIST | 反转后的列表 |
| .sort | LIST | 按字母排序后的列表 |
| .sortnum | LIST | 按数字排序后的列表。列表中的每个元素必须是数字 |
| .shuffle | LIST | 打乱后的列表（随机排列） |
| .get.{index} | STRING | 指定 `index` 位置的元素 |
| .join.{delimiter} | STRING | 用 `delimiter` 连接所有元素 |
| .contains.{element} | BOOLEAN | 列表是否包含 `element` |
| .maxnumber | DOUBLE | 列表中的最大数值 |
| .minnumber | DOUBLE | 列表中的最小数值 |
| .indexof.{value} | INTEGER | 首次出现 `value` 的索引 |
| .lastindexof.{value} | INTEGER | 末次出现 `value` 的索引 |
| .slice.{from}.{to} | LIST | 从 `from` 到 `to` 的切片 |
| .slicefrom.{index} | LIST | 从 `index` 到末尾的切片 |
| .sliceto.{index} | LIST | 从开头到 `index` 的切片 |
| .append.{value} | LIST | 在末尾添加 `value` |
| .prepend.{value} | LIST | 在开头添加 `value` |
| .insert.{index}.{value} | LIST | 在指定 `index` 处插入 `value` |
| .remove.{index} | LIST | 移除指定 `index` 处的值 |
| .{index} | STRING | 指定 `index` 位置的元素 |
> [跳转至说明>>](#元变量占位符)

#### 映射元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .size | INTEGER | 键值对数量 |
| .keys | LIST | 所有键的列表 |
| .values | LIST | 所有值的列表 |
| .get.{key} | STRING | 关联到指定 `key` 的值 |
| .{key} | STRING | 关联到指定 `key` 的值 |
> [跳转至说明>>](#元变量占位符)

#### 时间元关键词
|  占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .delta.{timestamp} | INTEGER | 值的时间与给定 `timestamp` 的差值 |
| .formatted.{pattern} | STRING | 用指定模式格式化日期/时间。模式可以是 Java 函数 [ZoneOffset.of](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneOffset.html#of-java.lang.String-) 接受的任何格式 |
| .duration | STRING | 将时间解释为原始「毫秒数」并显示总秒数、分钟、小时、天数、月数和年数。对于倒计时等场景很有用，尤其与 `.delta` 元关键词结合使用时 |
> [跳转至说明>>](#元变量占位符)

#### 物品元关键词
| 占位符 | 返回类型 | 返回值说明 |
|-------|---------|----------|
| .withType.{material} | ITEM | 返回同一物品但类型设置为指定 `material`（不区分大小写，必须是有效的 Material 枚举值） |
| .withDurability.{value} | ITEM | 返回同一物品但耐久度设置为指定整数值 |
| .withMaxDurability.{value} | ITEM | 返回同一物品但最大耐久度设置为指定整数值 |
| .withLore.{list} | ITEM | 返回同一物品但描述设置为指定字符串列表 |
| .withName.{name} | ITEM | 返回同一物品但显示名称设置为 `name` |
| .withMythicType.{type} | ITEM | 返回同一物品但持久化的「Mythic 类型」设置为 `type`，从而使 Mythic 认为修改后的物品是 `type` 类型的 Mythic 物品 |
| .withEnchants.{map} | ITEM | 返回同一物品但附魔替换为映射中提供的附魔。应用新附魔之前会移除所有旧附魔 |
| .withCustomData.{namespace}.{key}.{value} | ITEM | 返回同一物品但带有指定的自定义持久化数据（`value` 存储在 `namespace:key` 下） |
| .withAmount.{value} | ITEM | 返回同一物品但堆叠数量设置为 `value` |
| .withUUID.{uuid} | ITEM | 返回同一物品但 UUID nbt 设置为指定值 |
| .withTimestamp.{timestamp} | ITEM | 返回同一物品但时间戳 nbt 设置为指定整数值 |
| .withCustomModelData.{value} | ITEM | 返回同一物品但自定义模型数据设置为 `value` |
| .withModel.{namespace}.{path} | ITEM | 返回同一物品但物品模型设置为 `{namespace}:{path}` |
| .type | STRING | 物品的类型，字符串形式（Material 名称） |
| .durability | INTEGER | 物品的当前耐久度值 |
| .maxDurability | INTEGER | 物品的最大耐久度值 |
| .lore | LIST | 物品的描述，字符串列表形式 |
| .name | STRING | 物品的显示名称 |
| .mythicType | STRING | 物品的持久化「Mythic 类型」值（若已设置） |
| .enchants | MAP | 物品上所有附魔的映射 |
| .getCustomData.{namespace}.{key} | STRING | 存储在物品自定义持久化数据 `{namespace}:{key}` 下的字符串值 |
| .customModelData | INTEGER | 物品的自定义模型数据值 |
| .model | STRING | 物品的模型标识符，`namespace:path` 格式 |
| .amount | INTEGER | 物品的堆叠数量 |
> [跳转至说明>>](#元变量占位符)


# 占位符属性
部分占位符可以使用一组属性来进一步定义其输出值。

| 属性      | 别名        | 描述                                        | 默认值 |
|----------|------------|---------------------------------------------|--------|
| rounding | round, r   | 返回的浮点数值的小数位数                       | 2      |

```yaml
  Skills:
  - message{m="<target.hp{round=2}>"} @self
```


# PlaceholderAPI 集成
除了在任何支持占位符的地方都可以使用 PlaceholderAPI 占位符之外，MythicMobs 还引入了一些新的 PAPI 占位符，可供第三方用于获取与 MythicMobs 相关的值。

| **PAPI 占位符**                       | **功能**                                           |
|--------------------------------------|---------------------------------------------------|
| %mythic_var_someVar%                 | 返回玩家上 `someVar` 变量的值                        |
| %mythic_var_world_someVar%           | 返回世界上 `someVar` 变量的值                        |
| %mythic_var_global_someVar%          | 返回服务器上 `someVar` 变量的值                      |
| %mythic_var_\<playerName\>_someVar%  | 返回指定玩家（按名称）上 `someVar` 变量的值            |
| %mythic_var_\<UUID\>_someVar%        | 返回指定实体（按 UUID）上 `someVar` 变量的值          |
| %mythic_spawner_[name]_cooldown%     | 返回名为 `name` 的生成器的冷却时间                    |
| %mythic_spawner_[name]_cooldownleft% | 返回名为 `name` 的生成器的剩余冷却时间                 |
| %mythic_spawner_[name]_warmup%       | 返回名为 `name` 的生成器的预热时间                    |
| %mythic_spawner_[name]_warmupleft%   | 返回名为 `name` 的生成器的剩余预热时间                 |
| %mythic_stat_[name]%                 | 返回所评估玩家指定属性的值                             |

## PlaceholderAPI 解析
在使用 PlaceholderAPI 的占位符时，需要注意其中一些是针对玩家解析的，如果对生物解析可能会出现意外行为。
具体而言，这意味着：
- 如果在技能内部使用，目标必须是玩家
- 如果在条件内部使用，被检查的实体必须是玩家（条件部分检查施法者，目标条件部分检查继承的目标，触发条件部分检查触发者）

……以此类推。

# 自定义占位符
可以在任意数据包中通过在包目录下创建 `placeholders.yml` 文件来定义自定义占位符。可以定义静态占位符，也可以定义条件占位符——第一个评估为真的会被选中，如果全部为假则使用 `Default`。

自定义占位符可通过 `<placeholder.[CustomPlaceholder]>` 使用，其中 _[CustomPlaceholder]_ 是你自定义占位符的名称。

```yaml
TestPlaceholder: 'some value'

TestConditionalPlaceholder:
  Day:
    Conditions:
    - day
    Value: day
  Night:
    Conditions:
    - night
    Value: night
  Default: idk

TestRandomPlaceholder:
- red
- green
- blue
```
> 不接受 "null" 值。

# 示例
**让生物在死亡时向自身周围 20 格内的所有玩家广播一条青色消息，用绿色显示击杀者的名字。**

```yaml
    Skills:
    - message{m="<&b><caster.name><&r> was slain by <&a><trigger.name><&r>."} @PIR{r=20} ~onDeath
```

**以下技能使生物在生成时发出通告，效果如下：**

![image](uploads/91ed6d8aaa669e8ae21f8745e8ff4643/image.png)

```yaml
  Skills:
  - Skill{s=SaveBossLocation} @self ~onSpawn
  - message{m="&eA &BGiant Zombie&e (Level &4<caster.level>&e) &ehas spawned at <caster.var.SpawnLoc>"} ~onSpawn @PlayersInWorld
  - message{m="&eThe &BGiant Zombie&e (Level &4<caster.level>&e) &espawned at <caster.var.SpawnLoc>&e has been slain."} ~onDeath @PlayersInWorld
```

记得在技能文件中放置以下技能：

```yaml
SaveBossLocation:
  Skills:
  - setvariable{var=SpawnLoc;type=STRING;value="&b<caster.l.x>&e, &b<caster.l.y>&e, &b<caster.l.z>";scope=CASTER} @self
```
**你也可以用颜色标签和格式标签为生物制作漂亮的名称：**

![image](uploads/9ad97422803c3f35fbeac2e4df7f7d52/image.png)

```yaml
ZOMBIE:
  Display: 'ZOMBIE &F- &A<caster.hp>/<caster.mhp>HP &F- &ELv.<caster.level>'
```


<!-- LINKS -->
[~onHear]: /Skills/Triggers/onHear
[~onDamaged]: /Skills/Triggers/onDamaged
[~onAttack]: /Skills/Triggers/onAttack
[~onBowHit]: /Skills/Triggers/onBowHit
[~onShoot]: /Skills/Triggers/onShoot
[onChat]: /skills/mechanics/onChat
[aura]: /skills/mechanics/aura
[raytrace]: /skills/mechanics/raytrace
[raytraceto]: /skills/mechanics/raytraceto
[onDamaged]: /skills/mechanics/onDamaged
[onAttack]: /skills/mechanics/onAttack
[通用属性]: /Skills/Mechanics#universal-attributes