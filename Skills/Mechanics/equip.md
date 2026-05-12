## 描述
Equips the 生物 with an item. Uses the exact same syntax as the
[Equipment](/生物/equipment) configuration.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | items, i, equipment, equip, e | The item config string to run on the 生物.           |      |


## 示例
此示例将 equip the casting 生物 with a diamond sword.
```yaml
EquipDiamondSword:
  Skills:
  - equip{item=diamond_sword HAND}
```

此示例将 equip the Skeleton King's crown as a helmet.
```yaml
EquipCrown:
  Skills:
  - equip{item=KingsCrown HEAD}
```


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->