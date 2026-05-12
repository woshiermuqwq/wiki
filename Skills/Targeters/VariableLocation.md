## 描述
Targets the 位置 stored in the specified 变量. One such 变量可以setvia the [SetVariableLocation](/技能/机制/setvariablelocation) 机制。

## 属性

| 属性 | 别名 | Description | 默认 |
|----------------|----------|------------------------------------------------------------|:-------:|
| 变量 | 名称, n, var, key, k | The 名称 of the 变量. | |
| 作用域 | s | The 作用域 of the 变量. Can optionally be set in the 名称, using the 作用域.名称 syntax | |

## 示例
```yaml
ExampleSkill:
  Skills:
  - setvarloc{var=caster.1;v=@targetlocation} @self
  - particle{y=2} @VariableLocation{var=caster.1}
```

## 别名
- [x] varLocation