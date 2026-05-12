## 描述
检查触发技能的方块材料类型。仅适用于特定的[触发器]。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| types     | type, t, material, mat, m, block, b | 要检查的[材料]列表               | DIRT<!--type:Block--> |


## 示例
```yaml
  Conditions:
  - triggerblocktype{mat=STONE,DIRT} true
```


## 别名
- [x] triggeringBlockType


<!-- LINKS -->
[材料]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html
[触发器]: /Skills/Triggers