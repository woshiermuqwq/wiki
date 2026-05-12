## 描述
技能的描述：它做什么、如何工作以及可能的注意事项。

> **这是 [Paper 专属] 技能！**

> **这是 [Premium 专属] 技能！**

> **这是无目标技能，受影响的实体将始终是施法者**

| [已实现的占位符]     |
|--------------------------------|
| `<skill.var.example1>`         |
| `<skill.var.example2>`         |

## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 属性1| 别名1, 别名2| 描述该属性做什么                 | 默认值|
| 属性2| 别名3    | 描述该属性做什么                     | 默认值|
| 属性3|           | 描述该属性做什么                     | 默认值|
| 属性4|           |描述该属性做什么 **<[Premium 专属]>**|默认值|
<!-- 可选，如果有属性继承 -->
> 此技能继承 [ExampleMechanic2](/Skills/Mechanics/ExampleMechanic2) 技能的每一个*可继承*属性
>> - `属性4` 属性的**默认值**为 `0`
>> - `属性5` 属性被**固定**在 `0` 且无法修改
<!-- 如果继承属性的默认值被修改 -->
<!-- 仅当有多个元素时才使用列表 -->

<!-- 如果技能没有任何属性 -->
> *此技能无属性*

### 属性1 详解
对该属性更深入的解释：它做什么、如何工作、接受哪些值等。可选，仅在需要时提供。


## 示例
下方示例的描述。
```yaml
  Skills:
  - examplemechanic{attribute1=value1} @targeter
```
## <!-- 使用 ## 分隔不同示例 -->
另一个示例：
```yaml
  Skills:
  - examplemechanic{attribute1=value1;attribute2=value2} @targeter
```


## 别名
- [x] mechanic_alias_1
- [x] mechanic_alias_2

<!-- LINKS -->
[Paper 专属]: https://papermc.io/downloads/all
[Premium 专属]: Premium-Features
[已实现的占位符]: /Skills/Placeholders#variable-placeholders
