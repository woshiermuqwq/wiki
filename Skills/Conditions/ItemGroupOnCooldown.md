## 描述
检查目标玩家的指定物品组是否处于冷却中。  
另请参阅相关的 [SetItemGroupCooldown 机制](/Skills/Mechanics/SetItemGroupCooldown)。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| group     | g         | 要检查的组                                           |         |


## 示例
```yaml
  Conditions:
  - ItemGroupOnCooldown{g=teleportingitems}
```