## 描述
Sets the 冷却 on an item group for the 目标 player


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| key       | k, group, g | The group to set the 冷却 to                      | minecraft:item_group |
| ticks     | t         | The amount of ticks the 冷却 将持续                           | 20      |



## 示例
```yaml
  Skills:
  - SetItemGroupCooldown{key=yournamespace.teleportingitems;ticks=200}
```