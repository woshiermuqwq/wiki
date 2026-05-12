## 描述
Moves the given [pin](/Pins) to the 目标 location.  
Cannot move MultiPins.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| pin       | p         | The pin to move                                                      |<!--type:Pin--> |


## 示例
```yaml
  Skills:
  - movepin{pin=example} @selflocation
```
> Moves the pin named "example" to the current location of the 施法者


<!--TAGS-->
<!--tag:Pin-->