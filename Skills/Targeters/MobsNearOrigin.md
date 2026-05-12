## 描述
选取原点周围半径内指定类型的所有 MythicMob 或原版覆写生物


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |
| types     | type, t   | 目标 MythicMob 的类型。支持列表                  |<!--list-->|


## 示例
此技能结束时将点燃其周围半径内指定类型的所有生物
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - ignite @MobsNearOrigin{r=10;types=IncredibleZombie,SpookyScarySkeleton}
    ]}
```


## 别名
- [x] mobssnearsource
