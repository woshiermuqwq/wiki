## 描述
基于指定操作比较两个值。  
比较是将 `value1` 对照 `value2` 进行的：这意味着，例如，在 `>` 操作中，如果 `value1` 大于 `value2`，将返回 `true`。  

此条件可以比较整数、浮点数、双精度浮点数（如同常规使用）和字符串（按字典顺序）。  

条件将尝试「推断」所给值的类型，并先尝试最严格的类型进行比较，逐级尝试更宽松的比较，直到找到适用的类型（整数 --> 双精度浮点数 --> 字符串）。

如果你已经知道传入值的类型，可以通过 `type` 属性指定，这样只会进行该特定类型的比较，无需浪费时间和尝试。如果因为值转换问题仍无法进行比较，条件将返回 false。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| value1 | val1, v1 | 比较的第一个值                                        |         |
| value2 | val2, v2 | 比较的第二个值                                       |         |
| operator | op     | 要使用的[运算符](#运算符属性)                                                      | EQUALS<!--type:CompareValues_Operator-->|
| type   | t        | （可选）比较的类型。如果未设置，将尝试从最严格到最宽松的所有可用类型。如果设置，比较将假定值的类型为指定类型。接受任何[变量类型](/Skills/Variables#variable-types)| <!--type:VariableType-->|


### 运算符属性
| 运算符 | 别名 |
|----------|---------|
| `==`     | `EQUALS`, `EQUAL`, `EQ`, `EQL` |
| `!=`     | `NOT_EQUALS`, `NOTEQUALS`, `NOTEQUAL`, `NE`, `NEQ`, `NEQL` |
| `>`      | `GREATERTHAN`, `GREATER_THAN`, `GTR`, `GT` |
| `<`      | `LT`, `LESSTHAN`, `LTR`, `LESS_THAN` |
| `>=`     | `GTE`, `GREATERTHANOREQUALS`, `GTEO`, `GREATER_THAN_OR_EQUALS` |
| `<=`     | `LTE`, `LESSTHANOREQUALS`, `LTEO`, `LESS_THAN_OR_EQUALS` |


## 示例
```yaml
  Conditions:
  - comparevalues{value1=%server_online%;operator=>=;value2=1/3*%bungee_total%}
```
> 如果服务器在线玩家数大于或等于网络总玩家数的 1/3，则返回 true。  


## 别名
- [x] comparevalue