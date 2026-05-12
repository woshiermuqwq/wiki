## 描述
Takes experience levels to 目标玩家


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount of levels to take                                         | 0       |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - takeexperiencelevels{a=1} @trigger ~onDamaged
```


## 别名
- [x] takeexplevels


<!--TAGS-->
<!--tag:Experience-->

