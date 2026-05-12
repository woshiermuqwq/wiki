## 描述
检测目标的饱食度。

## 属性

| 属性       | 别名          | 描述                     | 默认值 |
| ---------- | ------------- | ------------------------ | ------ |
| amount     | a, food, f    | 要检测的饱食度范围        | 0      |


## 示例
```yaml
  TargetConditions:
  - FoodLevel{a=<10} true
```

## 别名
- [x] hunger
- [x] food
- [x] hungerlevel
