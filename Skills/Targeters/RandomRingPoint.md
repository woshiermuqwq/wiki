## 描述
在施法者周围的环形区域中随机选取点


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 环形的半径                                               | 5       |
| points    | p         | 生成的点数量                                     | 10      |
| amount    | a         | 从生成的点中选取多少个                  | 1       |
| rotationx | rotx, rx  | X 轴旋转角度                                           | 0       |
| rotationy | roty, ry  | Y 轴旋转角度                                           | 0       |
| rotationz | rotz, rz  | Z 轴旋转角度                                           | 0       |
| offsetx   | offx, ox  | X 轴偏移                                             | 0       |
| offsety   | offy, oy  | Y 轴偏移                                             | 0       |
| offsetz   | offz, oz  | Z 轴偏移                                             | 0       |


## 示例
```yaml
  Skills:
  - particle @randomRingPoint{r=4;p=20;a=10}
```
