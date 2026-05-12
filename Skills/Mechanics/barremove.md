## 描述
Removes a custom boss bar on the casting mob (cannot be player).


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| name      | n         | The name of the bossbar to remove                                    | infobar |


## 示例
```yaml
  Skills:
  - barRemove{name="MyBossBar"} @self ~onInteract
```


<!--TAGS-->
<!--tag:BossBar-->
