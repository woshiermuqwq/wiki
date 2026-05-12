## 描述
光环（Aura）机制充当目标实体上的状态效果，可以在其持续时间内触发其他技能。光环允许你创建自定义状态效果（如增益和减益），它们会被跟踪其持续时间，也可以在其他机制和条件中使用。

[[_TOC_]]

| [已实现的占位符]         |
|------------------------------------|
| `<skill.var.aura-name>`            |
| `<skill.var.aura-type>`            |
| `<skill.var.aura-charges>`         |
| `<skill.var.aura-duration>`        |
| `<skill.var.aura-duration-millis>` |
| `<skill.var.aura-stacks>`          |

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraName  | aura, b, buff, buffname, debuff, debuffname, n, name | 可选名称，使用引用特定光环的关联机制和条件时需要。如果未定义则分配随机 UUID                            |         |
| auratype  | auragroup, group, type, g | 光环的类型，类似于其名称       |         |
| attachmenttype | attachment, attach | 要应用到光环所施加实体上的[附着](#attachment-types)                             | NONE    |
| onStartSkill | onStart, os | 元技能，在光环首次启动时执行                  |<!--type:Metaskill-->|
| onTickSkill  | onTick, ot  | 元技能，每隔 [interval] 刻在受影响实体上执行|<!--type:Metaskill-->|
| onEndSkill   | onEnd, oe   | 元技能，在光环结束时执行                          |<!--type:Metaskill-->|
| ShowBarTimer | bartimer, bt| 如果设置，光环将在持续期间为施法者显示 BOSS 条        | false   |
| Charges   | c         | 如果设置，光环在充能耗尽时消失。可由其他机制修改                                                                                     | 0       |
| Duration  | ticks, t, d, time, t | 光环持续的最大时长（刻）        | 200     |
| Interval  | i         | 光环触发其 onTick 技能的频率（刻）                 | 1       |
| maxStacks | ms        | 如果多次应用，同一目标实体上光环的堆叠次数                                                                                          | 1       |
| refreshDuration | rd  | 当同一实体再次被施加相同光环时，使光环的持续时间刷新到机制中定义的值                                              | true    |
| mergeSameCaster | msc, mc | 将一个实体对另一实体施加的所有同名光环合并为一个光环（防止同一生物在同一实体上多次堆叠光环）            | 如果 `mergeAll`、`overwriteAll` 或 `overwriteSameCaster` 中任一为 `true` 则为 `false` |
| mergeAll        | ma  | 将所有实体对另一实体施加的所有同名光环合并为一个光环（防止多个生物在同一实体上多次堆叠同一光环）| false  |
| overwriteSameCaster | osc, oc | 应用时，停止目标上同一施法者施加的所有相同光环，并用新光环替换（不能与合并选项一起使用）                                                | false   |
| overwriteAll    | overwrite, ow | 应用时，停止目标上的所有相同光环并用新光环替换（不能与合并选项一起使用）                                                                | false   |
| CancelOnGiveDamage | cogd    | 如果拥有光环的实体对其他实体造成任何伤害，则取消光环                                                                                         | false   |
| CancelOnTakeDamage | cotd    | 如果拥有光环的实体受到任何伤害，则取消光环|false|
| CancelOnDeath      | cod     | 如果拥有光环的实体死亡，则取消光环             | true    |
| CancelOnCasterDeath| cocd    | 如果光环的施法者死亡，则取消光环               | false   |
| CancelOnTeleport   | cot     | 如果拥有光环的实体传送（无论是通过其他机制还是服务器命令），则取消光环                                                             | false   |
| CancelOnChangeWorld | cocw    | 如果拥有光环的实体切换世界，则取消光环（大多数情况下适用于玩家）                                                                            | false   |
| CancelOnSkillUse    | cosu    | 如果拥有光环的实体在光环激活时使用其他技能，则取消光环                                                                             | false   |
| CancelOnQuit        | coq     | 如果拥有光环的实体登出，则取消光环（仅真正适用于玩家）                                                                            | true    |
| DoEndSkillOnTerminate | desot, alwaysrunendskill, ares | 当光环被 auraremove 机制移除时，是否仍执行 onEndSkill                                                       | true    |

### ShowBarTimer 属性
如果设为 `true`，将提供额外的属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bartimerdisplay | bartimertext | Boss 血条中显示的文本                                    | auraname |
| bartimercolor |       | Boss 血条的[颜色](/Mobs/BossBar#color)      | RED<!--type:BarColor--> |
| bartimerstyle |       | Boss 血条的[样式](/Mobs/BossBar#style)    | SOLID<!--type:BarStyle--> |


## 附着类型
附着是可选的"对象"，应用于（附着到）光环所施加的实体上

| 附着  | 缩写      | 描述                                                               |
|-------------|--------------|---------------------------------------------------------------------------|
| [MODELENGINE](#modelengine-attachment) | MEG, ME      | 一个 ModelEngine 模型                            |

### ModelEngine 附着
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| attachmentmodel | attachmodel, model | 附着的模型                           |         |
| attachmentstate | attachstate, state | 模型将播放的状态                   |         |
| attachmentcolor | attachcolor | 应用于模型的颜色                               |         |
| attachmentscale | attachscale | 模型的缩放                                       | 1       |
| attachmentViewRadius | attackviewradius | 模型的视距。设为 -1 使用 ModelEngine 的默认设置 | -1 |
| attachmentEnchanted | attachEnchanted, enchanted | 模型是否应带附魔光效 | false |
| attachmentGlowing | attachGlowing, glowing | 模型是否应发光             | false   |
| attachmentglowcolor | attachglowcolor | 模型的发光颜色，前提是 `attachmentGlowing` 设为 `true` | |
| attachmentCulling | attachCulling, culling | 模型是否可被 ModelEngine 剔除 | true | 
| attachmentoffset | attachoffset | 模型相对于附着实体的偏移，格式为 `x,y,z,yaw,pitch`<br>也可以写成 `x,y,z` 或 `x,y,z,yaw` | 0,0,0,0,0 |

## 示例
```yaml
  Skills:
  - Aura{auraName=Retributing_Light;onTick=RetributingLightDamage;interval=10;duration=240} @self
```
给予目标（在此例中为实体自身）名为 Retributing_Light 的光环，持续 12 秒。每 10 刻（即半秒）触发一次 RetributingLightDamage 技能。
##
```yaml
 Skills:
  - onDamaged{auraName=fire_shield;onHit=FireShield;duration=200;charges=5;multiplier=0.5} @self
```
在此例中，施法者在 10 秒内受到的下 5 次攻击将触发 FireShield 技能，瞄准攻击者并造成 50% 的伤害。但如果 FireShield 的条件失败，将造成普通伤害，因为倍率也不会触发。
##
```yaml
  Skills:
  - onAttack{auraName=fiery_strikes;onHit=FireStrike;duration=200;charges=5;multiplier=2} @self
```
在此例中，施法者在 10 秒内的下 5 次物理攻击将触发 FireStrike 技能，瞄准被攻击的目标并造成 200% 的伤害。但如果 FireStrike 的条件失败，将造成普通伤害，因为倍率也不会触发。


## 别名
- [x] buff
- [x] debuff


<!-- LINKS -->
[已实现的占位符]: /Skills/Placeholders#variable-placeholders


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:Meta-Mechanic-->