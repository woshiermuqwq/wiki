## 描述
Equips the mob with an item. Uses the exact same syntax as the
[Equipment](/mobs/equipment) configuration.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | items, i, equipment, equip, e | The item config string to run on the mob.           |      |


## 示例
This example would equip the casting mob with a diamond sword.
```yaml
EquipDiamondSword:
  Skills:
  - equip{item=diamond_sword HAND}
```

This example would equip the Skeleton King's crown as a helmet.
```yaml
EquipCrown:
  Skills:
  - equip{item=KingsCrown HEAD}
```


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->
