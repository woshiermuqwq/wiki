## 描述
检测目标是否手持指定的材料物品。
使用 [物品匹配器](/Items/Item-Matcher)。

## 属性
| 属性        | 别名                          | 描述                                       | 默认值          |
| ----------- | ----------------------------- | ------------------------------------------ | --------------- |
| material    | m, type, t, item, i, mat, types | 要检测的材料、MythicItem 或 MMOItems 内部 ID |<!--type:Item--> |
| strict      | exact, e                      | 匹配器是否更严格地匹配目标物品               | false           |
| vanillaonly | vanilla                       | 是否只匹配原版物品                           | false           |


## 示例
```yaml
# 确保材料名称全部大写，否则控制台会提示不是有效材料！
Conditions:
- holding{m=DIAMOND_SWORD} true
```
使用 MMOItems 中物品的示例。格式为 `mmoitems.分类.物品`：
```yaml
Conditions:
- holding{m=mmoitems.TOOL.PICKAXE_5} true
```


<!--TAGS-->
<!--tag:ItemMatcher-->
