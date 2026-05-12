## 描述
Ex执行 the 技能 when a 玩家 interacts with, or *right-clicks*, the 生物.
> The associated [@触发器](/技能/目标选择器/触发器) is the 玩家 that interacted 与 施法者


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onInteract)
- [MythicRPG](/../../../mythicrpg/-/wikis/技能/触发器/onInteract)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when a player right-clicks the mob
    - message{m=INTERACTED} @World ~onInteract
```