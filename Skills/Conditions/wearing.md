## 描述
此条件检查目标实体是否穿戴了指定物品。  
使用[物品匹配器](/Items/Item-Matcher)进行匹配。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| armorslot | slot, s   | 要检查的[物品槽位](/Skills/EquipSlot)。       | HEAD<!--type:EquipSlot--> |
| material  | mat, m, item, i, t, type, types | 要检查的材料或 MythicItem 名称。也支持 MMOItems，格式为 mmoitems.TYPE.ID                                               | DIRT <!--type:Item-->   |
| strict    | exact, e  | 匹配器是否应更严格地匹配目标物品       | false   |
| vanillaonly | vanilla | 匹配的物品是否仅限原版物品                   | false   |

## 示例
```yaml
Conditions:
  - wearing{slot=HAND;m=IRON_SWORD} true
  - wearing{slot=CHEST;m=mmoitems.TYPE.ID} true
```


## 别名
- [x] iswearing 
- [x] wielding 
- [x] iswielding


<!--TAGS-->
<!--tag:ItemMatcher-->