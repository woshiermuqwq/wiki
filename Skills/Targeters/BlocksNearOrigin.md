## 描述
以all 方块 in a 半径 在...周围 原点 of the 元技能为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 2 |
| radiusy | ry, yradius, yr | The y component of the 半径 | 半径 |
| 形状 | s | The 形状 of the selected 方块. Can be `SPHERE`, `CUBE` | SPHERE<!--类型:形状-->|
| noise | n | The randomness of the 目标选择器 | 0 |
| noair | na | Whether air 不应 be targeted | true |
| 仅air | oa | Whether 仅 air 应为 targeted | false |


## 示例
This 技能 will 目标 some of the 方块 in a 10 方块 半径 在...周围 原点 of the 元技能

```yaml
ExampleSkill:
  Skills:
  - effect:particles @BlocksNearOrigin{r=10;noise=0.5}
```


## 别名
- [x] BNO