## 描述
以random 位置 near the 施法者为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 数量 | a | The 数量 of points | 5 |
| 半径 | r, maxradius, maxr | The 半径 in which 目标 points 将 generated | 5 |
| minradius | minr | The minimum 半径 in which 目标 points 将 generated | 0 |
| spacing | s | The minimum 数量 of space between selected targets | 0 |
| onSurface | onsurf, os| Only 目标 位置 above solid 方块 | false |


## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @RandomLocationsNearCaster{a=5;r=2}
```


## 别名
- [x] randomLocations
- [x] RLNC