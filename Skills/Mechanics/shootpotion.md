## 描述
Throws a potion 在targeted entity or location, causing the splash
potion effect of the given type to all entities hit.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| velocity  | v         | The velocity of the thrown potion                                    | 1       |
> This 机制 inherits every *inheritable* attribute of the [Potion](/Skills/Mechanics/Potion) 机制


## 示例
Throws a potion 在target that slows them down.
```yaml
ThrownCripplingPotion:
  Skills:
  - shootpotion{type=SLOW;duration=200;level=4;velocity=5} @target
```


<!--TAGS-->
<!--tag:Projectile-->
