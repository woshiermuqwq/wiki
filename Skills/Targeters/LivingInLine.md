## 描述
选取继承目标与施法生物之间连线上的所有实体


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 连线上各点之间的间距，同时也是每个点周围选取实体的半径                                                                | 1       |
| fromorigin| fo        | 是否从嵌套技能的原点开始画线         | false   |


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
