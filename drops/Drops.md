Drops 标签可以添加到你的自定义生物中，使其在死亡时掉落你选择的物品。MythicMobs 中有三种自定义掉落类型可以区分使用。


[[_TOC_]]


Drops 是实现自定义掉落的最简单方式。

## Drops 配置
```yaml
internal_mobname:
  Type: <mobtype>
  Drops:
  - <drop> <amount> <chance>
  - <drop> <amount> <chance>
  - ...
```

### Drop（掉落类型）
可以是 MythicMobs 的物品、原版物品、经验、掉落表或受支持插件的物品/经验。可用[掉落类型](Drops#drop-types)列表见下方

### Amount（数量）
要掉落的物品数量。  

可以是数字范围，例如：`1-3` 或 `1to3`。  
这种情况下，掉落物品数量不会小于最左侧的数字，也永远不会**等于或大于**最右侧的数字
> 写 `1to3` 会掉落至少 1 个物品，最多 2 个物品

### Chance（概率）
指定物品掉落的概率。
  - 必须是 0 到 1 之间的数字
  - **注意：** 允许使用百分比形式（如 10% 而不是 0.1）。

## 掉落类型
| **类型**                    | **说明**                                          | **示例**                             |
|-----------------------------|----------------------------------------------------------|-----------------------------------------|
| [MythicMob](/drops/DropTypes/MythicMob)| 掉落一只 MythicMob                         |                |
| [Mythic Item](/drops/DropTypes/MythicItem)| 掉落一个 Mythic 物品                    |                |
| [VanillaLootTable](/drops/DropTypes/VanillaLootTable) | 从原版战利品表和数据包中掉落物品 | `- vanillaLootTable minecraft:table_name` |
| **champions-exp**           | 为 `Champions` 插件掉落经验值。  |                                         |
| [skillapi-exp](/drops/DropTypes/SkillAPIExp)| 为 `SkillAPI` 插件掉落经验值 |                                         |
| **heroesexp**               | 为 `Heroes` 插件掉落经验值。     |                                         |
| [mcmmo-exp](/drops/DropTypes/McMMOExp)| 为 `MCMMO` 插件掉落经验值。 | `- mcmmo-exp 69`                       |
| **exp**                     | 掉落常规 Minecraft 经验值。           | `- exp 420`                                         |
| [money](/drops/DropTypes/Money)| 为 `Vault` 插件掉落金钱。               | `- money 1500`                                        |
| **mythicdrop &lt;item&gt;** | 从 `MythicDrops` 插件掉落 &lt;item&gt;。 | `- mythicdrop CoolSword 1`                                        |
| [phatloot](/drops/DropTypes/PhatLoot)| 从 `PhatLoot` 插件掉落物品。    | `- phatloot LootTableName 1`                                        |
| [command](/drops/DropTypes/Command)| 在控制台运行一条指令。                    | `- cmd{c="warp <trigger.name> spawn"} 1`  |
| [mmoitems](https://gitlab.com/phoenix-dvpmt/mmoitems/-/wikis/Item%20Drop%20Tables#adding-mmoitems-to-mythicmobs-drop-tables)    | 掉落一个 `mmoitems` 物品                                    | `- mmoitems{type=SWORD;id=CUTLASS} 1 1` |
| **nothing**                 | 什么都不掉落。在创建带权重的掉落表时很有用 | `- nothing`                                        |
| [ItemVariable](/drops/DropTypes/ItemVariable)| 掉落指定物品变量中定义的物品    | `- itemvariable{variable=caster.stolenitem} 1 1`|


### 示例
此示例有 20% 概率掉落 3 颗钻石，60% 概率运行一条指令，12% 概率掉落 100 到 600 经验值
```yaml
YourMob:
  Type: ZOMBIE
  Drops:
  - diamond 3 0.2
  - cmd{c="crate give <trigger.name> RewardCrate 1"} 1 0.6
  - exp 100to600 0.12
```
## 内联掉落

对于非常基础的装备，你可以添加一些内联物品数据，这样就无需总是创建 Mythic 物品。
你可以使用[内联物品配置](/Mobs/Equipment#in-line-items)中的所有物品数据！

```yaml
 Drops:
 - leather_chestplate{name="暗色皮革";lore="&8一件由深色皮革制成的背心";color=BLACK} 1 1
```

### 示例
下面的掉落部分将掉落一个带有 2 个附魔的熊猫玩家头颅物品，以及 3 件钻石护甲，每件都有名称、物品描述和附魔！

```yaml
  Drops:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} 1 1
  - DIAMOND_CHESTPLATE{name="熊猫的意志";lore="熊猫必须保持警惕";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_LEGGINGS{name="熊猫的力量";lore="熊猫必须强大";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_BOOTS{name="熊猫的速度";lore="熊猫必须迅速";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} 1 1
```
