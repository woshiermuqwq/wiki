你是否曾觉得掉落有点*太平淡*了？想让它们闪耀一些？别担心：本页面将告诉你如何做到！

但请记住！华丽掉落仅适用于 **Mythic、[MMOItems](/drops/Drops#drop-types)、[掉落表](/drops/DropTables) 或原版物品**！

[[_TOC_]]

## 掉落选项
这是生物配置中的一个额外字段 `DropOptions`，允许你决定有关掉落的各种行为。

```yaml
  DropOptions:
    DropMethod: FANCY
    ShowDeathChatMessage: false
    ShowDeathHologram: false
    PerPlayerDrops: false
    ClientSideDrops: false
    Lootsplosion: false
    HologramItemNames: false
    ItemGlowByDefault: false
    ItemBeamByDefault: false
    ItemVFXByDefault: false
    ItemVFX:
      Material: STONE
      Model: 0
    RequiredDamagePercent: 1
    HologramTimeout: 6000
    HologramMessage:
    - ...
    - ...
    ChatMessage:
    - ...
    - ...
```

### DropMethod
可设为以下两个值之一：
- `VANILLA`，保留所有"正常"掉落行为
- `FANCY`，启用伤害追踪、记分板及更高级的掉落效果。如果相关配置允许，掉落还可以为每个参战者分别计算，而非只计算一次

所以本质上，此项必须设为 `FANCY` 才能使本页面其余内容生效。
默认为 `VANILLA`
```yaml
  DropOptions:
    DropMethod: FANCY
```


### ShowDeathChatMessage
是否向玩家显示死亡聊天消息。
默认为 `false`。
```yaml
  DropOptions:
    ShowDeathChatMessage: true
```


### ShowDeathHologram
是否向玩家显示死亡全息图。
默认为 `false`。
```yaml
  DropOptions:
    ShowDeathHologram: true
```


### PerPlayerDrops
是否分别计算每个参战玩家的掉落。本质上，掉落会为每个玩家各投掷一次。
> **这是 [Paper 专属] 功能！**
```yaml
  DropOptions:
    PerPlayerDrops: true
```


### ClientSideDrops
是否为每个玩家以客户端方式分别显示掉落。启用后，每位玩家只能看到他们自己获得的战利品。
```yaml
  DropOptions:
    ClientSideDrops: false
```


### Lootsplosion
掉落物是否默认展示战利品爆炸效果。
```yaml
  DropOptions:
    Lootsplosion: true
```


### HologramItemNames
物品是否默认显示全息名称。
```yaml
  DropOptions:
    HologramItemNames: true
```


### ItemGlowByDefault
物品是否默认发光。
使用此选项似乎会为掉落物品添加 NBT，使它们与其他非此方式获得的物品无法堆叠。
```yaml
  DropOptions:
    ItemGlowByDefault: true
```


### ItemBeamByDefault
物品是否默认显示光束。
```yaml
  DropOptions:
    ItemBeamByDefault: true
```


### ItemVFXByDefault
物品是否默认显示视觉特效。
```yaml
  DropOptions:
    ItemVFXByDefault: true
```


### ItemVFX
关于物品默认视觉特效的选项
```yaml
  DropOptions:
    ItemVFX:
      Material: STONE # 视觉特效的默认材质
      Model: 0 # 视觉特效的默认模型
```


### RequiredDamagePercent
玩家需要对该生物造成的伤害量（以其生命值的百分比量化），才能为该特定玩家生成掉落。
```yaml
  DropOptions:
    RequiredDamagePercent: 1
```


### HologramTimeout
生物死亡时生成的全息图消失的时长（毫秒）
默认为 `6000`
```yaml
  DropOptions:
    HologramTimeout: 6000
```


### HologramMessage
生物死亡时生成的全息图所显示的内容。可使用特定的占位符。
```yaml
  DropOptions:
    HologramMessage:
    - '<#FF9B00>========================'
    - '<mob.name> - <mob.hp>HP'
    - ''
    - '<#FFA300>第一名 | <1.name> | <1.damage>'
    - '<#D1FFFF>第二名 | <2.name> | <2.damage>'
    - '<#D1FFFF>第三名 | <3.name> | <3.damage>'
    - '<#E57A00>第四名 | <4.name> | <4.damage>'
    - '<#E57A00>第五名 | <5.name> | <5.damage>'
    - ''
    - '你的排名：#<player.rank> | <player.damage>'
    - '<#FF9B00>========================'
```
> 如果指定排名没有玩家（例如，生物被少于 5 个玩家击杀），使用占位符的行将不显示


### ChatMessage
生物死亡时发送给玩家的消息内容。可使用特定的占位符。
```yaml
  DropOptions:
    ChatMessage:
    - '<#F28800>===================================='
    - '<#FFA300>BOSS 已击败！'
    - '<#F2B600><mob.name>'
    - ''
    - '<#ffe259>第一名 »<#ffe259> <1.name> - <1.damage>'
    - '<#D1FFFF>第二名 »<#D1FFFF> <2.name> - <2.damage>'
    - '<#D1FFFF>第三名 »<#D1FFFF> <3.name> - <3.damage>'
    - '<#E57A00>第四名 »<#E57A00> <4.name> - <4.damage>'
    - '<#E57A00>第五名 »<#E57A00> <5.name> - <5.damage>'
    - ''
    - '<#F2B600>你的排名：#<player.rank> - <player.damage>（保底：<pity>）'
    - '<#F28800>===================================='
```
> 如果指定排名没有玩家（例如，生物被少于 5 个玩家击杀），使用占位符的行将不显示



## 掉落属性
除上述选项外，你还可以通过内联属性为每个掉落指定特定行为

```yaml
  Drops:
  - amber_1{itemglow=true;itemglowcolor=GOLD;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
```

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| lootsplosion | lootsplosionenabled, ls | 生成的掉落物是否应向外散开        | |
| clientsidedrops | clientsidedropsenabled, csd | 掉落物是否应以客户端方式显示               | |
| hologramname | hologramnameenabled, hn | 掉落物是否应显示全息名称 | |
| itemglow  | itemglowenabled, ig | 掉落物是否发光                                       | |
| itemglowcolor | glowcolor, gc | 发光颜色（如已设置）                                        | |
| itembeam  | itembeamenabled, ib | 掉落物是否在其上方生成粒子光束      | |
| itembeamcolor | beamcolor, bc | 光束颜色（如已设置）                                        | |
| itemvfx   | ivfx, vfx | 掉落物是否具有视觉特效                                      | |
| vfxmaterial | vfxmat, vfxm | 视觉特效的材质                                                 | |
| vfxdata   | vfxd      | 视觉特效的数据                                                  | 0       |
| vfxmodel   | vfxitemmodel | 视觉特效的物品模型。Minecraft 1.21.3+                             | |
| vfxcolor  | vfxc, color | 视觉特效的颜色                                                       | |
| pityModifier | pitymod, pmod | 保底的修正值                                      | 0.0     |
| resetpity | resetp, rp | 是否重置保底                                    | false   |
| pcategory | pitycategory, category | 保底分类                                | DEFAULT |
| damage    | mindamage, min | 玩家必须对该生物造成的最小伤害量，才能为此玩家生成此掉落                                  | 0.0     |
| top       | placement, required | 玩家在伤害排行榜中需要达到的名次才能获得此掉落                                                                    | 2147483647 |
| billboarding | billboard, bill | 全息图的[朝向]                         | VERTICAL |
| brightness | bright, b | 全息图的亮度                                      | 0       |
| fortune   | | 此掉落是否受时运附魔影响                    | false   |
| fortuneMod | | 每级时运附魔对掉落数量的影响程度             |         |


### 时运
时运掉落数量计算：
```math
  amount = min(1, floor(<random.float.0to1> * (2 + fortuneLevel) * fortuneMod ) ) * amount
```

### 示例
```yaml
  Drops:
  - amber_1{itemglow=true;itemglowcolor=GOLD;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - adamantium_ore{itemglow=true;itemglowcolor=WHITE;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - amethyst_1{itemglow=true;itemglowcolor=YELLOW;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - andesite_bricks{itemglow=true;itemglowcolor=LIGHT_PURPLE;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - bananarang{itemglow=true;itemglowcolor=RED;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - augment_sword_midas_6{itemglow=true;itemglowcolor=AQUA;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - blue_stained_tiles{itemglow=true;itemglowcolor=GREEN;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - black_stained_tiles{itemglow=true;itemglowcolor=BLUE;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - bismuth_2{itemglow=true;itemglowcolor=DARK_RED;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxmodel="mythic:effects/item_beam_3"} 1 1
```

<!-- LINKS -->
[朝向]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Display.Billboard.html
[Paper 专属]: https://papermc.io/downloads/all
