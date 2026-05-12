## 描述
若to 目标 仅 its outline, its 位置 and so on，返回the # of points 目标 位置 that comprise a rectangle. Depending on the 参数, some elements of the rectangle can be modified, 例如 it being filled or not,。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| x | | The size of the rectangle on the **x** axis | 1 |
| y | | The size of the rectangle on the **y** axis | 1 |
| z | | The size of the rectangle on the **z** axis | 1 |
| xOffset | | The 偏移 of the rectangle on the **x** axis | 0 |
| yOffset | | The 偏移 of the rectangle on the **y** axis | 0 |
| zOffset | | The 偏移 of the rectangle on the **z** axis | 0 |
| points | p, density, d | 数量 of points per cube 'line' | 10 |
| filled | fill, f | If the rectangle 应为 filled | false |
| outline | edge, 仅Edge, e, 仅Outline, o | If 仅 the outline 应为 drawn | false |
| 旋转 | r | The 3D 旋转 of the rectangle | 0,0,0 |
| fromOrigin| 原点 | If the rectangle 应为 drawn 从 原点 of the 元技能 | false |


## 示例
```yaml
ExampleMob1:
  Type: ZOMBIE
  Skills:
  - particle{p=FLAME;a=1} @Rectangle{d=12;f=false;r=45,45,0;yOffset=1.5;outline=true} ~onDamaged

ExampleMob2:
  Type: ZOMBIE
  Skills:
  - particle{p=SOUL_FIRE_FLAME;a=1} @Rectangle{d=12;r=45,45,45;yOffset=3;fill=true} ~onDamaged
```


## 别名
- [x] cube
- [x] cuboid