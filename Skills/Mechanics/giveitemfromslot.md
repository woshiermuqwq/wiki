## 描述
Gives a copy of the caster's slot to the target.  

Won't consume the item in the given slot of caster.  

This 技能 does nothing when the target has no space in its inventory.  

fakeLooting was added in 4.12 and it makes the item being given show up on the screen and fly toward the players inventory like when a player picks an item up off of the ground.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| slot        | s       | The caster's [slot](/Skills/EquipSlot)                               | <!--type:EquipSlot--> |
| fakeLooting | fl, dofakelooting | Plays the pickup-item animation from the origin            | false   |



## 示例
Give caster's main hand item to all players on the server, and plays the pickup animation.
```yaml
  Skills:
  - giveitemfromslot{slot=HAND;fakelooting=true} @server ~onTimer:10
```


## 别名
- [x] givefromslot


<!--TAGS-->
<!--tag:Inventory-->
<!--tag:Item-->
