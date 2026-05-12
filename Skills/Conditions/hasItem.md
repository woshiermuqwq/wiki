## 描述
测试目标玩家或物品容器是否恰好拥有指定数量的给定物品。  
使用[物品匹配器](/Items/Item-Matcher)进行匹配。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | i, material, m, type, t, mat, types | 要检查的物品                      | DIRT<!--type:Item-->|
| amount    | a         | 要检查的数量                                              | >0      |
| strict    | exact, e  | 匹配器是否应更严格地匹配目标物品       | false   |
| vanillaonly | vanilla | 匹配的物品是否仅限原版物品                   | false   |


## 示例
```yaml
  Conditions:
  - hasitem{i=stick;amount=>1} true
```
```yaml
  Conditions:
  - hasitem{i=my_custom_item;amount=<10} true
```
```yaml
  Conditions:
  - hasitem{i=mmoitems.SWORD.CUTLASS;amount=1to10} true
```


<!--TAGS-->
<!--tag:ItemMatcher-->