## 描述
选取继承目标周围半径范围内的所有方块。


## 属性 
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 2       |
| radiusy   | ry, yradius, yr | 半径的 Y 轴分量                                  | radius  |
| shape     | s         | 选择区域的形状。可选 `SPHERE`（球体）、`CUBE`（立方体）            | SPHERE<!--type:Shape-->|
| noise     | n         | 选取的随机程度                                       | 0       |
| noair     | na        | 是否不选取空气方块                                   | true    |
| onlyair   | oa        | 是否仅选取空气方块                                  | false   |
| nearorigin| no        | 是否同时选取原点                        | false   |


## 示例

以下嵌套技能可选取技能树触发器周围 10 格半径内的所有非空气方块

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @trigger

ExampleSkill2:
  Skills:
  - effect:particles @BlocksInRadius{r=10}
```


## 别名
- [x] BIR
