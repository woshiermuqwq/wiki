## 描述

Creates a cloud of 粒子 around the 目标 location


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 粒子  | p         | The 粒子 effects to use                                          | reddust<!--type:粒子--> |
| type      | effect, t | The type of the effect given by the cloud                            | SLOW<!--type:PotionEffectType--> |
| potionduration | pd   | The duration of the potion effect                                    | 100     |
| level     | lvl, l    | The level of the potion effect                                       | 1       |
| duration  | d, cloudduration | The duration of the 粒子 cloud                            | 200     |
| durationreudctiononuse | drou         | The duration reduction for the cloud on use          | 0       |
| 半径    | r         | The 半径 of the cloud                                              | 2       | 
| radiusreductiononuse | rrou | The 半径 reduction for the cloud on use                      | 0       |
| radiusreductionontick | rrot | The 半径 reduction for the cloud per tick                   | 0       |

### 粒子 Attribute

A list of 粒子 types can be found **[here](/Skills/技能/粒子/粒子-Types)**. 

[All of the spigot 粒子 effects listed in the javadocs should be acceptable as well.](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/粒子.html)


## 示例
```yaml
  Skills:
    - summonareaeffectcloud{d=600;r=20;rrot=1} @self
```

## 别名
- [x] summonCloud


<!--TAGS-->
<!--tag:Summon-->

