MythicMobs 包含许多不同的功能和术语，学习这些很重要。本页面简要描述了你在制作生物时可能遇到的所有不同概念。

## 生物（Mobs）
[生物 Wiki](/Mobs/Mobs)

正如插件名称所示，生物是 MythicMobs 最重要、最核心的组成部分。

### 选项（Options）
[生物选项 Wiki](/Mobs/Options)

生物选项允许你更改生物的各种设置。不是所有生物都能使用所有选项，请查看 Wiki 页面了解不同生物类型可使用哪些选项。

### 自定义 AI（Custom AI）
[自定义 AI Wiki](/Mobs/Custom-AI)

自定义 AI 让你能够改变生物默认行为方式。你可以让它们选择不同的目标，并以不同方式对待它们。自定义 AI 由两个选择器组成：Goals（目标）和 Targets（目标选择器）。

Goals：决定生物做什么，例如躲避玩家、在水面浮游和攻击等。

Targets：决定生物以谁或什么为目标，例如玩家和其他生物。

## 机制（Mechanics）
[机制 Wiki](/Skills/Mechanics)

机制是为你的生物添加有趣且独特能力的主要方式。最基本的使用方式是将机制添加到生物的 Skills 部分，并配合触发器和目标选择器，但也可以将其添加到元技能中。大多数机制都有可使用的属性列表，用于修改其工作方式。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

## 目标选择器（Targeters）
[目标选择器 Wiki](/Skills/Targeters)

目标选择器告诉机制以谁为目标。例如，如果你使用 giveitem 机制，目标选择器将决定把物品给谁。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

## 触发器（Triggers）
[触发器 Wiki](/Skills/Triggers)

触发器告诉生物何时激活其机制和能力。触发器必须以 `~` 开头，并放在目标选择器之后。触发器只能直接写在生物上，写在元技能中将不起作用。示例中，`~onTimer:20` 是触发器，告诉机制每 20 ticks（1 秒）运行一次。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`


## 条件（Conditions）
[条件 Wiki](/Skills/Conditions)

条件允许你限制事物的执行方式。你可以在任何使用条件的地方进行内联条件或使用 conditions 部分。


## 属性（Attributes）
属性是你可以传递给机制/目标选择器/条件的信息，用于自定义其工作方式。在此示例中，`cd=10` 和 `i=DIAMOND` 是属性，告诉机制要给予什么物品以及冷却时间为 10 秒。属性使用 `;` 符号分隔，且必须在你设置的值之前加上 `=`。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

<details><summary>属性表</summary>
在每个机制的 Wiki 页面中，你会看到一个表格，列出了所有可用的属性（如有）及相关信息。
例如：

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 属性1| 别名1, 别名2| 描述该属性做什么                 | 默认值|
| 属性2| 别名3    | 描述该属性做什么                     | 默认值|
| 属性3|           | 描述该属性做什么                     | 默认值|

这告诉你该机制有 3 个不同属性：`属性1`、`属性2` 和 `属性3`。每个属性都有对应的功能描述和一个"默认值"，如果未显式指定，将应用默认值。有些属性还有"别名"，就是你设置同一属性时可以使用的不同名称。
</details>

<details><summary>属性继承</summary>
有时你会在属性部分看到*类似*这样的文字：

> 此机制继承 [Damage](/Skills/Mechanics/Damage) 机制的每一个*可继承*属性

这意味着除了 Wiki 页面本身的属性外，所指示机制中的属性也会被使用（除非标记为"不可继承"）。例如，用作示例的 Damage 机制只有一个不可继承的属性（`amount`），而其他所有属性都被继承。
</details>


## 元技能（MetaSkills）
[元技能 Wiki](/Skills/Metaskills)

技能是 MythicMobs 的基本功能，它让你能够将多个机制组合成一个，使你能够创建带有多种效果和视觉表现的有趣攻击和功能。

## 物品（Items）
[物品 Wiki](/Items/Items)

MythicMobs 能够创建基础的自定义物品，可供生物使用或给予玩家。如果你拥有 [MythicCrucible](https://mythiccraft.io/index.php?resources/crucible-custom-items-armor-furniture-blocks-more.2/) 扩展插件，可以进一步扩展这些物品。

## 随机生成（RandomSpawns）
[随机生成 Wiki](/Random-Spawns)

RandomSpawns 用于让你的生物在世界中自然生成，无需指令或生成器。你可以添加条件来决定它们何时生成。

## 生成器（Spawners）
[生成器 Wiki](/Spawners)

生成器可用于在固定位置周期性生成生物。这在地下城或 RPG 地图中非常有用。

请注意：生成器文件在服务器运行期间无法编辑，你必须停止服务器才能编辑文件。可以使用游戏内指令代替。

## 变量（Variables）
[变量 Wiki](/Skills/Variables)

变量是一个用于存储信息的便捷系统。之后你可以在各种其他地方使用这些信息，例如机制和条件中的占位符。

## 占位符（Placeholders）
[占位符 Wiki](/Skills/Placeholders)

占位符用于显示/获取实体、位置或元技能的信息。例如，`<caster.hp>` 占位符可以用来获取施法实体的生命值。

**[>> 第二步](/Guides/(Step-2)-Files-And-Directories)**
