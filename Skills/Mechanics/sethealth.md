## 描述
Sets the health of the 目标 entity.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | Amount of health to set to                                           | 1.0     |


## 示例
此示例将 set 玩家的' health to 6 (3 hearts) when they
right-click the 生物.
```yaml
  Skills:
  - sethealth{a=6} @trigger ~onInteract
  - ...
```


## 别名
- [x] sethp


<!--TAGS-->
<!--tag:Health-->
