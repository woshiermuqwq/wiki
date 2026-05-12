附魔 属性用于to应用 附魔 to 物品 made using MythicMobs。
任何of these都可以put on any 物品 and can exceed natural 附魔-等级 limits set by Minecraft。
Some 附魔 可能不 have any 效果 if put on 物品 that they 不是 made for.

Syntax
------
```yml
internal_itemname:
  Id: <material>
  Enchantments:
  - <enchantment> <level>
  - <enchantment> <level>
  - ...
```
****\<附魔>**
类型 of 附魔 to be applied to the specified 物品.

****\<等级>**
The 等级 of the specified 附魔.

## Available 附魔

A 列表 of available [附魔](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/附魔/附魔.html)可以found在 Spigot Javadocs 上。

附魔 can 也 be added via the `namespace:enchant_name` syntax, if there are 其他 providers

## 示例
```yml
lethal_pickaxe:
  Id: diamond_pickaxe
  Enchantments:
  - SHARPNESS 3
  - KNOCKBACK 1
  - mythic:example_enchant 2
```