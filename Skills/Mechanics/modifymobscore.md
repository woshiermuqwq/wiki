## 描述
Modifies the scoreboard-objective value of the casting mob.
Does not support targeters.

## 属性
> 此技能继承所有[ModifyGlobalScore](/Skills/Mechanics/modifyglobalscore) 技能

  
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
