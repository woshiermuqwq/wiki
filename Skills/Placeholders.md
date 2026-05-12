These are all of the 占位符 and special characters 您可以 use in
技能 and 技能 that use strings. There are some 示例 of usage at the bottom to get you started.

__**注意:** Usage of many 变量 in 技能 are locked to the premium versions, 排除 MMOCore, special characters, 颜色代码, and `setvariable`__.


[[_TOC_]]

# Special Characters
| **占位符** | **Function** | Symbol |
|:---------------:|----------------------------------------------------------------------------|---------|
| <&co> | 返回 a colon | `:` |
| <&sq> | 返回 an apostrophe | `'` |
| <&da> | 返回 a dash | `-` |
| <&bs> | 返回 a backslash | `\` |
| <&fs> | 返回 a forward slash | `/` |
| <&sp> | 返回 a space | ` ` |
| <&cm> | 返回 a comma | `,` |
| <&sc> | 返回 a semicolon | `;` |
| <&eq> | 返回 an equals symbol | `=` |
| <&dq> | 返回 double quotes | `"` |
| <&rb> | 返回 a right bracket | `]` |
| <&lb> | 返回 a left bracket | `[` |
| <&rc> | 返回 a right curly bracket | `}` |
| <&lc> | 返回 a left curly bracket | `{` |
| <&nm> | 返回 a number sign | `#` |
| <&nl> | Forces a new line | <br> |
| <&heart> | 返回 a heart | `❤` |
| <&skull> | 返回 a skull and bones | `☠` |
| <&lt> | 返回 the 小于 symbol | `<` |
| <&gt> | 返回 the 大于 symbol | `>` |
| <^dot> | 返回 a dot | `.` |
| <^dot2> | 返回 the 占位符 that 返回 a dot. Useful when there is sensitive 占位符 parsing involved | `<^dot>` |

# Color Codes
These 颜色代码 work 任何地方 in 生物- and 技能-文件. They will even
pproperly 格式 tellraw-指令 used in 指令 技能!

Legacy 颜色代码:

| **Code** | **Color** | **Code** | **Color** |
|:--------:|:-----------:|:--------:|:--------------:|
| &0 | Black | &B | Aqua |
| &1 | Dark Blue | &C | Red |
| &2 | Dark Green | &D | Light Purple |
| &3 | Dark Aqua | &E | Yellow |
| &4 | Dark Red | &F | White |
| &5 | Dark Purple | &K | Magic |
| &6 | Gold | &L | Bold |
| &7 | Gray | &M | Strike 通过 |
| &8 | Dark Gray | &N | Underline |
| &9 | Blue | &O | Italic |
| &A | Green | &R | Reset |

It recommended that 您使用 [MiniMessage tags](https://docs.adventure.kyori.net/minimessage/格式.html#standard-tags) for text styling and text decorations.
Here an 示例 using MiniMessage tags:
```yml
MessageSkill:
  Skills:
    - message{m=<rainbow>This text is a rainbow</rainbow> but <red>this is red</red>!} @target
    - message{m=<#bae5f4>This is a cool color that I picked from</#bae5f4> <red><click:open_url:https://www.color-hex.com/color/bae5f4>color-hex site</click></red>} @target
```
MiniMessage 也 has a [web viewer](https://webui.adventure.kyori.net/) to see what your text will look like in game.

# Additional 占位符
Links to 占位符 added by addon 插件. Any 占位符 从se links 不会 work 没有 that 插件 installed.

- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/占位符)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#占位符)

# 占位符

## 施法者 占位符
These 占位符将返回whatever 属性 of the 施法者 即 called. For instance `<caster.l.y.#>` will 返回 the 施法者 Y 位置。

| 施法者 占位符 | Function |
|:----------------------------------:|-------------------------------------------------------------------|
| <施法者.伤害> | 返回 the 施法者 Attack_Damage 属性 值 |
| <施法者.显示> | 返回 the 施法者 displayed 名称 |
| <施法者.mythic_type> | 返回 the 施法者 internal 生物 类型 |
| <施法者.类型> |返回 the internal id of a MythicMob or the 实体 名称 否则|
| <施法者.类型.名称> |返回 the 显示 名称 of a MythicMob or the 实体 名称 否则|
| <施法者.uuid> | 返回 the UUID of the 施法者 |
| <施法者.等级> | 返回 the 等级 of the 施法者 |
| <施法者.名称> | 返回 the 名称 of the 施法者 |
| <施法者.生命值> | 返回 current 生命值 of the 施法者 |
| <施法者.mhp> | 返回 the max 生命值 of the 施法者 |
| <施法者.php> | 返回 the 百分比 生命值 of the 施法者 |
| <施法者.thp> | 返回 the full number 生命值 of the 施法者 |
| <施法者.tt.top> | 返回 the 名称 of the top 仇恨 holder of the 施法者 |
| <施法者.l.w> | 返回 the 世界 名称 the 施法者 is in |
| <施法者.l.x> | 返回 the X coordinate of the 施法者 |
| <施法者.l.x.{Float}> | 返回 the X coordinate of the 施法者 +- random number between {Float} |
| <施法者.l.x.double> | 返回 the precise X coordinate of the 施法者 |
| <施法者.l.y> | 返回 the Y coordinate of the 施法者 |
| <施法者.l.y.{Float}> | 返回 the Y coordinate of the 施法者 +- random number between {Float} |
| <施法者.l.y.double> | 返回 the precise Y coordinate of the 施法者 |
| <施法者.l.z> | 返回 the Z coordinate of the 施法者 |
| <施法者.l.z.{Float}> | 返回 the Z coordinate of the 施法者 +- random number between {Float} |
| <施法者.l.z.double> | 返回 the precise Z coordinate of the 施法者 |
| <施法者.l.yaw> | 返回 the yaw of the 施法者 |
| <施法者.l.pitch> | 返回 the pitch of the 施法者 |
| <施法者.stance> | 返回 the current stance of the 施法者 |
| <施法者.stat.{Stat}> | 返回 the 值 of the specified {Stat} on the 施法者 |
| <施法者.heldenchantlevel.{整数}> | 返回 the enchant 等级 of specified {整数} enchant |
| <施法者.技能.{元技能}.冷却> | 返回 the current 冷却 of the give 技能 as a float number |
| <施法者.raytrace.{Float}> | 返回 the 名称 of the 方块 being looked at by the 施法者 if 在...内 {Float} 范围, if {Float} is specified. If 仅 <施法者.raytrace> is used, then the 范围 默认为 `4.5`. If no 方块 is found, `AIR` is returned.|
| <施法者.子级.size> | 返回 the number of 子级 this 实体 has |
| <施法者.attack_cooldown> | 返回 the 攻击 冷却 of the 玩家 equipped 物品. The 值 将 a float between 0 (maximum 冷却 对于 物品) and 1 (no 冷却) |

## 目标 占位符
These 占位符将返回whatever 目标 selector 已被 used. For instance <目标.名称> + @NearestPlayer will 返回 the 名称 of the 玩家 closest to the casting 生物. The following are 仅 some of the 占位符 that can have a `target` 作用域, and in general any 占位符 即 也 present in the [施法者 占位符](#施法者-占位符) section 还将 work。

| **目标 占位符** | **Function** |
|:-----------------------:|-------------------------------------------------------------------|
| <目标.uuid> | 返回 the UUID of the 目标 |
| <目标.名称> | 返回 the 名称 of the 目标 |
| <目标.生命值> | 返回 current 生命值 of the 目标 |
| <目标.mhp> | 返回 the max 生命值 of the 目标 |
| <目标.php> | 返回 the 百分比 生命值 of the 目标 |
| <目标.thp> | 返回 the full number 生命值 of the 目标 |
| <目标.仇恨> | 返回 the 仇恨 等级 of the 目标 |
| <目标.l.w> | 返回 the 世界 名称 the 目标 is in |
| <目标.l.x> | 返回 the X coordinate of the 目标 |
| <目标.l.x.{Float}> | 返回 the X coordinate of the 目标 +- random number between {Float} |
| <目标.l.y> | 返回 the Y coordinate of the 目标 |
| <目标.l.y.{Float}> | 返回 the Y coordinate of the 目标 +- random number between {Float}|
| <目标.l.z> | 返回 the Z coordinate of the 目标 |
| <目标.l.z.{Float}> | 返回 the Z coordinate of the 目标 +- random number between {Float} |
| <目标.l.yaw> | 返回 the yaw of the 目标 |
| <目标.l.pitch> | 返回 the pitch of the 目标 |
| <目标.等级> | 返回 the 等级 of the 目标 |
| <目标.方块.类型> | 返回 the 方块 类型 of the 目标 |
| <目标.方块.data> | 返回 the 方块 data of the 目标 方块 |
| <目标.entity_type> | 返回 the 实体 类型 of the 目标 |
| <目标.物品.类型> | 返回 the 类型 of the targeted 物品 实体 |
| <目标.held.物品> | 返回 the 物品 held by the 目标 |
| <目标.itemstack_amount> | 返回 the 数量 of 物品 实体 on the ground |
| <目标.stat.{StatName}> | 返回 the 值 of the specified stat on the 目标 |
| <目标.raytrace.{Float}> | 返回 the 名称 of the 方块 being looked at by the 目标 if 在...内 {Float} 范围, if {Float} is specified. If 仅 <目标.raytrace> is used, then the 范围 默认为 `4.5`. If no 方块 is found, `AIR` is returned.|
| <目标.fovoffset{旋转=0;absolute=true}> | 返回 the angular 偏移 (in degrees) 在...之间 方向 the 施法者 is looking and the 方向 从 施法者 to the 目标 实体. This 偏移可以usedto determine how far the 目标 is 从 施法者 center of view |。
| <目标.距离> | 返回 the 距离 在...之间 施法者 and the 技能 目标. If the 目标 不能 be found in the 施法者 世界, 返回 the maximum double 值 |
| <目标.distancesquared> | 返回 the squared 距离 在...之间 施法者 and the 技能 目标. If the 目标 不能 be found in the 施法者 世界, 返回 the maximum double 值 |
|| <目标.armor> | 返回 the 目标 armor 值 |
| <目标.物品.itemstack.{EquipSlot}> | 返回 the ItemStack of the 物品 in the specified 栏位 on the 目标 玩家. The 栏位 可以是 a named one (HAND, OFFHAND etc.) or a number |

## 触发器 占位符
These 占位符将返回whatever 属性 of the 实体 that caused the 技能 to happen. For instance `<trigger.name>` combined with an `~onDeath` 触发器 will 返回 the 名称 of the 实体 that killed the 生物。

```yaml
    Skills:
    - message{m="<&b><caster.name><&r> was slain by <&a><trigger.name><&r>."} @PIR{r=20} ~onDeath
```

The following are 仅 some of the 占位符 that can have a `trigger` 作用域, and in general any 占位符 即 也 present in the [施法者 占位符](#施法者-占位符) section 还将 work.


| 触发器 占位符 | Function |
|:--------------------:|----------------------------------------------------------------------------------------|
| <触发器.uuid> | 返回 the UUID of the 实体 triggering the 技能 |
| <触发器.名称> | 返回 the 名称 of the 实体 triggering the 技能 |
| <触发器.生命值> | 返回 the current 生命值 of the 实体 triggering the 技能 |
| <触发器.mhp> | 返回 the max 生命值 of the 实体 triggering the 技能 |
| <触发器.仇恨> | 返回 the 仇恨 等级 of the 实体 triggering the 技能 |
| <触发器.l.w> | 返回 the 世界 名称 of the 实体 triggering the 技能 |
| <触发器.l.x> | 返回 the X coordinate of the 实体 triggering the 技能 |
| <触发器.l.x.{Float}> | 返回 the X coordinate of the 实体 triggering the 技能 +- random number between {Float} |
| <触发器.l.y> | 返回 the Y coordinate of the 实体 triggering the 技能 |
| <触发器.l.y.{Float}> | 返回 the Y coordinate of the 实体 triggering the 技能 +- random number between {Float} |
| <触发器.l.z> | 返回 the Z coordinate of the 实体 triggering the 技能 |
| <触发器.l.z.{Float}> | 返回 the Z coordinate of the 实体 triggering the 技能 +- random number between {Float} |
| <触发器.l.yaw> | 返回 the yaw of the 触发器 |
| <触发器.l.pitch> | 返回 the pitch of the 触发器 |
| <触发器.held.物品> | 返回 the 物品 held by the 触发器 |
| <触发器.raytrace> | 返回 the 名称 of the 方块 being looked at by the 触发器 (4.5 方块 of 范围) |
| <触发器.物品.数量> | 返回 the 数量 of the 物品 the 触发器 is holding |
| <触发器.物品.类型> | 返回 the 类型 of the 物品 the 触发器 is holding |
| <触发器.物品.model> | 返回 the model of the 物品 the 触发器 is holding |
| <触发器.stat.{Stat}> | 返回 the 值 of the specified stat on the 触发器 |
| <触发器.raytrace.{Float}> | 返回 the 名称 of the 方块 being looked at by the 触发器 if 在...内 {Float} 范围, if # is specified. If 仅 <触发器.raytrace> is used, then the 范围 默认为 `4.5`. If no 方块 is found, `AIR` is returned.|
| <触发器.距离> | 返回 the 距离 在...之间 施法者 and the skilltree 触发器. If the 触发器 不能 be found in the 施法者 世界, 返回 the maximum double 值 |
| <触发器.distancesquared> | 返回 the squared 距离 在...之间 施法者 and the skilltree 触发器. If the 目标 不能 be found in the 施法者 世界, 返回 the maximum double 值 |


## Misc 占位符
| **占位符** | **Function** |
|-----------------------------|-------------------------------------------------------------------------|
| <掉落.数量> | 返回 the 数量 dropped 当 used in specific 掉落 类型 |
| <掉落.xp> | 返回 the xp dropped via specific 掉落 类型 |
| <掉落.money> | 返回 the money dropped 通过 vault plug-in |
| <random.#to#> | 返回 a random 整数 in the specified 范围 |
| <random.float.#to#> | 返回 a random float number in the specified 范围 |
| <utils.epoch> | 返回 the current epoch |
| <utils.epoch.seconds> | 返回 the current epoch |
| <utils.epoch.timestamp> | 返回 the 数量 of milliseconds elapsed 自纪元以来的 |
| <utils.epoch.millis> | 返回 the 数量 of milliseconds of the current epoch |
| <utils.epoch.ticks> | 返回 the current epoch, converted in ticks. Assumes that the 服务器 总是 maintains 20 ticks per second. Accounts for milliseconds. <br>While unorthodox, 自从 time 在...内 Minecraft (and by extension Mythic) is measured in ticks, this may be of some help streamlining some processes where converting the normal epoch time to accomodate for ticks may be burdensome if done at scale |

## 物品 占位符
| **占位符** | **Function** |
|-----------------------------|-------------------------------------------------------------------------|
| <物品.数量> | 返回 the 数量 of the 物品 that triggered the 技能 |
| <mythicitem.{MythicItem}.material>| 返回 the material of the specified mythic 物品 |
| <mythicitem.{MythicItem}.model> | 返回 the custommodeldata of the specified mythic 物品 |
| <mythicitem.{MythicItem}.显示> | 返回 the 显示 名称 of the specified mythic 物品 |
| <mythicitem.{MythicItem}.itemstack> | 返回 the itemstack of the specified mythic 物品 |

## 分数 占位符
| **占位符** | **Function** |
|-----------------------------|-------------------------------------------------------------------------|
| <施法者.分数.{Objective}> | 返回 the 分数 of the 施法者 from "{Objective}" |
| <目标.分数.{Objective}> | 返回 the 目标选择器 分数 from "{Objective}" |
| <触发器.分数.{Objective}> | 返回 the 分数 of the 触发器 from "{Objective}" |
| <global.分数.{Objective}> | 返回 the 分数 of fake 玩家: \_\_GLOBAL\_\_ 分数 from "{Objective}" |
| <分数.objective.玩家> | 返回 the 分数 of the defined 玩家 from "objective" |
| <分数.objective.dummyname> | 返回 the 分数 of "dummyname" (fake 玩家) from "objective" |

```yaml
  - message{m=You have slain <trigger.var.slainmobs> Mobs!} @trigger ~onInteract
```

## 变量 占位符
ThThese 占位符将返回whatever 变量 已被 called. For instance <施法者.var.\[名称\]> will 返回 the 值 of the 施法者 \[名称\] 变量。
SoSome of these 变量 are 仅 generated and available under some special circumstances, 例如 some specific 触发器/属性/metamechanic being used 之前 in the skilltree.

| 变量 占位符 | Generated by | Function |
|:-------------------------:|---------------------------------|------------------------------------------|
| <施法者.var.{VariableName}> | | 返回 the 值 of the 变量 {VariableName} on the 变量 registry of the 施法者 of the 技能 |
| <目标.var.{VariableName}> | | 返回 the 值 of the 变量 {VariableName} on the 变量 registry of the 目标 of the 技能 |
| <世界.var.{VariableName}> | | 返回 the 值 of the 变量 {VariableName} on the 变量 registry of the 世界 the 技能 is used in |
| <global.var.{VariableName}> | | 返回 the 值 of the 变量 {VariableName} on the 变量 registry of the whole 服务器 |
| <技能.var.{VariableName}> | | 返回 the 值 of the 变量 {VariableName} on the current [技能 树](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/技能/SkillTrees) |
| <技能.var.伤害-数量> | [~onDamaged] 触发器 <br> [~onAttack] 触发器 <br> [~onBowHit] 触发器 <br> [onDamaged] 技能 <br> [onAttack] 技能 | 返回 the 数量 of 伤害 taken or done |
| <技能.var.伤害-类型> | [~onDamaged] 触发器 <br> [~onAttack] 触发器 <br> [~onBowHit] 触发器 <br> [onDamaged] 技能 <br> [onAttack] 技能 | 返回 the 类型 of 伤害 taken or done, if any |
| <技能.var.伤害-cause> | [~onDamaged] 触发器 <br> [~onAttack] 触发器 <br> [~onBowHit] 触发器 <br> [onDamaged] 技能 <br> [onAttack] 技能 | 返回 the cause of 伤害 taken/done |
| <技能.var.光环-名称> | Every [光环] 技能 | 返回 the 名称 of the 光环 |
| <技能.var.光环-类型> | Every [光环] 技能 | 返回 the 类型 of the 光环 |
| <技能.var.光环-charges> | Every [光环] 技能 | 返回 the 数量 of charges the 光环 has left |
| <技能.var.光环-持续时间> | Every [光环] 技能 | 返回 the remaining 持续时间 of the 光环 |
| <技能.var.光环-持续时间-millis> | Every [光环] 技能 | 返回 the remaining 持续时间 of the 光环, in milliseconds |
| <技能.var.光环-堆叠> | Every [光环] 技能 | 返回 the 数量 of 堆叠 the 光环 has left |
| <技能.var.input> | [onChat] 技能 | 返回 the chat input |
| <技能.targets> | | 返回 the 数量 of inherited targets |
| <技能.var.间隔> | Using the `repeat` and `repeatInterval` [universal 属性] | 返回 the current iteration |
| <技能.var.itr> | Using the `repeat` and `repeatInterval` [universal 属性] | 返回 the current iteration |
| <技能.var.volume> | [~onHear] 触发器 | 返回 a float 值 between 1 and 15 representing the intensity of the sound. Directly proportional to the 距离 (the further away the source, the higher this 值) |
| <技能.var.sound-类型> | [~onHear] 触发器 | 返回 the 类型 of the sound |
| <技能.var.hit-方块-类型> | [raytrace] 技能 | 返回 the 方块 that was hit, or AIR if 没有 |
| <技能.var.bow-tension> | [~onShoot] 触发器 | 返回 the force with which the 弹射物 已被 shot |

```yaml
  Skills:
  - setvariable{var=caster.test1;val=1} @self
  - setvariable{var=target.test2;val=2} @self
  - message{m=<caster.var.test1> <caster.var.test2> <target.var.test1> <target.var.test2>} @self
```
> If you 执行 this 元技能 您自己, this will send you a 消息 saying `1 2 1 2` 因为 the 目标 of every 技能 is the 施法者, so the affected registry is 总是 the 施法者 即使 a "目标" 作用域 is used

### Meta 变量 占位符

You can append some keywords (that we will call "meta keywords"), each specific to a 变量 类型, at the end of a 变量 占位符 为了 修改 its 返回 值 and 类型.

```yaml
<{VariableScope}.var.{VariableName}.{keywords}>
```

Each keyword has an
- `Input Type`, 即 the 变量 类型 the keyword 应用 to
- `Output Type`, 即 the 变量 类型 that可以created从 keyword returned 值。

> 占位符支持is allowed in every place inside of 变量 占位符, so each keyword can 也 be 另一个 占位符 to be parsed。

##

```yaml
<skill.var.exampleString.capitalize>
```
> Among all keywords 对于 字符串 类型, we are using the `capitalize` one, which has as an output a 字符串 类型. This 意味着 that
> - It is applied to a 字符串 变量
> - It does some form of conversion to its 值 (在此情况下, capitalizing every character of the 字符串)
> - It 返回 a 字符串 值


```yaml
<skill.var.exampleString.size>
```
> Among all keywords 对于 字符串 类型, we are using the `size` one, which has as an output an 整数 类型. This 意味着 that
> - It is applied to a 字符串 变量
> - It does some form of conversion to its 值 (在此情况下, returning the length of the 字符串)
> - It 返回 an 整数 值

###

Given that each meta keyword has a specific input and output 类型, 可以 *chain* them 一起, obtaining a compound 效果 where each keyword coverts the 变量 值 and pass the 结果 to the following one

```yaml
<skill.var.exampleString.substring.0.9.size.add.1>
```
> Among all keywords 对于 字符串 类型, we are using the `substring` one, which has as an output a 字符串 类型. This 意味着 that
> - It is applied to a 字符串 变量
> - It does some form of conversion to its 值 (在此情况下, extracting the first 10 characters 从 字符串)
> - It 返回 a 字符串 值
>
> Among all keywords 对于 字符串 类型, we are using the `size` one, which has as an output an 整数 类型. This 意味着 that
> - It is applied to a 字符串 变量 (which the `substring` keyword 仅 returned)
> - It does some form of conversion to its 值 (In this case, returning the length of the 字符串, which we know 将 between 0 and 10)
> - It 返回 an 整数 值
>
> Among all keywords 对于 整数 类型, we are using the `add` one, which has as an output an 整数 类型. This 意味着 that
> - It is applied to an 整数 变量 (which the `size` keyword 仅 returned)
> - It does some form of conversion to its 值 (In this case, adding a 值 of 1 to the 整数 值)
> - It 返回 an 整数 值

#### Universal Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|----------|
| .cache | | Given the input 值 and the keywords used 之后 it, this keyword will cache the 结果 the first time the 占位符 is parsed, and directly 返回 the cached 值 each subsequent parsing |
| .formatted | 字符串 | 返回 a more human-readable version of the input 值 |
| .tointeger | 整数 | Converts the 值 to an 整数 没有 doing any specific operation, allowing chaining for 整数 meta keywords |
| .tofloat | FLOAT | Converts the 值 to a Float 没有 doing any specific operation, allowing chaining for Float meta keywords |
| .todouble | DOUBLE | Converts the 值 to a Double 没有 doing any specific operation, allowing chaining for Double meta keywords |
| .toboolean | 布尔值 | Converts the 值 to a 布尔值 没有 doing any specific operation, allowing chaining for 布尔值 meta keywords |
| .tostring | 字符串 | Converts the 值 to a 字符串 没有 doing any specific operation, allowing chaining for 字符串 meta keywords |
| .tolocation | 位置 | Converts the 值 to a 位置 没有 doing any specific operation, allowing chaining for 位置 meta keywords |
| .tovector | 向量 | Converts the 值 to a 向量 没有 doing any specific operation, allowing chaining for 向量 meta keywords |
| .tolist | 列表 | Converts the 值 to a 列表 没有 doing any specific operation, allowing chaining for 列表 meta keywords |
| .toset | SET | Converts the 值 to a Set 没有 doing any specific operation, allowing chaining for Set meta keywords |
| .tomap | MAP | Converts the 值 to a Map 没有 doing any specific operation, allowing chaining for Map meta keywords |
| .totime | TIME | Converts the 值 to a Time 没有 doing any specific operation, allowing chaining for Time meta keywords |
> > [Go To Explanation>>](#meta-变量-占位符)

#### 整数 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|----------|
| .添加.{整数} | 整数 | The addition 在...之间 值 and the specified 整数 |
| .sub.{整数} | 整数 | The subtraction 在...之间 值 and the specified 整数 |
| .mul.{整数} | 整数 | The multiplication 在...之间 值 and the specified 整数 |
| .div.{整数} | 整数 | The division 在...之间 值 and the specified 整数 |
| .abs | 整数 | The absolute 值 of the 值 |
> > [Go To Explanation>>](#meta-变量-占位符)

#### Float Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|----------|
| .添加.{Float} | FLOAT | The addition 在...之间 值 and the specified Float |
| .sub.{Float} | FLOAT | The subtraction 在...之间 值 and the specified Float |
| .mul.{Float} | FLOAT | The multiplication 在...之间 值 and the specified Float |
| .div.{Float} | FLOAT | The division 在...之间 值 and the specified Float |
| .abs | FLOAT | The absolute 值 of the 值 |
> > [Go To Explanation>>](#meta-变量-占位符)

#### Double Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|----------|
| .添加.{Double} | DOUBLE | The addition 在...之间 值 and the specified Double |
| .sub.{Double} | DOUBLE | The subtraction 在...之间 值 and the specified Double |
| .mul.{Double} | DOUBLE | The multiplication 在...之间 值 and the specified Double |
| .div.{Double} | DOUBLE | The division 在...之间 值 and the specified Double |
| .abs | DOUBLE | The absolute 值 of the 值 |
> > [Go To Explanation>>](#meta-变量-占位符)

#### 布尔值 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|----------|
| .inverse | 布尔值 | The inverse of the 值 |
| .number | 整数 | The 值 as 也 a 0 (false) or 1 (true) |
| .yesno | 字符串 | The 值 as 也 a no (false) or yes (true) |
| .union.{布尔值} | 布尔值 | Logical OR with specified 布尔值 |
| .intersection.{布尔值} | 布尔值 | Logical AND with specified 布尔值 |
| .difference.{布尔值} | 布尔值 | True if 值 is true and argument is false |
> > [Go To Explanation>>](#meta-变量-占位符)

#### 字符串 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .size | 整数 | The length of the 字符串 |
| .uppercase | 字符串 | The 字符串 in uppercase |
| .lowercase | 字符串 | The 字符串 in lowercase |
| .capitalize | 字符串 | The 字符串 与 first character in uppercase |
| .trim | 字符串 | The 字符串 with leading and trailing spaces removed |
| .replace.{old}.{new} | 字符串 | The 字符串 with occurrences of `old` replaced by `new` |
| .移除.{text} | 字符串 | The 字符串 with occurrences of `text` removed |
| .包含.{text} | 布尔值 | Whether the 字符串 包含 `text` |
| .substring.{start}.{end} | 字符串 | A substring from index `start` to `end` |
| .shift.{整数} | 字符串 | 移除 the first `Integer` characters |
| .split.{regex}.{joiner} | 字符串 | Splits the 字符串 by `regex`, then joins it with `joiner` |
| .indexof.{text} | 整数 | The index of the first occurrence of `text` |
| .lastindexof.{text} | 整数 | The index of the last occurrence of `text` |
| .startswith.{text} | 布尔值 | Whether the 字符串 starts with `text` |
| .endswith.{text} | 布尔值 | Whether the 字符串 ends with `text` |
| .append.{text} | 字符串 | Appends `text` to the end of the 字符串 |
| .prepend.{text} | 字符串 | Prepends `text` to the beginning of the 字符串 |
| .insert.{index}.{text} | 字符串 | Inserts `text` at the specified `index` |
| .regex.{pattern} | 布尔值 | Whether the 字符串 匹配 the regex `pattern` |
| .{index} | 字符串 | 返回 the character at the specified `index` |
> > [Go To Explanation>>](#meta-变量-占位符)

#### Set Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .size | 整数 | The number of elements in the set |
| .join.{delimiter} | 字符串 | Joins all elements using the `delimiter` |
| .包含.{element} | 布尔值 | Whether the set 包含 the given `element` |
> > [Go To Explanation>>](#meta-变量-占位符)

#### 位置 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .x | DOUBLE | The X coordinate |
| .y | DOUBLE | The Y coordinate |
| .z | DOUBLE | The Z coordinate |
| .世界 | 字符串 | The 世界 名称 |
| .yaw | DOUBLE | The yaw |
| .pitch | DOUBLE | The pitch |
| .coords | 列表 | A 列表 与 X, Y, and Z coordinates |
> > [Go To Explanation>>](#meta-变量-占位符)

#### 向量 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .x | DOUBLE | The X component |
| .y | DOUBLE | The Y component |
| .z | DOUBLE | The Z component |
| .normalized | 向量 | The normalized 向量 |
| .length | DOUBLE | The length (magnitude) of the 向量 |
| .mul.{向量} | 向量 | Multiplies the 向量 by 另一个 向量 |
| .div.{向量} | 向量 | Divides the 向量 by 另一个 向量 |
| .添加.{向量} | 向量 | 添加 另一个 向量 |
| .sub.{向量} | 向量 | Subtracts 另一个 向量 |
| .rotate.{axis}.{角度} | 向量 | Rotates the 向量 around `axis` by `angle` radians |
> > [Go To Explanation>>](#meta-变量-占位符)

#### 列表 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .size | 整数 | Number of elements in the 列表 |
| .first | 字符串 | First element in the 列表 |
| .last | 字符串 | Last element in the 列表 |
| .reverse | 列表 | The 列表 reversed |
| .sort | 列表 | The 列表 sorted alphabetically |
| .sortnum | 列表 | This 列表 sorted numerically. Each element of the 列表 需要 be a number |
| .shuffle | 列表 | Shuffles the 列表, randomizing its elements |
| .get.{index} | 字符串 | Element at specified `index` |
| .join.{delimiter} | 字符串 | Joins elements using `delimiter` |
| .包含.{element} | 布尔值 | Whether the 列表 包含 `element` |
| .maxnumber | DOUBLE | Maximum numerical 值 in 列表 |
| .minnumber | DOUBLE | Minimum numerical 值 in 列表 |
| .indexof.{值} | 整数 | Index of first occurrence of `value` |
| .lastindexof.{值} | 整数 | Index of last occurrence of `value` |
| .slice.{from}.{to} | 列表 | Slice of 列表 from `from` to `to` |
| .slicefrom.{index} | 列表 | Slice of 列表 from `index` to end |
| .sliceto.{index} | 列表 | Slice of 列表 from start to `index` |
| .append.{值} | 列表 | 添加 `value` to the end of the 列表 |
| .prepend.{值} | 列表 | 添加 `value` to the start of the 列表 |
| .insert.{index}.{值} | 列表 | Inserts `value` at the given `index` |
| .移除.{index} | 列表 | 移除 值 at given `index` |
| .{index} | 字符串 | Element at specified `index` |
> > [Go To Explanation>>](#meta-变量-占位符)

#### Map Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .size | 整数 | Number of 键值对 |
| .keys | 列表 | 列表 of all keys |
| .值 | 列表 | 列表 of all 值 |
| .get.{key} | 字符串 | 值 关联 the specified `key` |
| .{key} | 字符串 | 值 关联 the specified `key` |
> > [Go To Explanation>>](#meta-变量-占位符)

#### Time Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|--------------|-------------|--------------|
| .delta.{timestamp} | 整数 | Difference 在...之间 值 time and the and given `timestamp` |
| .formatted.{pattern} | 字符串 | Formatted date/time using the specified pattern. The pattern can be 任何事物 the Java function [ZoneOffset.of](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneOffset.html#of-java.lang.字符串-) accepts |
| .持续时间 | 字符串 | Interprets the Time as a raw "数量 of milliseconds" and displays the total 数量 of Seconds, Minutes, Hours, Days, Months and Years. Can be useful for countdowns and the likes, 尤其 if paired 与 `.delta` meta keywords|
> > [Go To Explanation>>](#meta-变量-占位符)

###### 物品 Meta Keywords
| 占位符 | 返回类型 | 返回 值 |
|-------------|-------------|--------------|
| .withType.{material} | 物品 | 返回 the same 物品 但具有 its 类型 set to the specified `material` (case-insensitive, must 匹配 a valid `Material` enum) |
| .withDurability.{值} | 物品 | 返回 the same 物品 但具有 its durability set to the specified 整数 `value` |
| .withMaxDurability.{值} | 物品 | 返回 the same 物品 但具有 its maximum durability set to the specified 整数 `value` |
| .withLore.{列表} | 物品 | 返回 the same 物品 但具有 its 物品描述 set to the specified 列表 of strings. |
| .withName.{名称} | 物品 | 返回 the same 物品 但具有 its 显示 名称 set to `name` |
| .withMythicType.{类型} | 物品 | 返回 the same 物品 但具有 its persistent "Mythic 类型" set to `type`, allowing you to make Mythic believe the modified 物品 is the `type` mythic 物品 |
| .withEnchants.{map} | 物品 | 返回 the same 物品 但具有 附魔 replaced by those provided in the map. 移除 all previous 附魔 之前 applying the new ones |
| .withCustomData.{namespace}.{key}.{值} | 物品 | 返回 the same 物品 但具有 自定义 persistent data (`value` stored under `namespace:key`) |
| .withAmount.{值} | 物品 | 返回 the same 物品 但具有 its 堆叠 数量 set to `value` |
| .withUUID.{uuid} | 物品 | 返回 the same 物品 但具有 its UUID nbt set to the specified 值 |
| .withTimestamp.{timestamp} | 物品 | 返回 the same 物品 但具有 its timestamp nbt set to the specified 整数 值 |
| .withCustomModelData.{值} | 物品 | 返回 the same 物品 但具有 its 自定义 Model Data set to `value` |
| .withModel.{namespace}.{path} | 物品 | 返回 the same 物品 但具有 its 物品 model set to `{namespace}:{path}` |
| .类型 | 字符串 | The 物品 类型 as a 字符串 (Material 名称) |
| .durability | 整数 | The current durability 值 of the 物品 |
| .maxDurability | 整数 | The maximum durability 值 of the 物品 |
| .物品描述 | 列表 | The 物品 物品描述 as 一系列 strings |
| .名称 | 字符串 | The 显示 名称 of the 物品 |
| .mythicType | 字符串 | The persistent "Mythic 类型" 值 of the 物品, if set |
| .enchants | MAP | A map of all 附魔 on the 物品 |
| .getCustomData.{namespace}.{key} | 字符串 | The 字符串 值 stored in the 物品 自定义 persistent data under `{namespace}:{key}` |
| .customModelData | 整数 | The 物品 自定义 Model Data 值 |
| .model | 字符串 | The 物品 model identifier in `namespace:path` 格式 |
| .数量 | 整数 | The 堆叠 数量 of the 物品 |
> > [Go To Explanation>>](#meta-变量-占位符)


# 占位符 属性
Some 占位符 can use 一组 属性 to further define the output 它们将 give

| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| rounding | round, r | The rounding of the returned float 值 | 2 |

```yaml
  Skills:
  - message{m="<target.hp{round=2}>"} @self
```


# PlaceholderAPI Integration
Other than being able to use PlaceholderAPI 占位符 任何地方 占位符 支持 is in place, MythicMobs introduces some new PAPI 占位符 that可以usedby third parties to fetch MythicMobs-related 值。
| **PAPI 占位符** | **Function** |
|-----------------------------|-------------------------------------------------------------------------|
| %mythic_var_someVar% | 返回 the 值 of the `someVar` 变量 即 set on the 玩家 |
| %mythic_var_world_someVar% | 返回 the 值 of the `someVar` 变量 即 set on the 世界 |
| %mythic_var_global_someVar% | 返回 the 值 of the `someVar` 变量 即 set on the 服务器 |
| %mythic_var_\<playerName\>_someVar% | 返回 the 值 of the `someVar` 变量 即 set on the specified 玩家, by their 名称 |
| %mythic_var_\<UUID\>_someVar% | 返回 the 值 of the `someVar` 变量 即 set on the specified 实体, by its UUID|
| %mythic_spawner_[名称]_cooldown% | 返回 the 冷却 of the 生成器 called `name` |
| %mythic_spawner_[名称]_cooldownleft% | 返回 the remaining 冷却 of the 生成器 called `name` |
| %mythic_spawner_[名称]_warmup% | 返回 the warmup of the 生成器 called `name` |
| %mythic_spawner_[名称]_warmupleft% | 返回 the remaining warmup of the 生成器 called `name` |
| %mythic_stat_[名称]% | 返回 the 值 of the specified stat on the evaluated 玩家 |

## PlaceholderAPI Parsing
WhWhen using 占位符 via PlaceholderAPI, 它是 important to remember that some of them are meant to be parsed 再次st a 玩家, and if parsed 再次st a 生物 they may behave unexpectedly.
MoMore concretely, 这意味着 that:
- - If used inside a 技能, the 目标 必须为 a 玩家
- - If used inside a 条件, the checked 实体 必须为 a 玩家 (施法者 for 条件, inherited targets for targetconditions, 触发器 for triggerconditions)

.....and so on

# 自定义 占位符
It possible to create 自定义 占位符 in any 包 by creating a 文件 named `placeholders.yml` in the 包 directory. These can be static or 您可以 define conditional 占位符 - the first one that evaluates true 将 chosen, or the `Default` if 它们是 all false.

Cu自定义 占位符可以usedvia `<placeholder.[CustomPlaceholder]>`, with _[CustomPlaceholder]_ being the 名称 of your 自定义 占位符。

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
> A 值 of "null" 不是 accepted


# 示例
**This will make a 生物 send a teal 消息 to all 玩家 in a 半径 of 20 方块 around in 自身, stating what 实体 killed it in green.**

```yaml
    Skills:
    - message{m="<&b><caster.name><&r> was slain by <&a><trigger.name><&r>."} @PIR{r=20} ~onDeath
```

**This 技能 will make an announcement when the 生物 spawns that looks like this:**

![image](uploads/91ed6d8aaa669e8ae21f8745e8ff4643/image.png)

```yaml
  Skills:
  - Skill{s=SaveBossLocation} @self ~onSpawn
  - message{m="&eA &BGiant Zombie&e (Level &4<caster.level>&e) &ehas spawned at <caster.var.SpawnLoc>"} ~onSpawn @PlayersInWorld
  - message{m="&eThe &BGiant Zombie&e (Level &4<caster.level>&e) &espawned at <caster.var.SpawnLoc>&e has been slain."} ~onDeath @PlayersInWorld
```

Be sure to place this 技能 某处 in the 技能 文件

```yaml
SaveBossLocation:
  Skills:
  - setvariable{var=SpawnLoc;type=STRING;value="&b<caster.l.x>&e, &b<caster.l.y>&e, &b<caster.l.z>";scope=CASTER} @self
```
**You can 也 use color tags and formatting tags to make the 生物 have pretty 名称:**

![image](uploads/9ad97422803c3f35fbeac2e4df7f7d52/image.png)

```yaml
ZOMBIE:
  Display: 'ZOMBIE &F- &A<caster.hp>/<caster.mhp>HP &F- &ELv.<caster.level>'
```


<!-- LINKS -->
[~onHear]: /技能/触发器/onHear
[~onDamaged]: /技能/触发器/onDamaged
[~onAttack]: /技能/触发器/onAttack
[~onBowHit]: /技能/触发器/onBowHit
[~onShoot]: /技能/触发器/onShoot
[onChat]: /技能/技能/onChat
[光环]: /技能/技能/光环
[raytrace]: /技能/技能/raytrace
[raytraceto]: /技能/技能/raytraceto
[onDamaged]: /技能/技能/onDamaged
[onAttack]: /技能/技能/onAttack
[universal 属性]: /技能/技能#universal-属性