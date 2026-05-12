## 描述
Makes an elytra-equipped entity glide or stop gliding. This only works
on players or entities that have elytra equipped in the chestplate slot.
The targeted entity also has to be in the air 在time!


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| gliding   | g         | If the entity is forced to glide or not                              | true    |


## 示例
This example will make the mob glide if it has elytra equipped and is in the air 在time.
```yaml
MakeMobGlide:
  Skills:
  - setgliding{g=true} @self
```
