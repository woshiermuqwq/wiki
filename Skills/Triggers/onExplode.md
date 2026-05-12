## 描述
Ex执行 the 技能 when the 生物 explodes.
`m`mobGriefing` gamerule 必须为 设为 true for this to work.
GeGenerally, this 触发器 仅 works with creepers and TNTs 自从 它们是 the 仅 生物 to 实际上 explode
> There is no associated [@触发器](/技能/目标选择器/触发器)


## 示例
```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob explodes
    - message{m=EXPLODE} @World ~onExplode
```