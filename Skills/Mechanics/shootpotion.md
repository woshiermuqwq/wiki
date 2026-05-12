## 描述
Throws a potion at 目标实体 or location, causing the splash
potion effect of the given type to all entities hit.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v         | The 速度 of the thrown potion                                    | 1       |
> This 技能 inherits every *inheritable* attribute of the [Potion](/Skills/技能/Potion) 技能


## 示例
Throws a potion at the 目标 that slows them down.
```yaml
ThrownCripplingPotion:
  Skills:
  - shootpotion{type=SLOW;duration=200;level=4;velocity=5} @target
```


<!--TAGS-->
<!--tag:Projectile-->
