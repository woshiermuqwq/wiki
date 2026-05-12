## 描述
Sets the base value of 目标实体's [attribute][]


## 属性

| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| attribute | attr      | The [attribute][] to set             | GENERIC_LUCK<!--type:PaperAttribute--> |
| amount    | amt, a    | The amount of the attribute                                            | 0     |
| duration  | dur       | The duration of the attribute                                          | 0     |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - attribute{attribute=GENERIC_LUCK;a=2;duration=1200} @trigger ~onDeath
```


## 别名
- [x] setattribute


  [attribute]: https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html


<!--TAGS-->
<!--tag:Attribute-->