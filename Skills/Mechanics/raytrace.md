## 描述
Traces a ray to the 目标.

> **This is a [Premium-Only] 技能!**

| [Implemented Placeholders]     |
|--------------------------------|
| `<skill.var.hit-block-type>`   |


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| entityskill   | eskill, es | meta-skill to use when the ray hits an entity                   |<!--type:Metaskill-->|
| locationskill | lskill, ls | meta-skill to use when the ray hits a location                  |<!--type:Metaskill-->|
| headshotskill | hsskill, hs | meta-skill to use when it's a headshot                         |<!--type:Metaskill-->|
| maxdistance   | distance, md, d | max distance to trace                                      | 50      |
| raywidth      | rw, w      | Width of the ray traced                                         | 0.2     | 
| ignoreentities | ignoreentity, ie | 是否 entities should be ignored, so that the raytrace will never be stopped by them | false |
| ignorepassableblocks | ignorepassable, ip    | ignores collision of passable blocks                                                                                                                     | true          |
| fluidcollisionmode   | fcm                   | [Determines the collision behaviour when fluids get hit during ray tracing](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/FluidCollisionMode.html) | NEVER<!--type:FluidCollisionMode-->|
| accuracy             | ac, a                 | spread of the traced ray                                                                                                                                 | 1             |
| verticalnoise        | vn                    | vertical spread of the ray                                                                                                                               | 0             |
| horizontalnoise      | hn                    | horizontal spread of the ray                                                                                                                             | 0             |
| raytrace条件   | rc, rcond, r条件| 条件 applied to the raytraced 目标                                                                                                               |<!--type:条件-->|
| headshotmultiplier   | hsmultipler, hsm     | headshot power multiplier                                                                                                                                | 1             |


## 示例
```yaml
MyRaytraceSkill:
  Skills:
  - raytrace{
      entitySkill=[
        - damage{amount=20}
      ];
      headshotSkill=[
        - effect:particles{particle=reddust;color=#ff0000}
      ];
      locationSkill=[
        - particles{p=flame;a=20;s=0.2;hS=0.1;vS=0.1}
      ];
      raytraceConditions=[
        - samefaction false
      ]} @targetlocation ~onUse
```


<!-- LINKS -->
[Premium-Only]: Premium-Features
[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders



<!--TAGS-->
<!--tag:Meta-Mechanic-->
<!--tag:Premium-Only-->