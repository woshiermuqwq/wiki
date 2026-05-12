## 描述
选取施法者所在世界中、指定半径内最近的结构


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | 结构类型                                         | STRONGHOLD |
| radius    | r         | 选取半径                                           | 5000    |
| unexplored | u        | 是否要求结构未被探索过                           | false   |


## 示例
```yaml
StrongholdFinder:
  Cooldown: 10
  Skills:
  - projectile{hp=false;se=false;sb=false;v=5;d=100;onTick=[ effect:particles ]} @NearestStructure{r=1000}
```
