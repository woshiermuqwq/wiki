## 描述
检查目标的饱食度。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a, food, f, saturation, s | 要检查的饱食度范围      | 0       |


## 示例
```yaml
  TargetConditions:
  - FoodSaturation{a=<1} true
```

## 别名
- [x] hungerSaturation