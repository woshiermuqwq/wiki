MythicMobs 完全围绕自定义实体/生物构建，有大量的选项和属性可供你使用。下面列出了可以添加到自定义生物中的所有选项和属性。

下面的大部分选项都是可选的，也就是说你不需要每次创建新生物都把整份清单配置一遍。真正必须填的只有 `Internal_Name`（内部名称）和 `Type`（实体类型）。

## 生物配置拆解

#### 内部名称 (Internal_Name)
这个字符串是 MythicMobs 内部引用该生物时使用的名称，你可以随意命名。
必须是唯一的名称，不能与其他内部生物名称冲突，**不允许使用空格**。
```yml
example_name:
```

#### 类型 (Type)
这个字段决定你的生物基于哪种实体类型。
完整的可用[实体类型]列表可以在 Spigot Javadoc 上找到，而[这里](/Mobs/Types)列出了已明确适配的类型列表。
> Minecraft 为基础游戏新增的实体类型，在 MythicMobs 添加对应支持之前，部分生物选项无法正常生效。

> 有些实体类型可能存在难以发现的负面特性。建议你先查阅[不稳定实体类型](/Mobs/Mobs/Unstable-Entity-Types)页面，更好地判断当前需求应该使用哪种实体。
```yml
example_mob:
  Type: zombie
```
```yml
another_mob:
  Type: ZOMBIE
```

#### 显示名称 (Display)
设置生物的显示名称。
此选项支持颜色代码和[占位符]。
**生物的名称不会自行更改或更新，你必须使用 [setname] 技能来更改或更新它。**
```yml
example_mob:
  Type: zombie
  Display: 示例生物
```
```yml
example_mob:
  Type: zombie
  Display: 示例生物 <caster.hp> <red><&heart></red>
```

#### 生命值 (Health)
设置生物最大生命值属性的基础值。
MythicMobs 对最大生命值没有任何限制，但 Spigot 将最大生命值上限设为 `2048`。
这个限制可以在 Spigot 的配置文件 `server_root\spigot.yml` 中轻松修改。
如果生物手持或穿戴带有属性修正的物品，也会影响总生命值上限。
```yml
example_mob:
  Type: zombie
  Display: 示例生物
  Health: 30
```

#### 伤害 (Damage)
设置生物近战攻击伤害属性的基础值。
1 点伤害等于 0.5 颗心，所以伤害为 6 的生物会造成 3 颗心的伤害。
此属性永远不会影响远程攻击（如弓箭或药水）造成的伤害。
如果生物手持或穿戴带有属性修正的物品，也会影响生物的近战伤害。
```yml
example_mob:
  Type: zombie
  Display: 示例生物
  Damage: 20
```

#### 护甲 (Armor)
设置生物护甲属性的基础值。
Minecraft 将护甲值上限设为 30。
如果生物手持或穿戴带有属性修正的物品，也会影响总护甲值。
```yml
example_mob:
  Type: zombie
  Display: 坦克手
  Armor: 25
```

#### 血量条 (HealthBar)
在生物上方创建一个基础的血量全息条，在生物受到伤害后显示。
```yml
example_mob:
  Type: zombie
  Display: 健康小子
  Health: 1000
  HealthBar:
    Enabled: true
    Offset: 1.45
```

#### Boss 血条 (BossBar)
定义并控制生物的 Boss 血条。
外观类似末影龙或凋灵的 Boss 血条，但外观可自定义。
参见 [BossBar](/Mobs/BossBar)
```yml
example_mob:
  Type: zombie
  Armor: 25
  BossBar:
    Enabled: true
    Title: 坦克手
    Range: 20
    Color: RED
    Style: NOTCHED_6
    CreateFog: true
    DarkenSky: true
    PlayMusic: true
```

#### 阵营 (Faction)
设置生物的阵营，可用于高级[自定义 AI]配置或[目标选择器过滤]。
阵营名称区分大小写，使用阵营条件时请注意。
```yml
example_mob:
  Type: zombie
  Armor: 25
  Faction: Tank
```

#### 坐骑 (Mount)
设置生物的坐骑。
必须是另一个 MythicMob 生物。
生物生成时会自动骑乘到所定义的坐骑上。
```yml
another_example:
  Type: chicken
  Mount: example_mob
```

#### 显示实体选项 (Display Options)
设置显示实体的选项。
可用选项列表见 [显示选项](/Mobs/DisplayOptions) 页面。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```

#### 选项 (Options)
这是一个特殊字段，包含大量子选项，比如决定生物是否消失、击退抗性、跟随距离、移动速度等等。
可用选项列表见 [生物选项](/Mobs/Options) 页面。
```yml
slow_persistent_mob:
  Type: husk
  Options:
    MovementSpeed: 0.025
    Despawn: PERSISTENT
```

#### 模块 (Modules)
此字段允许你启用或禁用模块，如[仇恨表]和/或[免疫表]。
```yml
example_mob:
  Type: husk
  Modules:
    ThreatTable: false
    ImmunityTable: false
```

#### AI 目标选择器 (AIGoalSelectors)
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

#### AI 攻击目标选择器 (AITargetSelectors)
修改和自定义生物的 [AI 攻击目标]。
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

#### 掉落 (Drops)
添加或完全修改生物的战利品掉落。
可以是原版物品、MythicMobs 物品、经验值、跨插件物品（如果支持），甚至是带有自定义条件系统的掉落表。
更多信息见 [掉落与掉落表](/drops/Drops)。
```yml
example_mob:
  Type: zombie
  Options:
    PreventOtherDrops: true
  Drops:
    - diamond 32 1
    - netherite_ingot 12 0.5
```

#### 伤害修正 (DamageModifiers)
修改生物从不同伤害来源受到的伤害量。
例如，可以用伤害修正让免疫近战攻击，但弱于远程攻击。
更多信息见 [伤害修正](/Mobs/DamageModifiers)。
```yml
example_mob:
  Type: zombie
  DamageModifiers:
    - ENTITY_ATTACK 0
    - PROJECTILE 1.25
```

#### 装备 (Equipment)
在生物首次生成时为其装备原版物品或 MythicMobs 物品。
更多信息见 [装备](/Mobs/Equipment)。
```yml
example_mob:
  Type: zombie
  Options:
    PreventRandomEquipment: true
  Equipment:
    - diamond_sword HAND
    - diamond_helmet{name=<green>普通</green>头盔} HEAD
```

#### 击杀信息 (KillMessages)
自定义生物击杀玩家时显示的[击杀信息]。
```yml
example_mob:
  Type: zombie
  Display: 坦克手
  KillMessages:
    - <caster.name> 把 <target.name> 打飞了！！
    - 你太弱了 <target.name>！！
```

#### 等级修正 (LevelModifiers)
MythicMobs 生物可以有[等级](/Mobs/Levels)，此字段用于决定它们等级变化时应该获得哪些属性的提升。
```yml
example_mob:
  Type: zombie
  Display: 傀儡
  LevelModifiers:
    Damage: 2
    Health: 0.25
```

#### 伪装 (Disguise)
改变生物的外观，使其看起来像其他实体类型。
需要在服务器上安装并正常运行的 [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/) 插件。
更多信息见 [扩展：伪装](/Mobs/Disguises)。
```yml
# 这个生物行为像僵尸，但看起来像鸡
example_mob:
  Type: zombie
  Disguise: chicken
```

#### 技能 (Skills)
技能是 MythicMobs 的核心功能。所有生物都可以拥有各种类型的技能，这些技能可以在不同的时机触发，并附带不同的条件。熟悉之后，MythicMobs 的技能系统非常直观，可以用来创建从简单生物到极其复杂的 BOSS 等各种内容。
要开始制作自己的技能，请查看[技能系统](/Skills/Skills)。
```yml
# 与右键点击该生物的玩家交换位置
example_mob:
  Type: zombie
  Skills:
    - swap @trigger ~onInteract
```

#### 名牌 (Nameplate)
如果使用 `Enabled: true` 选项，将强制在生物上使用 MythicMobs 名牌。
这使得像 `Display: "你好\n世界！"` 这样的显示名称能分行显示在两行上。
```yaml
ExampleMob:
  Type: PIG
  Display: "你好\n世界！"
  Nameplate:
    Enabled: true

    # 名牌的偏移量
    Offset: 1.8 
    
    # 名牌的缩放
    Scale: 1,1,1

    # 如果设置，强制名牌配合 ModelEngine 插件的模型实体使用
    Mounted: true
```

#### 听觉 (Hearing)
允许生物像监守者一样"听到"声音。
开启此选项将启用 [~onHear](/Skills/Triggers/onHear) 触发器。
```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="我能听到你 <trigger.name>！<skill.var.volume>？太吵了！"} @trigger ~onHear
```

#### 图腾 (Totem)
允许你配置一个自定义结构，一旦被搭建完成，就会召唤一只生物。
```yaml
ExampleMob:
  Type: ZOMBIE
  Totem:

    # 放置后触发插件检测图腾结构的方块类型
    Head: player_head

    # 一组偏移向量和材质，定义图腾的外观
    Pattern:
    - 1,2,0 player_head
    - 0,2,0 player_head
    - -1,2,0 player_head
    - 1,1,0 NETHERITE_BLOCK
    - -1,1,0 NETHERITE_BLOCK
    - 0,1,0 NETHERITE_BLOCK
    - 0,0,0 NETHERITE_BLOCK

    # 可选：替换方案中的方块列表
    # 如果未设置替换方案，图案中的每个方块都会被替换为空气
    Replacement:
    - 0,0,0 AIR
```

`Head` 的值是实际方块类型，一旦在世界中放置该方块，插件就会检查图腾结构是否已搭建完成。因此，建议不要使用过于常见的方块类型。

方块偏移使用 x,y,z 语法，配置视角为 yaw=0，0,0,0 是图腾的最底部，也是生物生成的位置。

<img src="https://i.imgur.com/yOc8Hnm.gif" alt="生物图腾" width="50%">

#### 变量 (Variables)
与其在 `~onSpawn` 中使用大量 `setvariable` 技能，你可以通过 Variables 生物字段让生物在生成时就携带已设置好的[变量](/Skills/Variables)。

```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```
> 上面的示例会设置：
> - 名为 `SomeVariable`，类型为 `STRING`，值为 `something` 的变量
> - 名为 `AnIntVariable`，类型为 `INTEGER`，值为 `2` 的变量
> - 名为 `AFloatVariable`，类型为 `FLOAT`，值为 `420.69` 的变量

可用的前缀：
- `int/`
- `float/`
- `set/`
- `list/`
- `map/`

#### 交易 (Trades)
自定义村民的交易内容。
村民必须拥有职业且职业等级达到 2，才能保留其自定义交易。

```yml
MerchantTest:
  Type: VILLAGER
  Display: '&6交易测试'
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
> 如果未设置 `MaxUses`，默认值为 `10000`。

## 示例

更多生物示例可以在[示例](/examples/Common-Examples#mobs)部分找到。

[实体类型]: https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html
[setname]: /Skills/mechanics/setname
[占位符]: /Skills/Placeholders
[目标选择器过滤]: /Skills/Targeters#targeter-options
[自定义 AI]: /Mobs/Custom-AI
[仇恨表]: /Mobs/ThreatTables
[免疫表]: /Mobs/ImmunityTables
[AI 目标]: /Mobs/Custom-AI#ai-goal-selectors
[AI 攻击目标]: /Mobs/Custom-AI#ai-target-selectors
[击杀信息]: /Mobs/KillMessages
