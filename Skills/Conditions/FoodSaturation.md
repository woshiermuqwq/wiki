## 描述
检测目标的饱食度饱和度。

## 属性

| 属性       | 别名                              | 描述                     | 默认值 |
| ---------- | --------------------------------- | ------------------------ | ------ |
| amount     | a, food, f, saturation, s         | 要检测的饱食度饱和度范围  | 0      |


## 示例
```yaml
  TargetConditions:
  - FoodSaturation{a=<1} true
```

## 别名
- [x] hungerSaturation
