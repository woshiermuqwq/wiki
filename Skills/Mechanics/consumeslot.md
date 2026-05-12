## 描述
Removes an item from a specific 栏位 of 玩家的 inventory.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 栏位      | s         | The inventory 栏位 to remove the item from. Accepts 栏位 0 to 35, or equipment 栏位.                                                                                         | HAND<!--type:EquipSlot--> |                                      
| amount    | a         | The amount of items to remove                                        | 1       |


## 示例
Would remove whatever item is in 栏位 0, or the first 栏位, of the nearest player's inventory
```yaml
  Skills:
  - consumeslot{slot=0;amount=1} @NearestPlayer{r=10}
```
##
Would remove whatever item is in the HAND equipment 栏位 the nearest player's inventory
```yaml
  Skills:
  - consumeslot{slot=HAND;amount=1} @NearestPlayer{r=10}
```


## 别名
- [x] consumeslotitem


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->