## 描述
以random points in a ring 在...周围 施法者为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the ring | 5 |
| points | p | The number of points to generate | 10 |
| 数量 | a | How many of the generated points 应为 targeted | 1 |
| rotationx | rotx, rx | The 旋转 on the x axis | 0 |
| rotationy | roty, ry | The 旋转 on the y axis | 0 |
| rotationz | rotz, rz | The 旋转 on the z axis | 0 |
| offsetx | offx, ox | The 偏移 on the x axis | 0 |
| offsety | offy, oy | The 偏移 on the y axis | 0 |
| offsetz | offz, oz | The 偏移 on the z axis | 0 |


## 示例
```yaml
  Skills:
  - particle @randomRingPoint{r=4;p=20;a=10}
```