## 描述
检查 [@origin] 是否在指定[钉点]的特定距离内。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| pin       | p         | 要检查的钉点                                             |<!--type:Pin--> |
| distance  | d         | 要检查的距离。可以是范围。                       |         |


## 示例
```yaml
  Conditions:
  - originDistanceFromPin{pin=example_pin;d=>10} true
```


<!-- LINKS -->
[钉点]: /Pins
[@origin]: /Skills/Targeters/Origin