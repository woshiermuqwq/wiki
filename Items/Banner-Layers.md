![image](uploads/204528492902aa041447fe90880071d8/image.png)

To make complex 旗帜 物品 in MythicMobs, 您可以 use the following syntax.
There is no hard limit placed by MythicMobs on the number of 旗帜 layers 您可以 use, and 您可以 go past the 原版 maximum of 6 layers set by Minecraft using this.
However, going past 6 layers may cause unusual 行为 and/or lag.

旗帜 layers are 也 applicable to shields.

Syntax
------
```yml
Banner:
  Id: <banner/shield>
  #For Banners, the base color is set by the item ID
  BannerLayers:
  - <color> <pattern>
  - <color> <pattern>
```
Patterns
--------

A 列表 of available [patterns](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/方块/旗帜/PatternType.html)可以foundon the spigot javadocs。

<!--
| **Patterns** | |
|--------------------------|-----------------------|
| BASE | SQUARE\_BOTTOM\_LEFT |
| BORDER | SQUARE\_BOTTOM\_RIGHT |
| CIRCLE\_MIDDLE | SQUARE\_TOP\_LEFT |
| CREEPER | SQUARE\_TOP\_RIGHT |
| CROSS | STRAIGHT\_CROSS |
| CURLY\_BORDER | STRIPE\_BOTTOM |
| DIAGONAL\_LEFT | STRIPE\_CENTER |
| DIAGONAL\_LEFT\_MIRROR | STRIPE\_DOWNLEFT |
| DIAGONAL\_RIGHT | STRIPE\_DOWNRIGHT |
| DIAGONAL\_RIGHT\_MIRROR | STRIPE\_LEFT |
| FLOWER | STRIPE\_MIDDLE |
| GRADIENT | STRIPE\_RIGHT |
| GRADIENT\_UP | STRIPE\_SMALL |
| HALF\_HORIZONTAL | STRIPE\_TOP |
| HALF\_HORIZONTAL\_MIRROR | TRIANGLE\_BOTTOM |
| HALF\_VERTICAL | TRIANGLE\_TOP |
| HALF\_VERTICAL\_MIRROR | TRIANGLES\_BOTTOM |
| MOJANG | TRIANGLES\_TOP |
| RHOMBUS\_MIDDLE | BRICKS |
| SKULL | GLOBE |
| PIGLIN | |
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