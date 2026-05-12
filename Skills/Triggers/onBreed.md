## 描述
执行 the 技能 when the 生物 breeds with 另一个 生物.

> This 触发器 has [`@Father`](/技能/目标选择器/Father) and [`@M其他`](/技能/目标选择器/M其他) 目标选择器.

> The associated [@触发器](/技能/目标选择器/触发器) is the 玩家 that made the 施法者 breed


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob breeds
    - message{m=LET'S GET THIS BREAD} @World ~onBreed
```