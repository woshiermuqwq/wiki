## 描述
Sets or changes the target mob's faction.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| faction   | f         | The name of the faction to apply to the mob                          |         |


## 示例
Sets the faction of the mob to "Hostile" when the mob spawns.
```yaml
  Skills:
  - setFaction{faction=Hostile} @self ~onSpawn
```
