## 描述
执行 the 技能 when the 生物 掉落 战斗.

> > **需要 [ThreatTables](/生物/ThreatTables) to be 启用**

> There is no associated [@触发器](/技能/目标选择器/触发器)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob enters combat
    - message{m=DROPPED COMBAT} @World ~onDropCombat
```


## 别名
- [x] onLeaveCombat
- [x] onCombatDrop
- [x] onExitCombat