## 描述
生物脱离战斗时执行技能。

> **需要启用 [ThreatTables](/Mobs/ThreatTables)**  

> 没有关联的 [@trigger](/Skills/Targeters/Trigger)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # 生物脱离战斗时向世界中所有玩家发送消息
    - message{m=脱离战斗} @World ~onDropCombat
```


## 别名
- [x] onLeaveCombat
- [x] onCombatDrop
- [x] onExitCombat
