![](http://fs5.directupload.net/images/160306/or6m6n2s.jpg)

在 MythicMobs 中制作自定义物品相当简单。
但与生物和技能不同，使用此插件制作的物品不附带任何特殊或独特的功能。
你用 MythicMobs 创建的任何物品也可以通过 Minecraft 指令创建，
不过使用 MythicMobs 配置来制作物品要舒适得多。

以下物品可用的选项中，只有 `internal_name` 和 `Id` 是必需的。所有其他选项/属性都是完全可选的。

你可以在 `\plugins\MythicMobs\Items` 文件夹中创建任意数量的文件，只要文件以 .yml 结尾，可以随意命名。

## 物品配置详解

#### Internal_Name
此字符串是物品在 MythicMobs 内部的引用名称，可以是任意名称。
必须为字母数字，**不允许有空格**。
```yml
example_item:
```

#### Id
物品使用的基础材料，可以是[此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)列出的任何有效材料。
```yml
example_item:
  Id: leather_chestplate
```

#### 模板
物品可以使用[模板](/Mobs/Templates)，和生物一样，同时可以引用其他物品。
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
用于指定物品已损耗的耐久度点数。
```yml
example_item:
  Id: leather_chestplate
  Data: 0
```
-->

#### 显示
设置物品的显示名称。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
```

#### 物品描述
设置物品的lore。你可以使用 `{min-max}`、`<random.#to#>` 或 `<random.float.#to#>` 来生成随机数。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Lore:
    - <rainbow>This line is a rainbow</rainbow>
    - <red>This line should be red</red>
    - This is a random generated number > <random.-1to50>
    - <gradient:#5e4fa2:#f79459>A really nice gradient</gradient>
    - There are some symbols, like <&sq>, that should never be put as is into a configuration. Use a placeholder!
```

#### CustomModelData
设置物品的 CustomModelData 标签。`Model` 也是 `CustomModelData` 的别名。
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
更改物品的最大使用次数。注意：必须是不可堆叠的物品。
```yaml
example_item:
  Id: diamond_sword
  MaxDurability: 600
```

#### Durability
设置要从物品中扣除的耐久度。以下示例将钻石剑的耐久度设为 1461，因为默认值是 1561。
```yml
example_item:
  Id: diamond_sword
  Durability: 100
  Display: <green>An Example Item</green>
```

#### 属性
特殊的字段，允许向特定装备栏位添加物品属性。参见[物品属性](/Items/Attributes)。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Attributes:
    Chest:
      Health: 25
```

#### Amount
设置当插件调用此物品时默认给予的物品数量。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Amount: 1
```

#### 选项
一个包含众多子选项的特殊字段。参见[物品选项](/Items/Options)。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Options:
    AppendType: true
    Color: 255,0,0
```

#### 附魔
任何物品都可以拥有任意附魔。
可用的附魔列表可在[此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html)找到。
另请参阅[附魔](/items/Enchantments)页面了解如何配置物品附魔。
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
特殊字段，允许从物品提示中隐藏特定内容。
所有可用的标志：
- [如果你使用 **Spigot**，在此查看](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/ItemFlag.html)
- [如果你使用 **Paper**，在此查看](https://jd.papermc.io/paper/1.21.3/org/bukkit/inventory/ItemFlag.html)
> 如果服务器版本 &lt;1.20.5，你也可以使用 `HIDE_POTION_EFFECTS`
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
设置物品的药水效果。如果[基础物品](#id)不是 `potion`、`splash_potion`、`lingering_potion` 或 `tipped_arrow`，这些效果将不会生效。
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
| 效果属性 | 别名 | 描述 | 默认 |
|--------------------|---------|---------------------------------------------------------------|---------|
| duration           | d       | 效果的持续时间 | 60 |
| level              | l       | 效果的等级。实际等级为此值 +1 | 0 |
| ambientparticles   | ambient, a | 是否显示环境粒子 | false |
| hasparticles       | particles, p | 是否显示粒子 | true |
| hasicon            | icon, i | 是否显示效果图标 | true |

#### BannerLayers
设置旗帜或盾牌的旗帜层。
参见[旗帜层](/Items/Banner-Layers)。
```yml
example_item:
  Id: yellow_banner
  BannerLayers:
    - RED BASE
    - WHITE CURLY_BORDER
    - WHITE STRIPE_CENTER
```

#### CanPlaceOn
设置此物品在冒险模式下可以放置的方块。
```yaml
MyCoolAnvil:
  Id: ANVIL
  CanPlaceOn:
  - diamond_block
```

#### CanBreak
设置此物品在冒险模式下可以破坏的方块。
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
允许物品用作鞘翅。
用于处理物品的 [Glider组件](https://minecraft.wiki/w/Data_component_format/glider)。
```yaml
MyItem:
  Glider: true
```

#### Group
设置物品在 `/mm items browse` 中的分组。
```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Group: 'Armor'
```

#### NBT
设置物品的 NBT 标签。
这允许与其他插件互通，或仅用于存储自定义信息。

在向物品添加 NBT 标签之前，你需要了解 [SNBT 格式](https://minecraft.wiki/NBT_format#SNBT_format)。
标签值的类型可以通过在标签值前添加前缀来更改：

| 前缀 | int/ | float/ | double/ | byte/ | bool/ | boolean/ |
|----------|------|--------|---------|-------|-------|----------|

让我们将此 SNBT：`{name1:123,name2:"sometext1",name3:{subname1:456,subname2:"sometext2"}}` 转换为 Mythic 格式：

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
设置物品的纹饰。
```yaml
example_item:
  Material: GOLDEN_CHESTPLATE
  Options:
    Trim:
      Material: iron
      Pattern: wild
```

#### Firework
设置烟花或烟花之星物品的各项属性。
参见[烟花](/Items/Firework)了解每个选项的详细分解。
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
书本选项组。
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
允许物品被食用。包含可自定义的动画和声音。
用于处理物品的 [Consumable组件](https://minecraft.wiki/w/Data_component_format/consumable)。
```yaml
MyExampleItem:
  Consumable:
    ConsumeSeconds: 3
    HasParticles: false
    Animation: SPEAR
    Sound: item.crossbow.quick_charge_3
    ConsumeEffects:
    # 以下是特殊机制，仅此字段中可用
    - potion{type=absorption;d=200}
    - randomteleport{radius=5}
    - removePotion{type=wither}
    - clearAllEffects
    - sound{sound=entity.ghast.scream}     
```

#### DeathProtection
如果存在，此物品会保护持有者免于死亡，恢复一点生命值，就像不死图腾一样。
用于处理物品的 [DeathProtection组件](https://minecraft.wiki/w/Data_component_format/death_protection)。
```yaml
MyTotemItem:
  DeathProtection:
    ConsumeEffects: # 与 Consumable 相同
    - potion{type=absorption;d=200}
    - randomteleport{radius=5}
    - removePotion{type=wither}
    - clearAllEffects
    - sound{sound=entity.ghast.scream}     
```

#### Food
用于处理物品的 [Food组件](https://minecraft.wiki/w/Data_component_format/food)。
需要设置 [Consumable](/Items/Items#consumable) 才能生效。
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
用于处理物品的 [Equippable组件](https://minecraft.wiki/w/Data_component_format/equippable)

| 标签 | 描述 | 默认 |
|-------------------|-------------------------------------------------------------------------|----------|
| Model             | 装备时使用的装备模型资源路径。如果不使用命名空间，将默认使用 `minecraft:` | |
| Slot              | 放置物品的[栏位](/Skills/EquipSlot)。如果未指定，插件会尝试根据基础材料是否包含以下字符串来"猜测"：`_HELMET`、`_CHESTPLATE`、`_LEGGINGS`、`_BOOTS` 或 `SHIELD` | |
| CameraOverlay     | 装备时使用的覆盖纹理资源路径。如果不使用命名空间，将默认使用 `minecraft:` | |
| Dispensable       | 物品是否可以通过发射器发射 | true |
| Swappable         | 物品是否可以通过右键点击装备到相应栏位 | true |
| DamageOnHurt      | 穿戴实体受伤时此物品是否受损 | true |
| EquipSound        | 装备物品时播放的声音 | item.armor.equip_generic |
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
用于处理物品的 [UseCooldown组件](https://minecraft.wiki/w/Data_component_format/use_cooldown)

| 标签 | 描述 | 默认 |
|-------------------|-------------------------------------------------------------------------|----------|
| CooldownGroup     | 用于标识此冷却组的唯一资源路径。如果存在，物品将加入一个冷却组，不再与其基础物品类型共享冷却，而是与同一冷却组中的其他物品共享冷却。如果不使用命名空间，将默认使用 `minecraft:` | |
| CooldownSeconds   | 冷却持续时间（秒）。必须是整数，因此冷却无法精确到 tick 级别 | |

```yaml
ExampleItem:
  Material: STICK
  UseCooldown:
    CooldownGroup: coolwands # 仅用小写字母！
    CooldownSeconds: 3
```

#### Tool
用于处理物品的 [Tool组件](https://minecraft.wiki/w/Data_component_format/tool)

| 标签 | 描述 | 默认 |
|-------------------|-------------------------------------------------------------------------|----------|
| DamagePerBlock    | 使用此工具破坏每个方块时消耗的耐久度。必须是非负整数 | |
| DefaultMiningSpeed | 此工具的默认挖掘速度，当没有规则覆盖时使用 | 1.0 |
| Rules             | 工具的规则列表 | |

| 规则属性 | 别名 | 描述 | 默认 |
|--------------------|---------|---------------------------------------------------------------|---------|
| materials          |         | 此规则适用的材料列表。也可以是一个方块标签 | |
| speed              |         | 如果正在挖掘的材料匹配，覆盖默认挖掘速度 | 1.0 |
| isCorrectForBlock  |         | 如果正在挖掘的材料匹配，覆盖是否视此工具为正确工具以最高效率挖掘，并在方块的战利品表需要时掉落物品 | false |

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
用于处理物品的 [提示框样式](https://minecraft.wiki/w/Data_component_format/tooltip_style)。
自定义提示框背景和边框精灵的资源路径，引用纹理 `/assets/<namespace>/textures/gui/sprites/tooltip/<id>_background` 和 `/assets/<namespace>/textures/gui/sprites/tooltip/<id>_frame`，可通过 TooltipStyle 的值 `<namespace>:<id>` 来使用。

```yaml
ExampleItem:
  Id: STONE_SWORD
  TooltipStyle: minecraft:verycooltooltip
```

#### Spawner
配置生成器物品的选项。
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
允许物品在掉落时自带特定的 [FancyDrops 选项](/drops/FancyDrops#drop-attributes)。

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
可选值：COMMON, UNCOMMON, RARE, EPIC
```yaml
TheMusical:
  Rarity: EPIC
  Material: COMPASS
```

## 示例
更多物品示例可以在[示例](/examples/Common-Examples#items)章节中找到。
