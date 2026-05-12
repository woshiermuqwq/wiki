## 描述
Sets the given metaskill's 冷却 to the given value (in seconds)

> If used to set the 冷却 of the metaskill the 技能 is in a delay of at least `0` between the execution of the metaskill and the 技能 must be used

> The 目标 Metaskill needs to have a 冷却 option to begin with. If you do not wish for it to have a 冷却 but you still want to use this 技能 to set it dynamically, use `冷却: 0`

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| skill     | s   | The [metaskill] of which you want to set the 冷却                      |<!--type:Metaskill-->|
| seconds   | sec, time, t | The duration of the 冷却                                      | 0       |


## 示例
```yaml
  Skills:
  - setSkillCooldown{skill=test_skill;seconds=10} @self
```
> 此示例将 set the 冷却 of the metaskill *test_skill* to 10 seconds for the 施法者

##
```yaml
ExampleSkill:
  Cooldown: 0
  OnCooldownSkill: ExampleSkill-DisplayCooldown
  Skills:
  - delay 0
  - setSkillCooldown{s=ExampleSkill;seconds=<skill.cooldown>/20} @self
```
> How to use the 技能 if you intend to set the 冷却 of the calling metaskill


## 别名
- [x] skillCooldown
- [x] setskillcd
- [x] skillcd


<!-- ALIASES -->
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Meta-->
<!--tag:Meta-Mechanic-->