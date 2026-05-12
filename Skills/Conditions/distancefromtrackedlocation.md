## 描述
检查施法者与其跟踪位置之间的距离是否在指定值范围内。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| distance  | d         | 要检查的值。可以是范围。                             |         |


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