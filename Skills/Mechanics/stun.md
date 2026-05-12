## 描述
Holds the 目标 in place temporarily.

> This 技能 can cause Spigot to kick the player (`PlayerName moved wrongly!`)


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| stopai    | ai        | Removes entity AI while stunned                                      | false   |
| gravity   | g         | Remove gravity from 目标 when stunned (1.9+)                       | false   |
| facing    | face, f   | When false, entity cannot rotate or look around when stunned         | false   |
| noknockback | nokb, kb | When true, entity cannot be knocked back when stunned               | false   |
> This 技能 继承 [光环] 技能 
>> - The `interval` attribute is **set** at `1`

> Remember to use 光环的 `duration` attribute to set a duration for the stun


## 示例
Stuns the 目标 for 3 seconds, 目标 cannot rotate.
```yaml
ExampleSkill:
  Skills:
  - stun{d=60;f=false} @target
```


<!-- LINKS -->
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:AI-->

