## 描述
以a plane of 方块 在...前方 the 施法者为目标。


## 属性

| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| forward | f, 数量, a | How distant should the targeted point be (accept decimals) | 5.0 |
| yoffset | y | The y 偏移 of the plane (accept decimals) | 0.0 |
| 高度 | h | The 高度 of the plane (whole numbers 仅) | 2 |
| 宽度 | w | The 宽度 of the plane (whole numbers 仅) | 3 |


## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @ForwardWall{f=5;y=1;h=2;w=2}
```