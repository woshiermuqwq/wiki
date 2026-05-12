## 描述
根据指定运算符比较两个值。
比较方向是 `value1` 对 `value2`：例如使用 `>` 运算符时，如果 `value1` 大于 `value2` 则返回 `true`。

此条件可以比较整数、浮点数、双精度浮点数（常规）和字符串（按字典序）。

条件会尝试「推断」传入值的类型，并优先尝试最严格的类型比较，如果不可用则逐步降级为更宽松的比较（整数 → 双精度 → 字符串）。

如果你已知传入值的类型，可以通过 `type` 属性指定，这样只会进行该特定类型的比较，避免了试错的开销。如果因值类型转换问题仍无法比较，条件将返回 `false`。

## 属性
| 属性      | 别名        | 描述                                                                                      | 默认值 |
| --------- | ----------- | ----------------------------------------------------------------------------------------- | ------ |
| value1    | val1, v1    | 比较的第一个值                                                                             |        |
| value2    | val2, v2    | 比较的第二个值                                                                             |        |
| operator  | op          | 使用的[运算符](#运算符属性)                                                                | EQUALS<!--type:CompareValues_Operator--> |
| type      | t           | （可选）比较类型。不设置时会从严格到宽松依次尝试所有可用类型。设置后只按指定类型比较。接受任何[变量类型](/Skills/Variables#variable-types) | <!--type:VariableType--> |

### 运算符属性
| 运算符  | 别名                                                                                   |
| ------- | -------------------------------------------------------------------------------------- |
| `==`    | `EQUALS`, `EQUAL`, `EQ`, `EQL`                                                         |
| `!=`    | `NOT_EQUALS`, `NOTEQUALS`, `NOTEQUAL`, `NE`, `NEQ`, `NEQL`                             |
| `>`     | `GREATERTHAN`, `GREATER_THAN`, `GTR`, `GT`                                             |
| `<`     | `LT`, `LESSTHAN`, `LTR`, `LESS_THAN`                                                   |
| `>=`    | `GTE`, `GREATERTHANOREQUALS`, `GTEO`, `GREATER_THAN_OR_EQUALS`                         |
| `<=`    | `LTE`, `LESSTHANOREQUALS`, `LTEO`, `LESS_THAN_OR_EQUALS`                               |


## 示例
```yaml
  Conditions:
  - comparevalues{value1=%server_online%;operator=>=;value2=1/3*%bungee_total%}
```
> 如果当前服务器在线玩家数大于等于整个网络总玩家数的 1/3，则返回 true。

## 别名
- [x] comparevalue
