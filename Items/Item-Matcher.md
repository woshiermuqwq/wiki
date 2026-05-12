MythicMobs 中的一些功能支持通过特定的语法来匹配物品或方块：

##

直接写 MythicMobs 物品或 [Mythic (Crucible) 自定义方块](/../../../mythiccrucible/-/wikis/Custom-Blocks)的内部名称，会匹配：
  - 对应的 MythicMobs 物品
  - 对应的 Mythic 自定义方块

##

写 [Spigot 材质类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)，会匹配：
  - 对应材质类型的物品
  - 对应材质类型的方块

##

在条目开头使用 `#`，会匹配：
  - 具有该[物品标签](https://minecraft.wiki/w/Tag#Item_tags_2)的物品
    - 例如 `#arrows`、`#axes` 等
  - 具有该[方块标签](https://minecraft.wiki/w/Tag#Block_tags_2)的方块
    - 例如 `#air`、`#animals_spawnable_on` 等

##

在条目中任意位置使用 `*`，会让每个 `*` 匹配任意数量的字符。如果你熟悉正则表达式，`*` 等同于 `.*`：
  - `netherite_*` 会匹配材质类型以 "netherite_" 开头的任意物品/方块
  - `*_log` 会匹配材质类型以 "_log" 结尾的任意物品/方块
  - `*a*` 会匹配材质类型中含有字母 "a" 的任意物品/方块
  - `*` 会匹配任何东西

##

仅对方块有效：可以在条目后面用一对方括号 `[]` 指定需要匹配的[方块状态](https://minecraft.wiki/w/Block_states)：
  - redstone_torch[lit=true;facing=north]


<!--

| 属性 ITEMMATCHER | 别名 | 说明 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| strict    | exact, e  | 匹配器是否应更严格地匹配目标物品 | false |
| types     | type, t, material, mat, m, item, i | 要匹配的物品。可以是列表 | DIRT |
| vanillaonly | vanilla | 是否只匹配原版物品 | false |

-->