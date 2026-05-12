## 描述
检查指定位置周围半径内指定方块类型的数量。

## 属性
| 属性      | 别名                                  | 描述                                      | 默认值 |
| --------- | ------------------------------------- | ----------------------------------------- | ------ |
| types     | type, t, material, mat, m, b, block   | 要检测的[材料]列表                         | DIRT<!--type:Block--><!--list--> |
| radius    | r                                     | 检测半径                                   | 8      |
| amount    | a                                     | 需要匹配的方块数量                          | >0     |


## 示例
```yaml
  TargetConditions:
  - blockTypeInRadius{type=STONE;amount=>10;radius=3} true
```


<!-- LINKS -->
[materials]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html
