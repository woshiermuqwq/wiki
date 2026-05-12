## 描述
检查目标玩家背包槽位中的物品是否与指定物品相似。  
具体来说，将比较它们的物品栈，如果匹配则条件返回 true。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | i, material, m, mm, mythicitem | 要检查的物品                           | DIRT<!--type:Item-->|
| slot      | s         | 要检查的背包槽位。接受 0 到 35，或装备槽位 | HAND<!--type:EquipSlot-->|


## 示例
测试目标玩家背包中槽位 0（即第一个槽位）的物品。
```yml
  Conditions:
  - itemissimilar{i=MyCustomItem;slot=0} true
```


## 别名
- [x] issimilar
- [x] similarto