MythicMobs 物品的属性部分负责处理 Minecraft 的属性系统。
它可以根据物品所在的槽位，为穿戴/持有该物品的实体赋予不同的属性。

[[_TOC_]]

## 格式
```yml
Item:
  Id: item_id
  Attributes:
    [Slot]:
      [Attribute]: [value] <operation> 
```


## 槽位
| 槽位 | 说明 |
|----------|---------------------------------------------------------------------------|
| All      | 将给定的属性应用到所有槽位。 |
| MainHand | 属性仅在物品位于主手时生效。 |
| OffHand  | 属性仅在物品位于副手时生效。 |
| Head     | 属性仅在物品穿戴在头部槽位时生效。 |
| Chest    | 属性仅在物品穿戴在胸甲槽位时生效。 |
| Legs     | 属性仅在物品穿戴在护腿槽位时生效。 |
| Feet     | 属性仅在物品穿戴在靴子槽位时生效。 |


## 属性值
你可以使用绝对值或相对值：
- 输入绝对值，直接写数字即可：
```yaml
      Damage: 10 ADD
```
- 输入相对百分比，在数字后面加 `%`：
```yaml
      Damage: 10% ADD
```


## 运算方式
| 运算 | 别名 | 说明 |
|---------------|--------------------|---------------------------------------------------------------------------------------------------|
| ADD           | 0, ADD_NUMBER      | 在基础值上加上或减去指定数值。 |
| MULTIPLY_BASE | 1, ADD_SCALAR      | 将基础值乘以所有修饰符数值的总和。 |
| MULTIPLY      | 2, MULTIPLY_SCALAR | 类似于 `MULTIPLY_BASE`，但会将所有修饰符的数值相乘而不是相加。 |

[*参见 MC Wiki 了解游戏如何计算所有修饰符的最终值*](https://minecraft.wiki/w/Attribute#Modifiers)


## 属性列表
以下是所有可附加到物品上的属性。
你可以使用通用占位符，如 `<random.#to#>` 或 `<random.float.#to#>`。
你可以查阅 [Minecraft Wiki 属性页面](https://minecraft.wiki/w/Attribute#Attributes)获取更多信息。

### AttackSpeed（攻击速度）
决定完全蓄力攻击的冷却速率。
```yml
custom_item:
  Id: stick
  Attributes:
    MainHand:
      AttackSpeed: 0.1 MULTIPLY
```

### Armor（护甲值）
设置护甲点数。
1 点护甲等于 0.5 个护甲图标。
原版上限为 30。
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      Armor: 2
```

### ArmorToughness（护甲韧性）
修改护甲属性的伤害减免百分比。[MC Wiki](https://minecraft.wiki/Armor#Armor_toughness)。
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      ArmorToughness: 0.5
```

### Damage（伤害）
设置近战攻击造成的伤害。
1 点伤害等于 0.5 颗心的伤害量（无护甲时）。
```yml
custom_item:
  Id: stick
  Attributes:
    All:
      Damage: 0.2 ADD_SCALAR
```

### Health（生命值）
持有或穿戴物品时，使用者的最大生命值修正。
1 点生命值等于 0.5 颗心。
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    MainHand:
      Health: 2 ADD
```

### Luck（幸运）
设置物品的幸运修正值。
此修正会影响战利品表的结果，也会影响[生物掉落](/drops/Drops)。
```yml
custom_item:
  Id: stick
  Attributes:
    OffHand:
      Luck: -10 ADD
```

### KnockbackResistance（击退抗性）
设置承受攻击时水平方向击退的抗性倍率。
```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      KnockbackResistance: 2 MULTIPLY_BASE
```

### MovementSpeed（移动速度）
设置物品的移动速度修正值。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MovementSpeed: -0.2 MULTIPLY_BASE
```

### MaxAbsorption（最大吸收值）
此生物的最大吸收生命值。
决定了通过吸收效果能获得的最高生命值。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MaxAbsorption: 1 ADD
```

### Scale（体型倍率）
实体大小的倍率。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      Scale: 2 ADD
```

### StepHeight（跨越高度）
实体无需跳跃即可跨上的最大方块高度。潜行只会阻止从高于此属性的高度跌落。仅当玩家高于方块的垂直高度小于或等于此属性时才会触发跨越。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      StepHeight‌: 2 ADD
```

### JumpHeight（跳跃高度）
实体能跳的高度，类似于跳跃提升效果。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      JumpHeight: 2 ADD
```

### BlockInteractionRange（方块交互距离）
玩家的方块交互范围，以方块为单位。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BlockInteractionRange: 2 ADD
```

### EntityInteractionRange（实体交互距离）
玩家的实体交互范围，以方块为单位。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      EntityInteractionRange: 2 ADD
```

### BlockBreakSpeed（方块破坏速度）
玩家破坏方块的速度倍率。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BlockBreakSpeed: 2 ADD
```

### Gravity（重力）
作用于实体的重力，单位为方块/刻²。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      Gravity: 2 ADD
```

### SafeFallDistance（安全坠落距离）
实体在开始累积摔落伤害之前可以坠落的最大方块数，同时也是产生摔落粒子和音效所需的最小坠落高度。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SafeFallDistance: 2 ADD
```

### FallDamageMultiplier（摔落伤害倍率）
实体承受摔落伤害的倍率。
```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      FallDamageMultiplier‌: 2 ADD
```

## 示例
以下示例物品在主手时会提供 +10 幸运，在副手时则提供 +7 幸运和 +2 额外伤害：
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
以下示例物品不管放在哪个槽位都提供 +2 额外生命值，但如果穿在脚上还会提供 +4% 移动速度：
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
以下物品每次生成时都会在主手槽位获得 3 到 5 之间的随机伤害值，以及 1% 到 5% 之间的随机速度加成：
```yml
lucky_sword:
  Id: wood_sword
  Display: '<yellow>Lucky Sword</yellow>'
  Attributes:
    MainHand:
      Damage: 3-5
      MovementSpeed: 0.01-0.05 MULTIPLY_BASE
```