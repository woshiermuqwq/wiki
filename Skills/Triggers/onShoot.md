## 描述
Ex执行 the 技能 when the 生物 shoots a 弹射物.
FoFor 示例, skeletons with bows will shoot arrows; ghasts, blazes, or ender dragon will shoot some 类型 of fireball.

> The associated [@触发器](/技能/目标选择器/触发器) is the 施法者

| [Implemented 占位符](/技能/占位符#变量-占位符) |
|--------------------------------|
| `<skill.var.bow-tension>` |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onShoot)
- [MythicRPG](/../../../mythicrpg/-/wikis/技能/触发器/onShoot)


## 示例
```yml
EXAMPLE_MOB:
  Type: SKELETON
  Skills:
    # sends a message to all the players in the world
    # when the skeleton shoots from a bow
    - message{m=I SHOT AN ARROW} @World ~onShoot
```


## 别名
- [x] onBowShoot
- [x] onShootBow