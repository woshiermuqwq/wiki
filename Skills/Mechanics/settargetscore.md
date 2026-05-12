## 描述
Modifies the a 计分板-objective value of the specified targeter(s).
Works exactly like the ModifyTargetScore-技能, but is only capeable
of performing the **set**-action.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| objective | obj, o    | Specifies the 计分板 objectiv to be changed. If the objective doesn't exist it will automatically be created by the 技能                                               |         |
| value     | v         | The value to perform the operation with                              |         |


## 示例
此示例将 track how often and whom damaged
the casting 生物 in battle.
```yaml
  Skills:
  - settargetscore{
      objective=damagescore;
      value=1
      } @trigger ~onDamaged
```


## 别名
- [x] sts


<!--TAGS-->
<!--tag:Scoreboard-->
