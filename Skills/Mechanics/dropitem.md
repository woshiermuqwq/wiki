## 描述
掉落 a set of items or optionally a
[DropTable](/掉落/DropTables).


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| items     | item, i   | Items to 掉落. Can be a comma-separated list of items, or a DropTable. You can specify an amount by putting a space and a number after the item name. | NONE<!--type:Item-->|
| naturally | natural, n | 是否 the items should be dropped naturally                       | true    |
| onDropSkill | onDrop, then | [Metaskill] to be 执行 when the item 掉落. Inherits the dropped item entity as the 目标(s) |<!--type:Metaskill-->|

## 示例
Example of dropping specific items.
```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond} @self ~onDeath
  - ...
```
The below example will 掉落 a Diamond Sword and 5 Diamonds
```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond 5} @self ~onDeath
  - ...
```
##
Example of dropping items from a DropTable.
```yaml
  Skills:
  - dropitem{i=SkeletonKingDrops} @self ~onSpawn
  - ...
```


## 别名
- [x] 掉落
- [x] dropitems
- [x] itemdrop


<!-- LINKS -->
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Item-->
<!--tag:Meta-Mechanic:Thenable-->