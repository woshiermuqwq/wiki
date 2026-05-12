## 描述
以any 实体 in a line 在...之间 inherited 目标 and the casting 生物为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 距离 between each point in the line and the 半径 around each point where 实体 将 targeted | 1 |
| fromorigin| fo | If the line 应为 drawn 从 原点 of the 元技能 | false |


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @Forward{f=10}

ExampleSkill2:
  Skills:
  - ignite @LivingInLine{r=0.5}
```


## 别名
- [x] entitiesInLine
- [x] livingEntitiesInLine
- [x] LEIL
- [x] EIL