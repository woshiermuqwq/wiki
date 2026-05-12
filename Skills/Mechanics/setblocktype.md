## 描述
Change blocktype at 目标 location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m, mat, t, type, types, block, b | The material for the block to 设为                              | [DIRT](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html "CLICK ME to view valid block materials")<!--type:Block-->                                            |
| physics   | p         | 是否 to apply physics to the affected area                        | true    |


## 示例
Sets a block at the location of the 施法者
```yaml
SetBlockExample:
  Skills:
  - setblock{m=STONE} @selflocation
```
##
Sets a mmoitems block at the location of the 目标
```yaml
SetMMOItemsBlock:
  Skills:
  - setblock{m=mmoitems:50} @targetlocation
```
##
Sets a block with specified blockstates at the location of the 目标
```yaml
SetButton:
 Skills:
 - setblock{m=JUNGLE_BUTTON[facing=east,face=floor]} @targetlocation
```


## 别名
- [x] setblock


<!--TAGS-->
<!--tag:World-->