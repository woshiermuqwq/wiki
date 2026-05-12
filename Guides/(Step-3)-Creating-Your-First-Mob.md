现在你已经了解了所有基础知识、如何使用它们以及在哪里使用，我们将创建自己的第一只生物！

我们将制作一只简单的生物——骷髅王，带几个基础技能和物品。

# 生物文件
`/plugins/MythicMobs/Mobs/SkeletonKing.yml`

基础生物，这里我们为生物设置了内部 ID、类型、显示名、生命值和伤害。

此生物的内部 ID 为 `SkeletonKing`，必须对每只生物唯一，不能与其他生物相同。我们将使用它来生成生物：`/mm m spawn SkeletonKing`
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
```

接下来，我们为生物添加一些选项。
- `AlwaysShowName: true` 使生物的 Display 名称显示在头顶上方
- `MovementSpeed: 0.2` 改变生物的行走速度
- `MaxCombatDistance: 25` 改变玩家可与生物战斗的距离（方块数）
- `PreventOtherDrops: true` 阻止生物类型掉落其原版掉落物
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
```

现在添加一些装备（Equipment），让我们自定义生物的外观和使用什么武器。这里使用的物品包括一双原版靴子和两个 Mythic 物品，后者我们将在下方物品文件中创建。
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
  Equipment:
  - KingsCrown HEAD
  - IRON_BOOTS FEET
  - SkeletonKingSword HAND
```

由于我们移除了生物的原版掉落物，我们将添加自己的掉落。我们将使用一个掉落表（DropTable）来处理，会在下面创建。
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
  Equipment:
  - KingsCrown HEAD
  - IRON_BOOTS FEET
  - SkeletonKingSword HAND
  Drops:
  - SkeletonKingDrops
```

最后，我们为生物添加一些技能，赋予它有趣的能力！

我们添加了 2 个技能和 2 个元技能到生物上，元技能将在下面的技能文件中创建。前往[技能](/Skills/Mechanics)、[目标选择器](/Skills/Targeters)和[触发器](/Skills/Triggers)页面了解各技能的作用！
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
  Equipment:
  - KingsCrown HEAD
  - IRON_BOOTS FEET
  - SkeletonKingSword HAND
  Drops:
  - SkeletonKingDrops
  Skills:
  - speak{m="没有人能挑战骷髅王！";cooldown=20} @PlayersInRadius{r=40} ~onCombat 0.2
  - speak{m="哈哈哈！去死吧，<trigger.name>！"} @PlayersInRadius{r=40} ~onPlayerKill
  - skill{s=SummonSkeletons} @self 0.1
  - skill{s=SmashAttack} @target 0.2
```
在某些技能后面加上 0.2 和 0.1 是给它们一个执行概率，意味着它们不会 100% 触发。概率基于 1，所以 0.2 是 20% 的概率。

# 技能文件
`/plugins/MythicMobs/Skills/SkeletonKing.yml`

技能文件将包含我们在生物文件中使用的元技能 `SummonSkeletons` 和 `SmashAttack`。

### SummonSkeletons
我们的技能内部 ID 为 `SummonSkeletons`，这是调用技能时使用的名称。我们给它设了 15 秒的冷却，意味着技能一旦执行，在该时长内不会再次触发。

技能：
- [message](/mechanics/message) 向生物周围 40 半径内的所有玩家发送消息，通知骷髅正在生成。我们使用 caster.name 占位符来获取生物的 Display 设置，以及 &co 占位符来插入冒号（直接使用冒号会干扰语法）。
- [delay 20](/mechanics/delay) 在消息和下一条技能之间添加 20 ticks（1 秒）的延迟
- [summon](/mechanics/summon) 生成 2 只基础骷髅，随机放置在骷髅王周围 5 个方块内。summon 技能支持原版生物（如我们所用）或其他 MythicMobs（使用它们的内部 ID）。
我们重复了 delay 和 summon 技能，将在 3 秒内总共生成 6 只骷髅。

```yaml
SummonSkeletons:
  Cooldown: 15
  Skills:
  - message{m="<caster.name><&co> 醒来吧，我的仆从们！"} @PlayersInRadius{r=40}
  - delay 20
  - summon{mob=SKELETON;amount=2;radius=5} @Self
  - delay 20
  - summon{mob=SKELETON;amount=2;radius=5} @Self
  - delay 20
  - summon{mob=SKELETON;amount=2;radius=5} @Self
```

### SmashAttack
这个技能会让生物传送到目标身边，对目标造成伤害并将其抛向空中。

我们使用条件确保目标在一定距离内，如果目标太远，技能不会执行。
- [TargetWithin{d=25}]() 确保目标在生物 25 个方块范围内

技能：
- [message](/mechanics/message) 向 40 方块半径内的所有玩家显示攻击警告
- [teleport](/mechanics/teleport) 将生物直接传送到目标玩家位置
- [sound](/mechanics/Sound) 在生物位置播放末影人传送音效
- [delay](/mechanics/delay) 延迟技能 10 ticks
- [damage](/mechanics/damage) 对生物周围 5 方块内的所有玩家直接造成 5 点伤害，忽略护甲
- [throw](/mechanics/throw) 用水平和垂直速度向量将玩家抛起
- [fakeexplosion](/mechanics/FakeExplosion) 产生一个不造成伤害、不破坏方块的爆炸效果
```yaml
SmashAttack:
  Cooldown: 8
  Conditions:
  - targetwithin{d=25}
  Skills:
  - message{cooldown=30;m="<mob.name><&co> 哈哈哈！我要碾碎你，蠢货！"} @PlayersInRadius{r=40}
  - teleport @target
  - sound{s=mob.endermen.portal;volume=1.0;pitch=0.5}
  - delay 10
  - damage{amount=5;ignorearmor=true} @PlayersInRadius{r=5}
  - throw{velocity=10;velocityY=5} @PlayersInRadius{r=5}
  - fakeexplosion @Self
```
# 物品文件
`/plugins/MythicMobs/Items/SkeletonKing.yml`

现在来创建生物所需的盔甲和武器物品。

首先创建我们的剑。我们给它 Display 和 Lore，在背包中悬停物品时显示，并给它附魔。DAMAGE_ALL 附魔对应锋利。我们为剑添加属性，让持有者获得 +10 生命值和 10% 额外移动速度。

```yaml
SkeletonKingSword:
  Id: DIAMOND_SWORD
  Display: '&3骷髅王的巨剑'
  Lore:
  - '&6一把由骷髅王使用的'
  - '&6强大之剑。'
  Enchantments:
  - DAMAGE_ALL:5
  - KNOCKBACK:2
  - FIRE_ASPECT:2
  Attributes:
    MainHand:
      Health: 10
      MovementSpeed: 0.1
```

现在创建王冠，与上面的剑类似，我们为它设置 Display、Lore、Enchantments 和 Attributes。我们还添加了 2 个 Hide 标志来隐藏物品描述中的属性和附魔。

```yaml
KingsCrown:
  Id: GOLDEN_HELMET
  Display: '&d国王之冠'
  Lore:
  - '&6一顶王者之冠，赋予'
  - '&6佩戴者坚定不移的力量！'
  Enchantments:
  - PROTECTION_ENVIRONMENTAL:2
  - PROTECTION_PROJECTILE:2
  - PROTECTION_FIRE:2
  - PROTECTION_EXPLOSIONS:2
  Hide:
  - ATTRIBUTES
  - ENCHANTS
  Attributes:
    Head:
      Health: 10
      KnockbackResistance: 10
```

# 掉落文件
`/plugins/MythicMobs/DropTables/SkeletonKing.yml`

对于掉落，我们创建 2 个掉落表，并让第一个掉落表嵌套掉落第二个。我们使用条件来确保第二个掉落表的物品仅在夜间死亡时掉落。

掉落格式为 `<掉落类型> <数量> <概率>`，因此在第一个掉落表中，我们 100% 掉落 1 个 SkeletonKingItemDrops 掉落表，并以 100% 的概率掉落 100-150 之间随机数量的经验。在 SkeletonKingItemDrops 中，王冠有 1% 的掉落概率，剑有 10% 的掉落概率。

我们使用 MinItems 和 MaxItems 来指示掉落表总共要掉落多少项物品，它将从列表中丢弃 1 或 2 项。这不是单个物品的总数量，因为金粒和钻石有数量范围，可能掉落 64 个金粒和 12 个钻石，但仍然只算 MaxItems 中的 2 项。

```yaml
SkeletonKingDrops:
  Drops:
  - SkeletonKingItemDrops 1 1
  - experience 100-150 1
  
SkeletonKingItemDrops:
  Conditions:
  - night
  MinItems: 1
  MaxItems: 2
  Drops:
  - KingsCrown 1 0.01
  - SkeletonKingSword 0.1
  - GOLD_NUGGET 32-64 1
  - DIAMOND 1-12 0.8
```

# 测试
现在你已经创建了自定义生物所需的所有文件！接下来进入游戏，使用 `/mm reload` 将生物及其物品加载到服务器中，然后用 `/mm m spawn SkeletonKing` 生成并检查是否正常工作！

# 随机生成文件
`/plugins/MythicMobs/RandomSpawns/SkeletonKing.yml`

既然有了生物，你可能想让它在世界中随机生成。我们可以设置一个简单的 RandomSpawns 文件来实现！

RandomSpawns 使用起来相当容易，你可以在其 Wiki 页面找到创建方法。

在本指南中，我们将制作一个基础的随机生成，让骷髅王在夜间室外生成。我们使用 REPLACE 操作，用自定义生物替换原版生物生成，并添加条件使其仅替换骷髅。

我们使用 `0.005` 的概率，这意味着每次有骷髅生成时，有 0.5% 的概率会被替换为我们的骷髅王。

请务必将 `world` 替换为你希望生物生成的世界名称（或用逗号分隔的世界列表）。

```yaml
RandomSkeletonKing:
  Type: SkeletonKing
  Worlds: world
  Chance: 0.005
  Priority: 1
  Action: REPLACE
  Conditions:
  - outside true
  - night true
  - entitytype{t=SKELETON}
```

**[>> 第四步](/Guides/(Step-4)-Essential-Commands)**
