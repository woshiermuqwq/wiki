## 描述
返回构成一个矩形的目标位置点。根据参数可以修改矩形的各种属性，例如是否填充、是否仅绘制边框、位置等


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| x         |           | 矩形在 **x** 轴上的大小                          | 1       |
| y         |           | 矩形在 **y** 轴上的大小                          | 1       |
| z         |           | 矩形在 **z** 轴上的大小                          | 1       |
| xOffset   |           | 矩形在 **x** 轴上的偏移                        | 0       |
| yOffset   |           | 矩形在 **y** 轴上的偏移                        | 0       |
| zOffset   |           | 矩形在 **z** 轴上的偏移                        | 0       |
| points    | p, density, d | 每条立方体"边线"上的点数                                 | 10      |
| filled    | fill, f   | 是否填充矩形                                    | false   |
| outline   | edge, onlyEdge, e, onlyOutline, o | 是否仅绘制边框          | false   |
| rotation  | r         | 矩形的 3D 旋转角度                                     | 0,0,0   |
| fromOrigin| origin    | 是否从嵌套技能的原点开始绘制矩形    | false   |


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
