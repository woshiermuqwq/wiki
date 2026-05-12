## 描述
Gives the caster an item while playing the pickup-item animation from the target entity or location when fakelooting is set to true.

Gives the caster an item from the target entity or location when fakelooting is set to false.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | items, i  | The item material (supports for mythicmobs item)                     |<!--type:Item-->|
| fakeLooting | dofakelooting, fl | plays the pickup-item animation from the target            | true    |


## 示例
```yaml
  Skills:
  - giveitem{i=diamond_sword;a=1} @PIR{r=20} ~onSpawn
```


## 别名
- [x] givefromtarget
- [x] giveitemsfromtarget
- [x] itemgivefromtarget


<!--TAGS-->
<!--tag:Inventory-->
<!--tag:Item-->
