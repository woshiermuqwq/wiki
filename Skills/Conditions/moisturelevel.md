## 描述
检测目标耕地方块是否达到指定的湿润等级。

- `0` 表示耕地干燥
- `1-6` 表示曾经湿润的耕地在失去水源后逐渐变干的过程
- `7` 表示耕地完全湿润


## 属性
| 属性       | 别名            | 描述               | 默认值 |
| ---------- | --------------- | ------------------ | ------ |
| l          | moistness, m    | 要检测的湿润等级     |        |


## 示例
```yml
  TargetConditions:
  - moisturelevel{l=3} true
```
```yml
  TargetConditions:
  - moistureness{l=1to6} true
```

## 别名
- [x] moistureness
- [x] moistness
