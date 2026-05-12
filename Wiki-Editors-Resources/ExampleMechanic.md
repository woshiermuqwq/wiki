## 描述
The description of the 技能: what 它会, how 它会 it, and possible 注意.

> **This is a [Paper-Only] 技能!**

> **This is a [Premium-Only] 技能!**

> **This is a no-目标 技能, and the affected 实体 总会 be the 施法者**

| [Implemented 占位符] |
|--------------------------------|
| `<skill.var.example1>` |
| `<skill.var.example2>` |

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| attribute1| alias1, alias2| The description of what the 属性 does | 默认 值|
| attribute2| alias3 | The description of what the 属性 does | 默认 值|
| attribute3| | The description of what the 属性 does | 默认 值|
| attribute4|The description of what the 属性 does **<[Premium-Only]>**|默认 值|
<!-- Optional, if an inheritance is in place -->
> This 技能 继承 every *inheritable* 属性 of the [ExampleMechanic2](/技能/技能/ExampleMechanic2) 技能
>> - The `attribute4` 属性 is **defaulted** at `0`
>> - The `attribute5` 属性 is **set** at `0` and 不能 be modified
<!-- If inherited attributes have their default value changed -->
<!-- Use a list only if more than one element is present -->

<!-- If the mechanic does not have any attributes-->
> *This 技能 has no 属性*

### Attribute1 属性
what the 属性 does, how 它会 it, what 值 are accepted and so on. 可选, 仅 if necessary的more in-depth explanation。


## 示例
the 示例 below的description。
```yaml
  Skills:
  - examplemechanic{attribute1=value1} @targeter
```
## <!-- Use ## to separate different 示例 -->
An其他 示例:
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
[Implemented 占位符]: /技能/占位符#变量-占位符