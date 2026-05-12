## 描述
Sets if the 目标 raider should be a raider patrol leader or not


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
|  leader   | l, bool, b| Should the 目标 raider be a leader                                 | true    |


## 示例
```yaml
  Skills:
  - setRaiderPatrolLeader{leader=true} @target
```

## 别名
- [x] setRaiderLeader