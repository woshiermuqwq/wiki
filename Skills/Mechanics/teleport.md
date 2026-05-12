## 描述
将施法者传送到目标位置/实体处。传送终点落在由 `spreadh` 和 `spreadv` 属性决定大小的区域内。

The skill 将尝试 find a safe landing location within the spread
area, if possible, and should generally avoid putting the 生物 inside of
blocks. The unsafe attribute will allow 生物 to teleport into the 目标 entity.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| spreadh   | sh, r, 半径 | The horizontal spread of the landing location.                   | 0       |
| spreadv   | sv        | The vertical spread of the landing location.                         | 0       |
| preservepitch | pp    | 是否 the 俯仰角(pitch) value should be carried over                       | true    |
| preserveyaw | py      | 是否 the 水平朝向(yaw) value should be carried over                         | true    |
| unsafe    | us        | Avoids finding a safe teleport (will ignore sH and sV)               | false   |


## 示例
此示例将 teleport the 生物 to within 5 blocks of the targeted
player, on the same vertical axis.
```yaml
Warp:
  Skills:
  - teleport{spreadh=5;spreadv=0} @target
```


## 别名
- [x] tp


<!--TAGS-->
<!--tag:Movement:Teleport-->

