## 描述
Modifies the 计分板-objective value of the casting 生物.
Does not support targeters.

## 属性
> This 技能 继承 [ModifyGlobalScore](/Skills/技能/modifyglobalscore) 技能

  
## 示例
```yaml
  Skills:
  - modifymobscore
      {
      objective=someobjective;
      action=multiply;
      v=2
      } ~onAttack
```


## 别名
- [x] mms


<!--TAGS-->
<!--tag:Scoreboard-->
