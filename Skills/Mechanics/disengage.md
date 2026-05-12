## 描述
Causes the caster to leap backwards away from the target entity


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| velocity  | v, magnitude | The velocity of the leap                                          | 1       |
| velocityy | yvelocity, vy, yv | The y component of the velocity of the leap                  | 0.01337 |


## 示例
```yaml
ExampleMob:
  Skills:
  - disengage @trigger ~onDamaged
```


<!--TAGS-->
<!--tag:Movement-->
