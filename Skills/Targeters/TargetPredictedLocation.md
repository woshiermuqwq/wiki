## 描述
Ta以位于which the 施法者 top [目标](/技能/目标选择器/目标) 将 之后 an 数量 of ticks has elapsed, 基于 its current 移动 速度的the predicted 位置为目标。

To do this, in the code 自身, a raytrace 从 目标 position is used, so, 例如, a 方块 will stop the raytrace 之前 它可以 reach its supposed end point


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| maxdistance | max, 距离, d | The maximum 距离 从 目标 current 位置 that the predicted 位置 can be located at. If the predicted 位置 is supposed to be further away, this 目标选择器 将改为 "fall short" of it, targeting the 位置 `maxdistance` 方块 away form the original 目标 位置, alongside its 移动 向量 | 64 |
| ticksPredicted | ticks, t | How "far 到 future" this 目标选择器 should predict. | 20 |
| ignoreTransparent | it | Whether the raytrace used 对于 prediction should 忽略 transparent 方块 | true |



## 示例
```yaml
  Skills:
  - skill{s=TheFloorIsLava} @targetPredictedLoc{ticks=15}
```


## 别名
- [x] targetPredictedLoc
- [x] TPL
- [x] PredictedTargetLocation