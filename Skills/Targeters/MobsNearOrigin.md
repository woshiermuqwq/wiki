## 描述
以all MythicMobs or 原版 覆盖 of the given 类型(s) in a 半径 在...周围 原点为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |
| 类型 | 类型, t | The 类型(s) of the 目标 MythicMobs. Can be a 列表 |<!--列表-->|


## 示例
This 技能 will ignite every 生物 of the given 类型 in a 半径 around 自身 when it ends
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