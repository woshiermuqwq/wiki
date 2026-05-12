## 描述
检测目标玩家的物品栏指定槽位中的物品是否与给定的物品相似。
具体来说，会比较它们的 ItemStack，匹配则返回 true。

## 属性

| 属性       | 别名                      | 描述                                           | 默认值    |
| ---------- | ------------------------- | ---------------------------------------------- | --------- |
| item       | i, material, m, mm, mythicitem | 要检测的物品                               | DIRT<!--type:Item--> |
| slot       | s                         | 要检测的物品栏槽位。支持 0 到 35，或装备槽位      | HAND<!--type:EquipSlot--> |


## 示例
检测目标玩家物品栏第 0 槽（第一个槽位）的物品。
```yml
  Conditions:
  - itemissimilar{i=MyCustomItem;slot=0} true
```

## 别名
- [x] issimilar
- [x] similarto
