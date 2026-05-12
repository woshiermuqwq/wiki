## 描述
以first solid 方块 在...下方 inherited targets为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tries | t, max, m | The maximum number of attempts the 目标选择器 will make to fetch the targets | 3 |


## 示例
This 机制 will mask the 方块 below every 玩家 in a 10 方块 半径 to ice
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