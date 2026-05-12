## 描述
Teleports all targeted entities to a location within &lt;spread&gt;
blocks of the casting 生物.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| spread    | s         | How spread out players will be from the casting 生物                  | 0       |
| vspread   | spreadv, vs| Lets you override the vertical spread value                         | spread  |


## 示例
此示例将 teleport all entities within 30 blocks to a random
location within 5 blocks of the boss.
```yaml
ForceGrip:
  Skills:
  - forcepull{spread=5} @EntitiesInRadius{r=30}
```


<!--TAGS-->
<!--tag:Movement:Teleport-->