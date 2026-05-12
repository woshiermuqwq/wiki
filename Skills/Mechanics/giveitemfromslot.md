## 描述
Gives a copy of 施法者的 栏位 to the 目标.  

Won't consume the item in the given 栏位 of 施法者.  

This 技能 does nothing when the 目标 has no space in its inventory.  

fakeLooting was added in 4.12 and it makes the item being given show up on the screen and fly toward 玩家的 inventory like when a player picks an item up off of the ground.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 栏位        | s       | 施法者的 [栏位](/Skills/EquipSlot)                               | <!--type:EquipSlot--> |
| fakeLooting | fl, dofakelooting | Plays the pickup-item animation from the 原点            | false   |



## 示例
Give 施法者's main hand item to all players on the server, and plays the pickup animation.
```yaml
  Skills:
  - giveitemfromslot{slot=HAND;fakelooting=true} @server ~onTimer:10
```


## 别名
- [x] givefromslot


<!--TAGS-->
<!--tag:Inventory-->
<!--tag:Item-->