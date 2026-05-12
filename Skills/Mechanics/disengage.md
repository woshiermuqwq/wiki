## 描述
Causes the 施法者 to leap backwards away from the 目标 entity


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v, magnitude | The 速度 of the leap                                          | 1       |
| velocityy | yvelocity, vy, yv | The y component of the 速度 of the leap                  | 0.01337 |


## 示例
```yaml
ExampleMob:
  Skills:
  - disengage @trigger ~onDamaged
```


<!--TAGS-->
<!--tag:Movement-->