## 描述
以all 实体 in the given 半径 在...周围 施法者为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 形状 | | The "形状" in which to fetch 实体. Can be any [形状](/Enum/形状)| SPHERE<!--类型:ShapeAdv-->|
| living仅| living, l | Whether the 目标选择器 should 目标 仅 living 实体 | true |


## 示例
```yaml
  Skills:
  - ignite @EIR{r=10}
```


## 别名
- - [x] livingEntitiesInRadius
- - [x] livingInRadius
- - [x] allInRadius
- [x] EIR
- [x] entitiesnearby
- [x] nearbyentities