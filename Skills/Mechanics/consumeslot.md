## 描述
Removes an item from a specific slot of the player's inventory.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| slot      | s         | The inventory slot to remove the item from. Accepts Slots 0 to 35, or equipment slots.                                                                                         | HAND<!--type:EquipSlot--> |                                      
| amount    | a         | The amount of items to remove                                        | 1       |


## 示例
Would remove whatever item is in slot 0, or the first slot, of the nearest player's inventory
```yaml
  Skills:
  - consumeslot{slot=0;amount=1} @NearestPlayer{r=10}
```
##
Would remove whatever item is in the HAND equipment slot the nearest player's inventory
```yaml
  Skills:
  - consumeslot{slot=HAND;amount=1} @NearestPlayer{r=10}
```


## 别名
- [x] consumeslotitem


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->
