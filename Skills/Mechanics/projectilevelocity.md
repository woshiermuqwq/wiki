## 描述

Modifies the 速度 of the calling [弹射物](/skills/技能/弹射物) or [制导弹射物](/skills/技能/制导弹射物). In this context, it works the same as the [速度](/skills/技能/速度) 技能.


## 属性

| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mode      | m         | The operation to perform. Can be SET, ADD, REMOVE, DIVIDE, or MULTIPLY. | SET<!--type:Velocity_Mode-->|
| velocityx | vx, x     | 速度 on the x-axis. Can be negative.                             | 1       |
| velocityy | vy, y     | 速度 on the y-axis. Can be negative.                             | 1       |
| velocityz | vz, z     | 速度 on the z-axis. Can be negative.                             | 1       |
| relative  | r         | If the change in 速度 should be relative to 弹射物的 facing direction. In this instance, the `z` axis becomes `forward/backward`, `y` becomes `up/down` and `x` becomes `left/right`| true     |


## 示例
```yaml
Projectile-onTick:
  Conditions:
  - chance{chance=0.1} true
  Skills:
  - projectilevelocity{mode=ADD;vz=0.3}
```


## 别名
- [x] pvelocity


<!--TAGS-->
<!--tag:Meta-->

