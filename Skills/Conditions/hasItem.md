## 描述
检测目标玩家或物品容器是否恰好拥有指定数量的指定材料物品。
使用 [物品匹配器](/Items/Item-Matcher)。

## 属性
| 属性        | 别名                          | 描述                             | 默认值    |
| ----------- | ----------------------------- | -------------------------------- | --------- |
| item        | i, material, m, type, t, mat, types | 要检测的物品                | DIRT<!--type:Item--> |
| amount      | a                             | 要检测的数量                      | >0       |
| strict      | exact, e                      | 匹配器是否更严格地匹配目标物品     | false    |
| vanillaonly | vanilla                       | 是否只匹配原版物品                 | false    |


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
