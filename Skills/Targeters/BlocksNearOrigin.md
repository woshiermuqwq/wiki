## 描述
选取嵌套技能原点周围半径范围内的所有方块


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 2       |
| radiusy   | ry, yradius, yr | 半径的 Y 轴分量                                  | radius  |
| shape     | s         | 选择区域的形状。可选 `SPHERE`（球体）、`CUBE`（立方体）            | SPHERE<!--type:Shape-->|
| noise     | n         | 选取的随机程度                                       | 0       |
| noair     | na        | 是否不选取空气方块                                   | true    |
| onlyair   | oa        | 是否仅选取空气方块                                  | false   |


## 示例
此技能将在嵌套技能原点周围 10 格半径内随机选取部分方块

```yaml
ExampleSkill:
  Skills:
  - effect:particles @BlocksNearOrigin{r=10;noise=0.5}
```


## 别名
- [x] BNO
