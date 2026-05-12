## 描述
检查触发技能的物品的材料类型。  
使用[物品匹配器](/Items/Item-Matcher)进行匹配。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| types     | type, t, material, mat, m, i, item | 要检查的[材料]列表               | DIRT<!--type:Item--><!--list-->|
| strict    | exact, e  | 匹配器是否应更严格地匹配目标物品       | false   |
| vanillaonly | vanilla | 匹配的物品是否仅限原版物品                   | false   |


## 示例
```yaml
  Conditions:
  - itemType{types=STONE,STONE_SWORD} true
```


<!-- LINKS -->
[材料]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html


<!--TAGS-->
<!--tag:ItemMatcher-->