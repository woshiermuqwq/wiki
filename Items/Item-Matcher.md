Some features inside of MythicMobs支持matching 物品 or 方块 via a specific syntax:。

##

Writing the internal 名称 of a Mythic 物品/[Mythic (Crucible) 自定义 方块](/../../../mythiccrucible/-/wikis/自定义-方块) will 匹配
  - that specific Mythic 物品
  - that specific Mythic 自定义 方块

##

Writing the [Spigot material 类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) will 匹配
  - 物品 with that material 类型
  - 方块 with that material 类型

##

Using `#` at the start of an entry will 匹配 再次st
  - 物品 with that [物品 Tag](https://Minecraft.wiki/w/Tag#Item_tags_2)
    - `#arrows`, `#axes` and so on
  - 方块 with that [方块 Tag](https://Minecraft.wiki/w/Tag#Block_tags_2)
    - `#air`, `#animals_spawnable_on` and so on

##

Using `*` at any point in the entry will make it so any * present will 匹配 再次st any number of characters. For those familiar with Regex syntax, `*` is 等于 `.*`
  - `netherite_*` will 匹配 any 物品/方块 whose 类型 stars with "netherite_"
  - `*_log` will 匹配 any 物品/方块 whose 类型 ends in "_log"
  - `*a*` will 匹配 any 物品/方块 whose 类型 has the letter "a" 某处 in it
  - `*` will 匹配 任何事物

##

For 方块 仅, 可以 specify some specific [方块 states](https://Minecraft.wiki/w/Block_states) to be matched by specifying them inside of a pair of square brackets `[]` 之后 the entry
  - redstone_torch[lit=true;facing=north]


<<!--

| 属性 ITEMMATCHER | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| strict | exact, e | Whether the matcher should more strictly 匹配 the 目标 物品 | false |
| 类型 | 类型, t, material, mat, m, 物品, i | The 物品 to 匹配. Can be a 列表 | DIRT |
| vanilla仅 | 原版 | Whether the matched 物品 can 仅 be a 原版 one | false |

-->