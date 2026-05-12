## 描述
Propels the caster of the 机制 towards the target.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| velocity  | magnitude, v | The velocity at which the mob 将会 propelled                   | 1       |


## 示例
Propels the caster towards the damager if they are over 6 blocks away.
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - propel{v=1;delay=1} @trigger ~onDamaged ?~distance{d=>6}
```


<!--TAGS-->
<!--tag:Movement-->
