## 描述
以all MythicMobs or 原版 覆盖 of the given 类型(s) in a 半径 在...周围 施法者为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |
| 类型 | 类型, t | The 类型(s) of the 目标 MythicMobs. Can be a 列表 | |
| checkiftemplate | cit | Whether to 检查 再次st the 生物 模板 而不是 the 生物 internal 名称 | false |


## 示例
```yaml
ExampleSkill:
  Skills:
  - ignite @MobsInRadius{r=10;types=IncredibleZombie,SpookyScarySkeleton}
```


## 别名
- [x] MIR
- [x] 生物