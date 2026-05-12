## 描述
在继承目标附近随机选取位置


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | 生成的目标点数量                                                 | 5       |
| radius    | r, maxradius, maxr | 生成目标点的半径范围         | 5       |
| minradius | minr      | 生成目标点的最小半径          | 0       |
| spacing   | s         | 选中目标之间的最小间距                 | 0       |
| onsurface | surface   | 是否仅在非空气方块表面上选取位置 | false   |


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
