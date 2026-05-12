附魔属性用于给 MythicMobs 制作的物品添加附魔。
任意附魔都可以放到任意物品上，甚至可以超出 Minecraft 原版设定的附魔等级上限。
不过有些附魔放在原本不是为它设计的物品上可能不会产生任何效果。

语法
------
```yml
internal_itemname:
  Id: <material>
  Enchantments:
  - <enchantment> <level>
  - <enchantment> <level>
  - ...
```
**\<enchantment>**
要应用到物品上的附魔类型。

**\<level>**
指定附魔的等级。

## 可用附魔

可用[附魔](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html)列表可在 Spigot Javadocs 上找到。

如果有其他附魔提供方，也可以通过 `namespace:enchant_name` 语法添加附魔。

## 示例
```yml
lethal_pickaxe:
  Id: diamond_pickaxe
  Enchantments:
  - SHARPNESS 3
  - KNOCKBACK 1
  - mythic:example_enchant 2
```