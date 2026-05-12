## 描述
Modifies the a 计分板-objective value of the casting 生物. The skill
is a no-目标 skill and will always affect the casting 生物's score.
Works exactly like the ModifyMobScore-技能, but is only capable of
performing the **set**-action.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| objective | obj, o    | Specifies the 计分板 objectiv to be changed. If the objective doesn't exist it will automatically be created by the 技能                                               |         |
| value     | v         | The value to perform the operation with                              |         |


## 示例
This will set the 生物 score to Zero on the objective "MyScore"
```yaml
ResetMyMobScore:
  Skills:
  - setmobscore{o=MyScore;v=0}
```


## 别名
- [x] sms


<!--TAGS-->
<!--tag:Scoreboard-->
