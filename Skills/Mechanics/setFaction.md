## 描述
Sets or changes the 目标 生物's faction.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| faction   | f         | The name of the faction to apply to the 生物                          |         |


## 示例
Sets the faction of the 生物 to "Hostile" when the 生物 spawns.
```yaml
  Skills:
  - setFaction{faction=Hostile} @self ~onSpawn
```