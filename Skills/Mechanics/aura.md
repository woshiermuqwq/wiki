## 描述
光环(光环)技能对目标实体施加状态效果，并可在持续时间内触发其他技能。光环让你能够创建自定义状态效果（如增益和减益），系统会追踪其持续时间，并可在其他技能和条件中引用。
触发 other skills over its duration. 光环 allow you to create custom
status effects (即 buffs and debuffs) that are tracked for their
duration and can also be used in other 技能 and 条件.  

[[_TOC_]]

| [Implemented Placeholders]         |
|------------------------------------|
| `<skill.var.光环-name>`            |
| `<skill.var.光环-type>`            |
| `<skill.var.光环-charges>`         |
| `<skill.var.光环-duration>`        |
| `<skill.var.光环-duration-millis>` |
| `<skill.var.光环-stacks>`          |

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraName  | 光环, b, buff, buffname, debuff, debuffname, n, name | Optional name, required to use associated 技能 & 条件 that reference a specific 光环. Given a random UUID if not defined.                            |         |
| auratype  | auragroup, group, type, g | The type of the 光环. It's similar to its name       |         |
| attachmenttype | attachment, attach | The [Attachment](#attachment-types) to apply to the entity the 光环 is applied to                             | NONE    |
| onStartSkill | onStart, os | Meta-Skill executed when the 光环 first starts                  |<!--type:Metaskill-->|
| onTickSkill  | onTick, ot  | Meta-Skill executed every [interval] ticks on the affected entity|<!--type:Metaskill-->|
| onEndSkill   | onEnd, oe   | Meta-Skill executed when the 光环 ends                          |<!--type:Metaskill-->|
| ShowBarTimer | bartimer, bt| If set, the 光环 will display a bar for 施法者 during it        | false   |
| Charges   | c         | If set, the 光环 will fade when it hits zero charges. Modifiable by other 技能.                                                                                     | 0       |
| Duration  | ticks, t, d, time, t | The max duration (in ticks) the 光环 will persist.        | 200     |
| Interval  | i         | How often (in ticks) the 光环 fires its onTick skill                 | 1       |
| maxStacks | ms        | How many times the 光环 stacks on the same targeted entity if applied multiple times                                                                                          | 1       |
| refreshDuration | rd  | Makes 光环的 duration refresh to the amount defined in the 技能 should the entity have the same 光环 applied to it again                                              | true    |
| mergeSameCaster | msc, mc | Merges all 光环 of the same name applied by one entity to another into one 光环 (Prevents a 生物 from being able to stack an 光环 multiple times on the same entity)            | `false` if any among `mergeAll`, `overwriteAll` or `overwriteSameCaster` is `true` |
| mergeAll        | ma  | Merges all 光环 of the same name applied by any and all entities to another into one 光环 (Prevents multiple 生物 from being able to stack an 光环 multiple times on the same entity)| false  |
| overwriteSameCaster | osc, oc | When applied, stops all of the same 光环 applied on the 目标 by the same 施法者 and replaces them with the new 光环 (cannot be used with merge options)                                                | false   |
| overwriteAll    | overwrite, ow | When applied, stops all of the same 光环 applied on the 目标 and replaces them with the new 光环  (cannot be used with merge options)                                                                | false   |
| CancelOnGiveDamage | cogd    | Cancels the 光环 if the entity with the 光环 deals any damage to another entity                                                                                         | false   |
| CancelOnTakeDamage | cotd    | Cancels the 光环 if entity with the 光环 takes any sort of damage|false|
| CancelOnDeath      | cod     | Cancels the 光环 if the entity with the 光环 dies             | true    |
| CancelOnCasterDeath| cocd    | Cancels the 光环 if the 施法者 of the 光环 dies               | false   |
| CancelOnTeleport   | cot     | Cancels the 光环 if the entity with the 光环 teleports at all, 是否 by another 技能 or server command                                                             | false   |
| CancelOnChangeWorld | cocw    | Cancels the 光环 if the entity with the 光环 changes worlds. (Most times applies to players)                                                                            | false   |
| CancelOnSkillUse    | cosu    | Cancels the 光环 if the entity with the 光环 uses another skill while the 光环 is active                                                                             | false   |
| CancelOnQuit        | coq     | Cancels the 光环 if the entity with the 光环 logs out. (Only really applies to players)                                                                            | true    |
| DoEndSkillOnTerminate | desot, alwaysrunendskill, ares | 是否 the 光环 will run onEndSkill when it's removed by auraremove 技能                                                       | true    |

### ShowBarTimer Attribute
If set to `true`, additional attributes becomes available
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bartimerdisplay | bartimertext | The text in the bossbar                                    | auraname |
| bartimercolor |       | The [Color](/生物/BossBar#color) of the bossbar      | RED<!--type:BarColor--> |
| bartimerstyle |       | The [Style](/生物/BossBar#style) of the bossbar    | SOLID<!--type:BarStyle--> |


## Attachment Types
附件是可选的"对象"，会被应用（附着）到被施加光环的实体上

| Attachment  | 缩写      | 描述                                                               |
|-------------|--------------|---------------------------------------------------------------------------|
| [MODELENGINE](#modelengine-attachment) | MEG, ME      | 一个ModelEngine模型                            |

### ModelEngine Attachment
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| attachmentmodel | attachmodel, model | The model of the attachment                           |         |
| attachmentstate | attachstate, state | The state the model will be playing                   |         |
| attachmentcolor | attachcolor | The color applied to the model                               |         |
| attachmentscale | attachscale | The scale of the model                                       | 1       |
| attachmentViewRadius | attackviewradius | The view 半径 of the model. Leave as -1 to use ModelEngine's 默认值： settings | -1 |
| attachmentEnchanted | attachEnchanted, enchanted | 是否 the model should have an enchantment glint applied to it | false |
| attachmentGlowing | attachGlowing, glowing | 是否 the model should be glowing             | false   |
| attachmentglowcolor | attachglowcolor | The glow color of the model, if `attachmentGlowing` is set to `true` | |
| attachmentCulling | attachCulling, culling | 是否 the model should be able to be culled by ModelEngine | true | 
| attachmentoffset | attachoffset | The model's offset from the attached entity, in a `x,y,z,水平朝向(yaw),俯仰角(pitch)` format.<br>Can also be written as `x,y,z` or `x,y,z,水平朝向(yaw)` | 0,0,0,0,0 |

## 示例
```yaml
  Skills:
  - Aura{auraName=Retributing_Light;onTick=RetributingLightDamage;interval=10;duration=240} @self
```
Gives the 目标 (Which in this case is the entity itself) the
Retributing_Light 光环 that lasts 12 seconds. Every 10 ticks (or half a
second) it will fire the RetributingLightDamage skill.
##
```yaml
 Skills:
  - onDamaged{auraName=fire_shield;onHit=FireShield;duration=200;charges=5;multiplier=0.5} @self
```
In this example, 施法者的 next 5 hits taken in 10 seconds would
触发 the FireShield skill targeting whatever hit them and also deal
50% damage. However, if FireShield's 条件 failed, it would deal
regular damage as the multiplier would not 触发 either.
##
```yaml
  Skills:
  - onAttack{auraName=fiery_strikes;onHit=FireStrike;duration=200;charges=5;multiplier=2} @self
```
In this example, 施法者的 next 5 physical hits within 10 seconds
would 触发 the FireStrike skill targeting whatever was hit and also
deal 200% damage. However, if FireStrike's 条件 failed, it would
deal regular damage as the multiplier would not 触发 either.


## 别名
- [x] buff
- [x] debuff


<!-- LINKS -->
[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:Meta-Mechanic-->