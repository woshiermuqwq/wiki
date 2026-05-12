## 描述
Ex执行 the 技能 when the 生物 deals 伤害 to 其他 实体 via a 技能.

> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that was damaged


## 示例
```yaml
ExampleMob:
  Type: 
  Skills:
  - damage @PIR{r=10} ~onTimer:20
  - message{m="Get damaged! MUHAHAHA"} @trigger ~onSkillDamage
```


## 别名
- [x] onSkillHit
- [x] onSkill_Damage