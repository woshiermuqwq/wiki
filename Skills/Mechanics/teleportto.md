## 描述
Will teleport 目标实体 or entities to the 指定的location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| location  | coordinates, loc, l, c, t, 目标, to | The coordinates of the teleport's destination, or a targeter    |     |
| world     | w         | The destination-world. Optional attribute if "location" is given     |         |
| 水平朝向(yaw)       | y         | The 水平朝向(yaw) that the affected entities should assume                     | 0       |
| 俯仰角(pitch)     | p         | The 俯仰角(pitch) that the affected entities should assume                   | 0       |
| relative  | r         | 是否 the location is relative or directional                      | false   |
| targetasorigin | tao  | Will use 目标的 location as the 原点 instead of the 施法者   | false   |


## 示例
Will teleport all players in a 半径 of 50 blocks around the casting
生物 to the 指定的location:
```yaml
  Skills:
  - teleportto{location=190,64,200;world=world_nether} @PIR{r=50}
```
##
Teleports all of 玩家的 in a 半径 of 50 blocks to a locations that is 10 blocks above the 施法者 of the 技能
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
