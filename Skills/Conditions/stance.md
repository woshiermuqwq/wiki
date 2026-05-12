## 描述
检查目标生物的 stance。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| stance    | s         | 要匹配的 stance                                                  | DEFAULT |
| strict    | str       | 是否精确匹配。如果设为 false，则检查当前 stance 是否包含此词                                             | true    |


## 示例
```yaml
  Conditions:
  - stance{s=CombatStance;str=true} true
```