## 描述
Removes the given amount from the casting player's held item. 

> **This is a no-目标 技能, and the affected player will always be the 施法者**

<details><summary>Easier Alternative:</summary>
The [consumeslot](skills/技能/consumeslot) 技能 is likely an easier choice for most use-cases, since it can 目标 entities directly and choose which 栏位 to remove from.
</details>

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount to remove                                                 | 1       |


## 示例
As a skill that only 目标 the casting player, a 生物 may need to use a [sudoskill](skills/技能/sudoskill) to remove 玩家的 item:
```yaml
munchy:
  Type: PIG
  Skills:
  - SudoSkill{s=removeApple} @trigger ~onInteract
```
This will cause a player to 施放 the `removeApple` meta-skill when right-clicking the 生物:
```yaml
removeApple:
  Conditions:
  - holding{m=APPLE} true
  Skills:
  - removeHeldItem{amount=1}
```
This example checks for if the player (now the 施法者) is holding an apple, and if so, remove 1 from their hand.


## 别名
- [x] consumeHeldItem
- [x] takeHeldItem


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->