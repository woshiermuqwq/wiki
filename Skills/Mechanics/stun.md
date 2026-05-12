## 描述
Holds the target in place temporarily.

> This 技能 can cause Spigot to kick the player (`PlayerName moved wrongly!`)


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| stopai    | ai        | Removes entity AI while stunned                                      | false   |
| gravity   | g         | Remove gravity from target when stunned (1.9+)                       | false   |
| facing    | face, f   | When false, entity cannot rotate or look around when stunned         | false   |
| noknockback | nokb, kb | When true, entity cannot be knocked back when stunned               | false   |
> 此技能继承所有[Aura] 技能 
>> - The `interval` attribute is **set** at `1`

> Remember to use the aura's `duration` attribute to set a duration 对于stun


## 示例
眩晕目标 for 3 seconds, target cannot rotate.
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
