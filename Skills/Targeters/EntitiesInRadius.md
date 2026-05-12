## 描述
选取施法者周围指定半径内的所有实体


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| shape     |           | 选取实体的"形状"。可以是任意 [shape](/Enum/Shape)| SPHERE<!--type:ShapeAdv-->|
| livingonly| living, l | 是否仅选取活着的实体              | true    |


## 示例
```yaml
  Skills:
  - ignite @EIR{r=10}
```


## 别名
- [x] livingEntitiesInRadius  
- [x] livingInRadius  
- [x] allInRadius  
- [x] EIR
- [x] entitiesnearby
- [x] nearbyentities
