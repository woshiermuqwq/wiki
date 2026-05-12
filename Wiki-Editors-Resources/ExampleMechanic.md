## 描述
技能的描述：它做什么、如何运作，以及可能的注意事项。

> **这是一个 [Paper 专属] 技能！**

> **这是一个 [Premium 专属] 技能！**

> **这是一个无目标技能，受影响的实体将始终是施法者**

| [已实现的占位符]     |
|--------------------------------|
| `<skill.var.example1>`         |
| `<skill.var.example2>`         |

## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| attribute1| alias1, alias2| 描述该属性做什么                 | 默认值|
| attribute2| alias3    | 描述该属性做什么                     | 默认值|
| attribute3|           | 描述该属性做什么                     | 默认值|
| attribute4|           |描述该属性做什么 **<[Premium 专属]>**|默认值|
<!-- 可选，如果存在属性继承 -->
> 此技能继承 [ExampleMechanic2](/Skills/Mechanics/ExampleMechanic2) 技能的每一个*可继承*属性
>> - `attribute4` 属性的**默认值**为 `0`
>> - `attribute5` 属性被**固定**为 `0` 且无法修改
<!-- 如果继承属性的默认值被修改 -->
<!-- 仅当有多个元素时才使用列表 -->

<!-- 如果技能没有任何属性 -->
> *此技能无属性*

### Attribute1 属性
对属性功能、运作方式、接受的取值等进行更深入的说明。可选，仅在必要时提供。

## 示例
下方示例的说明。
```yaml
  Skills:
  - examplemechanic{attribute1=value1} @targeter
```
## <!-- 使用 ## 来分隔不同示例 -->
另一个示例：
```yaml
  Skills:
  - examplemechanic{attribute1=value1;attribute2=value2} @targeter
```

## 别名
- [x] mechanic_alias_1
- [x] mechanic_alias_2

<!-- LINKS -->
[Paper-Only]: https://papermc.io/downloads/all
[Premium-Only]: Premium-Features
[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders
