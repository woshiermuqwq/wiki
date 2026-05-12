## 描述
Modifies the a scoreboard-objective value of the casting mob. The skill
is a no-target skill and will always affect the casting mob's score.
Works exactly like the ModifyMobScore-机制, but is only capable of
performing the **set**-action.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| objective | obj, o    | Specifies the scoreboard objectiv to be changed. If the objective doesn't exist it will automatically be created by the 机制                                               |         |
| value     | v         | The value to perform the operation with                              |         |


## 示例
This will set the mob score to Zero on the objective "MyScore"
```yaml
ResetMyMobScore:
  Skills:
  - setmobscore{o=MyScore;v=0}
```


## 别名
- [x] sms


<!--TAGS-->
<!--tag:Scoreboard-->
