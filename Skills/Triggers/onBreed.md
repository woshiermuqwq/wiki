## 描述
生物与另一只生物繁殖时执行技能。

> 此触发器提供 [`@Father`](/Skills/Targeters/Father) 和 [`@Mother`](/Skills/Targeters/Mother) 目标选择器。

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为使施法者繁殖的玩家


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 生物繁殖时向世界中所有玩家发送消息
    - message{m=LET'S GET THIS BREAD} @World ~onBreed
```
