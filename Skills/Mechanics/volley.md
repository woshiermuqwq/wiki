## 描述
Shoots a volley of arrows or item-projectiles 在targeted entity or
location that deals damage. Can use any attribute from the Shoot
机制.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|---------|---------------------------------------------------|---------|
| amount    | a       | The amount of projectiles                         | 10      |
| source    | s       | The type of the volley. Can be REGULAR or RAIN    | REGULAR<!--type:REGULAR,RAIN-->|
| radius    | r       | The radius of the volley                          | 1       |
| yoffset   | y       | The y offset of the target location of the projectiles | 0  |
| canPickup   | pickup  | Whether the arrows 可以 picked up by players             | true    |
> This 机制 inherits every *inheritable* attribute of the [Shoot](/Skills/Mechanics/Shoot) 机制


## 示例
```yaml
  Skills:
  - volley{type=EGG;velocity=5;damage=10;amount=20}
```


## 别名
- [x] shootvolley


<!--TAGS-->
<!--tag:Projectile-->
<!--tag:Meta-Mechanic-->
