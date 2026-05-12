## 描述
检查给定[变量](/Skills/Variables)是否已设置。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| variable  | name, n, var, key, k | 变量的名称。可选地可以加上作用域前缀|    |
| scope     | s         | 变量的[作用域](/Skills/Variables#variable-scopes)，即变量所在位置                                                                            |<!--type:VariableScope-->|


## 示例
```yaml
  Conditions:
  - variableisset{var=target.dazed} true
```


## 别名
- [x] varisset
- [x] varset