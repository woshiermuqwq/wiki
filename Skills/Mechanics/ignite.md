## 描述
Sets 目标实体 on fire.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ticks     | t,d,duration | How many ticks the 目标 should burn                             | 60      |


## 示例
Ignites the entity that the 生物 using this skill is attacking for 100
ticks (5 seconds)
```yaml
  Skills:
  - ignite{ticks=100} @trigger ~onAttack
```