## 描述
Gives an item to the 目标. Supports Droptables.  

This 技能 do nothing when targeted 目标's have no space in its inventory.  

fakeLooting was added in 4.12 MM and it makes the item being given show up on the screen and fly toward 玩家的 inventory like when a player picks an item up off of the ground.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | items, i, type, t, material, mat, m | The item material (supports for Mythic生物' [Items](https://git.lumine.io/mythiccraft/Mythic生物/-/wikis/Items/Items) and [Droptables](https://git.lumine.io/mythiccraft/Mythic生物/-/wikis/掉落/掉落#掉落-tables)) You can specify an amount by putting a space and a number after the item name                | <!--type:Item-->|
| fakeLooting | dofakelooting, fl | Plays the pickup-item animation from the 原点            | false   |
| variable  | var       | The Item variable whose value is to be given as an actual item                 |


## 示例
```yaml
  Skills:
  - giveitem{i=diamond_sword} @PIR{r=20} ~onSpawn
  - ...
```
The below example would give 玩家的 6 cookies.
```yaml
  Skills:
  - giveitem{i=cookie 6} @PIR{r=20} ~onSpawn
  - ...
```


## 别名
- [x] give
- [x] giveitems
- [x] itemgive


<!--TAGS-->
<!--tag:Inventory-->
<!--tag:Item-->