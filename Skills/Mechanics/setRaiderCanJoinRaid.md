## 描述
Sets if the 目标 raider entity can join a raid or not


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bool      | b, can, c | 是否 the entity can join the raid                                 | true    |


## 示例
```yaml
  Skills:
  - setRaiderCanJoinRaid{c=false} @self
```


## 别名
- [x] setCanJoinRaid