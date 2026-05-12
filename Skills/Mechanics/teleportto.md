## 描述
Will teleport the targeted entity or entities to the specified location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| location  | coordinates, loc, l, c, t, target, to | The coordinates of the teleport's destination, or a targeter    |     |
| world     | w         | The destination-world. Optional attribute if "location" is given     |         |
| yaw       | y         | The yaw that the affected entities should assume                     | 0       |
| pitch     | p         | The pitch that the affected entities should assume                   | 0       |
| relative  | r         | Whether the location is relative or directional                      | false   |
| targetasorigin | tao  | Will use the target's location as the origin instead of the caster   | false   |


## 示例
Will teleport all players in a radius of 50 blocks around the casting
mob to the specified location:
```yaml
  Skills:
  - teleportto{location=190,64,200;world=world_nether} @PIR{r=50}
```
##
Teleports all of the players in a radius of 50 blocks to a locations that is 10 blocks above the caster of the 机制
```yaml
  Skills:
  - teleportto{location=@selflocation{y=10}} @PIR{r=50}
```


## 别名
- [x] teleportlocation
- [x] tpt
- [x] tpl


<!--TAGS-->
<!--tag:Movement:Teleport-->
