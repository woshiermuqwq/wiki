## 描述
Teleports all targeted entities to a location within &lt;spread&gt;
blocks of the casting mob.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| spread    | s         | How spread out players 将会 from the casting mob                  | 0       |
| vspread   | spreadv, vs| Lets you override the vertical spread value                         | spread  |


## 示例
This example would teleport all entities within 30 blocks to a random
location within 5 blocks of the boss.
```yaml
ForceGrip:
  Skills:
  - forcepull{spread=5} @EntitiesInRadius{r=30}
```


<!--TAGS-->
<!--tag:Movement:Teleport-->
