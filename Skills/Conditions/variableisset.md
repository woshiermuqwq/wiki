## 描述
检测给定的[变量](/Skills/Variables)是否已被设置。

## 属性
| 属性       | 别名                      | 描述                                            | 默认值          |
| ---------- | ------------------------- | ----------------------------------------------- | --------------- |
| variable   | name, n, var, key, k      | 变量名称。可选地加上作用域前缀                    |                 |
| scope      | s                         | 变量的[作用域](/Skills/Variables#variable-scopes) |<!--type:VariableScope--> |


## 示例
```yaml
  Conditions:
  - variableisset{var=target.dazed} true
```

## 别名
- [x] varisset
- [x] varset
