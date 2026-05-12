## 描述
以points in a sphere 在...周围 施法者为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |
| points | p | The 数量 of points | 10 |
| yoffset | y | The 偏移 of the targets on the y axis | 0 |
| exact | e | If the 目标选择器 should draw a perfect sphere | false |

## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @Sphere{r=6;points=50}
```