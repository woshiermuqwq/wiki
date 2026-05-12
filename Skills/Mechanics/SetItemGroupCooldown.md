## 描述
Sets the cooldown on an item group 对于target player


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| key       | k, group, g | The group to set the cooldown to                      | minecraft:item_group |
| ticks     | t         | The amount of ticks the cooldown will last                           | 20      |



## 示例
```yaml
  Skills:
  - SetItemGroupCooldown{key=yournamespace.teleportingitems;ticks=200}
```
