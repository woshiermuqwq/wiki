## 描述
在原点周围的指定环形中选取位置。

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
  - projectile{...;
    onEnd=[
      - effect:particles @RingAroundOrigin{r=5;p=15}
    ]}

# 此示例将绘制一个竖直的圆环而非水平圆环：
VerticalRingSkill:
  Skills:
  - particles{p=enchanted_hit;a=1;} @RAO{r=2;rz=1.57;p=9;relative=true}
```


## 别名
- [x] ringOrigin
- [x] RAO
