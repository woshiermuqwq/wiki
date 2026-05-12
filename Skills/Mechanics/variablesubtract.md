## 描述
Subtracts an amount to a [variable](/skills/variables) on the specified
scope.

> This 技能 has different behavior based on the variable type. [More Info Here](/Skills/Variables#variable-types-behavior)


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a, value, val, v  | The value to subtract                                       | 0       |
> This 技能 inherits every *inheritable* attribute of the [SetVariable](skills/技能/setvariable) 技能


## 示例
```yaml
  Skills:
  - variablesubtract{var=skill.testVar;amount=1} ~onInteract
```


## 别名
- [x] variableSub
- [x] subtractVariable
- [x] subVar
- [x] reduceVariable


<!--TAGS-->
<!--tag:Variable-->