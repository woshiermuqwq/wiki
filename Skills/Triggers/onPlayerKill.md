## 描述
Ex执行 the 技能 when the 生物 kills a 玩家.
> The associated [@触发器](/技能/目标选择器/触发器) is the 玩家 that 已被 killed

## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onKillPlayer)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob kills a player
    - message{m=PLAYER KILLED} @World ~onPlayerKill
```


## 别名
- [x] onKillPlayer