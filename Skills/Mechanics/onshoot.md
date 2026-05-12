## 描述
Applies an 光环 to the 目标 that 触发 a skill when they shoot with a bow. Can use any [光环] attribute

| [Implemented Placeholders]     |
|--------------------------------|
| `<skill.var.bow-tension>`      |


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onShootSkill | onshoot, osh, onbowshoot, onbowshootskill | Skill to 执行 when the entity shoots |<!--type:Metaskill-->|
| cancelEvent | cE      | 是否 to cancel the event that triggered the 光环           | false   |
| forceaspower | fap    | 是否 to pass the force of the bow as 技能的 power            | true    |

> This 技能 继承 [光环] 技能


## 示例
```yaml
  Skills:
  - onShoot{auraName=fireball_bow;onShoot=[ shootfireball ];duration=200;charges=5;cancelEvent=true} @self
```
In this example, 施法者的 next 5 bow shots will shoot fireballs
instead of arrows.


## 别名
- [x] onbowshoot


<!-- LINKS -->
[aura]: /skills/mechanics/aura
[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
