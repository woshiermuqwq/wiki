## 描述
检查目标是否手持给定的物品。  
使用[物品匹配器](/Items/Item-Matcher)进行匹配。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m, type, t, item, i, mat, types | 要检查的材料、MythicItem 或 MMOItems 内部 ID |<!--type:Item-->|
| strict    | exact, e  | 匹配器是否应更严格地匹配目标物品       | false   |
| vanillaonly | vanilla | 匹配的物品是否仅限原版物品                   | false   |


## 示例
```yaml
# 请确保材料名称使用全大写，否则控制台会提示不是有效材料！
Conditions:
- holding{m=DIAMOND_SWORD} true
```
以下是使用 MMOItems 物品的示例。格式为：mmoitems.类别.物品
```yaml
Conditions:
- holding{m=mmoitems.TOOL.PICKAXE_5} true
```


<!--TAGS-->
<!--tag:ItemMatcher-->