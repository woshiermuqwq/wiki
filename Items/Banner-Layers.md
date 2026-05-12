![image](uploads/204528492902aa041447fe90880071d8/image.png)

要在 MythicMobs 中制作复杂的旗帜物品，可以使用以下语法。
MythicMobs 不限制旗帜图层的数量，你可以超出 Minecraft 原版设定的最多 6 层限制。
但超过 6 层可能会导致异常行为和/或卡顿。

旗帜图层同样适用于盾牌。

语法
------
```yml
Banner:
  Id: <旗帜/盾牌>
  #旗帜的底色由物品 ID 决定
  BannerLayers:
  - <颜色> <图案>
  - <颜色> <图案>
```
图案列表
--------

可用[图案](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/banner/PatternType.html)列表可在 Spigot Javadocs 上找到。

<!--
| **图案** | |
|--------------------------|-----------------------|
| BASE                     | SQUARE\_BOTTOM\_LEFT  |
| BORDER                   | SQUARE\_BOTTOM\_RIGHT |
| CIRCLE\_MIDDLE           | SQUARE\_TOP\_LEFT     |
| CREEPER                  | SQUARE\_TOP\_RIGHT    |
| CROSS                    | STRAIGHT\_CROSS       |
| CURLY\_BORDER            | STRIPE\_BOTTOM        |
| DIAGONAL\_LEFT           | STRIPE\_CENTER        |
| DIAGONAL\_LEFT\_MIRROR   | STRIPE\_DOWNLEFT      |
| DIAGONAL\_RIGHT          | STRIPE\_DOWNRIGHT     |
| DIAGONAL\_RIGHT\_MIRROR  | STRIPE\_LEFT          |
| FLOWER                   | STRIPE\_MIDDLE        |
| GRADIENT                 | STRIPE\_RIGHT         |
| GRADIENT\_UP             | STRIPE\_SMALL         |
| HALF\_HORIZONTAL         | STRIPE\_TOP           |
| HALF\_HORIZONTAL\_MIRROR | TRIANGLE\_BOTTOM      |
| HALF\_VERTICAL           | TRIANGLE\_TOP         |
| HALF\_VERTICAL\_MIRROR   | TRIANGLES\_BOTTOM     |
| MOJANG                   | TRIANGLES\_TOP        |
| RHOMBUS\_MIDDLE          | BRICKS                |
| SKULL                    | GLOBE                 |
| PIGLIN                   |                       |
-->

示例
--------
```yml
SkeletonKingBannerShield:
  Id: shield
  Display: <dark_red>Skeleton King's Banner</dark_red>
  BannerLayers:
  - RED BASE
  - WHITE CURLY_BORDER
  - WHITE STRIPE_CENTER
  - BLACK STRIPE_BOTTOM
  - WHITE CREEPER
  - YELLOW STRIPE_TOP
  - BLACK TRIANGLES_TOP
```
```yml
SkeletonKingBanner:
  Id: orange_banner
  Display: <dark_red>Skeleton King's Banner</dark_red>
  BannerLayers:
  - RED BASE
  - WHITE CURLY_BORDER
  - WHITE STRIPE_CENTER
  - BLACK STRIPE_BOTTOM
  - WHITE CREEPER
  - YELLOW STRIPE_TOP
  - BLACK TRIANGLES_TOP
```