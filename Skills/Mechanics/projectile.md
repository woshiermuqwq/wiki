## 描述
The Projectile skill fires a meta-"projectile" that 可以 decorated
using particle and sound effects.  
It's great for creating complex, aesthetically pleasing skills, such as
shadow bolts, balls of ice, or even meteors.  
It has a lot of options (more than any other 机制) and 可以 a bit of a
nightmare to jump into without knowing what you're doing.  
It will disappear after hitting an entity or location that is able to stop the projectile. This behavior 可以 configured via attributes like `stopatblock`, `stopatentity` and `stopconditions`

It is of importance to note that other 机制s (such as [Missile](/skills/mechanics/missile) and [Totem](/skills/mechanics/totem)) are an "extension" of this 机制, and can as such use a great deal of this 机制's attributes. The attributes that those 机制s can use are listen in [Inheritable Attributes](/skills/mechanics/projectile#inheritable-attributes)

[[_TOC_]]

## 属性
### 可继承属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onStartSkill | onStart, oS | 元技能，在 the projectile starts 在projectile's origin location.                                                                                      |<!--type:Metaskill-->|
| onTickSkill  | onTick, oT, m, meta, s, skill | Meta-Skill executed every [interval] ticks 在projectile's origin location                                                                                       |<!--type:Metaskill-->|
| onHitSkill   | onHit, oH   | 元技能，在 the projectile hits entities that are allowed be hit. Targets hit are inherited by the meta-skill.                                              |<!--type:Metaskill-->|
| onEndSkill   | onEnd, oE   | 元技能，在 the projectile ends.                   |<!--type:Metaskill-->|
| onBounceSkill| onBounce    |元技能，在 the projectile bounces. **Premium Only**.|<!--type:Metaskill-->|
| onHitBlockSkill |onHitBlock, ohb | 元技能，在 the projectile hits a block.     |<!--type:Metaskill-->|
| onInteractSkill |onInteract| 元技能，在 the projectile is interacted with.     |<!--type:Metaskill-->|
| BulletType   | bullet, b   | The type of the bullet. If set, additional attributes becomes available depending on the specified bullet type. A list of bullet types and associated attributes is available [below](/skills/mechanics/projectile#projectile-bullets)                                       | <!--type:Projectile_BulletType-->|
| Interval  | int, i      | How often (in ticks) the projectile updates its position           | 1       |
| HorizontalRadius | hRadius, hR, r | The horizontal radius entities 将会 hit in around the projectile.                                                                                                                                    | 1.25    |
| VerticalRadius   | vRadius, vR | The vertical radius entities 将会 hit in around the projectile.                                                                                                                                      | 1.25    |
| Duration  | maxDuration, md, d | The max duration (in ticks) the projectile will persist.    | 400     |
| MaxRange  | mr        | The maximum range (in blocks) the projectile will travel.            | 40      |
| Velocity  | v         | The velocity of the projectile, expressed in blocks traveled per second| 5     |
| DeathDelay| death, dd | Delays the removal of project bullets when the projectile is terminated | 2    |
| StartYOffset | syo    | Lets you offset where on the casting mob the projectile shoots from. | 1       |
| StartFOffset | forwardoffset, sfo |  How far in front of the mob the projectile starts       | 1       |
| TargetYOffset | tyo, targety | Lets you offset where on the target the projectile shoots at. | 0       |
| SideOffset | soffset, so | The value of this attribute gets inherited by StartSideOffset and EndSideOffset if no value is specified for them                                                | 0       |  
| StartSideOffset | ssoffset, sso | How far to the side of the mob the projectile starts      |sideoffset|
| EndSideOffset | endoffset, esoffset, eso | How far to the side of the target location the projectile will end up                                                                                   |sideoffset|
| startingdirection | startingdir, startdir, sdir | Start direction of the projectile. For now, it only works if inherited by a missile 机制                                                      |@Targeted<!--type:Targeter-->|
| HorizontalOffset | hO | Horizontal Offset will rotate the projectile's horizontal starting velocity around a 360-degree axis                                                                      | 0        |
| VerticalOffset   | vO | Vertical Offset will add a [slope](https://en.wikipedia.org/wiki/Grade_(slope)) to the projectile's starting direction. To give it a specific angle, you can use [this image](https://en.wikipedia.org/wiki/Grade_(slope)#/media/File:Slope_quadrant.svg) as reference: the value you need 将会 the number shown in red divided by 100 (so if you want 40°, you will need to input 83.9/100 = `0.839`)| 0        |
| Accuracy  | ac, a     | Determines the accuracy of the projectile                           | 1        |
| HorizontalNoise | hn  | The randomness of the projectile in horizontal direction            |(1-ac)*45 |
| VerticalNoise   | vn  | The randomness of the projectile in the vertical direction          |(1-ac)*4.5|
| StopAtEntity | sE     | Whether the projectile will stop upon hitting a targetable entity   | true     |
| StopAtBlock  | sB     | Whether the projectile will stop upon hitting an opaque block       | true     |
| PowerAffectsRange | par | Whether a mob's [power level](/Mobs/Power) affects the projectile's range| true|
| PowerAffectsVelocity | pav | Whether a mob's [power level](/Mobs/Power) affects the projectile's velocity.                                                                                     | true     |
| Interactable |        | Whether the projectile is interactable                              | false    |
| HitSelf   |           | Whether the projectile can hit the caster                           | false    |
| HitPlayers | hp       | Whether the projectile can hit players                              | true     |
| HitNonPlayers | hnp   | Whether the projectile can hit non player entities                  | false    |
| HitTarget | ht        | Whether the projectile can hit the 机制's target                | true     |
| HitTargetOnly | hto   | Whether the projectile can **only** hit the 机制's target       | false    |
| ImmuneDelay | immune, id | Sets the immunity delay (when the target 可以 hit by the projectile again) | 2000  |
| hitConditions | conditions, cond, c | A list of conditions that a target must meet in order 对于projectile 能够击中它. **Premium Only** Mechanic  |<!--type:Conditions-->|
| stopconditions | stpcond | A list of conditions that a target must meet in order 对于projectile to end 当击中它们时                                                                         | null     |
| doEndSkillOnHit | esoh | Whether the onEnd metaskill 应当 run when the projectile ends by hitting an entity | true |
| fromorigin | fo       | Whether the projectile should start from the origin of the 机制 | false    |
| requireLineOfSight | rlos, los, requirelos | Whether the starting point must have line-of-sight to the origin.  Values 可以 `true`, `false`, `PLAYERS_ONLY`                                             | PLAYERS_ONLY<!--type:Projectile_HighAccuracyMode-->|
| drawHitbox |          | Draw the hitbox of the projectile, useful for debugging             | false    |
| tickinterpolation | interpolation, ti | Interpolates the specified amount of additional points between each tick of the projectile. The onTick and onHit skills 将会 applied there as well. Useful to fill in the gaps with super-fast projectiles and also prevent entities from being "skipped over"      | 0        |
| shareSubHitboxCooldown | shcd | Whether all meg sub hitboxes should share the same immune delay with its base entity | true | 
| hitTargeter | htr     | An entity targeter. Once the projectile hits, targeted entities 将会 targeted by the onHit Metaskill and given immune delay just like the projectile's main target          | <!--type:Targeter--> |

### 弹射物专属属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| Type      |           | The "type" of projectile. Default projectiles are launched from the mob's location towards the target. METEOR type projectiles fall from the sky above the target.       | NORMAL<!--type:Projectile_Type-->|
| gravity   | g         | Determines the gravity of the projectile; use fractions (0.1-0.2) for low gravity                                                                                        | 0       |
| Bounces   | bounce    | Should the projectile bounce. Bounce radius depends on the projectile's hitbox. **Premium Only**.                                                                              | false   |
| BounceVelocity | bv   | Every time the projectile bounces, its velocity 将会 multiplied by this value. **Premium Only** .                                                                      | 0.9     |
| HugSurface| hs        | Whether or not the projectile should move along the ground.          | false   |
| HugLiquid | hugwater, huglava | when using hugSurface will also move on top of liquids       | false   |
| HeightFromSurface| hfs| For NORMAL projectiles, how high above the surface the projectile should glide if HugSurface is set to TRUE. For METEOR projectiles, how high above the surface the projectile starts above the target.                                                                              | 0.5     |
| MaxClimbHeight | mch  | The number of attempts the projectile will make to **increase** its y-location before terminating itself, when the projectiles is "hugging" either a block or a liquid        | 3       |
| MaxDropHeight  | mdh  | The number of attempts the projectile will make to **decrease** its y-location before terminating itself, when the projectiles is "hugging" either a block or a liquid        | 10      |
| highAccuracyMode | ham| Whether to use high-accuracy mode, which raytraces every tick to ensure the projectile cannot ever go through anything. Values 可以 `true`, `false`, `PLAYERS_ONLY`         | PLAYERS_ONLY<!--type:Projectile_HighAccuracyMode-->|


## Special Notes

**For the <u>onStart</u> Skill:** onStart skills work in a special way -
any buff or "special effect" 机制s fired by onStart that have a
duration (such as ParticleTornado) will attach to the projectile for
their duration, which allows for some interesting effects.

**For the <u>onTick</u> Skill:** using the **@origin** targeter will
cause any skills or effects to target the projectile's location. This is
the intended way to configure how the projectile looks.

**For the <u>onHit</u> Skill:** Any targets the projectile hits are
passed to the skill inherently. Any targeters you put in the onHit skill
will *override* these and cause your skill to likely not work as you
intend.

**For the <u>onEnd</u> Skill:** Special effects 对于projectile's end
also use **@origin**. Also, If you want entities near the end-point of
the projectile to be hit in a certain way (such as a final large
fireball explosion) you can use the **@PlayersNearOrigin{r=[radius]}**
targeter.

**Types:**  
There are two types of projectiles, the normal variant and also the
Meteor variant.  
Meteor projectiles are created above the target, rather than 在mob
that is firing the projectile.  
Because of this, meteor projectiles cannot use certain attributes (which
ones are pending further testing).


## Projectile Bullets

The bullet type that will represent the projectile. These 可以 specified via the BulletType attribute.
These work with the projectile, missile, and orbital 机制s.

| BulletType  | Aliases      | Description                                                               |
|-------------|--------------|---------------------------------------------------------------------------|
| [ARROW][]   |              | The bullet 将会 a minecraft projectile                                 |
| [BLOCK][]   |              | The bullet 将会 a block                                                |
| [SMALLBLOCK][]|            | The bullet 将会 a small block                                          |
| [ITEM][]    | MYTHICITEM   | The bullet 将会 an item or MythicItem                                  |
| [MOB][]     |              | The bullet 将会 a mob. If a Mythicmobs, it will retain its skills      |
| [TRACKING][]| ARMOR_STAND, ARMORSTAND, PSTAND | The bullet 将会 an item, but its rotation 将会 adjusted depending on the projectile's direction                                                         |
| [REALTRACKING][] | RTRACKING, REAL_ARMOR_STAND, REALARMORSTAND, STAND | As above, but a real armor stand will also be spawned instead of a packet |
| [DISPLAY][] |              | The projectile 将会 a display entity                                   |
| [TEXT][]    |              | The projectile will display a line of text                                |
| [ME][]      | MEG, MODELENGINE | The projectile 将会 a [ModelEngine] model                          |

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
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletforwardoffset | bulletfo, bulletoffset, bfo | 子弹的偏移量                 | 1.8     |
| bulletYOffset | byo   | 子弹的 Y 偏移量                                           | 0       | 

### ARROW Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| arrowtype | bulletarrowtype | 要使用的弹射物类型. 可以为 `NORMAL`、`SPECTRAL`、`TRIDENT` | NORMAL<!--type:NORMAL,SPECTRAL,TRIDENT--> |

### BLOCK Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet                                  | STONE<!--type:Block--> |
| bulletspin | bspin    | The spin of the bullet                                               | 0       |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### SMALLBLOCK Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet                                  | STONE<!--type:Material--> |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### ITEM Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet, either a vanilla item type or custom MythicItem    | STONE<!--type:Item-->  |
|bulletModel| model     | The CustomModelData integer 对于material (建议改用 MythicItem 定义模型字符串)   | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletmatchdirection | bmd, bulletsmall | 子弹是否应面向弹射物的朝向 | false |
| bulletEnchanted | enchanted | 材料是否应附魔                               | false   |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### MOB Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mob       | mobType, mm | The mob of the bullet                         | SkeletalKnight<!--type:Mob-->|
| bulletspin | bspin    | The spin of the bullet                                               | 0       |
| bulletmatchdirection | bmd | 子弹是否应面向弹射物的朝向           | false   |
| bulletKillable | bk   | 允许其他实体伤害弹射物子弹                 | false   |
| bulletYOffset| byo | 子弹的 Y 偏移量 mob                                          | 1.35    | 
| bulletForwardOffset| bfo| The forward offset of the bullet mob                               | 1.35    | 

### TRACKING Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet, 可以 vanilla item type or MythicItem     | STONE<!--type:Item--> |
|bulletModel| model     | The CustomModelData integer 对于material (建议改用 MythicItem 定义模型字符串)  | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletEnchanted | enchanted | 材料是否应附魔                               | false   |
| pitch     |           | 俯仰旋转（弧度）                                       | 0       |
| yaw       |           | 偏航旋转（弧度）                                         | 0       |
| roll      |           | 翻滚旋转（弧度）                                        | 0       |
| rotation  | rot       | 子弹的旋转（弧度）, in the x,y,z format           | 0,0,0   |
| pitchspeed| ps        | 俯仰旋转速度                                             | 0       |
| yawspeed  | ys        | 偏航旋转速度                                               | 0       |
| rollspeed | rs        | 翻滚旋转速度                                              | 0       |
| rotationspeed | rotspeed, rots | 子弹的旋转速度, in the x,y,z format      | 0,0,0   |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |

### REALTRACKING Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat | The material of the bullet, 可以 vanilla item type or MythicItem | STONE<!--type:Item--> |
|bulletModel| model     | The CustomModelData integer 对于material (建议改用 MythicItem 定义模型字符串) | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletEnchanted | enchanted | 材料是否应附魔                               | false   |

### DISPLAY Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletmaterial | material, mat, bulletitem | The material of the bullet, 可以 vanilla item type or MythicItem  | STONE<!--type:Item--> |
|bulletModel| model     | The CustomModelData integer 对于material (建议改用 MythicItem 定义模型字符串) | 0       |
|bulletColor|           | The color of the material, if applicable                             |         |
| bulletEnchanted | enchanted | 材料是否应附魔                               | false   |
|bulletscale| scale     | 子弹的缩放                                            |0.5,0.5,0.5|
| bulletyoffset | byoffset, byo | The y offset of the bullet                                   | 0.2     |
| bulletBillboarding | bulletBillboard | 子弹的[公告牌类型]                    | FIXED   |
| bulletbrightness | bulletbrightnessblock | 子弹的亮度                           | -1      |
| bulletbrightnesssky | | 子弹的天空光亮度                           | bulletbrightness |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | The range in which the bullet 将会 visible                                                                                        | 50      |
| pitch     |           | 俯仰旋转（弧度）                                       | 0       |
| yaw       |           | 偏航旋转（弧度）                                         | 0       |
| roll      |           | 翻滚旋转（弧度）                                        | 0       |
| rotation  | rot       | 子弹的旋转（弧度）, in the x,y,z format           | 0,0,0   |
| pitchspeed| ps        | 俯仰旋转速度                                             | 0       |
| yawspeed  | ys        | 偏航旋转速度                                               | 0       |
| rollspeed | rs        | 翻滚旋转速度                                              | 0       |
| rotationspeed | rotspeed, rots | 子弹的旋转速度, in the x,y,z format       | 0,0,0   |
| tx        |           | x 轴平移                                        | 0       |
| ty        |           | y 轴平移                                        | 0       |
| tz        |           | z 轴平移                                        | 0       |
| translation | pos, offset | 各轴的平移, in the x,y,z format                | 0,0,0   |
| hideFirstTick | hft   | Hides the item 对于first tick                                    | false   |
| bulletCullingHeight | cullHeight | 子弹的展示剔除高度                       | 0.0     |
| bulletCullingWidth | cullWidth | 子弹的展示剔除宽度                          | 0.0     |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |
| bulletgen | generation, bulletgeneration | If MythicCrucible is installed, the generation option 对于bullet item |

### ME Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletModel | model   | The MEG model to use 对于bullet                                  |         |
| bulletstate | state   | The state to play 对于MEG model                                  |         |
| bulletcolor |         | 子弹模型的色调                                       |         |
| bulletscale |         | 子弹的缩放                                              | 1       |
| bulletEnchanted | enchanted | Whether the bullet's model 应当 enchanted                 | false   | 
| bulletGlowing | glowing | Whether the bullet's model 应当 glowing                       | false   |
| bulletglowcolor |     | 子弹的发光颜色，前提是 `bulletGlowing` 设为 true      |         |
| bulletCulling  | culling | Whether to apply culling 对于bullet model                     | true    |
| bulletViewRadius |    | From how far the bullet 可以 seen, if greater than 0.              | -1      |

### TEXT Bullet
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bulletText| text      | 子弹的文本                                               | *       |
| bulletBillboard | billboard | 子弹的[公告牌类型]                             | CENTER<!--type:Billboard-->|
|bulletscale| scale     | 子弹的缩放                                            |0.5,0.5,0.5|
| forcedBulletRotation  | forcedRotation | 使用指定的俯仰、偏航和翻滚强制旋转子弹，格式为 x,y,z。留空则允许子弹根据移动方向动态旋转 |   |
| bulletRotatesBasedOnDirection | | 文本子弹是否应根据移动方向旋转。可能*不是*你预期的效果 | false |
| bulletyoffset | byoffset, byo | The y offset of the bullet                                   | 0       |
| bulletforwardoffset | bulletfo, bulletoffset, bfo | The forward offset of the bullet         | 1.8     |
| backgroundcolor | color | 背景颜色，ARGB 格式                          | 64,0,0,0 |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | The range in which the bullet 将会 visible                                                                                        | 50      |
| bulletCullingHeight | cullHeight | 子弹的展示剔除高度                       | 0.0     |
| bulletCullingWidth | cullWidth | 子弹的展示剔除宽度                          | 0.0     |
| bulletBrightness | bulletBrightnessBlock | 子弹的亮度, if the value is > -1     | -1      |
| bulletBrightnessSky| |子弹的天空光亮度, if the value is > -1                | -1      |
| audience  |           | The [Audience][] of the bullet                                       | world<!--type:Audience--> |


## 示例

This example shoots a fast-moving ball of ice that damages and slows the
first entity it hits:  
**Mob File**  
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
hitConditions usage example:
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
