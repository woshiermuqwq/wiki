在本页面中，你可以找到关于当前各页面文档编写语法的较完整总结。如果某些内容没有被记录，请咨询正确的语法应该是什么。

在每个页面中，你可以查看嵌入在页面 markdown 内部的注释来获取进一步的说明。你可以通过"编辑"页面来查看它们。

## 通用规则
- 每个"章节"（以 `## 标题` 定义的章节）之间应始终留两个空行（即按两次回车产生的字符）。
- 使用超链接时，应始终注意 `/wiki/` 路径是起始路径，因此可以像下面这样制作相对路径：
`[ExampleMechanic](Wiki-Editors-Resources/ExampleMechanic)`
因此，如果资源在 wiki 本身上，请务必使用此方法。

## 嵌入数据
Wiki 中以 HTML 注释形式存在一些嵌入数据。这些数据用于构建 wiki 的数据集，因此重要的是在编辑时务必小心处理。

### 属性数据
这些添加在任意属性的默认值字段中。
可以嵌入两种类型的数据，它们可以一起使用并以任意顺序放置。只要它们*在*那里某处就行。

这也适用于不在任何特定技能内的通用属性。

`| type      | types, t  | 要匹配的实体类型列表           |<!--type:EntityType--><!--list--> |`

#### 类型
如果使用此项，属性值将只能来自特定的枚举（例如 Material 或 BarStyle 等，仅举几例）。

为此，[可以在此处找到有效类型列表](https://github.com/Lxlp38/MythicScribe/blob/master/generated/enumList/enumList.md)，且可以使用任意大小写。

#### 列表
如果使用此项，将声明属性值可以是逗号分隔的元素列表。
如果与 `type` 一起使用，每个元素必须来自同一枚举。

### 触发器数据
触发器可以在页面的任意位置包含以下任一注释（最好放在 `## 描述` 之前）。

- `MobTrigger` 表示仅供生物使用的触发器
- `PlayerTrigger` 表示所有玩家都可以激活的触发器
- `ItemTrigger` 表示专门用于物品的触发器
- `ArchetypeTrigger` 表示需要配合使用的触发器

`<!--type:PlayerTrigger-->`

如果未指定任何类型，触发器将被视为"通用"，因此可以在多个地方使用。如果不确定，就保持原样。

### 目标选择器通用属性数据
决定目标选择器的一系列通用属性是实体类还是位置类。

实际上来说，你永远不需要修改此项。

通过在属性表头中放置注释来设置：

`| Attribute <!-- ETA --> | Aliases   | Description                                           | Default |`

值可以是 ETA（实体类）或 LTA（位置类）。

## 示例页面
- [技能 Wiki 页面](Wiki-Editors-Resources/ExampleMechanic)
- [目标选择器 Wiki 页面](Wiki-Editors-Resources/ExampleMechanic "使用与技能页面相同的语法")
- [条件 Wiki 页面](Wiki-Editors-Resources/ExampleMechanic "使用与技能页面相同的语法")

## [测试页面](Wiki-Editors-Resources/Test-Page)

## 快速复制粘贴
```
## Attributes
| Attribute | Aliases   | Description                                                          | Default |
|-----------|-----------|----------------------------------------------------------------------|---------|
```
```
## Aliases
- [x] alias1
- [x] alias2
```
```
> **这是一个 [Paper 专属] 技能！**

> **这是一个 [Premium 专属] 技能！**

**<[Premium 专属]>**
```
```
<!-- LINKS -->
[metaskill]: /Skills/Metaskills
[mechanic]: /Skills/Mechanics
[targeter]: /Skills/Targeters
[trigger]: /Skills/Triggers
[condition]: /Skills/Conditions
[origin]: /Skills/Targeters/Origin
[audience]: /Skills/Audience

[Paper-Only]: https://papermc.io/downloads/all
[Premium-Only]: Premium-Features

[material]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html

[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders
```
