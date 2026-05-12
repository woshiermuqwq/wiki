## 描述
Steals an item from the target and puts it in the mob's hand


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount to steal                                                  | 1       |
| dropchance | dc | Sets the chance 对于stolen item to be dropped upon death               | 0.0     |
| strict    | exact, e  | Whether the matcher should more strictly match the target item       | false   |
| types     | type, t, material, mat, m, item, i | The items to match. Can be a list           | DIRT    |
| vanillaonly | vanilla | Whether the matched item can only be a vanilla one                   | false   |
| onStealSkill | onsteal, then | The Metaskill to execute once an item is successfully stolen  |<!--type:Metaskill-->|

## 示例
```yaml
  Skills:
  - stealitem @trigger ~onDamaged 0.1 =100%
```


## 别名
- [x] steal
- [x] stealitems
- [x] itemsteal


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->
<!--tag:ItemMatcher-->
<!--tag:Meta-Mechanic:Thenable-->
