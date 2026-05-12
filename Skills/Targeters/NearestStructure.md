## 描述
以nearest 结构 of the specified 类型 在...内 a 半径 in the 施法者 世界为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 类型 | t | The 类型 of the 结构 | STRONGHOLD |
| 半径 | r | The 半径 of the 目标选择器 | 5000 |
| unexplored | u | Whether the 结构 应为 unexplored | false |


## 示例
```yaml
StrongholdFinder:
  Cooldown: 10
  Skills:
  - projectile{hp=false;se=false;sb=false;v=5;d=100;onTick=[ effect:particles ]} @NearestStructure{r=1000}
```