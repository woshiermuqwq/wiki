## 描述
Propels the 施法者 of the 技能 towards the 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | magnitude, v | The 速度 at which the 生物 will be propelled                   | 1       |


## 示例
Propels the 施法者 towards the damager if they are over 6 blocks away.
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - propel{v=1;delay=1} @trigger ~onDamaged ?~distance{d=>6}
```


<!--TAGS-->
<!--tag:Movement-->

