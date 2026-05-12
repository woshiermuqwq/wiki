## 描述
Sets the given metaskill's cooldown to the given value (in seconds)

> If used to set the cooldown of the metaskill the 机制 is in a delay of at least `0` between the execution of the metaskill and the 机制 必须 used

> The target Metaskill needs to have a Cooldown option to begin with. If you do not wish for it to have a Cooldown but you still want to use this 机制 to set it dynamically, use `Cooldown: 0`

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| skill     | s   | The [metaskill] of which you want to set the cooldown                      |<!--type:Metaskill-->|
| seconds   | sec, time, t | 冷却的持续时间                                      | 0       |


## 示例
```yaml
  Skills:
  - setSkillCooldown{skill=test_skill;seconds=10} @self
```
> This example would set the cooldown of the metaskill *test_skill* to 10 seconds 对于caster

##
```yaml
ExampleSkill:
  Cooldown: 0
  OnCooldownSkill: ExampleSkill-DisplayCooldown
  Skills:
  - delay 0
  - setSkillCooldown{s=ExampleSkill;seconds=<skill.cooldown>/20} @self
```
> How to use the 机制 if you intend to set the cooldown of the calling metaskill


## 别名
- [x] skillCooldown
- [x] setskillcd
- [x] skillcd


<!-- ALIASES -->
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Meta-->
<!--tag:Meta-Mechanic-->
