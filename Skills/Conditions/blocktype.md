## 描述
检测目标位置处的材料类型是否为指定类型。
支持所有 [Spigot 材料类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)、通配符和方块标签。

## 属性
| 属性      | 别名                                  | 描述                                                  | 默认值 |
| --------- | ------------------------------------- | ----------------------------------------------------- | ------ |
| types     | type, t, material, mat, m, block, b   | 要检测的材料列表或 MMOItem 方块名称。支持通配符和方块标签 | DIRT<!--type:Block--><!--list--> |


## 示例
```yaml
  Conditions:
  - blocktype{type=dirt} true
```

```yaml
  Conditions:
  - blockType{type=#leaves,*_log,redstone_torch[lit=true]}
```

## 别名
- [x] inblock
- [x] insideblock
