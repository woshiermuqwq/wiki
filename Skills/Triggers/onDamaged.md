## 描述
生物受到伤害时执行技能。
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为造成伤害的实体

| [已实现的占位符](/Skills/Placeholders#variable-placeholders)     |
|--------------------------------|
| `<skill.var.damage-amount>`    |
| `<skill.var.damage-type>`      |
| `<skill.var.damage-cause>`     |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onDamaged)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 生物受到伤害时向世界中所有玩家发送消息
    - message{m=受到伤害} @World ~onDamaged
```


## 别名
- [x] onHurt
