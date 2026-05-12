## 描述
匹配目标生物脚下所站的方块。
可用材料列表可在 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) 中找到。

## 属性

| 属性       | 别名                              | 描述                                                   | 默认值  |
| ---------- | --------------------------------- | ------------------------------------------------------ | ------- |
| material   | types, type, t, mat, m, block, b  | 要匹配的材料列表。匹配任一即通过。支持通配符和方块标签  | STONE<!--type:Block--><!--list--> |


## 示例
```yaml
  TargetConditions:
  - onblock{m=BEDROCK,OAK_LEAVES,ACACIA_FENCE} false
```

```yaml
  TargetConditions:
  - onblock{m=DIRT,STONE,GRAVEL} true
```
