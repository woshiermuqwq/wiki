触发器用于决定技能在生物配置的技能部分内如何被触发。

<u>**触发器不能在元技能中使用，也不应该写在元技能中。**</u>  

触发器只能用于*激活*元技能本身（在生物的配置文件中使用）。

> 每个触发器均以 `on` 开头。该字符串**区分大小写**，因此请务必写对，否则触发器不会生效。

## 使用触发器
触发器定义在生物配置的 Skills 部分，前面必须加一个波浪号（~）。对于定时触发器（Timer），还需要指定以游戏刻为单位的时间间隔。
```yml
SkeletalWizard_Fire:
  Type: WITHER_SKELETON
  Display: '&Skeletal Fire Wizard'
  Health: 50
  Damage: 0.5
  Skills:
  - ignite{ticks=100} @target ~onAttack
  - skill{s=FireShield} @trigger ~onDamaged 0.1
  - skill{s=AOEFire} ~onTimer:300
```

在这个例子中，生物在近战攻击时会点燃它的目标，受到伤害时有 10% 概率使用 "FireShield" 技能，并且每 300 游戏刻（即每 15 秒）会施放 "AOEFire" 技能。

## 不使用触发器的情况……
技能触发器在精确定义技能何时触发方面提供了极大的灵活性。**强烈**建议使用高级触发器来触发所有技能，而不是使用旧的、传统的方法。

如果一条技能没有触发器，它将默认使用 `~onCombat` 触发器，该触发器会在以下事件发生时执行：
- 生物造成或受到伤害时
- 生物生成时
- 生物死亡时

```yml
SkeletalWarrior:
  Mobtype: skeleton
  Display: '<blue>A Skeletal Warrior</blue>'
  Skills:
  - skill{s=Bash} =10%-90%
```
在这个例子中，当生物的生命值在 10% 到 90% 之间，且造成或受到伤害时，Bash 技能会被触发。


# @trigger 目标选择器

你可能已经注意到上面示例中出现了 [`@trigger`](/Skills/Targeters/Trigger) 目标选择器，它也在[目标选择器](/Skills/Targeters)部分中列出。`@trigger` 会以「导致」技能触发的那个实体为目标，例如当玩家伤害了某个生物，而该生物有一个 `~onDamaged` 技能时，它会以该玩家为目标。如果某个生物收到了信号，它会以发送信号的生物为目标，依此类推。


# 扩展触发器
以下是扩展插件添加的触发器链接。如果没有安装对应的插件，这些触发器不会生效。

- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Triggers)


# 触发器列表
**所有可用触发器的表格：**
| 触发器                                   | 触发时机…                                                     |
|-----------------------------------------|--------------------------------------------------------------|
| [onCombat](/Skills/Triggers/onCombat)   | 默认                                                          |
| [onAttack](/Skills/Triggers/onattack)    | 当生物击中某物时                                               |
| [onDamaged](/Skills/Triggers/ondamaged)  | 当生物受到伤害时                                               |
| [onSpawn](/Skills/Triggers/onspawn)      | 当生物生成时                                                   |
| [onDespawn](/Skills/Triggers/ondespawn)  | 当生物被移除时                                                 |
| [onReady](/Skills/Triggers/onready)      | 当生物首次从生成器中生成时                                       |
| [onLoad](/Skills/Triggers/onload)        | 当生物在服务器重启后被加载时                                     |
| [onSpawnOrLoad](/Skills/Triggers/onspawnorload) | 当生物[生成](/Skills/Triggers/onspawn)或[加载](/Skills/Triggers/onload)时 |
| [onDeath](/Skills/Triggers/ondeath)      | 当生物死亡时                                                   |
| [onTimer](/Skills/Triggers/onTimer)      | 每 # 游戏刻（其中 # 为以游戏刻为单位的时间间隔）                  |
| [onInteract](/Skills/Triggers/oninteract) | 当生物被右键点击时                                             |
| [onPlayerKill](/Skills/Triggers/onplayerkill) | 当生物杀死一名玩家时                                       |
| [onEnterCombat](/Skills/Triggers/onentercombat) | 当生物进入战斗时（需要开启仇恨表）                          |
| [onDropCombat](/Skills/Triggers/ondropcombat) | 当生物脱离战斗时（需要开启仇恨表）                            |
| [onChangeTarget](/Skills/Triggers/onchangetarget) | 当生物切换目标时（需要开启仇恨表）                        |
| [onExplode](/Skills/Triggers/onexplode) | 当生物爆炸时（通常仅用于爬行者）                                  |
| [onPrime](/Skills/Triggers/onprime)      | 当爬行者蓄力准备爆炸时                                          |
| [onCreeperCharge](/Skills/Triggers/oncreepercharge) | 当爬行者被充能时（闪电击中爬行者时）                    |
| [onTeleport](/Skills/Triggers/onteleport) | 当生物传送时（通常仅用于末影人）                                 |
| [onSignal](/Skills/Triggers/onsignal)    | 当生物收到信号时                                               |
| [onShoot](/Skills/Triggers/onshoot)      | 当生物发射弹射物时                                             |
| [onBowHit](/Skills/Triggers/onbowhit)    | 当生物发射的弹射物击中实体时                                     |
| [onTame](/Skills/Triggers/ontame)        | 当生物被驯服时                                                 |
| [onBreed](/Skills/Triggers/onbreed)      | 当生物与另一生物繁殖时                                          |
| [onTrade](/Skills/Triggers/ontrade)      | 当村民完成一次交易时。需要 Paper 端                              |
| [onChangeWorld](/Skills/Triggers/onchangeworld) | 当生物切换世界时                                         |
| [onBucket](/Skills/Triggers/onbucket)    | 当牛被挤奶或实体被桶装时（美西螈等）                              |
| [onSkillDamage](/Skills/Triggers/onskilldamage) | 当生物通过技能对其他实体造成伤害时                           |
| [onHear](/Skills/Triggers/onhear)        | 当生物听到声音时，[前提是已启用](/Mobs/Mobs#hearing)             |
| [onProjectileHit](/Skills/Triggers/onProjectileHit) | 当生物的特殊弹射物击中实体时                         |
| [onProjectileLand](/Skills/Triggers/onProjectileLand) | 当生物的特殊弹射物击中方块时                         |

<!-- LINKS -->
[ThreatTables]: /Mobs/ThreatTables
[@trigger]: /Skills/Targeters/Trigger
[@origin]: /Skills/Targeters/Origin
[已实现的占位符]: /Skills/Placeholders#variable-placeholders