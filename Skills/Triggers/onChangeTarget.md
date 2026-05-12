## 描述
执行 the 技能 when the 生物 changes 目标.

> **需要 [ThreatTables](/生物/ThreatTables) to be 启用**


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob's target changes
    - message{m=Target Changed} @World ~onChangeTarget
```


## 别名
- [x] onTargetChange