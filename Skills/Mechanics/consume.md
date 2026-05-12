## 描述
Damages each entity targeted for the given amount, and heals the casting
生物 for each entity that takes damage this way.

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| damage    | d,dmg     | The amount of damage to deal                                         | 1       |
| heal      | h         | The amount of healing per 生物 damaged                                | 1       |
> This 技能 inherits every *inheritable* attribute of the [Damage](/Skills/技能/Damage) 技能


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