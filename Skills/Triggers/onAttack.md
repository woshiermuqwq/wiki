## 描述
生物攻击实体时执行技能。
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为被攻击的实体

| [已实现的占位符](/Skills/Placeholders#variable-placeholders)     |
|--------------------------------|
| `<skill.var.damage-amount>`    |
| `<skill.var.damage-type>`      |
| `<skill.var.damage-cause>`     |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onAttack)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Damage: 1
  Skills:
    # 生物攻击实体时向世界中所有玩家发送消息
    - message{m=ATTACK} @World ~onAttack
```


## 别名
- [x] onHit
