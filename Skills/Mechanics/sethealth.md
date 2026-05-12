## 描述
设置目标的生命值 entity.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | Amount of health to set to                                           | 1.0     |


## 示例
This example will set the players' health to 6 (3 hearts) when they
right-click the mob.
```yaml
  Skills:
  - sethealth{a=6} @trigger ~onInteract
  - ...
```


## 别名
- [x] sethp


<!--TAGS-->
<!--tag:Health-->
