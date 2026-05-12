## 描述
以位置 在...之间 生物 and the inherited 目标为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 距离 between each point in the line | 1 |
| fromorigin| fo | If the line 应为 drawn 从 原点 of the 元技能 | false |


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @Forward{f=10}

ExampleSkill2:
  Skills:
  - effect:particles @Line{r=0.5}
```