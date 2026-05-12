## 敌对生物

### 恶魔（Demon）
恶魔对玩家、攻击它的实体以及任何属于"good"阵营的 MythicMob 持敌对态度。它装备着一把下界合金斧，带有火焰粒子效果，并且可以悬空和发射火球（因为它使用烈焰人作为基础生物！）。它使用需要 [Disguises](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Disguises) 的自定义皮肤。

难度：`⭐⭐⭐`（中级）
<details>
  <summary>逐步教程</summary>
  
### 教程
让我们为生物添加一些基础选项：
```yml
Demon:
  Type: blaze # 生物类型
  Display: 'Demon' # 生物显示名称
  Damage: 6 # 造成的伤害量
  Health: 60 # 拥有的生命值
  Faction: bad # 将恶魔的阵营设为"bad"。
  Disguise: Player 164_ setCustomName Demon setCustomNameVisible false # 将其伪装为带有皮肤的玩家。需要 LibsDisguises。
```

然后，给它一些自定义 AI，防止它攻击不需要的实体：

```yml
  # ...
  AIGoalSelectors:  # 我们不清除生物的基础 AI，而是在其基础上追加
  - meleeattack # 使用近战攻击
  - randomstroll # 随机走动
  - float # 在水上浮游
  AITargetSelectors:
  - clear # 清除生物的基础 AI
  - players # 首先以玩家为目标
  - attacker # 以攻击它的实体为目标
  - specificfaction good # 以"good"阵营的生物为目标
```

给生物一把斧头：

```yml
  # ...
  Equipment:
  - NETHERITE_AXE HAND # 让生物手持一把下界合金斧
```

现在，我们进一步自定义一下生物：

1. 不要让生物总是显示名称。
2. 阻止生物死亡时掉落原版烈焰人掉落物。
3. 阻止被恶魔杀死的生物掉落它们的战利品。
4. 将生物的移动速度设置为 `0.35`。
5. 给生物添加音效。
   
最终结果是：

```yml
  # ...
  Options:
    AlwaysShowName: false # 除非悬停，否则不总是显示名称
    PreventOtherDrops: true # 死亡时不掉落默认的烈焰人掉落物
    PreventMobKillDrops: true # 阻止被恶魔杀死的生物掉落战利品
    MovementSpeed: 0.35 # 设置移动速度
    Silent: false # 播放默认的烈焰人音效
```

最后，让我们添加一些能力让生物更有趣。

```yml
  # ...
  Skills:
  # 粒子效果
  - effect:flames @self ~onTimer:100 # 每 100 ticks（5 秒），在生物位置显示生成器火焰效果。
  # 音效
  - effect:sound{s=entity.elder_guardian.ambient;v=1;p=2} @self 0.5 ~onTimer:150 # 每 150 ticks（7.5 秒），50% 概率以音量 1、音高 2 播放 entity.elder_guardian.ambient 音效
  - effect:sound{s=entity.elder_guardian.hurt;v=1;p=0.7} @self ~onDamaged # 当生物受伤时，以音量 1、音高 0.7 播放 entity.elder_guardian.hurt 音效
  - effect:sound{s=entity.elder_guardian.death;v=1;p=0.7} @self ~onDeath # 当生物死亡时，以音量 1、音高 0.7 播放 entity.elder_guardian.death 音效
  - effect:sound{s=entity.blaze.death;v=0.3;p=0.7} @self ~onDeath # 当生物死亡时，同时以音量 0.3、音高 0.7 播放 entity.blaze.death 音效
```

这些技能本质上是为生物添加自定义音效和效果，让它真正变得生动起来。
</details>

<details>
  <summary>最终成品</summary>

```yml
Demon:
  Type: blaze # 生物类型
  Display: 'Demon' # 生物显示名称
  Damage: 6 # 造成的伤害量
  Health: 60 # 拥有的生命值
  Faction: bad # 将恶魔的阵营设为"bad"。
  Disguise: Player 164_ setCustomName Demon setCustomNameVisible false # 将其伪装为带有皮肤的玩家。需要 LibsDisguises。
  AIGoalSelectors:  # 我们不清除生物的基础 AI，而是在其基础上追加
  - meleeattack # 使用近战攻击
  - randomstroll # 随机走动
  - float # 随机浮游
  AITargetSelectors:
  - clear # 清除生物的基础 AI
  - players # 首先以玩家为目标
  - attacker # 以攻击它的实体为目标
  - specificfaction good # 以"good"阵营的生物为目标
  Equipment:
  - NETHERITE_AXE HAND # 让生物手持一把下界合金斧
  Options:
    AlwaysShowName: false
    PreventOtherDrops: true
    PreventMobKillDrops: true
    MovementSpeed: 0.35
    Silent: false
  Skills:
  # 粒子效果
  - effect:flames @self ~onTimer:100 # 每 100 ticks（5 秒），在生物位置显示生成器火焰效果。
  # 音效
  - effect:sound{s=entity.elder_guardian.ambient;v=1;p=2} @self 0.5 ~onTimer:150 # 每 150 ticks（7.5 秒），50% 概率以音量 1、音高 2 播放 entity.elder_guardian.ambient 音效
  - effect:sound{s=entity.elder_guardian.hurt;v=1;p=0.7} @self ~onDamaged # 当生物受伤时，以音量 1、音高 0.7 播放 entity.elder_guardian.hurt 音效
  - effect:sound{s=entity.elder_guardian.death;v=1;p=0.7} @self ~onDeath # 当生物死亡时，以音量 1、音高 0.7 播放 entity.elder_guardian.death 音效
  - effect:sound{s=entity.blaze.death;v=0.3;p=0.7} @self ~onDeath # 当生物死亡时，同时以音量 0.3、音高 0.7 播放 entity.blaze.death 音效
```
</details>

---

### 哨兵（The Sentinel）

一只快速且危险的小 Boss，发出恐怖的声音，带有粒子效果，头上戴着一个命令方块，手持一把下界合金剑来击败挡路的一切。

```yaml
Sentinel:
  Type: wither_skeleton # 基础生物为凋零骷髅。请注意，这意味着当该生物攻击其他实体时，它们将受到凋零效果。
  Display: 'Sentinel' # 生物名称。
  Damage: 10 # 命中造成 10 点伤害
  Health: 120 # 拥有 120 生命值。
  Faction: bad # 将生物设置为"bad"阵营
  AIGoalSelectors: # 生物要做什么？
  - clear # 清除生物 AI
  - meleeattack # 近战攻击目标
  - lookatplayers # 注视玩家。
  - randomstroll # 脱战时随机走动。
  AITargetSelectors:
  - clear # 清除生物 AI
  - players # 以玩家为目标
  - attacker # 然后以攻击它的实体为目标
  - otherfaction # 以不在"bad"阵营的实体为目标
  Options: # 额外生物选项
    PreventSunburn: true # 防止生物在白天燃烧
    AlwaysShowName: false # 防止生物总是显示名称。（玩家需要注视生物才能显示名称）
    PreventOtherDrops: true # 阻止原版凋零骷髅掉落物。
    PreventMobKillDrops: true # 阻止被哨兵杀死的生物掉落战利品。
    MovementSpeed: 0.45 # 快速移动速度。
    Silent: true # 禁用默认音效。使用自定义音效时很有用。
  Equipment: # 生物穿戴的物品。
  - COMMAND_BLOCK HEAD # 头上戴一个命令方块。
  - NETHERITE_SWORD HAND # 手持一把下界合金剑
  Skills:
  # 音效
  - effect:sound{s=entity.enderman.scream;v=1;p=0.2} @self ~onDeath
  - effect:sound{s=entity.enderman.hurt;v=1;p=0.2} @self ~onDamaged
  - effect:sound{s=entity.enderman.stare;v=.2;p=0.2} @self ~onTimer:150 0.5
  # 粒子
  - effect:particles{particle=spell;amount=50;hS=1;vS=1;speed=5} @self ~onTimer:2 0.8
  # 能力
  - throw{velocity=8;velocityY=4} @EIR{r=4} ~onDamaged 0.2 # 受伤时，生物有 20% 概率将半径 4 范围内的附近玩家抛起。
```

## 中立生物

### 冒险家（The Adventurer）

一只保护陆地的简单生物，用铁剑攻击敌对生物，随机说话，防御攻击者，庆祝他的胜利。使用需要 [Disguises](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Disguises) 的自定义皮肤。

```yaml
Adventurer:
  Type: zombie
  Display: 'Adventurer'
  Damage: 6
  Health: 65
  Faction: good
  Disguise: Player Refreshin setCustomName Adventurer setCustomNameVisible true
  AIGoalSelectors:
  - clear
  - meleeattack
  - lookatplayers
  - randomstroll
  - float
  AITargetSelectors:
  - clear
  - attacker
  - otherfactionmonsters
  Equipment:
  - IRON_SWORD HAND
  Options:
    PreventSunburn: true
    AlwaysShowName: false
    PreventOtherDrops: true
    PreventMobKillDrops: true
    MovementSpeed: 0.26
    Silent: true
  Skills:
  - effect:sound{s=entity.villager.ambient;v=.6;p=0.7} @self ~onTimer:60 0.6
  - effect:sound{s=entity.villager.yes;v=.6;p=0.7} @self ~onKill
  - effect:sound{s=entity.villager.hurt;v=.6;p=0.7} @self ~onDamaged
  Drops:
  - IRON_SWORD 1
```

## 被动生物

### 市民（The Civilian）

市民是温顺的 NPC 生物，不爱战斗。他们会逃离战斗，并在玩家右键点击时与之交谈。他们也会像普通村民一样获取职业。使用需要 [Disguises](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Disguises) 的自定义皮肤。还使用了需要 [MythicMobs Premium](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Premium-Features) 的 AIGoalSelectors。

```yaml
Citizen:
  Type: VILLAGER
  Display: 'Civilian'
  Damage: 6
  Health: 20
  Faction: good
  Disguise: Player Refreshin setCustomName Civilian setCustomNameVisible true
  AIGoalSelectors:
  - fleeConditional{distance=15;speed=1;safespeed=1;conditions=[ - incombat true ]}
  AITargetSelectors:
  - clear
  - attacker
  Options:
    PreventItemPickup: false
    AlwaysShowName: false
    Despawn: true
    PreventOtherDrops: true
    PreventMobKillDrops: true
    MovementSpeed: 0.35
    Silent: true
  Skills:
  - effect:sound{s=entity.villager.yes;v=.6;p=0.8} @self ~onInteract
  - effect:sound{s=entity.villager.hurt;v=.6;p=0.8} @self ~onDamaged
  - effect:sound{s=entity.villager.death;v=.6;p=0.8} @self ~onDeath
  Drops:
  - BREAD 1-3 0.4
  - CARROT 1-3 0.4
  - BEETROOT 1-3 0.4
  - POTATO 1-3 0.4
  - EMERALD 1-2 0.1
  - GOLD_NUGGET 1-6 0.2
  - DIAMOND 1 0.01
```
