## 描述
以all 方块 in a chunk relative to the inherited 目标(s)为目标。

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| noair | na | Whether air 不应 be targeted | true |
| 仅air | oa | Whether 仅 air 应为 targeted | false |
| nearorigin| no | Whether the 目标选择器 should 也 目标 the 原点 | false |


## 示例
Those 元技能 will 目标 every non air 方块 in the chunk 该 触发器 of the skilltree is located
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @trigger

ExampleSkill2:
  Skills:
  - effect:particles @BlocksInChunk
```


## 别名
- [x] BIC