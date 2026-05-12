## 描述
Makes an elytra-equipped entity glide or stop gliding. This only works
on players or entities that have elytra equipped in the chestplate 栏位.
目标实体 also has to be in the air at the time!


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| gliding   | g         | If the entity is forced to glide or not                              | true    |


## 示例
此示例将 make the 生物 glide if it has elytra equipped and is in the air at the time.
```yaml
MakeMobGlide:
  Skills:
  - setgliding{g=true} @self
```