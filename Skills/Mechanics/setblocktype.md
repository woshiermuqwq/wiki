## 描述
Change blocktype at target location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m, mat, t, type, types, block, b | The material 对于block to be set to                              | [DIRT](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html "CLICK ME to view valid block materials")<!--type:Block-->                                            |
| physics   | p         | Whether to apply physics to the affected area                        | true    |


## 示例
Sets a block 在location of the caster
```yaml
SetBlockExample:
  Skills:
  - setblock{m=STONE} @selflocation
```
##
Sets a mmoitems block 在location of the target
```yaml
SetMMOItemsBlock:
  Skills:
  - setblock{m=mmoitems:50} @targetlocation
```
##
Sets a block with specified blockstates 在location of the target
```yaml
SetButton:
 Skills:
 - setblock{m=JUNGLE_BUTTON[facing=east,face=floor]} @targetlocation
```


## 别名
- [x] setblock


<!--TAGS-->
<!--tag:World-->
