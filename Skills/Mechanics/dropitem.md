## 描述
Drops a set of items or optionally a
[DropTable](/drops/DropTables).


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| items     | item, i   | Items to drop. Can be a comma-separated list of items, or a DropTable. You can specify an amount by putting a space and a number after the item name. | NONE<!--type:Item-->|
| naturally | natural, n | Whether the items 应当 dropped naturally                       | true    |
| onDropSkill | onDrop, then | [Metaskill] to be execute when the item drops. Inherits the dropped item entity as the target(s) |<!--type:Metaskill-->|

## 示例
Example of dropping specific items.
```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond} @self ~onDeath
  - ...
```
The below example will drop a Diamond Sword and 5 Diamonds
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
- [x] drop
- [x] dropitems
- [x] itemdrop


<!-- LINKS -->
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Item-->
<!--tag:Meta-Mechanic:Thenable-->
