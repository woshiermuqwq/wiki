## 描述
以位置 in a specified ring 在...周围 原点为目标。

Rotations are in radians, 例如 90 degrees of axis 旋转 being `1.57`.

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |
| points | p | The points that make up the ring | 10 |
| rotationx | rotx, rx | The 旋转 of the ring on the x axis | 0 |
| rotationy | roty, ry | The 旋转 of the ring on the y axis | 0 |
| rotationz | rotz, rz | The 旋转 of the ring on the z axis | 0 |
| offsetx | offx, ox | The 偏移 of the ring on the x axis | 0 |
| offsety | offy, oy | The 偏移 of the ring on the y axis | 0 |
| offsetz | offz, oz | The 偏移 of the ring on the z axis | 0 |
| relative | | Whether the Ring orientation 应为 relative to the 施法者 | false |

## 示例
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - effect:particles @RingAroundOrigin{r=5;p=15}
    ]}

# This will draw a vertical circle instead of a flat one:
VerticalRingSkill:
  Skills:
  - particles{p=enchanted_hit;a=1;} @RAO{r=2;rz=1.57;p=9;relative=true}
```


## 别名
- [x] ringOrigin
- [x] RAO