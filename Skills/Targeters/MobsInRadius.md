## 描述
选取施法者周围半径内指定类型的所有 MythicMob 或原版覆写生物


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |
| types     | type, t   | 目标 MythicMob 的类型。支持列表                  |         |
| checkiftemplate | cit | 是否按生物的模板名称而非内部名称进行匹配 | false |


## 示例
```yaml
ExampleSkill:
  Skills:
  - ignite @MobsInRadius{r=10;types=IncredibleZombie,SpookyScarySkeleton}
```


## 别名
- [x] MIR
- [x] mobs
