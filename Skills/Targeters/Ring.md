## 描述
在施法者周围的指定环形区域中选取位置。

旋转角度以弧度为单位，例如绕轴旋转 90 度为 `1.57`。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |
| points    | p         | 组成环形的点数量                                     | 10      |
| rotationx | rotx, rx  | 环形在 X 轴上的旋转角度                               | 0       |
| rotationy | roty, ry  | 环形在 Y 轴上的旋转角度                               | 0       |
| rotationz | rotz, rz  | 环形在 Z 轴上的旋转角度                               | 0       |
| offsetx   | offx, ox  | 环形在 X 轴上的偏移                                 | 0       |
| offsety   | offy, oy  | 环形在 Y 轴上的偏移                                 | 0       |
| offsetz   | offz, oz  | 环形在 Z 轴上的偏移                                 | 0       |
| relative  |           | 环形的朝向是否相对于施法者的朝向    | false   |


## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @Ring{r=10;p=15}
```
