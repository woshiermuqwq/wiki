## 描述
生物进入战斗时执行技能。

> **需要启用 [ThreatTables](/Mobs/ThreatTables)**  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为使施法者进入战斗的实体

## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # 生物进入战斗时向世界中所有玩家发送消息
    - message{m=进入战斗} @World ~onEnterCombat
```
