## 描述

Creates a cloud of particles around the target location


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| particle  | p         | The particle effects to use                                          | reddust<!--type:Particle--> |
| type      | effect, t | The type of the effect given by the cloud                            | SLOW<!--type:PotionEffectType--> |
| potionduration | pd   | The duration of the potion effect                                    | 100     |
| level     | lvl, l    | The level of the potion effect                                       | 1       |
| duration  | d, cloudduration | The duration of the particle cloud                            | 200     |
| durationreudctiononuse | drou         | The duration reduction 对于cloud on use          | 0       |
| radius    | r         | The radius of the cloud                                              | 2       | 
| radiusreductiononuse | rrou | The radius reduction 对于cloud on use                      | 0       |
| radiusreductionontick | rrot | The radius reduction 对于cloud per tick                   | 0       |

### Particle Attribute

A list of particle types 可以 found **[here](/Skills/Mechanics/Particle/Particle-Types)**. 

[All of the spigot particle effects listed in the javadocs 应当 acceptable as well.](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)


## 示例
```yaml
  Skills:
    - summonareaeffectcloud{d=600;r=20;rrot=1} @self
```

## 别名
- [x] summonCloud


<!--TAGS-->
<!--tag:Summon-->
