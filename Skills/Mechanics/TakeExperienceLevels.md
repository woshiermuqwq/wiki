## 描述
Takes experience levels to the targeted players


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | 要扣除的等级数                                         | 0       |


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

