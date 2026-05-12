The 装备 section in a 生物 配置 定义 what kind of 装备 the 生物 will 生成 with. The 装备 只会 be applied to the 生物 when it spawns or 期间 a reload, and can be changed 之后wards by using the [Equip 机制](/技能/机制/equip).

若the PreventOtherDrops 选项 不是 启用，then the 生物将willnaturally 掉落 all of its equipped 物品 on death。

若您想要 your 生物 to not wear any 装备，you将canuse the 选项 "PreventRandomEquipment". See [生物 选项](/生物/选项). An alternative to using that 选项 is to equip your 生物 with *dummy 物品*, 例如 AIR。

装备 栏位 can 也 accept [droptables](/掉落/DropTables#装备-droptables), allowing 对于 creation of "sets" where a random 物品 is selected 从 set. For 示例, a droptable可以createdthat 包含 every 原版 helmet, which can then be used on the 生物 in the 装备 tab to select one random helmet to wear。

[[_TOC_]]

## 语法
```yaml
internal_mobname:
  Type: <mobtype>
  Equipment:
  - <item> <slot>
  - <item> <slot>
  - ...
```

##### 物品
Can be 也 the 名称 of a [MythicMobs 物品](/物品/物品#internal_name) or a 原版 物品.

#### 栏位
Defines the 栏位 on the 生物 that 物品 应为 carried on.

| 栏位 | Description |
|---------|----------------------------------------------------------------------------------------------|
| HEAD | The head 栏位. Accepts regular helmets, playerheads, and even blocktypes. |
| CHEST | The chest 栏位. Will 仅 render chestplates, but will carry any 物品. |
| LEGS | The leg 栏位. Will 仅 render leggings, but will carry any 物品. |
| FEET | The feet 栏位. Will 仅 render boots, but will carry any 物品. |
| HAND | The mainhand (right) hand 栏位. |
| OFFHAND | The offhand (left) hand 栏位. |

```yaml
awesome_boss:
  Type: pig_zombie
  Equipment:
  - awesome_boss_helmet HEAD
  - diamond_sword HAND
```

## In-line 物品
For very basic 装备, 您可以 添加 some 内联 物品 data so that you 不要 总是 必须 create a mythic 物品.
All the 内联 物品 data that works under `Equipment` 还将 work 在...下 [掉落](/掉落/掉落) section.

```yaml
 Equipment:
 - leather_chestplate{name="Dark Leather";lore="&8A vest made of darkened leather";color=BLACK} CHEST
```

### Available 内联 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 名称 | 显示, n, d | The 显示 名称 of the 物品 | |
| data | | The "Data" of the 物品, to not be confused with CustomModelData | 0 |
| model | | The CustomModelData of the 物品 | 0 |
| 数量 | a | The 数量 of the 物品 | 1 |
| 物品描述 | l | The 物品描述 of the 物品 | |
| 附魔 | enchants, ench, e | A 列表 of [附魔] of the 物品 | |
| potioneffects | peffects, 药水, pe | A 列表 of [药水 效果] of the 物品, if a 药水 | |
| color | c, potioncolor, pcolor, pc | The color of the 物品, if a 药水 | |
| skullowner | | The 主人 of the 物品, if a skull | |
| skulltexture | | The SkinURL of the texture of the 物品, if a skull | |

[附魔]: /物品/附魔
[药水 效果]: /物品/药水


## MMOItems
To equip a 生物 with an mmoitem, use the following syntax:
```yaml
  Equipment:
  - mmoitems{type=ARMOR;id=STEEL_HELMET} HEAD
  - mmoitems{type=ARMOR;id=STEEL_CHESTPLATE} CHEST
  - mmoitems{type=ARMOR;id=STEEL_LEGGINGS} LEGS
  - mmoitems{type=ARMOR;id=STEEL_BOOTS} FEET
  - mmoitems{type=SWORD;id=RUBY_SWORD} HAND
```
Please 注意 that mmo stats on the armor DO NOT work on MythicMobs. As such, 它们将 not have extra 血量, 防御 or 攻击 伤害 因为 of it.


## 示例
The 示例 below will 生成 a zombie with a panda 玩家 head equipped in their head 栏位.
```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==} HEAD
```

Now lets take this Panda Zombie and give it some 自定义 armor with a 名称, 物品描述, and 附魔.

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

Lastly, remember that we can use the 内联 物品 data in the 掉落 section. Killing the PandaZombie will make it 掉落 all of the 物品, 与ir 名称, 物品描述, and enchants all 不 need to make any mythic 物品!

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