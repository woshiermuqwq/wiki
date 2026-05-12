## 描述
选取继承目标下方第一个实心方块


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tries     | t, max, m | 目标选择器尝试选取目标的最大次数 | 3 |


## 示例
此技能将 10 格半径内所有玩家脚下的方块替换为冰
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @PIR{r=10}

ExampleSkill2:
  Skills:
  - blockmask{r=1;m=ICE} @FloorOfTargets
```


## 别名
- [x] floorsOfTarget
- [x] FOT
