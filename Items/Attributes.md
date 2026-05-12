使用MythicMobshandles the Minecraft 属性 system的The 属性 section for 物品。
It makes it possible to 应用 different 属性 给予 the 实体 wearing/using the 物品 取决于 the 栏位.

[[_TOC_]]

## 格式
```yml
Item:
  Id: item_id
  Attributes:
    [Slot]:
      [Attribute]: [value] <operation> 
```


## 栏位
| 栏位 | Description |
|----------|---------------------------------------------------------------------------|
| All |将应用the given 属性 to all 栏位. |。
| MainHand | 属性 只会 应用 if 物品 is being held in the main hand. |
| OffHand | 属性 只会 应用 if 物品 is being held in the off hand. |
| Head | 属性 只会 应用 if 物品 is being worn on the head 栏位. |
| Chest | 属性 只会 应用 if 物品 is being worn on the chest/torso 栏位. |
| Legs | 属性 只会 应用 if 物品 is being worn on the legs 栏位. |
| Feet | 属性 只会 应用 if 物品 is being worn on the feet 栏位. |


## 值
You can input 两者都 absolute or relative 值:
- To input an absolute 值, 仅仅 write it out
```yaml
      Damage: 10 ADD
```
- To input a relative 值, use a % symbol 之后 it
```yaml
      Damage: 10% ADD
```


## Operations
| Operation | 别名 | Description |
|---------------|--------------------|---------------------------------------------------------------------------------------------------|
| 添加 | 0, ADD_NUMBER | 添加 or subtracts the specified 值 to the base 值. |
| MULTIPLY_BASE | 1, ADD_SCALAR | Multiplies the base 值 与 sum of all the modifier 数量. |
| MULTIPLY | 2, MULTIPLY_SCALAR | Similar to `MULTIPLY_BASE` but multiplies all the modifier 数量 而不是 adding all of them |

[*See MC wiki on how the game calculates the 值 for all modifiers*](https://Minecraft.wiki/w/属性#Modifiers)


## 属性
These are all the available 属性 that can be put on the 物品.
YoYou can use general 占位符 like `<random.#to#>` or `<random.float.#to#>`.
You can find out more ab移除se 属性 by looking at [The Minecraft Wiki page regarding them](https://Minecraft.wiki/w/属性#属性)

### AttackSpeed
决定the recharge rate of a fully charged 攻击。
```yml
custom_item:
  Id: stick
  Attributes:
    MainHand:
      AttackSpeed: 0.1 MULTIPLY
```

### Armor
设数量 of armor。
1 armor is 等于 0.5 armor plates.
原版 caps the 数量 to 30.
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      Armor: 2
```

### ArmorToughness
Alters the 伤害 reduction percentage of the armor 属性. [MC wiki](https://Minecraft.wiki/Armor#Armor_toughness).
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      ArmorToughness: 0.5
```

### 伤害
设伤害 dealt by melee 攻击。
1 伤害 equals to 0.5 hearts of 伤害 dealt (没有 armor).
```yml
custom_item:
  Id: stick
  Attributes:
    All:
      Damage: 0.2 ADD_SCALAR
```

### 血量
The maximum 血量 modifier the user can have when 也 holding or wearing the 物品.
1 血量 equals to 0.5 hearts.
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    MainHand:
      Health: 2 ADD
```

### Luck
S设数量 of luck modifier of the 物品。
This modifier affects the 结果 of loot tables and 也 the [生物 掉落](/掉落/掉落).
```yml
custom_item:
  Id: stick
  Attributes:
    OffHand:
      Luck: -10 ADD
```

### KnockbackResistance
设horizontal scale knockback resisted from 攻击。
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      KnockbackResistance: 2 MULTIPLY_BASE
```

### MovementSpeed
设移动 速度 modifier of the 物品。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MovementSpeed: -0.2 MULTIPLY_BASE
```

### MaxAbsorption
ThThe maximum absorption of this 生物.
决定the highest 血量 they may gain by the Absorption 效果。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MaxAbsorption: 1 ADD
```

### Scale
The multiplier of the size of an 实体
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      Scale: 2 ADD
```

### StepHeight‌
Th方块 that an 实体 can step up 没有 jumping. Sneaking 仅 阻止 掉落 from heights 即 higher than this 属性.[5] This 仅 happens if the 高度 that the 玩家 is above a 方块 is equal or 小于 the 属性的maximumnumber。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      StepHeight‌: 2 ADD
```

### JumpHeight
The 高度 an 实体 can jump, 类似 the Jump Boost 效果
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      JumpHeight: 2 ADD
```

### BlockInteractionRange
玩家 in 方块的方块 interaction范围。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BlockInteractionRange: 2 ADD
```

### EntityInteractionRange
玩家 in 方块的实体 interaction范围。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      EntityInteractionRange: 2 ADD
```

### BlockBreakSpeed
The 速度 the 玩家 can break 方块 as a multiplier
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BlockBreakSpeed: 2 ADD
```

### Gravity
The gravity affecting an 实体 in 方块 per tick squared
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      Gravity: 2 ADD
```

### SafeFallDistance
方块 the 实体 必须 fall to make fallling 粒子 and sounds的number of 方块 an 实体 can fall 之前 fall 伤害 starts to be accumulated. Also the minimum数量。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SafeFallDistance: 2 ADD
```

### FallDamageMultiplier‌
The 数量 of fall 伤害 an 实体 takes as a multiplier
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      FallDamageMultiplier‌: 2 ADD
```

## 示例
This 示例 物品 will grant +10 luck when the 物品 is held in the main
hand, but will grant +7 luck and +2 extra 伤害 if the 物品 is held in
the offhand 栏位:
```yml
lucky_charms:
  Id: potato_item
  Display: 'Rotten Lucky Charm'
  Attributes:
    MainHand:
      Luck: 10
    OffHand:
      Luck: 7
      Damage: 2
```
This 示例 物品 grants +2 extra 血量 no matter which 栏位 the 物品 is being held, but 还将 grant +4% 移动 速度 if the 物品 is worn in the feet 栏位:
```yml
happy_feet:
  Id: leather_boots
  Display: 'Penguin Hide'
  Attributes:
    All:
      Health: 2
    Feet:
      MovementSpeed: 0.04
```
Each time this 物品 is generated 它将 have a random 伤害 值 between 3 and 5 and a random 速度 bonus between 1% and 5% when worn in the main hand:
```yml
lucky_sword:
  Id: wood_sword
  Display: '<yellow>Lucky Sword</yellow>'
  Attributes:
    MainHand:
      Damage: 3-5
      MovementSpeed: 0.01-0.05 MULTIPLY_BASE
```