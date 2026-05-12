MythicMobs 完全围绕自定义实体/生物构建，有大量的选项和属性可供你使用。以下是可添加到自定义生物中的完整选项/属性列表。

以下大部分选项都是可选的，意味着你不需要在每次创建新生物时都配置整个列表。真正必需的是 `Internal_Name` 和 `Type`。

目录：

[[_TOC_]]

## 生物配置详解

#### Internal_Name
此字符串是生物在 MythicMobs 内部的引用名称，可以是你喜欢的任何名称。
必须是一个唯一的名称，不与其他内部生物名称冲突，**不允许有空格**。
```yml
example_name:
```

#### Type
此字段决定你的生物基于哪个实体类型。
可用[实体类型]的完整列表可以在 Spigot Javadocs 上找到，而[这里](/Mobs/Types)列出了明确实现的类型。
> 对于 Minecraft 添加到原版游戏中的新实体类型，在 Mythic 添加对这些实体类型的支持之前，许多生物选项不会生效。

> 某些实体类型可能存在负面的、难以发现的怪异行为。建议你参考[不稳定实体类型](/Mobs/Mobs/Unstable-Entity-Types)页面，以便更好地判断当前项目中应使用哪种实体。
```yml
example_mob:
  Type: zombie
```
```yml
another_mob:
  Type: ZOMBIE
```

#### Display
设置生物的显示名称。
此选项支持颜色代码和[占位符]。
**生物的名称不会自行更改或更新，你必须使用 [setname] 技能来更改或更新它。**
```yml
example_mob:
  Type: zombie
  Display: Example Mob
```
```yml
example_mob:
  Type: zombie
  Display: Example Mob <caster.hp> <red><&heart></red>
```

#### Health
设置生物最大血量属性的基础值。
Mythic 对最大血量没有限制，但 Spigot 将最大血量上限设为 `2048`。
这可以在 Spigot 的配置文件 `server_root\spigot.yml` 中轻松更改。
当生物手持或穿戴带有属性修正的物品时，也会影响总最大血量。
```yml
example_mob:
  Type: zombie
  Display: Example Mob
  Health: 30
```

#### Damage
设置生物近战攻击伤害属性的基础值。
1 点伤害等于 0.5 颗心，因此伤害为 6 的生物将造成 3 颗满心的伤害。
此属性不会影响远程攻击（如箭矢或药水）造成的伤害。
当生物手持或穿戴带有属性修正的物品时，也会影响该生物的近战伤害。
```yml
example_mob:
  Type: zombie
  Display: Example Mob
  Damage: 20
```

#### Armor
设置生物护甲属性的基础值。
Minecraft 将最大护甲值上限设为 30。
当生物手持或穿戴带有属性修正的物品时，也会影响总护甲值。
```yml
example_mob:
  Type: zombie
  Display: Tanker
  Armor: 25
```

#### HealthBar
在生物受伤后，在其上方创建一个基础血量条全息显示。
```yml
example_mob:
  Type: zombie
  Display: HealthyBoi
  Health: 1000
  HealthBar:
    Enabled: true
    Offset: 1.45
```

#### BossBar
定义并控制生物的血条。
外观类似末影龙或凋灵的血条，但外观可配置。
参见 [Boss血条](/Mobs/BossBar)
```yml
example_mob:
  Type: zombie
  Armor: 25
  BossBar:
    Enabled: true
    Title: Tanker
    Range: 20
    Color: RED
    Style: NOTCHED_6
    CreateFog: true
    DarkenSky: true
    PlayMusic: true
```

#### Faction
设置生物的阵营，可用于高级[自定义 AI]配置或[目标选择器过滤]。
Faction 区分大小写，因此在使用阵营条件时请谨慎。
```yml
example_mob:
  Type: zombie
  Armor: 25
  Faction: Tank
```

#### Mount
设置生物的坐骑。
必须是另一个 MythicMobs 生物。
生物将在生成时自动骑乘到指定的坐骑上。
```yml
another_example:
  Type: chicken
  Mount: example_mo
```

#### Display Options
设置显示实体选项。
可用显示选项列表可在[显示选项](/Mobs/DisplayOptions)页面找到。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```

#### Options
这是一个包含众多子选项的特殊字段，例如决定生物是否应消失、设置击退抗性、跟随范围、移动速度等等。
可用生物选项列表可在[生物选项](/Mobs/Options)页面找到。
```yml
slow_persistent_mob:
  Type: husk
  Options:
    MovementSpeed: 0.025
    Despawn: PERSISTENT
```

#### Modules
此字段允许你启用或禁用模块，如[仇恨表]和/或[免疫表]。
```yml
example_mob:
  Type: husk
  Modules:
    ThreatTable: false
    ImmunityTable: false
```

#### AIGoalSelectors
修改和自定义生物的 [AI 目标]。
```yml
dummy_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
```
```yml
passive_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
    - randomstroll
    - randomlookaround
```

#### AITargetSelectors
修改和自定义生物的 [AI 目标选择器]。
```yml
neutral_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
    - meleeattack
    - randomstroll
    - randomlookaround
  AITargetSelectors:
    - clear
    - attacker
```

#### Drops
添加或完全修改生物的战利品掉落。
可以是原版物品、Mythic 物品、经验值、跨插件物品（如果支持），甚至是带有自己条件系统的自定义掉落表。
参见 [掉落与掉落表](/drops/Drops) 了解更多信息。
```yml
example_mob:
  Type: zombie
  Options:
    PreventOtherDrops: true
  Drops:
    - diamond 32 1
    - netherite_ingot 12 0.5
```

#### DamageModifiers
修改生物对不同伤害来源承受的伤害量。
例如，DamageModifiers 可用于使生物免疫近战攻击，但对远程攻击脆弱。
参见 [伤害修正](/Mobs/DamageModifiers) 了解更多信息。
```yml
example_mob:
  Type: zombie
  DamageModifiers:
    - ENTITY_ATTACK 0
    - PROJECTILE 1.25
```

#### Equipment
在生物首次生成时为其装备原版物品或 Mythic 物品。
参见 [装备](/Mobs/Equipment) 了解更多信息。
```yml
example_mob:
  Type: zombie
  Options:
    PreventRandomEquipment: true
  Equipment:
    - diamond_sword HAND
    - diamond_helmet{name=<green>COMMON</green> helmet} HEAD
```

#### KillMessages
自定义生物击杀玩家时显示的[击杀信息]。
```yml
example_mob:
  Type: zombie
  Display: Tanker
  KillMessages:
    - <caster.name> yeeted <target.name>!!
    - You're too weak <target.name>!!
```

#### LevelModifiers
MythicMobs 生物可以有[等级](/Mobs/Levels)，此字段用于决定它们在等级变化时应获得哪些统计增益。
```yml
example_mob:
  Type: zombie
  Display: Dummy
  LevelModifiers:
    Damage: 2
    Health: 0.25
```

#### Disguise
改变生物的外观，使其看起来像其他实体类型。
需要在服务器上安装并正常运行的插件 [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/)。
参见 [扩展：伪装](/Mobs/Disguises) 了解更多信息。
```yml
#此生物行为像僵尸，但看起来像鸡
example_mob:
  Type: zombie
  Disguise: chicken
```

#### Skills
技能是 Mythic 的核心功能。所有生物都可以拥有多种类型的技能，它们可以在不同情况下被不同类型的触发器激活，并附带不同的条件。Mythic 技能系统一旦上手就非常直观，可以用来创建从简单生物到极其复杂的 Boss 等各种内容。
参见 [技能](/Skills/Skills) 开始制作你自己的技能。
```yml
#与右键点击生物进行互动的玩家交换位置
example_mob:
  Type: zombie
  Skills:
    - swap @trigger ~onInteract
```

#### Nameplate
在生物上强制使用 Mythic 名牌，如果设置了 `Enabled: true` 选项。
这会使显示名称如 `Display: "Hello\nWorld!"` 分两行显示。
```yaml
ExampleMob:
  Type: PIG
  Display: "Hello\nWorld!"
  Nameplate:
    Enabled: true

    # 名牌的偏移量
    Offset: 1.8 
    
    # 名牌的缩放
    Scale: 1,1,1

    # 如果设置，强制名牌与 ModelEngine 插件的建模实体配合使用
    Mounted: true
```

#### Hearing
允许生物像监守者一样"听到"声音。
启用此功能将启用新的 [~onHear](/Skills/Triggers/onHear) 触发器。
```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="I can hear you <trigger.name>! <skill.var.volume>? Way too loud!"} @trigger ~onHear
```

#### Totem
允许你配置一个自定义结构，建造完成后将召唤一个生物。
```yaml
ExampleMob:
  Type: ZOMBIE
  Totem:

    # 放置后提示插件检查图腾的方块
    Head: player_head

    # 定义图腾外观的偏移向量和材料列表
    Pattern:
    - 1,2,0 player_head
    - 0,2,0 player_head
    - -1,2,0 player_head
    - 1,1,0 NETHERITE_BLOCK
    - -1,1,0 NETHERITE_BLOCK
    - 0,1,0 NETHERITE_BLOCK
    - 0,0,0 NETHERITE_BLOCK

    # 图案的可选替换方块列表。
    # 如果未设置替换，图案中的每个方块将被替换为 AIR
    Replacement:
    - 0,0,0 AIR
```

Head（头部方块）的值是实际的方块类型，放置在世界中后将提示插件检查图腾结构是否已建立。因此，建议不要使用常见的方块类型作为头部方块。

方块偏移使用 x,y,z 语法，从朝向 yaw=0 的视角配置，0,0,0 是图腾最底部（生物生成的位置）。

<img src="https://i.imgur.com/yOc8Hnm.gif" alt="Mob Totem" width="50%">

#### Variables
与其在 `~onSpawn` 中使用大量 `setvariable` 技能，你可以通过 Variables 生物字段让生物在生成时就带有已设置好的[变量](/Skills/Variables)。

```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```
> 以上示例将设置
> - 类型为 `STRING`、值为 `something` 的 `SomeVariable` 变量
> - 类型为 `INTEGER`、值为 `2` 的 `AnIntVariable` 变量
> - 类型为 `FLOAT`、值为 `420.69` 的 `AFloatVariable` 变量

可用前缀：
- `int/`
- `float/`
- `set/`
- `list/`
- `map/`

#### Trades
自定义村民的交易。
村民必须有职业且职业等级为 2 才能保留其自定义交易。

```yml
MerchantTest:
  Type: VILLAGER
  Display: '&6Merchant Test'
  Options:
    Profession: CLERIC
    Type: DESERT
    Level: 2
  Trades:
    1:
      Item1: 5 EMERALD
      Item2: 5 DIAMOND
      Result: DIAMOND_SWORD
    2:
      Item1: 64 EMERALD
      Result: mmoitems.SWORD.CUTLASS
      MaxUses: 1
    3:
      Item1: 32 EMERALD
      Item2: 1 PAPER
      Result: 1 CUSTOM_ITEM
      MaxUses: 1
```
> 如果未设置 `MaxUses`，将默认为 `10000`。


## 示例

更多生物示例可以在[示例](/examples/Common-Examples#mobs)章节中找到。

[entity types]: https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html
[setname]: /Skills/mechanics/setname
[placeholders]: /Skills/Placeholders
[targeter filtering]: /Skills/Targeters#targeter-options
[Custom AI]: /Mobs/Custom-AI
[Threat Tables]: /Mobs/ThreatTables
[Immunity Tables]: /Mobs/ImmunityTables
[AI goals]: /Mobs/Custom-AI#ai-goal-selectors
[AI targets]: /Mobs/Custom-AI#ai-target-selectors
[kill messages]: /Mobs/KillMessages
