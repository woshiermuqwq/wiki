## 描述
Ex执行 the 技能 when the 生物 spawns.
> There is no associated [@触发器](/技能/目标选择器/触发器)


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onSpawn)
- [MythicRPG](/../../../mythicrpg/-/wikis/技能/触发器/onSpawn)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob spawns
    - message{m=SPAWN} @World ~onSpawn
```