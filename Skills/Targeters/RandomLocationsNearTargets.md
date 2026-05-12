## 描述
以random 位置 near the inherited targets为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 数量 | a | The 数量 of points | 5 |
| 半径 | r, maxradius, maxr | The 半径 in which 目标 points 将 generated | 5 |
| minradius | minr | The minimum 半径 in which 目标 points 将 generated | 0 |
| spacing | s | The minimum 数量 of space between selected targets | 0 |
| onsurface | surface | Whether the selected 位置 应为 on a surface that 不是 air | false |


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @PIR{r=10}

ExampleSkill2:
  Skills:
  - effect:particles @RandomLocationsNearTargets{a=5;r=2}
```


## 别名
- [x] randomLocationsNearTarget
- [x] randomLocationsNearTargetEntities
- [x] randomLocationsNearTargetLocations
- [x] RLNT
- [x] RLNTE
- [x] RLNTL