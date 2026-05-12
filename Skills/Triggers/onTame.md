## 描述
Ex执行 the 技能 when the 玩家 tames the 生物.

> The associated [@触发器](/技能/目标选择器/触发器) is the 玩家 that tamed the 生物


## 示例
```yml
EXAMPLE_MOB:
  Type: WOLF
  Skills:
    # sends a message to all the players in the world
    # when a player tames the mob
    - message{m=I GOT TAMED} @World ~onTame
```