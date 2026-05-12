## 描述
Shoots a volley of arrows or item-弹射物 at 目标实体 or
location that deals damage. Can use any attribute from the Shoot
技能.


## 属性
| 属性 | 缩写 | 描述                                       | 默认值 |
|-----------|---------|---------------------------------------------------|---------|
| amount    | a       | The amount of 弹射物                         | 10      |
| source    | s       | The type of the volley. Can be REGULAR or RAIN    | REGULAR<!--type:REGULAR,RAIN-->|
| 半径    | r       | The 半径 of the volley                          | 1       |
| yoffset   | y       | The y offset of the 目标 location of 弹射物的 | 0  |
| canPickup   | pickup  | 是否 the arrows can be picked up by players             | true    |
> This 技能 inherits every *inheritable* attribute of the [Shoot](/Skills/技能/Shoot) 技能


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

