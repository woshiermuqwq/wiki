## 描述
Ex执行 the 技能 when the 生物 teleports.
> There is no associated [@触发器](/技能/目标选择器/触发器)


## 示例
```yml
EXAMPLE_MOB:
  Type: ENDERMAN
  Skills:
    # sends a message to all the players in the world
    # when the mob teleports
    - message{m=TELEPORT} @World ~onTeleport
```