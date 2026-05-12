## 描述
检查给定变量是否包含特定值。
- 对于字符串变量，检查变量是否包含某个子串。根据使用的 compareType，还可以检查变量是否「以给定值开头」或「以给定值结尾」。
- 对于列表或集合变量
  - 如果值是简单字符串，则检查列表或集合是否包含该值
  - 如果条目是另一个列表或集合，则根据 compareType 检查变量是否包含值的全部或任意元素。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| variable  | name, n, var, key, k | 变量的名称。可选地可以加上作用域前缀|    |
| scope| s| 变量的[作用域](/Skills/Variables#variable-scopes)，即变量所在位置                                                                                        |<!--type:VariableScope-->|
| compareType | compare, comp | 要使用的比较类型。可以是 `ALL`、`ANY`、`STARTS_WITH` 或 `ENDS_WITH`。 | ALL |
| value     | val, v    | 比较的值                                          |         |

### CompareType 属性
如果变量是字符串，可以使用 `STARTS_WITH` 或 `ENDS_WITH` 检查变量是否以给定值开头或结尾。

如果变量是列表或集合且值也是列表或集合，可以使用 `ALL` 检查值的所有元素是否都存在于变量中，或使用 `ANY` 检查是否至少存在一个元素。


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