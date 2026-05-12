## 描述
以random 位置 near the 原点 of the 元技能为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 数量 | a | The 数量 of points | 5 |
| 半径 | r, maxradius, maxr | The 半径 in which 目标 points 将 generated | 5 |
| minradius | minr | The minimum 半径 in which 目标 points 将 generated | 0 |
| spacing | s | The minimum 数量 of space between selected targets | 0 |
| onSurface | onsurf, os| Only 目标 位置 above solid 方块 | false |

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