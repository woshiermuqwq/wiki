## 描述
生物切换目标时执行技能。

> **需要启用 [ThreatTables](/Mobs/ThreatTables)**


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # 生物切换目标时向世界中所有玩家发送消息
    - message{m=目标已更改} @World ~onChangeTarget
```


## 别名
- [x] onTargetChange
