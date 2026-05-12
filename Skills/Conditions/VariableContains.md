## 描述
检测给定变量是否包含某个值。
- 对于字符串变量，检测变量是否包含子串。根据使用的 compareType，还可以检测变量是否「以……开头」或「以……结尾」。
- 对于列表或集合变量：
  - 如果值是简单字符串，检测列表/集合是否包含该值
  - 如果值本身也是列表或集合，根据 compareType 检测变量是否包含值的「全部」或「任一」元素

## 属性
| 属性         | 别名                      | 描述                                                      | 默认值          |
| ------------ | ------------------------- | --------------------------------------------------------- | --------------- |
| variable     | name, n, var, key, k      | 变量名称。可选地加上作用域前缀                              |                 |
| scope        | s                         | 变量的[作用域](/Skills/Variables#variable-scopes)           |<!--type:VariableScope--> |
| compareType  | compare, comp             | 比较类型。可为 `ALL`、`ANY`、`STARTS_WITH` 或 `ENDS_WITH`    | ALL             |
| value        | val, v                    | 要比较的值                                                  |                 |

### CompareType 属性
如果变量是字符串，可以使用 `STARTS_WITH` 或 `ENDS_WITH` 来检测变量是否以给定值开头或结尾。

如果变量是列表/集合且值也是列表/集合，使用 `ALL` 检测值的所有元素是否都存在于变量中，使用 `ANY` 检测至少有一个元素存在。

## 示例
```yaml
  Conditions:
  - variablecontains{var=skill.examplelist;val=hello}

  - variablecontains{var=skill.examplelist;val=hello,world;compareType=ANY}

  - variablecontains{var=skill.examplestring;val=pizza}

  - variablecontains{var=skill.examplestring;val=dungeon_;compareType=STARTS_WITH}
```

## 别名
- [x] variableContain
- [x] varContains
- [x] varContain
- [x] varCont
