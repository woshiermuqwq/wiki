## 描述
Gives experience levels to the targeted players


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | 要给予的等级数                                         | 0       |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - giveexperiencelevels{a=1} @trigger ~onDamaged
```


## 别名
- [x] giveexplevels


<!--TAGS-->
<!--tag:Experience-->