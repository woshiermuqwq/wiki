## 描述
以all living 实体 near the inherited 目标为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |


## 示例
This 技能 will 伤害 every 实体 in a 2 方块 半径 从 目标 of the 生物 一旦 executed
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @target

ExampleSkill2:
  Skills:
  - damage{a=10} @LivingNearTargetLocation{r=2}
```


## 别名
- [x] livingentitiesneartargetlocation
- [x] LNTL
- [x] ENTL
- [x] ENT