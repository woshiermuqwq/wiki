## 描述
执行 the 技能 when the 生物 enters 战斗.

> > **需要 [ThreatTables](/生物/ThreatTables) to be 启用**

> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that made the 施法者 enter 战斗

## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob enters combat
    - message{m=ENTERED COMBAT} @World ~onEnterCombat
```