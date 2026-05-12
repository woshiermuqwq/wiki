## 描述
Modifies the 速度 of 目标实体(s). 可用于 on players,
too. Useful for all sorts of things like true knockback resistance,
force-skills or simulated wind.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mode      | m         | The operation to perform. Can be SET, ADD, REMOVE, DIVIDE, or MULTIPLY. | SET<!--type:Velocity_Mode-->|
| velocityx | vx, x     | 速度 on the x-axis. Can be negative.                                | 1    |
| velocityy | vy, y     | 速度 on the y-axis. Can be negative.                                | 1    |
| velocityz | vz, z     | 速度 on the z-axis. Can be negative.                                | 1    |
| relative  | r         | If the change in 速度 should be relative to 目标的 facing direction. In this instance, the `z` axis becomes `forward/backward`, `y` becomes `up/down` and `x` becomes `left/right`                                                                                    | false  |


## 示例
此示例将 stop all momentum of the casting 生物 upon taking
damage. The effect will only last until the 生物 decides to move again or
is moved by other sources.
```yaml
internal_mobname:
  Type: Zombie
  Skills:
  - velocity{m=set;x=0;y=0;z=0} @self ~onDamaged
```
##
While the example above works most of the time, the bow's ARROW_KNOCKBACK enchantment 仍将 manage to move them. This can be prevented by doing a slight modification to the 技能, as shown below.
```yaml
internal_mobname:
  Type: Zombie
  Skills:
  - velocity{m=set;x=0;y=0;z=0;delay=1} @self ~onDamaged
```


<!--TAGS-->
<!--tag:Movement-->
