## 描述
Adds an amount to a [variable](/skills/variables) on the specified
scope.

> This 技能 has different behavior based on the variable type. [More Info Here](/Skills/Variables#variable-types-behavior)


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a, value, val, v  | The value to add                                             | 0       |
> This 技能 inherits every *inheritable* attribute of the [SetVariable](skills/mechanics/setvariable) 技能


## 示例
```yaml
  Skills:
  - variableadd{var=skill.testVar;amount=1} ~onInteract
```


## 别名
- [x] addVariable
- [x] varAdd
- [x] addVar
- [x] incrementVariable


<!--TAGS-->
<!--tag:Variable-->
