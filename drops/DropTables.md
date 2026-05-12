掉落表（Drop Tables）是分配给生物的多个掉落集合。使用它们可以让你在几乎所有需要生物掉落多种物品的情况下更容易地组织掉落。

掉落表存储在其各自的配置文件中，位于 \/MythicMobs\/DropTables。它们的优势在于能够使用[条件](/Skills/conditions)和各种其他特殊选项，并且可以被多个生物共享而无需重复配置。

你可以在 DropTables 文件夹中创建任意数量的文件，只要文件以 `.yml` 结尾，文件可以随便命名。

掉落表可以嵌套——一个掉落表可以包含多个其他掉落表。
```yaml
internal_mobname:
  Type: <mobtype>
  Drops:
  - <internal_droptablename>
```
一个完整配置的掉落表结构如下：
```yaml
# 让你精确指定此表将掉落多少项物品
internal_droptablename: 
  TotalItems: <数量>
  MinItems: <数量> # 默认为 TotalItems 的值
  MaxItems: <数量> # 默认为 TotalItems 的值
  BonusLuckItems: <乘数>
  BonusLevelItems: <乘数>
# 掉落者需满足的条件
  Conditions:
  - condition 1
  - condition 2
  - ...
# 触发掉落的人需满足的条件（即击杀生物者）
  TriggerConditions:
  - condition 1
  - ...
  Drops:
  - <item/exp/droptable> <数量> <概率>
  - ...
```

## 掉落表选项

> 在下面的描述中，"drop"指的是单个"掉落行"，而不是该掉落生成的实际物品数量。因此，如果你有一个像 `bone 5` 的掉落，虽然生成了 5 个骨头物品，但这算作一次掉落，因为它由单个"掉落行"生成

**TotalItems: \[数字\]**

-   精确地定义该表将生成多少次掉落
-   设置此项会使物品概率被视为权重来计算

**MaxItems: \[数字\]**

-   定义将生成的最大掉落次数
-   如果仅设置此项，掉落将按列表顺序执行，直到达到最大物品数量为止

**MinItems: \[数字\]**

-   定义将生成的最小掉落次数
-   如果仅设置此项，掉落将按列表顺序执行，直到达到最小物品数量为止
-   如果同时启用 **两者** ```MinItems``` 和 ```MaxItems```，每个表项的概率将变为*权重*。

**BonusLevelItems: \[数字\]/\[范围\]**

-   基于生物等级的掉落数量修正器
-   可以设为范围值，比如 ```0.2to0.5```
-   计算方式：```数量 = 数量 + (生物等级 * bonus_level_items)```
-   要求表中已设置 ```TotalItems```、```MinItems``` 或 ```MaxItems```

**BonusLuckItems: \[数字\]/\[范围\]**

-   基于击杀者幸运属性的掉落数量修正器
-   可以设为范围值，比如 ```0.15to8```
-   与幸运属性、幸运相关附魔/诅咒和幸运药水效果配合使用
-   计算方式：```数量 = 数量 + (幸运值 * bonus_luck_items)```
-   要求表中已设置 ```TotalItems```、```MinItems``` 或 ```MaxItems```

### 示例

此生物将始终掉落经验值和一些腐肉，但也使用了一个下面描述的掉落表。
```yaml
snow_loving_zombie:
  Type: zombie
  Health: 100
  Equipment:
  - snowsword:0
  Drops:
  - exp 75-125 1
  - rare_snowsword_droptable
```

这是一个有 5% 概率掉落一把自定义剑的掉落表，但仅在生物在 "ICE\_PLAINS" 生物群系中被击杀且半径 20 方块内有玩家时才会掉落。

```yaml
rare_snowsword_droptable:
  Conditions:
  - biome{b=ICE_PLAINS}
  - playerwithin{d=20}
  Drops:
  - snowsword 1 0.05
```
在此示例中，如果玩家没有幸运值，则掉落 5 个金粒/钻石；如果玩家拥有幸运 V 效果，则掉落 15-27 个金粒/钻石。
```yaml
LuckyDroptable:
  TotalItems: 5
  BonusLuckItems: 2to5
  Drops:
  - GOLD_NUGGET 1 1
  - DIAMOND 1 0.2
```


## 装备掉落表
也可以使用掉落表来配置装备组合。这类掉落表可以直接在生物的 [Equipment 元素](/Mobs/Mobs#equipment)中使用，或者通过 [Equip 技能](/skills/mechanics/equip)使用。
其语法与"普通"掉落表类似，只是在这种情况下，需要指定一个装备槽位。

### 示例
```yaml
# 掉落表配置
Example_EquipmentDropTable:
  Drops:
  - LEATHER_HELMET HELMET 1 1
  - LEATHER_CHESTPLATE CHEST 1 1
  - CHAINMAIL_CHESTPLATE CHEST 1 0.5
  - DIAMOND_CHESTPLATE CHEST 1 0.1
  - NETHERITE_CHESTPLATE CHEST 1 0.05
```
```yaml
# 生物配置
ExampleMob:
  Type: ZOMBIE
  Equipment:
  - Example_EquipmentDropTable
```
这些配置将使 `ExampleMob` 能够
- 始终拥有皮革头盔
- 始终至少拥有一件皮革胸甲，同时在满足概率条件时可能拥有更强大的装备
