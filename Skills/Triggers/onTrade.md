## 描述
Ex执行 the 技能 when the villager trades with a 玩家.

> The associated [@触发器](/技能/目标选择器/触发器) is the 玩家 that traded 与 villager


## 示例
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob's target changes
    - message{m=TRADED} @World ~onTrade
```