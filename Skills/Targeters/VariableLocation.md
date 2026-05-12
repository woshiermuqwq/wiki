## 描述
选取指定变量中存储的位置。此类变量可通过 [SetVariableLocation](/skills/mechanics/setvariablelocation) 技能设置。

## 属性

| 属性      | 别名  | 描述                                                | 默认值 |
|----------------|----------|------------------------------------------------------------|:-------:|
| variable       | name, n, var, key, k | 变量名称                      |         |
| scope          | s        | 变量的作用域。也可在名称中使用 `scope.name` 语法设置                                                                        |         |

## 示例
```yaml
ExampleSkill:
  Skills:
  - setvarloc{var=caster.1;v=@targetlocation} @self
  - particle{y=2} @VariableLocation{var=caster.1}
```

## 别名
- [x] varLocation
