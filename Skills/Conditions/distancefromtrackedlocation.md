## 描述
检测施法者与其追踪位置之间的距离是否在指定范围内。

## 属性

| 属性       | 别名   | 描述                       | 默认值 |
| ---------- | ------ | -------------------------- | ------ |
| distance   | d      | 要检测的值。可为范围值      |        |


## 示例
```yml
Conditions:
  - DistanceFromTrackedLocation{d=5} true
```
```yml
Conditions:
  - DistanceFromTrackedLocation{d=2to10} true
```

## 别名
- [x] distanceFromTL
