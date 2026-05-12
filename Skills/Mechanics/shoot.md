## 描述

Shoots an arrow or item-弹射物 at 目标实体 or location
that deals damage. The shoot-技能 has been significantly changed in
version 2.4. 请查看下文了解 both how it worked prior and after those
additions.

Added most of the options from the 弹射物 技能 to Shoot & Volley in MM 4.11


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | Type of 弹射物 to shoot.                                         | arrow<!--type:Shoot_Type-->|
| damage    | d, amount | How much damage the 弹射物 will cause                            | 5       |
| 速度  | v         | The 速度 of the 弹射物                                       | 1       |
| maxDistance | md      | The maximum distance the 弹射物 will travel                      | 64      |
| poweraffectsvelocity | pav | 是否 生物的 power level should affect the 速度 of the 弹射物                 | true    |
| interval  | int, i    | How often per second the 弹射物 creates a tick-event             | 4       |
| item      |           | The item being shot. Only applicable to some 弹射物 types        |<!--type:Material-->|
| ontickskill | ontick, ot, m, meta, s, skill | The meta-skill to 执行 on each tick/interval of the 弹射物 |<!--type:Metaskill-->|
| onhitskill | onhit, oh| The meta-skill to 执行 when the 弹射物 hits its 目标        |<!--type:Metaskill-->|
| onendskill | onend, oe| The meta-skill to 执行 when the 弹射物 misses and ends        |<!--type:Metaskill-->|
| bounce    |           | 是否 the 弹射物 will bounce when it hits something            | false   |
| pickup    |           | Can pickup the item.                                                 | false   |
| expiration | duration, expire, e | How many ticks should the 弹射物 exist for after it has landed before it gets removed                                                                         | 100     |
| accuracy  | ac, a     | Accuracy of the 弹射物                                           | 1       |
| knockback | kb        | knockback strength of the 弹射物                                 | 0       |
| piercelevel | pl      | The amount of times the arrow can pierce through an entity           | 0       | 
| verticaloffset       | vo         | The vertical offset of the shot 弹射物               | 0       |
| horizontaloffset     | ho         | The horizontal offset of the shot 弹射物             | 0       |
| forwardoffset | startfoffset, sfo | The forward offset of the shot 弹射物 | 1 |
| sideoffset | soffset, so | The side offset of the shot 弹射物 | 0 |
| startsideoffset | ssoffset, sso | The side offset of the shot 弹射物. Yes, it is the same as the above, but *this* attribute has placeholder support. | `sideOffset's value`|
| gravity   | g         | 是否 the 弹射物 should be affected by gravity                 | true    |
| startyoffset | syo    | The starting y offset of the 弹射物                              | 0       |
| adjustvelocity | av   | If the 施法者 is a player, adjusts the 速度 and direction as if the player was shooting it themselves | true  |
| calculatefiringangle | cfa        | If this is set and the 弹射物 has `gravity`, the 弹射物 will  trace an arc in the air before landing at the 目标 location                                  | false   | 
| verticalnoise  | vn  | The vertical noise (randomness) of the shot 弹射物 | ((1-`accuracy`)*45)/10 |
| horizontalnoise | hn  | The horizontal noise (randomness) of the shot 弹射物   | (1-`accuracy`)*45 |         
| fromorigin| fo        | 是否 the 弹射物 should be shot from the 原点 of the 技能| false   |  
> This 技能 inherits every *inheritable* attribute of the [Damage](/Skills/技能/Damage) 技能

### Type Attribute
The types for the 弹射物 can be
| Type            | 缩写        |
|-----------------|----------------|
| `ARROW`         |                |
| `SNOWBALL`      |                |
| `EGG`           |                |
| `ENDERPEARL`    |                |
| `POTION`        | `SPLASH_POTION`|
| `LINGERING_POTION` |             |
| `ITEM`          |                |
| `BLOCK`         | `FALLING_BLOCK`|
| `TRIDENT`       |                |

#### Potion Type Attributes
These attributes apply if the 弹射物 is of `type` `POTION`
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| potiontype     | ptype, effect, pt, pe | The type of the potion applied to the 弹射物, if POTION | SLOW<!--type:PotionEffectType-->|
| potionduration | pduration, pd | The duration of the potion effect                           | 100     |
| potionlevel    | plevel, lvl, pl | The level of the potion effect                            | 1       |
| force          | overwrite, ow, override, or | 是否 to override the effect on the 目标 if already applied    | false  |
| potioncolor | pc      | The color of the potion                                              | #FFFFFF<!--type:Color--> |
| hasParticles | 粒子 | 是否 not to show the status effect 粒子.                  | true    |
| hasIcon   | icon  | 是否 not to show the status effect icon.                              | true    |
| ambientparticles | ambient  | 是否 to show ambient 粒子.                             | false   |


#### Trident Type Attributes
These attributes apply if the 弹射物 is of `type` `TRIDENT`
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tridentitem | titem, ti | The trident item                                                   |         |

## 示例
```yaml
ArrowBarrage:
  Skills:
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
```


## 别名
- [x] shootprojetile


<!--TAGS-->
<!--tag:Projectile-->
<!--tag:Meta-Mechanic-->