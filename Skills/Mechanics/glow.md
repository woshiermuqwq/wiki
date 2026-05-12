## 描述
Makes the target entity glow (like with the Glowing potion effect).  
This 机制 is also an [aura].

> **[Glow API](https://www.spigotmc.org/resources/api-glowapi-1-9-1-10.19422/)** is required for minecraft version 1.16.

> Please note that this 机制 is not actually giving the *glowing* effect in any form: it will just *look* like it. If you want to check against the presence of this 机制, you must check against the presence of the applied aura (an [hasaura](/skills/conditions/hasaura) condition con do the trick, for instance)

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraname  | buffname, debuffname | The name of the aura                                      | #glowing|
| color     | c         | The [color] with which the entity will glow                          | white<!--type:GlowColor--> |
| audience  |           | The [audience] of the glow effect                                    | nearby<!--type:Audience--> |
> 此机制继承所有[Aura] 机制 
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
使目标发光 red for 1000 ticks (50 seconds).
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
