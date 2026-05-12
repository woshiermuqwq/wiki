![](http://fs5.directupload.net/images/160306/or6m6n2s.jpg)

在 MythicMobs 中制作自定义物品非常简单。
但与生物和技能不同，通过本插件制作的物品并不附带任何特殊的或独特的功能。
你用 MythicMobs 创建的任何物品，理论上也能用 Minecraft 原生命令做出来，
只不过用 MythicMobs 配置来制作物品要舒服得多。

以下列出的物品配置项中，只有 `internal_name` 和 `Id` 是必填的。其余所有选项和属性都是完全可选的。

你可以在 `\plugins\MythicMobs\Items` 文件夹中创建任意数量的文件，
只要你喜欢，文件名随便起，但必须以 .yml 结尾。

拆解物品配置
-------------------------

#### Internal_Name
这个字符串是物品在 MythicMobs 内部的引用名称，随便你喜欢叫什么都可以。
必须是字母数字，**不允许有空格**。
```yml
example_item:
```

#### Id
物品的基础材质，可以是[这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)列出的任意有效材质。
```yml
example_item:
  Id: leather_chestplate
```

#### Template
物品可以像生物一样使用[模板](/Mobs/Templates)，引用其他物品来继承配置。
```yaml
MyItem:
  Template: MyOtherItem
```
```yaml
MyOtherItem:
  Template: YetAnotherItem, AndAnotherOne
```

<!--
#### **Data**
用于指定物品已消耗的耐久值。
```yml
example_item:
  Id: leather_chestplate
  Data: 0
```
-->

#### Display
设置物品的显示名称。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
```

#### Lore
设置物品的描述文本。你可以用 `{min-max}`、`<random.#to#>` 或 `<random.float.#to#>` 来生成随机数字。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Lore:
    - <rainbow>这行是彩虹色的</rainbow>
    - <red>这行应该是红色的</red>
    - 这是一个随机生成的数字 > <random.-1to50>
    - <gradient:#5e4fa2:#f79459>一个很漂亮的渐变</gradient>
    - 有一些符号，比如 <&sq>，不应该直接写进配置里。请用占位符代替！
```

#### CustomModelData
设置物品的自定义模型数据标签。`Model` 也是 `CustomModelData` 的别名。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  CustomModelData: 12345
```
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Model: 12345
```

#### MaxDurability
修改物品的最大使用次数。注意：必须是不可堆叠的物品。
```yaml
example_item:
  Id: diamond_sword
  MaxDurability: 600
```

#### Durability
设置物品要扣除的耐久值。以下示例中，钻石剑默认有 1561 耐久，设置 100 后还剩 1461。
```yml
example_item:
  Id: diamond_sword
  Durability: 100
  Display: <green>An Example Item</green>
```

#### Attributes
特殊字段，允许为特定装备槽位添加物品属性。参见[物品属性](/Items/Attributes)。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Attributes:
    Chest:
      Health: 25
```

#### Amount
设置插件调用此物品时默认给予的数量。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Amount: 1
```

#### Options
一个包含多种子选项的特殊字段。参见[物品选项](/Items/Options)。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Options:
    AppendType: true
    Color: 255,0,0
```

#### Enchantments
任何物品都可以添加任意附魔。
可用附魔列表参见[这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html)。
也请参阅[附魔](/items/Enchantments)页面了解如何配置物品附魔。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Options:
    Color: 255,0,0
  Enchantments:
    - PROTECTION_ENVIRONMENTAL:2
    - THORNS:3
```

#### Hide
特殊字段，用于在物品提示框中隐藏特定信息。
所有可用标志参见：
- [Spigot 版点这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/ItemFlag.html)
- [Paper 版点这里](https://jd.papermc.io/paper/1.21.3/org/bukkit/inventory/ItemFlag.html)
> 如果服务器版本低于 1.20.5，还可以使用 `HIDE_POTION_EFFECTS`
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Attributes:
    Chest:
      Health: 25
  Enchantments:
    - THORNS:3
  Options:
    Color: 255,0,0
  Hide:
    - ATTRIBUTES
    - ENCHANTS
```

#### PotionEffects
设置物品的药水效果。如果[基础物品](#id)不是 `potion`、`splash_potion`、`lingering_potion` 或 `tipped_arrow`，这些效果不会生效。
参见[药水](/Items/Potions)。
```yml
example_item:
  Id: potion
  Display: <#f99cb3>Pink potion
  Options:
    Color: 249,156,179
  PotionEffects:
    - CONFUSION 100 2
```
| 效果属性 | 别名 | 说明 | 默认值 |
|--------------------|---------|---------------------------------------------------------------|---------|
| duration           | d       | 效果持续时长 | 60 |
| level              | l       | 效果的等级。实际等级为此值 +1 | 0 |
| ambientparticles   | ambient, a | 是否显示环境粒子 | false |
| hasparticles       | particles, p | 是否显示粒子 | true |
| hasicon            | icon, i | 是否显示效果图标 | true |


#### BannerLayers
设置旗帜或盾牌的图案层。
参见[旗帜图案层](/Items/Banner-Layers)。
```yml
example_item:
  Id: yellow_banner
  BannerLayers:
    - RED BASE
    - WHITE CURLY_BORDER
    - WHITE STRIPE_CENTER
```

#### CanPlaceOn
设置玩家处于冒险模式时，此物品可以放置在哪类方块上。
```yaml
MyCoolAnvil:
  Id: ANVIL
  CanPlaceOn:
  - diamond_block
```

#### CanBreak
设置玩家处于冒险模式时，此物品可以破坏哪类方块。
```yaml
MyCoolStick:
  Id: STICK
  CanBreak:
  - grass_block
  - diamond_block
  - obsidian
```

#### BlockStates
允许你指定物品的方块状态。
```yaml
TestBlockStates:
  Material: OAK_SLAB
  Display: 'Waterlogged Slab'
  Options:
    Placeable: true # Crucible 选项
  BlockStates:
  - type top
  - waterlogged true
```

#### Glider
允许物品当作鞘翅使用。
用于处理物品的[滑翔组件](https://minecraft.wiki/w/Data_component_format/glider)。
```yaml
MyItem:
  Glider: true
```

#### Group
设置物品在 `/mm items browse` 中所属的分组。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Group: 'Armor'
```

#### NBT
设置要附加到物品上的 NBT 标签。
这可以让你与其他插件产生联动，或者仅仅用来存储自定义信息。

在给物品添加 NBT 标签之前，你需要了解 [SNBT 格式](https://minecraft.wiki/NBT_format#SNBT_format)。
你可以通过在标签值前面加前缀来改变值的类型：

| 前缀 | int/ | float/ | double/ | byte/ | bool/ | boolean/ |
|----------|------|--------|---------|-------|-------|----------|

举个例子，把这个 SNBT：`{name1:123,name2:"sometext1",name3:{subname1:456,subname2:"sometext2"}}` 转换成 MythicMobs 的格式：

```yml
example_item:
  Id: STICK
  NBT:
    name1: int/123
    name2: sometext1
    name3:
      subname1: int/456
      subname2: sometext2
```

```yml
#带有 MYTHIC_TYPE 标签的物品
example_item:
  Id: stick
  NBT:
    MYTHIC_TYPE: example_item
```

```yml
example_item:
  Id: diamond_sword
  NBT:
    CanDestroy:
      - stone
      - dirt
    Base:
      ATag: int/20
      SomeOtherTag: something
    SomeModifier:
      Value: double/0.25
      CanDoThis: boolean/true
    Denizen NBT:
      somedenizentag: a_string
```

```yml
another_example_item:
  Id: diamond_sword
  NBT:
    Base:
      ATag: 20
      SomeOtherTag: something
    GemSlots:
      RedGem: 0
    Denizen NBT:
      somedenizentag: a_string
```

#### Trim
设置物品的盔甲纹饰。
```yaml
example_item:
  Material: GOLDEN_CHESTPLATE
  Options:
    Trim:
      Material: iron
      Pattern: wild
```

#### Firework
设置烟花火箭或烟花之星物品的各种属性。
参见[烟花](/Items/Firework)了解各项选项的详细说明。
```yml
example_item:
  Id: firework
  Firework:
    Colors:
    - 255,0,255
    - 0,0,0
    FadeColors:
    - 200,0,0
    Flicker: true
    Trail: true
```

#### Book
成书的一系列选项。
```yaml
SomeBook:
  Id: WRITTEN_BOOK
  Title: <green>How to make YouTube Videos
  Author: CarsonJF
  Pages:
  - "Page 1"
  - "Page 2\n\nwith some other lines"
  - "Page 3"
```

#### Consumable
允许物品被食用。包含可自定义的动画和音效。
用于处理物品的[可食用组件](https://minecraft.wiki/w/Data_component_format/consumable)。
```yaml
MyExampleItem:
  Consumable:
    ConsumeSeconds: 3
    HasParticles: false
    Animation: SPEAR
    Sound: item.crossbow.quick_charge_3
    ConsumeEffects:
    # 以下均为特殊技能，也是此字段中唯一可用的技能
    - potion{type=absorption;d=200}
    - randomteleport{radius=5}
    - removePotion{type=wither}
    - clearAllEffects
    - sound{sound=entity.ghast.scream}     
```

#### DeathProtection
如果存在此配置，该物品会在持有者濒死时恢复 1 点生命值，就像不死图腾那样。
用于处理物品的[免死组件](https://minecraft.wiki/w/Data_component_format/death_protection)。
```yaml
MyTotemItem:
  DeathProtection:
    ConsumeEffects: # 与 Consumable 的 ConsumeEffects 用法相同
    - potion{type=absorption;d=200}
    - randomteleport{radius=5}
    - removePotion{type=wither}
    - clearAllEffects
    - sound{sound=entity.ghast.scream}     
```


#### Food
用于处理物品的[食物组件](https://minecraft.wiki/w/Data_component_format/food)。
需要先设置 [Consumable](/Items/Items#consumable) 才能生效。
```yaml
NetheritePops:
  Material: NETHERITE_SCRAP
  Display: 'Delicious Scraps'
  Food:
    Nutrition: 2
    Saturation: 2
    CanAlwaysEat: true
```


#### Equippable
用于处理物品的[可装备组件](https://minecraft.wiki/w/Data_component_format/equippable)。

| 标签 | 说明 | 默认值 |
|-------------------|-------------------------------------------------------------------------|----------|
| Model             | 装备时使用的装备模型资源路径。如果不写命名空间，默认使用 `minecraft:` | |
| Slot              | 物品装备的[槽位](/Skills/EquipSlot)。如果不指定，插件会尝试根据基础材质中是否含以下字符串来"猜测"：`_HELMET`、`_CHESTPLATE`、`_LEGGINGS`、`_BOOTS` 或 `SHIELD` | |
| CameraOverlay     | 装备时使用的覆盖层纹理资源路径。如果不写命名空间，默认使用 `minecraft:` | |
| Dispensable       | 是否可以通过发射器来装备此物品 | true |
| Swappable         | 是否可以通过右键单击将物品装备到对应槽位 | true |
| DamageOnHurt      | 穿戴者受伤时此物品是否会损坏 | true |
| EquipSound        | 装备时播放的音效 | item.armor.equip_generic |
| EntityTypes       | 可以装备此物品的实体类型列表 | |

```yaml
KING_HELMET:
  Id: PAPER
  Display: '&dKing Helmet'
  Equippable:
    Model: yourNamespace:thePathToYourCustomModel
    Slot: HEAD
    CameraOverlay: yournamespace:thePathToYourTexture
    Dispensable: true
    Swappable: true
    DamageOnHurt: true
    EquipSound: "item.armor.equip_iron"
    EntityTypes: 
      - "PLAYER"
```

#### UseCooldown
用于处理物品的[使用冷却组件](https://minecraft.wiki/w/Data_component_format/use_cooldown)。

| 标签 | 说明 | 默认值 |
|-------------------|-------------------------------------------------------------------------|----------|
| CooldownGroup     | 用于标识此冷却组的唯一资源路径。如果存在，该物品将纳入此冷却组，不再与基础物品类型共享冷却，而是与该冷却组中的其他物品共享冷却。如果不写命名空间，默认使用 `minecraft:` | |
| CooldownSeconds   | 冷却时长，以秒为单位。必须为整数，因此无法精确到 tick | |

```yaml
ExampleItem:
  Material: STICK
  UseCooldown:
    CooldownGroup: coolwands # 只能用小写字母！
    CooldownSeconds: 3
``` 

#### Tool
用于处理物品的[工具组件](https://minecraft.wiki/w/Data_component_format/tool)。

| 标签 | 说明 | 默认值 |
|-------------------|-------------------------------------------------------------------------|----------|
| DamagePerBlock    | 每次用此工具破坏方块时消耗的耐久值。必须为非负整数 | |
| DefaultMiningSpeed | 此工具的默认挖掘速度，在没有规则覆盖时使用 | 1.0 |
| Rules             | 工具的规则列表 | |

| 规则属性 | 别名 | 说明 | 默认值 |
|--------------------|---------|---------------------------------------------------------------|---------|
| materials          |         | 此规则适用的材质列表。也可以是一个单独的方块标签 | |
| speed              |         | 如果正在挖掘的材质匹配，覆盖默认挖掘速度 | 1.0 |
| isCorrectForBlock  |         | 如果正在挖掘的材质匹配，覆盖此工具是否被视为"合适的工具"——这影响挖掘是否达到最高效率，以及如果方块的战利品表有要求时是否会掉落物品 | false |

```yaml
OBSIDIAN_BREAKER:
  Id: COD
  Display: '&8Obsidian Breaker'
  Tool:
    DamagePerBlock: 1
    DefaultMiningSpeed: 0.0
    Rules:
      - materials: "OBSIDIAN,CRYING_OBSIDIAN"
        speed: 10000.0
        isCorrectForBlock: true
```
```yaml
TREE_BREAKER:
  Id: COD
  Display: '&aTree Breaker'
  Tool:
    DamagePerBlock: 1
    DefaultMiningSpeed: 0.0
    Rules:
      - materials: "completes_find_tree_tutorial" # 使用标签的示例
        speed: 10000.0
        isCorrectForBlock: true
```

#### TooltipStyle
用于处理物品的[提示框样式](https://minecraft.wiki/w/Data_component_format/tooltip_style)。
自定义提示框背景和边框精灵图的资源路径，对应纹理分别为 `/assets/<namespace>/textures/gui/sprites/tooltip/<id>_background` 和 `/assets/<namespace>/textures/gui/sprites/tooltip/<id>_frame`，在使用 TooltipStyle 时值为 `<namespace>:<id>`。

```yaml
ExampleItem:
  Id: STONE_SWORD
  TooltipStyle: minecraft:verycooltooltip
```

#### Spawner
配置刷怪笼物品的选项。
```yaml
TestSpawner:
  Material: SPAWNER
  Display: 'Testing Spawner'
  Spawner:
    Delay: 0
    MinSpawnDelay: 20
    MaxSpawnDelay: 80
    RequiredPlayerRange: 16
    SpawnCount: 4
    SpawnRange: 8
    MaxNearbyEntities: 8
    Mobs:
    - Type: TestingDummy
      Weight: 5
      MinBlockLight: 10
      MaxBlockLight: 10
      MinSkyLight: 10
      MaxSkyLight: 10
```


#### DropOptions
允许物品在掉落时自带指定的[华丽掉落选项](/drops/FancyDrops#drop-attributes)。

```yaml
LegendarySword:
  Id: DIAMOND_SWORD
  Display: '<red>Legendary Sword'
  DropOptions:
    # 此物品的默认掉落设置
    DropGlowColor: GOLD
    DropBeamColor: '#FFA500' # 橙色光束
    DropLootsplosion: true
    DropHologram: true
    DropVFX: true
    DropVFXMaterial: DIAMOND
    DropVFXData: 0
    DropVFXColor: '#55FF55'
    DropBillboarding: CENTER
    DropBrightness: 15
    DropClientSide: false
```

#### Rarity
设置物品的稀有度。
可选值：COMMON、UNCOMMON、RARE、EPIC。
```yaml
TheMusical:
  Rarity: EPIC
  Material: COMPASS
```


## 完整示例
更多物品示例请参见[示例](/examples/Common-Examples#items)章节。