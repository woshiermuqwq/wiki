## 描述
将施法者传送到目标位置ed location/entity. The end point of the teleportation 将会 within an area whose size depends on the `spreadh` and `spreadv` attributes.

The skill will attempt to find a safe landing location within the spread
area, if possible, and should generally avoid putting the mob inside of
blocks. The unsafe attribute will allow mobs to teleport into the target entity.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| spreadh   | sh, r, radius | The horizontal spread of the landing location.                   | 0       |
| spreadv   | sv        | The vertical spread of the landing location.                         | 0       |
| preservepitch | pp    | Whether the pitch value 应当 carried over                       | true    |
| preserveyaw | py      | Whether the yaw value 应当 carried over                         | true    |
| unsafe    | us        | Avoids finding a safe teleport (will ignore sH and sV)               | false   |


## 示例
This example would teleport the mob to within 5 blocks of the targeted
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
