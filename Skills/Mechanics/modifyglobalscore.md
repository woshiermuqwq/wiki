## 描述
Modifies the scoreboard-objective value of the fake player `__GLOBAL__`.
This is a notarget skill and cannot affect any other players' score.

A list of possible operations 对于action-syntax:

-   `SET`
-   `ADD`
-   `SUBTRACT`
-   `MULTIPLY`
-   `DIVIDE`
-   `MOD` [^mod]


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| objective | obj, o    | Specifies the scoreboard objectiv to be changed. If the objective doesn't exist it will automatically be created by the 技能                                               |         |
| action    | a         | The operation to perform                                             | ADD<!--type:ScoreAction--> |
| value     | v         | The value to perform the operation with                              |         |

  
## 示例
```yaml
  Skills:
  - modifyglobalscore{objective=someobjective;action=multiply;v=2} ~onAttack
```


## 别名
- [x] mgs


[^mod]: shorthand for "Modular Division"


<!--TAGS-->
<!--tag:Scoreboard-->
