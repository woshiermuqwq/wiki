## 指令

MythicMobs 拥有简洁的指令结构，通过输入 **/mythicmobs** 即可访问。输入后显示所有可用指令的菜单，每级指令都会提供菜单或功能介绍。所有由 [] 包围的指令参数为必填项，&lt;&gt; 则代表可选项。

## 标志
部分指令可以在第一个参数之前添加一组标志，改变指令的行为。

| 标志 | 描述            | 影响的指令                      | 示例                       |
| ---- | -----------------------|--------------------------------------- | ----------------------------- |
| -s | 静默指令，不会返回任何聊天反馈 | `mm mobs spawn`<br>`mm item give`<br>`mm test cast`<br>`mm test mechanic` |`/mm test cast -s [元技能]` |
| -p <玩家名> | 使用此标志让指令在指定玩家处执行 | `mm mobs spawn`<br>`mm spawners create`<br>`mm spawners move` |`/mm m s -p <玩家> [生物名]` |
| -t | 在目标位置执行指令 | `mm mobs spawn` |`/mm m s -t [生物名]` |
| -n | 模拟生物为自然生成（`NATURAL` 生成原因，而非 `COMMAND`） | `mm mobs spawn` |`/mm m s -n [生物名]` |
| -p | 同时击杀持久性生物 | `mm mobs killall` | `/mm m killall -p` |
| -f | 击杀匹配指定阵营的所有生物 | `mm mobs kill` |`/mm m kill -f [阵营名]` |
| -d | 如果背包已满，物品掉落在地面上 | `mm item give` | `/mm i give -d [物品名]` |

## 通用指令

-    **/mm**（别名: **/mythicmobs**）*插件的基础指令。显示所有其他指令。*
-    **/mm debug [级别]**（别名: **/mm d [级别]** *设置插件的调试级别。0 = 关闭。*
-    **/mm debugmode [true/false]** *启用调试模式，关闭随机生成器、生物生成器及其他会导致调试困难的随机内容。*
-    **/mm reload**（别名: **/mm r**）*重载插件。*
-    **/mm save** *强制保存所有活跃生物和生成器。*
-    **/mm version** *显示 MythicMobs 版本。*

物品指令
-------------

-    **/mm items**（别名: **/mm i**）*所有物品相关指令的基础。*
-    **/mm items get [物品名] &lt;数量&gt;** *从配置的生物装备中给自己一个物品。*
-    **/mm items give [玩家] [物品名] &lt;数量&gt;** *从配置的生物装备中给玩家一个物品。*
-    **/mm items give -s [玩家] [物品名] &lt;数量&gt;** *静默地从配置的生物装备中给玩家一个物品。*
-    **/mm items give -d [玩家] [物品名] &lt;数量&gt;** *从配置的生物装备中给玩家一个物品，多余物品掉落地面。*
-    **/mm items list** *列出所有已配置的生物装备。*
-    **/mm item import &lt;物品名&gt; [文件名]** *将手持物品导入到 Items 文件夹。（文件名默认为 &lt;物品名&gt;.yml）*
-    **/mm items browse** *打开一个展示所有已加载 Mythic 物品的图形界面。*（仅限 Premium）

生物指令
------------

-    **/mm mobs**（别名: **/mm m**）*所有生物相关指令的基础。*
-    **/mm mobs info [生物名]** *显示某个 Mythic 生物的详细信息。*
-    **/mm mobs list** *显示服务器已加载生物列表。*
-    **/mm mobs listactive** *显示当前已生成生物列表及各自数量。*
-    **/mm mobs kill [生物名]** *移除所有指定名称的 Mythic 生物。*
-    **/mm mobs kill -f [阵营]** *移除所有指定阵营的 Mythic 生物。*
-    **/mm mobs killall** *移除所有活跃的 Mythic 生物。*
-    **/mm mobs killall -p** *移除所有持久性 Mythic 生物。*
-    **/mm mobs spawn [生物名]:&lt;等级&gt; &lt;数量&gt; &lt;世界,x,y,z,yaw,pitch&gt;** *生成指定名称的生物。*
-    **/mm mobs spawn -s [生物名]:&lt;等级&gt; &lt;数量&gt; &lt;世界,x,y,z,yaw,pitch&gt;** *静默生成生物——不输出控制台信息。*
-    **/mm mobs stats** *显示服务器生物数量的有用信息。（统计数量）*

生物蛋指令
----------------

-    **/mm egg**（别名: **/mm e**）*所有生物蛋相关指令的基础。*
-    **/mm egg get [生物名] &lt;数量&gt;** *给自己指定 Mythic 生物的生物蛋。*
-    **/mm egg give [玩家] [生物名] &lt;数量&gt;** *给玩家指定 Mythic 生物的生物蛋。*

生成器指令
----------------

-   在大多数指令中，可在生成器名称位置使用特殊过滤器和通配符，一次对多个生成器执行操作。
-   使用 **g:组名** 对整个生成器组运行指令。
-   使用 **r:半径** 对指定**半径**方块内的所有生成器运行指令。
-   使用 **?** 作为单字符通配符：运行指令 **/mm s set ?at leashrange 32** 会对名为 Cat、Rat、Fat 的生成器生效，但不会对名为 Matt 的生效。
-   使用 **\*** 作为任意数量字符的通配符：运行指令 **/mm s set T\* leashrange 32** 会将所有以 T 开头的生成器的牵引范围设为 32。
-   **使用 \* 作为生成器名称将修改所有生成器**
-   **/mm spawners**（别名: **/mm s**）*所有生成器相关指令的基础。*
-   **/mm s create** *[生成器名]* *[生物名]*
    -   在玩家准星所指位置创建新生成器。
    -   生成器将生成你指定的任何生物名称，可以是任何 Minecraft 内部原版生物名称或你在配置页面（如 ExampleMobs.yml）中创建的自定义生物名称。
    -   **/mm s create Ruins_Skeleton1 DecayingSkeleton**
-   **/mm s set [生成器名] [设置项] [值]**
    -   修改生成器的某个设置。全部设置项见下文。
    -   所有可设置项参见 [生成器选项章节](Spawners)。
-   **/mm s addcondition [生成器名] [条件] [值]**
    -   添加生成器条件，决定当计时器到时是否应该生成生物。
    -   可应用的条件参见 [生成器条件](/Skills/conditions)。
-   **/mm s removecondition [生成器名] [条件]**
    -   移除生成器条件。
    -   **/mm s removecondition Ruins_Skeleton1 outside**
-   **/mm s info [生成器名]**
    -   提供特定生成器的信息列表。
    -   **/mm s info Ruins_Skeleton1**（列出 Ruins_Skeleton1 生成器的信息）
-   **/mm s listnear &lt;距离&gt;**
    -   列出附近所有生成器。
    -   添加距离参数可缩小列表范围。
    -   **/mm s listnear 15**（显示 15 个方块范围内的所有生成器名称）
-   **/mm s resettimers [名称]**
    -   重置指定生成器的冷却和重置计时器。
-   **/mm s resettimers Ruins_Skeleton1**（重置 Ruins_Skeleton1 生成器）
-   **/mm s activate [名称]**
    -   激活（强制生成）特定生物生成器。
-   **/mm s activate** Ruins_Skeleton1**（生成 Ruins_Skeleton1 生成器的生物）
-   **/mm s cut [搜索字符串]**
    -   根据给定字符串剪切一组生成器。
-   **/mm s cut g:BoneCastle**（剪切"BoneCastle"生成器组中的所有生成器）
-   **/mm s cut r:200**（剪切 200 方块半径内的所有生成器）
-   **/mm s cut Elementals_**（剪切名称以 Elementals_ 开头的所有生成器）
-   **/mm s cut**（剪切所有生成器。请非常小心！）
-   **/mm s paste**
    -   在相对新位置粘贴一组已剪切的生成器。
    -   生成器可多次粘贴，但会替换之前的粘贴。（不会重复）
-   **/mm s undo**
    -   撤销上一步剪切操作，将生成器恢复到原位。
    -   仅在尚未剪切一组新生成器时有效。

标点指令
-------------
参见 [标点 Wiki 页面](/Pins#commands)

实用指令
----------------
- **/mm test cast [技能名]** - 允许你像生物一样运行某个技能。
- **/mm test mechanic [行]** - 允许你像生物一样运行某行技能。
-  **/mm i get [掉落表]** - 允许你从掉落表中获取物品，就像你击杀了掉落该物品的生物一样。

信号指令
---------------

-   **/mm signal &lt;UUID&gt; &lt;信号&gt;**
  -   用于向生物发送信号以切换某些技能
  -   仅在使用生物的 UUID 时有效，不支持生物名
  -   通常作为 tellraw 指令组件使用
  - 要使用此指令，必须授予以下 3 个权限
    - `mythicmobs.signal`
    - `mythicmobs.command.signal`
    - `mythicmobs.command.base`

权限
===========

目前 MythicMobs 仅支持两个权限节点来授予插件的完整访问权限。原因是 MythicMobs 中几乎所有指令都极易被滥用，目前没有必要为每个功能设置单独权限。无论如何，将来有时间我会为有需要的用户添加更多权限，但这并不是我的优先事项。

通用
-------

-   **mythicmobs.admin** - *授予插件指令的完整访问权限。*


指令
--------

-   可以使用 **mythicmobs.command.&lt;命令&gt;** 授予单个指令的访问权限

- **mythicmobs.command.info** - *访问 **/mm info** 指令的权限。*
- **mythicmobs.command.mobs.list** - *访问 **/mm mobs list** 指令的权限。*
- **mythicmobs.command.signal** - *使用 "/mm signal &lt;mob.uuid&gt; &lt;signal&gt;" 指令的权限*
- **mythicmobs.command.test.cast** - *使用 "/mm test cast" 指令的权限*
- **mythicmobs.command.test.addthreat** - *使用 "/mm test addthreat" 指令的权限*
- **mythicmobs.command.test.reducethreat** - *使用 "/mm test reducethreat" 指令的权限*
