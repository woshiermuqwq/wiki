生物配置中的装备区块定义了生物生成时会携带什么样的装备。装备仅在生物生成或重载时应用，之后可以通过[装备技能](/skills/mechanics/equip)进行更改。

如果未启用 `PreventOtherDrops` 选项，生物死亡时会自然掉落所有已装备的物品。

如果你希望生物不穿戴任何装备，可以使用选项 `PreventRandomEquipment`，参见[生物选项](/Mobs/Options)。另一种替代方案是给生物装备*占位物品*，例如 `AIR`。

装备槽位也可以接受[掉落表](/drops/DropTables#equipment-droptables)，从而可以创建"套装"——从套装中随机选中一件物品。例如，可以创建一个包含所有原版头盔的掉落表，然后在生物配置的装备栏中使用它，从而随机选择一顶头盔来穿戴。

[[_TOC_]]

## 语法
```yaml
internal_mobname:
  Type: <生物类型>
  Equipment:
  - <物品> <槽位>
  - <物品> <槽位>
  - ...
```

### 物品
可以是 [MythicMobs 物品](/Items/Items#internal_name) 的名称，也可以是原版物品。

### 槽位
定义物品应装备在生物身上的哪个槽位。

| 槽位    | 说明                                                                                        |
|---------|--------------------------------------------------------------------------------------------|
| HEAD    | 头盔槽位。接受普通头盔、玩家头颅，甚至方块类型                                                  |
| CHEST   | 胸甲槽位。只会渲染胸甲，但可以携带任何物品                                                      |
| LEGS    | 护腿槽位。只会渲染护腿，但可以携带任何物品                                                      |
| FEET    | 靴子槽位。只会渲染靴子，但可以携带任何物品                                                      |
| HAND    | 主手（右手）槽位                                                                             |
| OFFHAND | 副手（左手）槽位                                                                             |

```yaml
awesome_boss:
  Type: pig_zombie
  Equipment:
  - awesome_boss_helmet HEAD
  - diamond_sword HAND
```

## 行内物品
对于非常基础的装备，你可以使用行内物品数据，这样就不必每次都创建一个 Mythic 物品。
所有在 `Equipment` 下有效的行内物品数据，在[掉落](/drops/Drops)区块下同样有效。

```yaml
 Equipment:
 - leather_chestplate{name="Dark Leather";lore="&8A vest made of darkened leather";color=BLACK} CHEST
```

### 可用的行内属性
| 属性         | 别名                  | 说明                                                    | 默认值  |
|-------------|----------------------|--------------------------------------------------------|--------|
| name        | display, n, d        | 物品的显示名称                                             |        |
| data        |                      | 物品的"Data"值，注意不要与 CustomModelData 混淆              | 0      |
| model       |                      | 物品的 CustomModelData                                    | 0      |
| amount      | a                    | 物品的数量                                                | 1      |
| lore        | l                    | 物品的描述信息                                              |        |
| enchantments | enchants, ench, e   | 物品的[附魔]列表                                           |        |
| potioneffects | peffects, potion, pe | 物品的药水[效果]列表（如果是药水的话）                         |        |
| color       | c, potioncolor, pcolor, pc | 物品的颜色（如果是药水的话）                             |        |
| skullowner  |                      | 物品的所有者（如果是头颅的话）                                  |        |
| skulltexture |                     | 物品材质的 SkinURL（如果是头颅的话）                           |        |

[附魔]: /Items/Enchantments
[效果]: /Items/Potions

## MMOItems
要给生物装备 MMOItems 物品，请使用以下语法：
```yaml
  Equipment:
  - mmoitems{type=ARMOR;id=STEEL_HELMET} HEAD
  - mmoitems{type=ARMOR;id=STEEL_CHESTPLATE} CHEST
  - mmoitems{type=ARMOR;id=STEEL_LEGGINGS} LEGS
  - mmoitems{type=ARMOR;id=STEEL_BOOTS} FEET
  - mmoitems{type=SWORD;id=RUBY_SWORD} HAND
```
请注意，MMO 装备上的 MMO 属性对 MythicMobs 无效。因此，它们不会因此获得额外的生命值、防御力或攻击伤害。

## 示例
下面的示例会生成一个僵尸，其头部装备了熊猫玩家头颅。
```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==} HEAD
```

现在让我们给这只熊猫僵尸配上一些带有名称、描述和附魔的自定义护甲。

```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} HEAD
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} CHEST
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} LEGS
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} FEET
```

最后，请记住我们也可以在掉落区块中使用行内物品数据。击杀熊猫僵尸后，它将掉落所有物品，包括它们的名称、描述和附魔，完全不需要创建任何 Mythic 物品！

```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} HEAD
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} CHEST
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} LEGS
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} FEET
  Drops:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} 1 1
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} 1 1
```
