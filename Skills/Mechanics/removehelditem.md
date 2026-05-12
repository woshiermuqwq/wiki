## 描述
Removes the given amount from the casting player's held item. 

> **This is a no-target 机制, and the affected player will always be the caster**

<details><summary>Easier Alternative:</summary>
The [consumeslot](skills/mechanics/consumeslot) 机制 is likely an easier choice for most use-cases, since it can target entities directly and choose which slot to remove from.
</details>

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount to remove                                                 | 1       |


## 示例
As a skill that only targets the casting player, a mob may need to use a [sudoskill](skills/mechanics/sudoskill) to remove the player's item:
```yaml
munchy:
  Type: PIG
  Skills:
  - SudoSkill{s=removeApple} @trigger ~onInteract
```
This will cause a player to cast the `removeApple` meta-skill when right-clicking the mob:
```yaml
removeApple:
  Conditions:
  - holding{m=APPLE} true
  Skills:
  - removeHeldItem{amount=1}
```
This example checks for if the player (now the caster) is holding an apple, and if so, remove 1 from their hand.


## 别名
- [x] consumeHeldItem
- [x] takeHeldItem


<!--TAGS-->
<!--tag:Item-->
<!--tag:Inventory-->
