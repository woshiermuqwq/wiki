## 描述
检测 [@origin] 是否在指定[标记点]的一定距离范围内。

## 属性
| 属性       | 别名   | 描述                       | 默认值          |
| ---------- | ------ | -------------------------- | --------------- |
| pin        | p      | 要检测的标记点              |<!--type:Pin-->  |
| distance   | d      | 要检测的距离。可为范围值     |                 |


## 示例
```yaml
  Conditions:
  - originDistanceFromPin{pin=example_pin;d=>10} true
```


<!-- LINKS -->
[标记点]: /Pins
[@origin]: /Skills/Targeters/Origin
