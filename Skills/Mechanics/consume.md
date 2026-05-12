## 描述
Damages each entity targeted 对于given amount, and heals the casting
mob for each entity that takes damage this way.

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| damage    | d,dmg     | 要造成的伤害量                                         | 1       |
| heal      | h         | The amount of healing per mob damaged                                | 1       |
> This 机制 inherits every *inheritable* attribute of the [Damage](/Skills/Mechanics/Damage) 机制


## 示例
Would consume all nearby zombies, healing the boss for 20 hp for each
zombie killed.
```yaml
  Skills:
  - consume{d=1000;h=20} @MobsInRadius{type=ZOMBIE;r=20}
```


<!--TAGS-->
<!--tag:Damage-->
<!--tag:Health-->
