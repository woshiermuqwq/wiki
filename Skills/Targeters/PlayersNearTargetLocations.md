## 描述
选取继承目标位置附近的所有玩家


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |


## 示例
此技能执行时会对生物目标周围 2 格半径内的所有玩家造成伤害
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @target

ExampleSkill2:
  Skills:
  - damage{a=10} @PlayersNearTargetLocations{r=2}
```


## 别名
- [x] playersNearTargetLocation
- [x] PNTL
