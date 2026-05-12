## 描述
根据施法者首要[目标](/Skills/Targeters/Target)的当前移动速度，预测其在指定刻数之后的位置。  

在代码实现中，该方法使用从目标位置出发的射线追踪，因此方块会在到达预期终点前阻挡射线


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| maxdistance | max, distance, d | 预测位置与目标当前位置之间的最大距离。如果预测位置在这个距离之外，此目标选择器将"够不到"，转而选取沿目标移动方向 `maxdistance` 格外的一个位置                                      | 64      |
| ticksPredicted | ticks, t | 向"未来"预测多少刻          | 20      |
| ignoreTransparent | it | 用于预测的射线追踪是否忽略透明方块 | true |



## 示例
```yaml
  Skills:
  - skill{s=TheFloorIsLava} @targetPredictedLoc{ticks=15}
```


## 别名
- [x] targetPredictedLoc
- [x] TPL
- [x] PredictedTargetLocation
