## 描述
检测触发技能的物品材料类型。仅配合特定的[触发器]使用。

## 属性
| 属性       | 别名                                  | 描述               | 默认值  |
| ---------- | ------------------------------------- | ------------------ | ------- |
| types      | type, t, material, mat, m, items, item, i | 要检测的[材料]列表 | DIRT<!--type:Material--><!--list--> |


## 示例
```yaml
  Conditions:
  - triggeritemtype{mat=STONE,DIRT,STONE_SWORD} true
```

## 别名
- [x] triggeringItemType


<!-- LINKS -->
[材料]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html
[触发器]: /Skills/Triggers
