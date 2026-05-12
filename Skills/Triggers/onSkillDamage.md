## 描述
生物通过技能对其他实体造成伤害时执行技能。  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为受到伤害的实体


## 示例
```yaml
ExampleMob:
  Type: 
  Skills:
  - damage @PIR{r=10} ~onTimer:20
  - message{m="吃伤害吧！哈哈哈哈"} @trigger ~onSkillDamage
```


## 别名
- [x] onSkillHit
- [x] onSkill_Damage
