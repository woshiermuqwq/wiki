## 描述
Makes the 目标 entity glow (like with the Glowing potion effect).  
This 技能 is also an [光环].

> **[Glow API](https://www.spigotmc.org/resources/api-glowapi-1-9-1-10.19422/)** is required for minecraft version 1.16.

> Please note that this 技能 is not actually giving the *glowing* effect in any form: it will just *look* like it. If you want to check against the presence of this 技能, you must check against the presence of the applied 光环 (an [hasaura](/skills/条件/hasaura) 条件 con do the trick, for instance)

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraname  | buffname, debuffname | The name of the 光环                                      | #glowing|
| color     | c         | The [color] with which the entity will glow                          | white<!--type:GlowColor--> |
| audience  |           | The [audience] of the glow effect                                    | nearby<!--type:Audience--> |
> This 技能 继承 [光环] 技能 
>> - The `auraname` attribute is **defaulted** at `#glowing`
>> - The `charges` attribute is **set** at `1` and cannot be modified.  
>> - The `maxStacks` attribute is **set** at `1` and cannot be modified.  
>> - The `mergeAll` attribute is **set** at `true` and cannot be modified.  


### Color Attribute
|    VALID     |   COLORS     |
|:------------:|:------------:|
| BLACK        | DARK_GRAY    |
| DARK_BLUE    | BLUE         |
| DARK_GREEN   | GREEN        |
| DARK_AQUA    | AQUA         |
| DARK_RED     | LIGHT_PURPLE |
| DARK_PURPLE  | YELLOW       | 
| GOLD         | WHITE        |
| GRAY         | RED          |


## 示例
Makes the 目标 glow red for 1000 ticks (50 seconds).
```yaml
  Skills:
  - effect:glow{color=RED;duration=1000}
```

## 别名
- [x] effect:glow
- [x] e:glow
- [x] glow

<!-- LINKS -->
[audience]: /Skills/Audience
[color]: #color-attribute
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:Effect-->