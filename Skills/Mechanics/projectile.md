## 描述
The 弹射物 skill fires a meta-"弹射物" that can be decorated
using 粒子 and sound effects.  
It's great for creating complex, aesthetically pleasing skills, such as
shadow bolts, balls of ice, or even meteors.  
It has a lot of options (more than any other 技能) and can be a bit of a
nightmare to jump into without knowing what you're doing.  
It will disappear after hitting an entity or location that is able to stop the 弹射物. This behavior can be configured via attributes like `stopatblock`, `stopatentity` and `stop条件`

It is of importance to note that other 技能 (such as [制导弹射物](/skills/技能/制导弹射物) and [Totem](/skills/技能/totem)) are an "extension" of this 技能, and can as such use a great deal of this 技能's attributes. The attributes that those 技能 can use are listen in [Inheritable Attributes](/skills/技能/弹射物#inheritable-attributes)

[[_TOC_]]

## 属性
### Inheritable Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onStartSkill | onStart, oS | Meta-Skill executed when the 弹射物 starts at 弹射物的 原点 location.                                                                                      |<!--type:Metaskill-->|
| onTickSkill  | onTick, oT, m, meta, s, skill | Meta-Skill executed every [interval] ticks at 弹射物的 原点 location                                                                                       |<!--type:Metaskill-->|
| onHitSkill   | onHit, oH   | Meta-Skill executed when the 弹射物 hits entities that are allowed be hit. 目标 hit are inherited by the meta-skill.                                              |<!--type:Metaskill-->|
| onEndSkill   | onEnd, oE   | Meta-Skill executed when the 弹射物 ends.                   |<!--type:Metaskill-->|
| onBounceSkill| onBounce    |Meta-Skill executed when the 弹射物 bounces. **Premium Only**.|<!--type:Metaskill-->|
| onHitBlockSkill |onHitBlock, ohb | Meta-Skill executed when the 弹射物 hits a block.     |<!--type:Metaskill-->|
| onInteractSkill |onInteract| Meta-Skill executed when the 弹射物 is interacted with.     |<!--type:Metaskill-->|
| BulletType   | bullet, b   | The type of the bullet. If set, additional attributes becomes available depending on the specified bullet type. A list of bullet types and associated attributes is available [below](/skills/技能/弹射物#弹射物-bullets)                                       | <!--type:Projectile_BulletType-->|
| Interval  | int, i      | How often (in ticks) the 弹射物 updates its position           | 1       |
| HorizontalRadius | hRadius, hR, r | The horizontal 半径 entities will be hit in around the 弹射物.                                                                                                                                    | 1.25    |
| VerticalRadius   | vRadius, vR | The vertical 半径 entities will be hit in around the 弹射物.                                                                                                                                      | 1.25    |
| Duration  | maxDuration, md, d | The max duration (in ticks) the 弹射物 will persist.    | 400     |
| MaxRange  | mr        | The maximum range (in blocks) the 弹射物 will travel.            | 40      |
| 速度  | v         | The 速度 of the 弹射物, expressed in blocks traveled per second| 5     |
| DeathDelay| death, dd | Delays the removal of project bullets when the 弹射物 is terminated | 2    |
| StartYOffset | syo    | Lets you offset where on the casting 生物 the 弹射物 shoots from. | 1       |
| StartFOffset | forwardoffset, sfo |  How far in front of the 生物 the 弹射物 starts       | 1       |
| TargetYOffset | tyo, targety | Lets you offset where on the 目标 the 弹射物 shoots at. | 0       |
| SideOffset | soffset, so | The value of this attribute gets inherited by StartSideOffset and EndSideOffset if no value is specified for them                                                | 0       |  
| StartSideOffset | ssoffset, sso | How far to the side of the 生物 the 弹射物 starts      |sideoffset|
| EndSideOffset | endoffset, esoffset, eso | How far to the side of the 目标 location the 弹射物 will end up                                                                                   |sideoffset|
| startingdirection | startingdir, startdir, sdir | Start direction of the 弹射物. For now, it only works if inherited by a 制导弹射物 技能                                                      |@Targeted<!--type:Targeter-->|
| HorizontalOffset | hO | Horizontal Offset will rotate 弹射物的 horizontal starting 速度 around a 360-degree axis                                                                      | 0        |
| VerticalOffset   | vO | Vertical Offset will add a [slope](https://en.wikipedia.org/wiki/Grade_(slope)) to 弹射物的 starting direction. To give it a specific angle, you can use [this image](https://en.wikipedia.org/wiki/Grade_(slope)#/media/File:Slope_quadrant.svg) as reference: the value you need will be the number shown in red divided by 100 (so if you want 40°, you will need to input 83.9/100 = `0.839`)| 0        |
| Accuracy  | ac, a     | Determines the accuracy of the 弹射物                           | 1        |
| HorizontalNoise | hn  | The randomness of the 弹射物 in horizontal direction            |(1-ac)*45 |
| VerticalNoise   | vn  | The randomness of the 弹射物 in the vertical direction          |(1-ac)*4.5|
| StopAtEntity | sE     | 是否 the 弹射物 will stop upon hitting a targetable entity   | true     |
| StopAtBlock  | sB     | 是否 the 弹射物 will stop upon hitting an opaque block       | true     |
| PowerAffectsRange | par | 是否 a 生物's [power level](/生物/Power) affects 弹射物的 range| true|
| PowerAffectsVelocity | pav | 是否 a 生物's [power level](/生物/Power) affects 弹射物的 速度.                                                                                     | true     |
| Interactable |        | 是否 the 弹射物 is interactable                              | false    |
| HitSelf   |           | 是否 the 弹射物 can hit the 施法者                           | false    |
| HitPlayers | hp       | 是否 the 弹射物 can hit players                              | true     |
| HitNonPlayers | hnp   | 是否 the 弹射物 can hit non player entities                  | false    |
| HitTarget | ht        | 是否 the 弹射物 can hit 技能的 目标                | true     |
| HitTargetOnly | hto   | 是否 the 弹射物 can **only** hit 技能的 目标       | false    |
| ImmuneDelay | immune, id | Sets the immunity delay (when the 目标 can be hit by the 弹射物 again) | 2000  |
| hit条件 | 条件, cond, c | A list of 条件 that a 目标 must meet in order for the 弹射物 to be able to hit it. **Premium Only** 技能  |<!--type:条件-->|
| stop条件 | stpcond | A list of 条件 that a 目标 must meet in order for the 弹射物 to end when hitting them                                                                         | null     |
| doEndSkillOnHit | esoh | 是否 the onEnd metaskill should be run when the 弹射物 ends by hitting an entity | true |
| fromorigin | fo       | 是否 the 弹射物 should start from the 原点 of the 技能 | false    |
| requireLineOfSight | rlos, los, requirelos | 是否 the starting point must have line-of-sight to the 原点.  Values can be `true`, `false`, `PLAYERS_ONLY`                                             | PLAYERS_ONLY<!--type:Projectile_HighAccuracyMode-->|
| drawHitbox |          | Draw the hitbox of the 弹射物, useful for debugging             | false    |
| tickinterpolation | interpolation, ti | Interpolates the 指定的amount of additional points between each tick of the 弹射物. The onTick and onHit skills 将被应用 there as well. Useful to fill in the gaps with super-fast 弹射物 and also prevent entities from being "skipped over"      | 0        |
| shareSubHitboxCooldown | shcd | 是否 all meg sub hitboxes should share the same immune delay with its base entity | true | 
| hitTargeter | htr     | An entity targeter. Once the 弹射物 hits, targeted entities will be targeted by the onHit Metaskill and given immune delay just like 弹射物的 main 目标          | <!--type:Targeter--> |

### 弹射物-Specific Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| Type      |           | The "type" of 弹射物. 默认值： 弹射物 are launched from 生物的 location towards the 目标. METEOR type 弹射物 fall from the sky above the 目标.       | NORMAL<!--type:Projectile_Type-->|
| gravity   | g         | Determines the gravity of the 弹射物; use fractions (0.1-0.2) for low gravity                                                                                        | 0       |
| Bounces   | bounce    | Should the 弹射物 bounce. Bounce 半径 depends on 弹射物的 hitbox. **Premium Only**.                                                                              | false   |
| BounceVelocity | bv   | Every time the 弹射物 bounces, its 速度 will be multiplied by this value. **Premium Only** .                                                                      | 0.9     |
| HugSurface| hs        | 是否 the 弹射物 should move along the ground.          | false   |
| HugLiquid | hugwater, huglava | when using hugSurface will also move on top of liquids       | false   |
| HeightFromSurface| hfs| For NORMAL 弹射物, how high above the surface the 弹射物 should glide if HugSurface is set to TRUE. For METEOR 弹射物, how high above the surface the 弹射物 starts above the 目标.                                                                              | 0.5     |
| MaxClimbHeight | mch  | The number of attempts the 弹射物 will make to **increase** its y-location before terminating itself, when 弹射物的 is "hugging" either a block or a liquid        | 3       |
| MaxDropHeight  | mdh  | The number of attempts the 弹射物 will make to **decrease** its y-location before terminating itself, when 弹射物的 is "hugging" either a block or a liquid        | 10      |
| highAccuracyMode | ham| 是否 to use high-accuracy mode, which raytraces every tick to ensure the 弹射物 cannot ever go through anything. Values can be `true`, `false`, `PLAYERS_ONLY`         | PLAYERS_ONLY<!--type:Projectile_HighAccuracyMode-->|


## Special Notes

**For the <u>onStart</u> Skill:** onStart skills work in a special way -
any buff or "special effect" 技能 fired by onStart that have a
duration (such as ParticleTornado) will attach to the 弹射物 for
their duration, which allows for some interesting effects.

**For the <u>onTick</u> Skill:** using the **@原点** targeter will
cause any skills or effects to 目标 弹射物的 location. This is
the intended way to configure how the 弹射物 looks.

**For the <u>onHit</u> Skill:** Any 目标 the 弹射物 hits are
passed to the skill inherently. Any targeters you put in the onHit skill
will *override* these and cause your skill to likely not work as you
intend.

**For the <u>onEnd</u> Skill:** Special effects for 弹射物的 end
also use **@原点**. Also, If you want entities near the end-point of
the 弹射物 to be hit in a certain way (such as a final large
fireball explosion) you can use the **@PlayersNearOrigin{r=[半径]}**
targeter.

**Types:**  
There are two types of 弹射物, the normal variant and also the
Meteor variant.  
Meteor 弹射物 are created above the 目标, rather than at the 生物
that is firing the 弹射物.  
Because of this, meteor 弹射物 cannot use certain attributes (which
ones are pending further testing).


## 弹射物 Bullets

The bullet type that will represent the 弹射物. These can be specified via the BulletType attribute.
These work with the 弹射物, 制导弹射物, and orbital 技能.

| BulletType  | 缩写      | 描述                                                               |
|-------------|--------------|---------------------------------------------------------------------------|
| [ARROW][]   |              | The bullet will be a minecraft 弹射物                                 |
| [BLOCK][]   |              | The bullet will be a block                                                |
| [SMALLBLOCK][]|            | The bullet will be a small block                                          |
| [ITEM][]    | MYTHICITEM   | The bullet will be an item or MythicItem                                  |
| [生物][]     |              | The bullet will be a 生物. If a Mythic生物, it will retain its skills      |
| [TRACKING][]| ARMOR_STAND, ARMORSTAND, PSTAND | The bullet will be an item, but its rotation will be adjusted depending on 弹射物的 direction                                                         |
| [REALTRACKING][] | RTRACKING, REAL_ARMOR_STAND, REALARMORSTAND, STAND | As above, but a real armor stand will also be spawned instead of a packet |
| [DISPLAY][] |              | The 弹射物 will be a display entity                                   |
| [TEXT][]    |              | The 弹射物 will display a line of text                                |
| [ME][]      | MEG, MODELENGINE | The 弹射物 will be a [ModelEngine] model                          |

Examples:
```yaml
  - projectile{bulletType=ARROW;arrowType=TRIDENT;...}
  - projectile{bulletType=BLOCK;material=STONE;...}
  - projectile{bulletType=ITEM;material=MyMythicItem;...}
  - projectile{bulletType=MOB;mob=SkeletonKing;...}
```

[ARROW]: /skills/mechanics/projectile#arrow-bullet
[BLOCK]: /skills/mechanics/projectile#block-bullet
[SMALLBLOCK]: /skills/mechanics/projectile#smallblock-bullet
[ITEM]: /skills/mechanics/projectile#item-bullet
[MOB]: /skills/mechanics/projectile#mob-bullet
[TRACKING]: /skills/mechanics/projectile#tracking-bullet
[REALTRACKING]: /skills/mechanics/projectile#realtracking-bullet
[DISPLAY]: /skills/mechanics/projectile#display-bullet
[TEXT]: /skills/mechanics/projectile#text-bullet
[ME]: /skills/mechanics/projectile#me-bullet
[ModelEngine]: /../../../model-engine-4/-/wikis

### Universal Bullet Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletforwardoffset | bulletfo, bulletoffset, bfo | The offset of the bullet                 | 1.8     |
| bulletYOffset | byo   | The Y offset of the bullet                                           | 0       | 

### ARROW Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| arrowtype | bulletarrowtype | The type of the 弹射物 to use. Can be `NORMAL`,`SPECTRAL`,`TRIDENT` | NORMAL<!--type:NORMAL,SPECTRAL,TRIDENT--> |

### BLOCK Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet                                  | STONE<!--type:Block--> |
| bulletspin | bspin    | The spin of the bullet                                               | 0       |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### SMALLBLOCK Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet                                  | STONE<!--type:Material--> |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### ITEM Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet, either a vanilla item type or custom MythicItem    | STONE<!--type:Item-->  |
|bulletModel| model     | The CustomModelData integer for the material (define model strings on a MythicItem instead)   | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletmatchdirection | bmd, bulletsmall | Should the bullet face where the 弹射物 is facing | false |
| bulletEnchanted | enchanted | Should the material be enchanted                               | false   |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### 生物 Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 生物       | mobType, mm | The 生物 of the bullet                         | SkeletalKnight<!--type:生物-->|
| bulletspin | bspin    | The spin of the bullet                                               | 0       |
| bulletmatchdirection | bmd | Should the bullet face where the 弹射物 is facing           | false   |
| bulletKillable | bk   | Allow other entities to damage the 弹射物 bullet                 | false   |
| bulletYOffset| byo | The Y offset of the bullet 生物                                          | 1.35    | 
| bulletForwardOffset| bfo| The forward offset of the bullet 生物                               | 1.35    | 

### TRACKING Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet, can be vanilla item type or MythicItem     | STONE<!--type:Item--> |
|bulletModel| model     | The CustomModelData integer for the material (define model strings on a MythicItem instead)  | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletEnchanted | enchanted | Should the material be enchanted                               | false   |
| 俯仰角(pitch)     |           | The 俯仰角(pitch) rotation, in radians                                       | 0       |
| 水平朝向(yaw)       |           | The 水平朝向(yaw) rotation, in radians                                         | 0       |
| roll      |           | The roll rotation, in radians                                        | 0       |
| rotation  | rot       | The rotation of the bullet in radians, in the x,y,z format           | 0,0,0   |
| pitchspeed| ps        | The 俯仰角(pitch) rotation speed                                             | 0       |
| yawspeed  | ys        | The 水平朝向(yaw) rotation speed                                               | 0       |
| rollspeed | rs        | The roll rotation speed                                              | 0       |
| rotationspeed | rotspeed, rots | The rotation speed of the bullet, in the x,y,z format      | 0,0,0   |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### REALTRACKING Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet, can be vanilla item type or MythicItem | STONE<!--type:Item--> |
|bulletModel| model     | The CustomModelData integer for the material (define model strings on a MythicItem instead) | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletEnchanted | enchanted | Should the material be enchanted                               | false   |

### DISPLAY Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat, bulletitem | The material of the bullet, can be vanilla item type or MythicItem  | STONE<!--type:Item--> |
|bulletModel| model     | The CustomModelData integer for the material (define model strings on a MythicItem instead) | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletEnchanted | enchanted | Should the material be enchanted                               | false   |
|bulletscale| scale     | The scale of the bullet                                            |0.5,0.5,0.5|
| bulletyoffset | byoffset, byo | The y offset of the bullet                                   | 0.2     |
| bulletBillboarding | bulletBillboard | The [billboard type] of the bullet                    | FIXED   |
| bulletbrightness | bulletbrightnessblock | The bullet's brightness                           | -1      |
| bulletbrightnesssky | | The bullet's sky light brightness                           | bulletbrightness |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | The range in which the bullet will be visible                                                                                        | 50      |
| 俯仰角(pitch)     |           | The 俯仰角(pitch) rotation, in radians                                       | 0       |
| 水平朝向(yaw)       |           | The 水平朝向(yaw) rotation, in radians                                         | 0       |
| roll      |           | The roll rotation, in radians                                        | 0       |
| rotation  | rot       | The rotation of the bullet in radians, in the x,y,z format           | 0,0,0   |
| pitchspeed| ps        | The 俯仰角(pitch) rotation speed                                             | 0       |
| yawspeed  | ys        | The 水平朝向(yaw) rotation speed                                               | 0       |
| rollspeed | rs        | The roll rotation speed                                              | 0       |
| rotationspeed | rotspeed, rots | The rotation speed of the bullet, in the x,y,z format       | 0,0,0   |
| tx        |           | The translation on the x axis                                        | 0       |
| ty        |           | The translation on the y axis                                        | 0       |
| tz        |           | The translation on the z axis                                        | 0       |
| translation | pos, offset | The translations on the axes, in the x,y,z format                | 0,0,0   |
| hideFirstTick | hft   | Hides the item for the first tick                                    | false   |
| bulletCullingHeight | cullHeight | The bullet's display culling height                       | 0.0     |
| bulletCullingWidth | cullWidth | The bullet's display culling width                          | 0.0     |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |
| bulletgen | generation, bulletgeneration | If MythicCrucible is installed, the generation option for the bullet item |

### ME Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletModel | model   | The MEG model to use for the bullet                                  |         |
| bulletstate | state   | The state to play for the MEG model                                  |         |
| bulletcolor |         | The tint of the bullet's model                                       |         |
| bulletscale |         | The scale of the bullet                                              | 1       |
| bulletEnchanted | enchanted | 是否 the bullet's model should be enchanted                 | false   | 
| bulletGlowing | glowing | 是否 the bullet's model should be glowing                       | false   |
| bulletglowcolor |     | The glow color of the bullet, if `bulletGlowing` is set to true      |         |
| bulletCulling  | culling | 是否 to apply culling for the bullet model                     | true    |
| bulletViewRadius |    | From how far the bullet can be seen, if greater than 0.              | -1      |

### TEXT Bullet
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletText| text      | The text of the bullet                                               | *       |
| bulletBillboard | billboard | The [billboard type] of the bullet                             | CENTER<!--type:Billboard-->|
|bulletscale| scale     | The scale of the bullet                                            |0.5,0.5,0.5|
| forcedBulletRotation  | forcedRotation | Forces the rotation of the bullet with the specified 俯仰角(pitch), 水平朝向(yaw) and roll, in the x,y,z format. Leave empty to allow the bullet to dynamically rotate based on the travel direction |   |
| bulletRotatesBasedOnDirection | | 是否 the text bullet should rotate based on the direction of movement. Might *not* be what you expect | false |
| bulletyoffset | byoffset, byo | The y offset of the bullet                                   | 0       |
| bulletforwardoffset | bulletfo, bulletoffset, bfo | The forward offset of the bullet         | 1.8     |
| backgroundcolor | color | The Background color, in the ARGB format                          | 64,0,0,0 |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | The range in which the bullet will be visible                                                                                        | 50      |
| bulletCullingHeight | cullHeight | The bullet's display culling height                       | 0.0     |
| bulletCullingWidth | cullWidth | The bullet's display culling width                          | 0.0     |
| bulletBrightness | bulletBrightnessBlock | The bullet's brightness, if the value is > -1     | -1      |
| bulletBrightnessSky| |The bullet's sky light brightness, if the value is > -1                | -1      |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |


## 示例

This example shoots a fast-moving ball of ice that damages and slows the
first entity it hits:  
**生物 File**  
```yaml
Mob:
  Type: SKELETON
  Skills:
  - skill{s=IceBolt} @target ~onTimer:100
```
**Skills File**  
```yaml
IceBolt:
  Skills:
  - projectile{onTick=IceBolt-Tick;onHit=IceBolt-Hit;v=8;i=1;hR=1;vR=1;hnp=true}
IceBolt-Tick:
  Skills:
  - effect:particles{p=snowballpoof;amount=20;speed=0;hS=0.2;vS=0.2} @origin
IceBolt-Hit:
  Skills:
  - damage{a=10}
  - potion{type=SLOW;duration=100;lvl=2}
```
hit条件 usage example:
```yaml
  - projectile{hitConditions=[  - isMonster true  - isFrozen false ]}
```


## 别名
- [x] p


<!-- LINKS -->
[Audience]: /Skills/Audience
[billboard type]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Display.Billboard.html


<!--TAGS-->
<!--tag:Projectile-->
<!--tag:Meta-Mechanic-->