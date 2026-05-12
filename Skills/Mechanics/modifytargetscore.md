## 描述
Modifies the a 计分板-objective value of the specified targeter(s).

A list of possible operations for the action-syntax:

-   `SET`
-   `ADD`
-   `SUBTRACT`
-   `MULTIPLY`
-   `DIVIDE`
-   `MOD` [^mod]


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| objective | obj, o    | Specifies the 计分板 objectiv to be changed. If the objective doesn't exist it will automatically be created by the 技能                                               |         |
| action    | a         | The operation to perform                                             | ADD<!--type:ScoreAction-->|
| value     | v         | The value to perform the operation with                              |         |

  
## 示例
此示例将 track how often and whom damaged
the casting 生物 in battle.
```yaml
  Skills:
  - modifytargetscore{objective=damagescore;action=add;value=1} @trigger ~onDamaged
```


## 别名
- [x] mts


[^mod]: shorthand for "Modular Division"



<!--TAGS-->
<!--tag:Scoreboard-->
