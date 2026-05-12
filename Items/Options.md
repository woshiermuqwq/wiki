这里会列出所有可用的选项。
这些选项必须放在物品配置中的 `Options:` 标签下面。
```yml
example_item:
  Id: diamond
  Options:
    SomeOption: value
```

# 通用选项
以下选项适用于所有物品：

#### Repairable
将物品的修复费用设为最大值，使其在铁砧和附魔台中完全无法编辑。
会覆盖 RepairCost 选项。
默认为 `false`。
```yaml
  Options:
    Repairable: false
```  

#### RepairCost
设置物品的修复费用。
如果设为小于 0，则使用原版默认值。
默认为 `-1`。
```yaml
  # 严格来说不是 Options 下的选项，但放在这里是因为和 Repairable 相关
  RepairCost: 10
```

#### Unbreakable
给物品打上不可破坏标签。
设为 true 的物品不会消耗耐久。
默认为 `false`。
```yaml
  Options:
    Unbreakable: true
```


#### Glint
给物品添加附魔光效。
默认为 `false`。
```yaml
  Options:
    Glint: true
```

#### HideFlags
**注意：此功能在 1.20.5 及以上版本不存在！** [请改用此方式](/Items/Items#hide)

隐藏所有物品标志，使附魔等信息不在物品描述中显示（但请注意，物品仍会保留附魔光效）。
默认为 `false`。
```yaml
  Options:
    HideFlags: true
```

#### PreventStacking
阻止该物品与同类物品堆叠。
默认为 `false`。
```yaml
  Options:
    PreventStacking: true
```

#### StackSize
设置物品在背包中的最大堆叠数量。与属性一起使用时无效。
```yaml
  Options:
    StackSize: 16
```

#### GenerateUUID
在物品生成时为其附加一个随机 UUID。便于检测复制物品。启用此选项会自动阻止同类物品堆叠，因为它们有不同的 UUID。
```yaml
  Options:
    GenerateUUID: true
```

#### GenerateTimestamp
在物品生成时附加当前的 Unix 时间戳。便于追溯物品的创建时间。启用此选项会阻止不同时间生成的同类物品堆叠。
```yaml
  Options:
    GenerateTimestamp: true
```


#### ItemModel
物品应使用的模型，[工作原理见此组件](https://minecraft.wiki/w/Data_component_format#item_model)。
```yaml
MODELED_ITEM:
  Id: PAPER
  Display: '&dKing Helmet'
  Options:
    ItemModel: SomeModel
```

#### FireResistant
物品是否防火，类似于下界合金的效果。
默认为 `false`。
```yaml
  Options:
    FireResistant: true
```

# 玩家头颅
仅适用于玩家头颅类物品

#### Player
设置玩家头颅的纹理。
值必须是目标玩家的游戏内名称。
玩家头颅必须使用 data 值 3 才能生效。
```yaml
  Options:
    Player: Herobrine
```

#### SkinTexture
同样用于设置玩家头颅的纹理，但改用皮肤 URL。
> - 在浏览器中访问：https://sessionserver.mojang.com/session/minecraft/profile/此处填写玩家的截断uuid。
> - 使用 http://mcuuid.net/ 来查找玩家的截断 UUID。

玩家头颅必须使用 data 值 3 才能生效。
此选项也支持哈希值。
```yaml
  Options:
    SkinTexture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdlMGFhOTQzM2RiYTliNzU5MzJhMTFkYzk0ZDQwNmJkZTE5ZTg2MzUxNDIxNDkyYjNlZDM3OGM4ZTFhN2NjIn19fQ==
```


# 可染色物品

#### Color
按照 RGB 设置给盔甲染色。范围 0-255。
也可以使用预定义的颜色名称，参见[这里](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。
可以用 Windows 自带的画图工具取色——打开后选择"编辑颜色"获取 RGB 值。
仅适用于皮革盔甲、旗帜、盾牌等可染色物品。
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
包含较多选项的示例：
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
烟花火箭的示例：
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