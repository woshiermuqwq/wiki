## 描述
检测触发技能所用的物品材料类型。
使用 [物品匹配器](/Items/Item-Matcher)。

## 属性
| 属性        | 别名                          | 描述                         | 默认值          |
| ----------- | ----------------------------- | ---------------------------- | --------------- |
| types       | type, t, material, mat, m, i, item | 要检测的[材料]列表        | DIRT<!--type:Item--><!--list--> |
| strict      | exact, e                      | 匹配器是否更严格地匹配目标物品 | false           |
| vanillaonly | vanilla                       | 是否只匹配原版物品             | false           |


## 示例
```yaml
  Conditions:
  - itemType{types=STONE,STONE_SWORD} true
```


<!-- LINKS -->
[materials]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html


<!--TAGS-->
<!--tag:ItemMatcher-->
