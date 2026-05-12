## 描述
Fills a chest with a list of items, or a [droptable](/drops/DropTables)


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| items     | item, i   | Items to fill a chest with. Can be a comma-separated list of items, or a DropTable                                                                                      | NONE    |
| shouldStack | stack   | Should the given items stack if possible. true/false                 |         |
| shouldempty | empty   | Should the container be emptied before the items are added. true/false |       |


## 示例
Example of filling a chest with specific items.
```yaml
  Skills:
  - fillchest{i=diamond_sword,diamond} @Location{x=#;y=#;z=#} ~onDeath
```
##
Example of filling a chest with a droptable.
```yaml
  Skills:
  - fillchest{i=SkeletonKingDrops} @Location{x=#;y=#;z=#} ~onSpawn
```


## 别名
- [x] populateChest
- [x] fillContainer
- [x] populateContainer


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->
<!--tag:World-->
