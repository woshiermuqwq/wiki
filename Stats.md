# 介绍

属性（Stats）是影响玩家、生物、物品、技能等各种机制的值。
虽然属性系统一开始学起来可能比较复杂，但它的多功能性将让你能够实现非常高级的效果，如战斗系统改造、技术工具以及全新游戏设计元素的创建。

属性在 `stats.yml` 文件中定义。该文件可以存放在 MythicMobs 根目录（`/plugins/MythicMobs/`）或[包](MythicMobs/-/wikis/Packs)文件夹中。

> ⚠️ 警告：要在物品上使用属性，必须安装 [Crucible](/../../../mythiccrucible/-/wikis/home)

- [自定义属性选项](#自定义属性选项)
  - [自定义属性类型](#自定义属性类型)
  - [特定类型选项](#特定类型选项)
  - [提示文本格式化](#提示文本格式化)
- [修正器](#修正器)
- [内置属性](#内置属性)
- [配置实现](#配置实现)
  - [生物](#生物)
  - [物品](#物品)
- [示例](#示例)
  - [自定义属性示例](#自定义属性示例)


# 自定义属性选项
可在属性中使用以更好进行自定义的选项

| 选项               |描述                                                                      |
|----------------------|---------------------------------------------------------------------------------|
| Enabled              | 该属性当前是否启用                                                |
| AlwaysActive         | 该属性是否强制应用于每个实体的每一个注册表                                     |
| Type                 | 属性的[类型](Stats#自定义属性类型)                                 |
| Display              | 属性显示的名称                                       |
| Formatting           | 属性在物品上的显示方式。取决于所使用的修正器                    |
| ShowInLore           | 是否在每个修正器的物品描述中显示提示文本                       |
| Priority             | 该属性相对于其他属性的生效优先级。*较低*的值使该属性*先于*较高值的属性触发 |
| MinValue             | 属性的最小值                                                      |
| MaxValue             | 属性的最大值                                                          |
| Triggers             | 触发属性效果的是什么。可以是任何 MythicMobs 触发器，去掉 "on" 前缀。<br />（例如：要使用 `onAttack`，需要写入 `ATTACK` 作为触发器）<br />截至 v.5.4.0，仅支持伤害类触发器；请关注开发构建版本以获取扩展功能。|
| ParentStats          | 该属性所依赖的其他属性的列表                                  |
| TriggerStats         | 触发实体可能拥有的属性列表及其 FormulaKey，以空格分隔。然后可在其他公式中使用 FormulaKey 来获取触发实体的值。[这里是示例](#ice_damage) |
| Formula              | 如果此属性有父属性，则为其基值的计算公式                      |
| FormulaKey           | 当此属性是另一个属性的父属性时，可在公式中使用的键          |
| BaseValue            | 如果没有父属性时的静态基值                                  |
| ExecutionPoint       | 对于修改触发器的属性，可以是 `PRE` 或 `POST`。决定属性是在任何机制之前还是之后被评估 |
| Skills               | 当属性激活时执行的技能                         |

## 自定义属性类型
`Type` 选项可设置的值
| Type                 |描述                                                                      |
|----------------------|---------------------------------------------------------------------------------|
| `STATIC`             | 静态值。本身不做任何事，但可通过占位符引用 |
| `DAMAGE_BONUS`       | 此属性增加固定数值的额外伤害                                    |
| `DAMAGE_MODIFIER`    | 使用公式修改伤害                                             |
| `PROC`               | 执行技能的概率                                                      | 

## 特定类型选项
仅在属性中使用特定类型时才可用的选项列表

### DAMAGE_MODIFIER

| 选项               |描述                                                                      |
|----------------------|---------------------------------------------------------------------------------|
| DamageType           | 指定自定义伤害类型。使用 `ALL` 来修改技能的最终总伤害                  |
| Conditions           | 指定可影响修正器的条件                                |
| DamageFormula        | 定义伤害如何被修改的公式。参见[此处](#fire_resistance)示例<br>伤害公式可以使用的一些额外键：<br>- `d` 表示伤害的原始值<br>- `v` 表示属性的值 |

### DAMAGE_BONUS

| 选项               |描述                                                                      |
|----------------------|---------------------------------------------------------------------------------|
| DamageType           | 指定自定义伤害类型                                                    |


## 提示文本格式化
| Formatting           |描述                                                                      |
|----------------------|---------------------------------------------------------------------------------|
| Additive             | 为加算修正器显示的提示文本                                      |
| Multiply             | 为乘算修正器显示的提示文本                                      |
| Compound             | 为复合修正器显示的提示文本                                      |
| Setter               | 为覆写修正器显示的提示文本                                        |
| Rounding             | 属性值中小数点后的数字位数                  |
| ShowInItemLore       | 每当使用 `{stats-each}` 时，是否在物品描述中显示提示文本。默认为 true，如果设置了 ShowInLore 选项则被覆盖 |

| ShowInLore           | 描述                                                                     |
|----------------------|---------------------------------------------------------------------------------|
| Additive             | 是否在物品描述中显示加减修正器提示文本                 |
| Multiply             | 是否在物品描述中显示乘算修正器提示文本                 |
| Compound             | 是否在物品描述中显示复合修正器提示文本                 |
| Setter               | 是否在物品描述中显示覆写修正器提示文本                   |

```yml
EXAMPLE_STAT:
  Enabled: true
  AlwaysActive: false
  Type: STATIC
  FormulaKey: 'SPD'
  Formatting:
    Additive: '+<value> 速度'
    Multiply: '+<value>% 速度'
    Compound: 'x<value>% 速度'
    Static: '强制 <value> <display>'
    Rounding: 2
  ShowInLore:
    Compound: false # 可选
```

# 修正器
修正器可用于在属性基值定义之后对其进行调整。
| 修正器             |描述                                                                                        |
|----------------------|---------------------------------------------------------------------------------------------------|
| `ADDITIVE`           | 为属性基值添加固定值                                                                  |
| `ADDITIVE_MULTIPLIER`| 为属性基值添加乘数                                                        |
| `COMPOUND_MULTIPLIER`| 将属性基值乘以乘数，然后加到基值上                               |
| `SETTER`             | 覆盖所有修正器和基值，强制属性为指定值                                                |

请注意，属性修正器可以由实体、玩家、物品、附魔和光环施加或被施加于它们。例如，一件物品可以增加或乘算其持有者的攻击速度，而一次攻击可以临时向目标施加 COMPOUND MULTIPLIER 使其攻击速度减半。

##

#### `ADDITIVE`
`ADDITIVE` 修正器非常直观：它们在基础属性上加算。
#### `ADDITIVE_MULTIPLIER`
`ADDITIVE_MULTIPLIER` 将基础属性的值乘以指定值。
它们会累加在一起（即加算乘数为 2 和 3 时，总乘数为 5，而不是 6），然后在加算修正之后再乘以基础属性。
#### `COMPOUND_MULTIPLIER`
最后，`COMPOUND_MULTIPLIER` 会乘算所有加算结果——这是应用减益等效果变化的绝佳位置，因为它们通常在加算属性增加和乘算之后计算。

##

## 属性计算 
`ADDITIVE_MULTIPLIER` 和 `COMPOUND_MULTIPLIER` 这两种修正器容易混淆；以下示例应该能让区别更清楚：

假设你有以下修正器：
 ``` rb
  8 基值
  10 加算
  2 加算
  5 乘算
  3 乘算
  2 复合（相当于 x2）
  0.4 复合（相当于 -60%）
```
...MythicMobs 会这样计算：
```rb
(8 + 10 + 2) * (5 + 3) * (2 * 0.4) = 128

(base + additive + additive) * (additive_multiplier + additive_multiplier) * (compound_multiplier * compound_multiplier) = 最终属性
```
普通乘数是累加的，复合乘数是累乘的。可以理解为 Additive Multiplier 是 "+10%"，而 Compound Multiplier 是 "x10%"。


# 内置属性

以下属性由 MythicMobs 原生支持，可以在插件根目录（`/plugins/MythicMobs/`）或包文件夹（`/plugins/MythicMobs/Packs/CoolPack/`）的 `stats.yml` 文件中进行配置。
玩家继承这些属性的 `BaseValue`；生物也以它们为默认值，除非在其配置的 `Stats:` 子项中指定了覆盖值。


|属性                                                         |描述                                                                                       |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
|[ATTACK_DAMAGE](#attack_damage)                              |基础伤害输出                                                                                |
|[ATTACK_SPEED](#attack_speed)                                |攻击冷却频率。通常仅用于玩家。                                       |
|[BONUS_DAMAGE](#bonus_damage)                                |额外伤害的附加修正器                                                      |
|[CRITICAL_STRIKE_CHANCE](#critical_strike_chance)            |触发会心一击的概率（基于概率的暴击）                                              |
|[CRITICAL_STRIKE_DAMAGE](#critical_strike_damage)            |通过会心一击造成的伤害                                                                  |
|[CRITICAL_STRIKE_RESILIENCE](#critical_strike_resilience)    |对会心一击的抗性                                                                     |
|[DAMAGE_REDUCTION](#damage_reduction)                        |通用伤害减免                                                                          |
|[DEFENSE](#defense)                                          |防御                                                                                           |
|[DODGE_CHANCE](#dodge_chance)                                |攻击在尝试造成伤害时失败的概率。由对手的 [DODGE_NEGATION](#dodge_negation) 减少。 |
|[DODGE_NEGATION](#dodge_negation)                                        |减少对手的 [DODGE_CHANCE](#dodge_chance)。            |
|[HEALTH](#health)                                            |生命值                                                                                     |
|[HEALTH_REGENERATION](#health_regeneration)                  |生命恢复速率                                                                       |
|[LIFESTEAL_CHANCE](#lifesteal_chance)                        |造成的伤害治疗攻击者的概率                                                      |
|[LIFESTEAL_POWER](#lifesteal_power)                          |生命偷取的治疗量。                                                                  |
|[MOVEMENT_SPEED](#movement_speed)                            |移动速度。                                                                                   |
|[PARRY_CHANCE](#parry_chance)                                |从正面近战攻击中减少并反弹伤害的概率。由对手的 [PARRY_NEGATION](#parry_negation) 减少。 |
|[PARRY_COUNTERATTACK](#parry_counterattack)                  |格挡时返还给对手的伤害量。                                        |
|[PARRY_POWER](#parry_power)                                  |格挡减少的伤害量。                                                            |
|[PARRY_NEGATION](#parry_negation)                                      |减少对手的 [PARRY_CHANCE](#parry_chance)。 |
| [SCALE](#scale)                                             | 实体的体型大小                |
| STEP_HEIGHT                                                 | 步高属性                |
| ARMOR                                                       | 护甲属性                      |
| ARMOR_TOUGHNESS                                             | 护甲韧性属性            |
| BURNING_TIME                                                | 燃烧时间属性               |
| EXPLOSION_KNOCKBACK_RESISTANCE                          | 爆炸击退抗性属性 |
| FALL_DAMAGE_MULTIPLIER                                      | 摔落伤害乘数属性     |
| GRAVITY                                                     | 重力属性                    |
| JUMP_STRENGTH                                               | 跳跃力度属性              |
| KNOCKBACK_RESISTANCE                                        | 击退抗性属性       |
| MOVEMENT_EFFICIENCY                                         | 移动效率属性        |
| OXYGEN_BONUS                                                | 氧气加成属性               |
| SAFE_FALL_DISTANCE                                          | 安全摔落距离属性         |
| SNEAKING_SPEED                                              | 潜行速度属性             |
| WATER_MOVEMENT_EFFICIENCY                                   | 水中移动效率属性  |
| BLOCK_BREAK_SPEED                                           | 方块破坏速度属性          |
| BLOCK_INTERACTION_RANGE                                     | 方块交互范围属性    |
| ENTITY_INTERACTION_RANGE                                    | 实体交互范围属性   |
| FLYING_SPEED                                                | 实体的飞行速度           |
| FOLLOW_RANGE                                                | 实体的跟随范围           |

# 内置属性详解

这是 MythicMobs 提供的内置属性详细说明。自定义属性请参见[自定义属性示例](#自定义属性示例)。

#### `DODGE_NEGATION`
攻击命中造成伤害的概率。减少对手的 [DODGE_CHANCE](#dodge_chance)。
如下所示，属性的显示名称和描述元素可以自定义，例如将"闪避抵消"显示为"命中率"。

<details><summary>配置</summary>
<br>

```yml
DODGE_NEGATION:
  Enabled: false
  AlwaysActive: false
  Display: '命中率'
  Formatting:
    Additive: '+<value> 命中率'
    Multiply: '+<value> 命中率'
    Compound: 'x<value> 命中率'
  BaseValue: 0
```

</details>

##
#### `ATTACK_DAMAGE`
基础伤害输出
<details><summary>配置</summary>
<br>

```yml
ATTACK_DAMAGE:
  Enabled: true
  AlwaysActive: false
  Display: '伤害'
  Formatting:
    Additive: '+<value> 伤害'
    Multiply: '+<value> 伤害'
    Compound: 'x<value> 伤害'
  BaseValue: 1
```

</details>

##
#### `ATTACK_SPEED`
攻击冷却频率。通常仅用于玩家。
<details><summary>配置</summary>
<br>

```yml
ATTACK_SPEED:
  Enabled: true
  AlwaysActive: false
  Display: '攻击速度'
  Formatting:
    Additive: '+<value> 攻击速度'
    Multiply: '+<value> 攻击速度'
    Compound: 'x<value> 攻击速度'
  BaseValue: 4.0
```

</details>

##
#### `BONUS_DAMAGE`
额外伤害的附加修正器
<details><summary>配置</summary>
<br>

```yml
BONUS_DAMAGE:
  Enabled: false
  AlwaysActive: false
  Display: '额外伤害'
  Formatting:
    Additive: '+<value> 额外伤害'
    Multiply: '+<value> 额外伤害'
    Compound: 'x<value> 额外伤害'
  BaseValue: 0
```

</details>

##
#### `CRITICAL_STRIKE_CHANCE`
触发会心一击的概率（基于概率的暴击）
<details><summary>配置</summary>
<br>

```yml
CRITICAL_STRIKE_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: '会心一击'
  Formatting:
    Additive: '+<value> 会心一击'
    Multiply: '+<value> 会心一击'
    Compound: 'x<value> 会心一击'
  BaseValue: 0
  MinValue: 0
  Skills:
  - particles{p=crit;a=50;hS=1;y=1;s=1} @trigger
```

</details>

##
#### `CRITICAL_STRIKE_DAMAGE`
通过会心一击造成的伤害
<details><summary>配置</summary>
<br>

```yml
CRITICAL_STRIKE_DAMAGE:
  Enabled: false
  AlwaysActive: true
  Display: '会心伤害'
  Formatting:
    Additive: '+<value> 会心伤害'
    Multiply: '+<value> 会心伤害'
    Compound: 'x<value> 会心伤害'
  BaseValue: 1
```

</details>

##
#### `CRITICAL_STRIKE_RESILIENCE`
对会心一击的抗性
<details><summary>配置</summary>
<br>

```yml
CRITICAL_STRIKE_RESILIENCE:
  Enabled: false
  Display: '韧性'
  AlwaysActive: false
  Formatting:
    Additive: '+<value> 韧性'
    Multiply: '+<value> 韧性'
    Compound: 'x<value> 韧性'
  BaseValue: 0
```

</details>

##
#### `DAMAGE_REDUCTION`
通用伤害减免
<details><summary>配置</summary>
<br>

```yml
DAMAGE_REDUCTION:
  Enabled: false
  AlwaysActive: false
  Display: '伤害减免'
  Formatting:
    Additive: '+<value> 伤害减免'
    Multiply: '+<value> 伤害减免'
    Compound: 'x<value> 伤害减免'
  BaseValue: 0
```

</details>

##
#### `DEFENSE`
防御
<details><summary>配置</summary>
<br>

```yml
DEFENSE:
  Enabled: false
  AlwaysActive: false
  Display: '防御'
  Formatting:
    Additive: '+<value> 防御'
    Multiply: '+<value> 防御'
    Compound: 'x<value> 防御'
  BaseValue: 0
```

</details>

##
 #### `DODGE_CHANCE`
 攻击在尝试造成伤害时失败的概率。减少对手的[命中率](#accuracy)。
<details><summary>配置</summary>
<br>

```yml
DODGE_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: '闪避'
  Formatting:
    Additive: '+<value> 闪避概率'
    Multiply: '+<value> 闪避概率'
    Compound: 'x<value> 闪避概率'
  BaseValue: 0
  Skills: []
```

</details>

##
#### `HEALTH`
生命值
<details><summary>配置</summary>
<br>

```yml
HEALTH:
  Enabled: false
  AlwaysActive: true
  Display: '生命值'
  Formatting:
    Additive: '+<value> 生命值'
    Multiply: '+<value> 生命值'
    Compound: 'x<value> 生命值'
  BaseValue: 20
  MinValue: 1
```

</details>

##
#### `HEALTH_REGENERATION`
生命恢复速率
<details><summary>配置</summary>
<br>

```yml
HEALTH_REGENERATION:
  Enabled: false
  AlwaysActive: false
  Display: '生命恢复'
  Formatting:
    Additive: '+<value> 恢复'
    Multiply: '+<value> 恢复'
    Compound: 'x<value> 恢复'
  BaseValue: 0
  MaxValue: 1000000
  MinValue: 0
  Frequency: 60
```

</details>

##
#### `LIFESTEAL_CHANCE`
造成的伤害治疗攻击者的概率
<details><summary>配置</summary>
<br>

```yml
LIFESTEAL_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: '生命偷取概率'
  Formatting:
    Additive: '+<value> 生命偷取概率'
    Multiply: '+<value> 生命偷取概率'
    Compound: 'x<value> 生命偷取概率'
  BaseValue: 0
```

</details>

##
#### `LIFESTEAL_POWER`
生命偷取的治疗量。
<details><summary>配置</summary>
<br>

```yml
LIFESTEAL_POWER:
  Enabled: true
  AlwaysActive: false
  Display: '生命偷取强度'
  Formatting:
    Additive: '+<value> 生命偷取强度'
    Multiply: '+<value> 生命偷取强度'
    Compound: 'x<value> 生命偷取强度'
  BaseValue: 0.1
```

</details>

##
#### `MOVEMENT_SPEED`
移动速度。
<details><summary>配置</summary>
<br>

```yml
MOVEMENT_SPEED:
  Enabled: false
  AlwaysActive: true
  Display: '移动速度'
  Formatting:
    Additive: '+<value> 移动速度'
    Multiply: '+<value>% 移动速度'
    Compound: 'x<value>% 移动速度'
  ParentStats:
  - SPEED
  Formula: '0.2 + (0.2 / (1 + e^(-0.005 * (SPD - 1000))))'
```

</details>

##
#### `PARRY_CHANCE`
从正面近战攻击中减少并反弹伤害的概率。
<details><summary>配置</summary>
<br>

```yml
PARRY_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: '格挡概率'
  BaseValue: 0
  Priority: 0
  Formatting:
    Additive: '+<value> 格挡概率'
    Multiply: '+<value> 格挡概率'
    Compound: 'x<value> 格挡概率'
  FrontAngle: 180
  UsableMaterials:
    - WOODEN_SWORD
    - STONE_SWORD
    - GOLDEN_SWORD
    - IRON_SWORD
    - DIAMOND_SWORD
    - NETHERITE_SWORD
  Skills: []
```

</details>

##
#### `PARRY_COUNTERATTACK`
格挡时返还给对手的伤害量。
<details><summary>配置</summary>
<br>

```yml
PARRY_COUNTERATTACK:
  Enabled: false
  AlwaysActive: false
  Display: '格挡反击'
  BaseValue: 1
  Formatting:
    Additive: '+<value> 格挡反击'
    Multiply: '+<value> 格挡反击'
    Compound: 'x<value> 格挡反击'
```

</details>

##
#### `PARRY_NEGATION`
影响并降低对手的 [PARRY_CHANCE](#parry_chance)。
如下所示，属性的显示名称和描述元素可以自定义，例如将"格挡抵消"显示为"专精"。
<details><summary>配置</summary>
<br>

```yml
PARRY_NEGATION:
  Enabled: false
  AlwaysActive: false
  Display: '专精'
  Formatting:
    Additive: '+<value> 专精'
    Multiply: '+<value> 专精'
    Compound: 'x<value> 专精'
  BaseValue: 0
```

</details>

##
#### `PARRY_POWER`
格挡减少的伤害量。
<details><summary>配置</summary>
<br>

```yml
PARRY_POWER:
  Enabled: false
  AlwaysActive: false
  Display: '格挡强度'
  BaseValue: 0.5
  Formatting:
    Additive: '+<value> 格挡强度'
    Multiply: '+<value> 格挡强度'
    Compound: 'x<value> 格挡强度'
```

</details>

##
#### `SCALE`
实体的体型大小
<details><summary>配置</summary>
<br>

```yml
SCALE:
  Enabled: false
  AlwaysActive: false
  Display: '体型'
  BaseValue: 1
  Formatting:
    Additive: '+<value> 体型'
    Multiply: '+<value> 体型'
    Compound: 'x<value> 体型'
```

</details>


##
# 配置实现

需要了解的重要一点是：玩家从 `stats.yml` 文件中获取所有基础属性值，而生物只从 `stats.yml` 文件中获取部分基础属性值：如果在生物的 Stats 中指定了其他值，则以指定值为准。

## 生物
此示例展示了 `Some_Mob` 和三个配置的属性：在 `Stats:` 章节中配置的 `CRITICAL_STRIKE_CHANCE`，以及它的 `Health` 和 `Damage`。
Health 和 Damage 属性类型以生物配置的常规格式原生处理。该生物配置的其他属性有：`ATTACK_DAMAGE`、`ATTACK_SPEED` 和 `MOVEMENT_SPEED`。
```yml
Some_Mob:
  Health: 50
  Damage: 10
  Stats:
  - CRITICAL_STRIKE_CHANCE 0.2
```

## 物品
```yaml
ExampleItem:
  Id: BLAZE_ROD
  Display: '测试'
  Stats:
  - CRITICAL_STRIKE_CHANCE 0.5 ADDITIVE
  - CRITICAL_STRIKE_DAMAGE 2.0 ADDITIVE
  - HEALTH 20to30 ADDITIVE
```
> ⚠️ 警告：要在物品上使用属性，必须安装 [Crucible](/../../../mythiccrucible/-/wikis/home)

# 示例

## 自定义属性示例

以下属性由终端用户创建。附有若干示例。


#### `ARMOR_GENERIC`
基于通用护甲的伤害减免。可应用于装备。
```yml
ARMOR_GENERIC:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: '通用护甲'
  DamageFormula: 'd - v'
  BaseValue: 0
  Formatting:
    Additive: '+<value> 通用护甲'
    Multiply: '+<value> 通用护甲'
    Compound: 'x<value> 通用护甲'

```
#### `ARMOR_BLUNT`
基于 `BLUNT` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的护甲减伤。
```yml
ARMOR_BLUNT:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: '钝击护甲'
  DamageType: BLUNT
  DamageFormula: 'd - v'
  BaseValue: 0
  Formatting:
    Additive: '+<value> 钝击护甲'
    Multiply: '+<value> 钝击护甲'
    Compound: 'x<value> 钝击护甲'

```
#### `ARMOR_SHARP`
基于 `SHARP` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的护甲减伤。
```yml
ARMOR_SHARP:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: '锐器护甲'
  DamageType: SHARP
  DamageFormula: 'd - v'
  BaseValue: 0
  Formatting:
    Additive: '+<value> 锐器护甲'
    Multiply: '+<value> 锐器护甲'
    Compound: 'x<value> 锐器护甲'

```
#### `DAMAGE_BLUNT`
`BLUNT` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的伤害输出。
```yml
DAMAGE_BLUNT:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_BONUS
  Priority: 1
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: '钝击伤害'
  DamageType: BLUNT
  BaseValue: 0
  Formatting:
    Additive: '+<value> 钝击伤害'
    Multiply: '+<value> 钝击伤害'
    Compound: 'x<value> 钝击伤害'

```
#### `DAMAGE_SHARP`
`SHARP` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的伤害输出。

```yml
DAMAGE_SHARP:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_BONUS
  Priority: 2
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: '锐器伤害'
  DamageType: SHARP
  BaseValue: 0
  Formatting:
    Additive: '+<value> 锐器伤害'
    Multiply: '+<value> 锐器伤害'
    Compound: 'x<value> 锐器伤害'

```
#### `FIRE_RESISTANCE`
配置用于抵抗 FIRE、FIRE_TICK [伤害原因](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/DamageCause)。
```yml
FIRE_RESISTANCE:
  Enabled: false
  AlwaysActive: false
  Display: '火焰抗性'
  Formatting:
    Additive: '+<value> 火焰抗性'
    Multiply: '+<value> 火焰抗性'
    Compound: 'x<value> 火焰抗性'
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  Conditions:
    - (damageCause FIRE || damageCause FIRE_TICK)
  ExecutionPoint: PRE
  DamageFormula: 'd * (1 - v)'
  MaxValue: 1
  MinValue: 0

```
#### `SPEED`
可在 [MOVEMENT_SPEED](#movement_speed) 属性计算中使用，以通过公式影响速度。
```yml
SPEED:
  Enabled: true
  AlwaysActive: false
  Type: STATIC
  FormulaKey: 'SPD'
  Formatting:
    Additive: '+<value> 速度'
    Multiply: '+<value>% 速度'
    Compound: 'x<value>% 速度'
```
#### `ICE_DAMAGE`
这是一个更复杂的示例，还涉及了 TriggerStats。
```yaml
ICE_DAMAGE:
  Enabled: true
  Type: DAMAGE_MODIFIER
  Priority: 50
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: '&f֍'
  DamageType: ALL
  BaseValue: 0
  TriggerStats:
  - LIGHTNING_DEFENSE LD
  - AIR_DEFENSE AD
  - EARTH_DEFENSE ED
  - FIRE_DEFENSE FD
  - AETHER_DEFENSE AE
  - VOID_DEFENSE VD
  DamageFormula: '1 + d * ( LD + AD - ED - FD + 0.5 * ( AE - VD ) ) / 100'
  Formatting:
    Rounding: 2
    Additive: '&a+<value>'
    Multiply: '&a+<value>%'
    Compound: '&ax<value>%'
```
