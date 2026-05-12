## 描述
Ex执行 the 技能 when the 生物 hears a sound, [if this feature 已被 启用](/生物/生物#hearing).
The `<skill.var.volume>` [占位符](/技能/占位符#变量-占位符)可以usedin the triggered 技能 to 返回 a float 值 between 1 and 15 representing the 距离 从 sound source。

> > The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that generated the sound

> > The associated [@原点](/技能/目标选择器/原点) is the 位置 该 sound was generated

| [Implemented 占位符](/技能/占位符#变量-占位符) |
|--------------------------------|
| `<skill.var.volume>` |
| `<skill.var.sound-type>` |


## 示例
```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="I can hear you <trigger.name>! <skill.var.volume>? Way too loud!"} @trigger ~onHear
```


## 别名
- [x] onVibration