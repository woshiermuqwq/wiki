## 描述
在嵌套技能原点附近随机选取位置


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | 生成的目标点数量                                                 | 5       |
| radius    | r, maxradius, maxr | 生成目标点的半径范围         | 5       |
| minradius | minr      | 生成目标点的最小半径          | 0       |
| spacing   | s         | 选中目标之间的最小间距                 | 0       |
| onSurface | onsurf, os| 仅在实心方块上方选取位置                             | false   |

## 示例
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - effect:particles @RandomLocationsNearOrigin{a=10;r=4;minr=1}
    ]}
```


## 别名
- [x] RLO
- [x] randomLocationsOrigin
- [x] RLNO
