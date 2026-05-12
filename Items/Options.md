All available 选项 将 listed here.
These 选项 必须为 placed 在...下 `Options:` tag inside your 物品 configurations.
```yml
example_item:
  Id: diamond
  Options:
    SomeOption: value
```

# Universal 选项
These 选项 are applicable to all 物品:

#### Repairable
Se将repair cost of the 物品设maximum, making it 完全 uneditable in anvils and/or 附魔 tables。
WiWill 覆盖 the RepairCost 选项.
Defaults to `false`.
```yaml
  Options:
    Repairable: false
```  

#### RepairCost
Se设repair cost of the 物品。
If若set to 小于 0，the 原版 one将willbe used。
DeDefaults to `-1`.
```yaml
  # Not an option, apparently, but kept here because of repairable
  RepairCost: 10
```

#### Unbreakable
Se设unbreakable tag on the 物品。
It物品 with this 设为 true 不会 lose durability.
DeDefaults to `false`.
```yaml
  Options:
    Unbreakable: true
```


#### Glint
添加 the 附魔 glint visual 效果 to an 物品
DeDefaults to `false`.
```yaml
  Options:
    Glint: true
```

#### HideFlags
**注意: this feature 不 exist >=1.20.5!** [Use this instead](/物品/物品#hide)

HiHides all the 物品 标志, making things like enchants not visible in the 物品 物品描述 (please 注意 但是 that the 物品 仍会 have an enchanted glow).
Defaults to `false`.
```yaml
  Options:
    HideFlags: true
```

#### PreventStacking
PrPrevents the 物品 from stacking to similar 物品.
DeDefaults to `false`.
```yaml
  Options:
    PreventStacking: true
```

#### StackSize
设maximum 堆叠 size of the 物品 in the inventory. Does not work when used alongside 属性。
```yaml
  Options:
    StackSize: 16
```

#### GenerateUUID
应用 a random UUID to the 物品 upon generation. Useful to easily detect duped 物品. Enabling this 选项 自动 阻止 similar 物品 from stacking, as they share different UUIDs.
```yaml
  Options:
    GenerateUUID: true
```

#### GenerateTimestamp
应用 the current unix time to the 物品 on generation. Useful to backtrack the exact time an 物品 was created. Enabling this 选项 will prevent 物品 from stacking if they were generated at different times.
```yaml
  Options:
    GenerateTimestamp: true
```


#### ItemModel
The model that 应为 applied to the 物品, which [works like this 物品 component](https://Minecraft.wiki/w/Data_component_format#item_model)
```yaml
MODELED_ITEM:
  Id: PAPER
  Display: '&dKing Helmet'
  Options:
    ItemModel: SomeModel
```

#### FireResistant
Whthe 物品是否resistant to 触发, as netherite is。
DeDefaults to `false`.
```yaml
  Options:
    FireResistant: true
```

# Playerheads
Only applicable to playerhead 类型 物品

#### 玩家
Se设texture of the 玩家 head。
ThThe 值 必须为 the IGN of the 目标 玩家.
Pl玩家 heads must use data 值 3 for this to work.
```yaml
  Options:
    Player: Herobrine
```

#### SkinTexture
AlAlso sets the texture of the 玩家 head, but instead uses a SkinURL.
> > - 类型 into browser: https://sessionserver.mojang.com/session/Minecraft/profile/trimmeduuidofplayerhere.
> > - Use http://mcuuid.net/ to find the trimmed uuid of the 玩家.

Pl玩家 heads must use data 值 3 for this to work.
ThThis 选项 也支持hashes。
```yaml
  Options:
    SkinTexture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdlMGFhOTQzM2RiYTliNzU5MzJhMTFkYzk0ZDQwNmJkZTE5ZTg2MzUxNDIxNDkyYjNlZDM3OGM4ZTFhN2NjIn19fQ==
```


# Dyeable 物品

#### 颜色
DyDyes the armor piece to a color according to RGB 设置. 0-255.
AlAlternately can use a predefined color. Found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html).
CaCan pick colors using the Paint program on Windows. Open it up then choose "Edit Colors" to get your RGB 值.
Only usable on leather armor 类型, banners, shields and such.
```yaml
  Options:
    Color: RED
```
```yaml
  Options:
    Color: 102,102,153
```


# 示例
```yaml
ClothSlippers:
  Id: 301
  Data: 0
  Display: '&fCloth Slippers'
  Lore:
  - ''
  - 'So Soft!'
  - ''
  Enchantments:
  - DURABILITY:1
  Options:
    Color: 200,200,200
```
Lots of possible 选项 included:
```yaml
TestHead:
  Id: 397
  Data: 3
  Options:
    Player: Rickyling
```
```yaml
dat_item_though:
  Id: banner
  Data: 4
  Display: '&c&lThe Banner&r'
  Lore:
  - ''
  - '&rIt<&sq>s the perfect stone.'
  - '&cNever question that.'
  - ''
  Amount: 8
  Options:
    Color: 200,200,200
    Unbreakable: true
  Enchantments:
  - DURABILITY:1
  - ARROW_FIRE:10
```
An 示例 of a firework rocket
```yaml
FireworkGoBoom:
  Id: FIREWORK_ROCKET
  Display: 'Rocket'
  Firework:
    Colors:
    - 255,0,255
    - 0,0,0
    FadeColors:
    - 200,0,0
    Flicker: true
    Trail: true
```