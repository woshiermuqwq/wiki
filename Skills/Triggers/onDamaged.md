## 描述
执行 the 技能 when the 生物 takes 伤害.
> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that dealt the 伤害

| [Implemented 占位符](/技能/占位符#变量-占位符) |
|--------------------------------|
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onDamaged)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob takes damage
    - message{m=DAMAGED} @World ~onDamaged
```


## 别名
- [x] onHurt