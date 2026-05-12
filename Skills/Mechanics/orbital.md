## 描述

The Orbital skill fires a special type of
[弹射物](/skills/技能/弹射物) that will orbit around the
目标 and can also act as an [光环](/skills/技能/光环), inheriting all of its attributes. Like the
弹射物, it will 触发 other skills on anyone that is hit by it
during its orbit.  
Much like 弹射物, it's great for creating complex skills, such as a
fire 护盾, and is a very complex skill to master.  

Added 弹射物 bullets to Orbital in MM 4.11. See how to use them on the [弹射物 技能](/skills/技能/弹射物) page.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onHit     | oH, onhitskill | Meta-Skill executed when the 弹射物 hits something. 目标 hit are inherited by the meta-skill                                                                    |<!--type:Metaskill-->|
| 半径    | r         | The 半径 of the orbit around the 目标                            | 4       |
| hitRadius | hr        | The 半径 around the orbital in which 目标 can be hit            | 1       |
| verticalHitRadius | vhr, vr | The y component of the hitradius                           | `hitradius` |                                                                                                                       
| points    | p         | How many "points" that comprise the circle that makes up the orbit. More points will make the circle more defined, but will also increase the time it takes to complete an orbit  | 32   |
| startingpoint | sp    | The starting step of the orbital 光环                                | 0       |
| tickinterpolation | interpolation, ti | Interpolates additional points between each tick of the 弹射物, running onTick multiple times                                                      | 0       |
| rotationx | rotx, rx  | Rotates the orbital along the X axis. Rotation is done in radians, 即 `3.14` is half a rotation, `6.28` is a full rotation                                                  | 0       |
| rotationy | roty, ry  | Rotates the orbital along the Y axis. Rotation is done in radians, 即 3.14 is half a rotation, 6.28 is a full rotation                                                       | 0       |
| rotationz | rotz, rz  | Rotates the orbital along the Z axis. Rotation is done in radians, 即 3.14 is half a rotation, 6.28 is a full rotation                                                       | 0       |
| offsetx   | ox, offx  | Offsets the orbital along the X axis of the 目标                   | 0       |
| offsety   | oy, offy  | Offsets the orbital along the Y axis of the 目标                   | 0       |
| offsetz   | oz, offz  | Offsets the orbital along the Z axis of the 目标                   | 0       |
| angularVelocityX | avx, vx | Modifies the angular 速度 of the orbital on the X axis      | 0       |
| angularVelocityY | avy, vy | Modifies the angular 速度 of the orbital on the Y axis      | 0       |
| angularVelocityZ | avz, vz | Modifies the angular 速度 of the orbital on the Z axis      | 0       |
| rotate    |           | 是否 the orbital should rotate                                    | true    |
| reversed  | reverse, backwards | 是否 the orbital should rotate in the opposite direction | false   |
| hitPlayers       | hp | 是否 can hit players                                              | true    |
| hitNonPlayers    | hnp| 是否 can hit non players                                          | false   |
| hitSelf          | hs | 是否 can hit 施法者                                               | false   |
| hugsurface       | hs      | 是否 the orbital should move along the ground         | false   |
| hugliquid        | hugwater, huglava | 是否 using `hugSurface` will also make the orbital move on top of liquids                                                                                     | false   |
| heightfromsurface | hfs    | How high above the surface the orbital should glide if `HugSurface` is set to `true`                                                                                      | 0.5     |
| maxclimbheight   | mch     | The number of attempts the 弹射物 will make to **increase** its y-location by 1 before terminating itself, when 弹射物的 is "hugging" either a block or a liquid| 3 |
| maxdropheight | mdh        | The number of attempts the 弹射物 will make to **decrease** its y-location by 1 before terminating itself, when 弹射物的 is "hugging" either a block or a liquid| 10|
| bullettype    | bullet, b  | The [弹射物 Bullet Type](/skills/技能/弹射物#弹射物-bullets). Also makes the orbital inherits every related attribute                               | NONE<!--type:Projectile_BulletType-->|
| castAsOrbital | cao        | 是否 the metaskills should be casted by the orbital itself rather than from the 施法者, as 弹射物 do                                                              | false  |
| immunedelay | immune, iD | Sets the immunity delay (when the 目标 can be hit by the 弹射物 again) | 2000 |
| drawhitbox |  | Draw the hitbox of the orbital, useful for debugging | false |
| hit条件 | 条件, cond, c | A list of 条件 that a 目标 must meet in order for the orbital to be able to hit it. **Premium Only** 技能 | <!--type:条件--> |
| stop条件 | stpcond | A list of 条件 that a 目标 must meet in order for the orbital to end when hitting them | <!--type:条件--> |
| hitTargeter | htr     | An entity targeter. Once the orbital hits, targeted entities will be targeted by the onHit Metaskill and given immune delay just like the orbital's main 目标          | <!--type:Targeter--> |
| shareSubHitboxCooldown | shcd | 是否 all meg sub hitboxes should share the same immune delay with its base entity | true | 


> This 技能 继承 [光环](/skills/技能/光环) 技能
  

### onStart Attribute
onStart skills work in a special way - any buff or "special effect" 技能 fired by onStart that have a
duration (such as ParticleTornado) will attach to the 弹射物 for their duration, which allows for some interesting effects.

### onTick Attribute
Using the **@原点** targeter will cause any skills or effects to 目标 弹射物的 location. This is the intended way to configure how the 弹射物 looks.

### onHit Attribute
Any 目标 the 弹射物 hits are passed to the skill inherently. Any targeters you put in the onHit skill will *override* these and cause your skill to likely not work as you intend.

### onEnd Attribute
Special effects for 弹射物的 end also use **@原点**. Also, If you want entities near the end-point of the 弹射物 to be hit in a certain way (such as a final large fireball explosion) you can use the **@PlayersNearOrigin{r=[半径]}** targeter.


## 示例
This example puts an icy-looking orbital 护盾 around the 生物 when it
is hit sometimes, that will last for 10 seconds or until it is triggered
once:  
```yaml
# Mob File
Mob:
  Type: SKELETON
  Skills:
  - skill{s=IceShield} @self ~onDamaged 0.2
```
```yaml
# Skills File
IceShield:
  Skills:
  - orbital{onTick=IceShield-Tick;onHit=IceShield-Hit;points=20;interval=1;duration=200;charges=1}
IceShield-Tick:
  Skills:
  - effect:particles{p=snowballpoof;amount=20;speed=0;hS=0.2;vS=0.2} @origin
IceShield-Hit:
  Skills:
  - damage{a=10}
  - potion{type=SLOW;duration=100;lvl=2}
```

##

This example shows how the orbital can be removed via the [Auraremove](`auraremove`) 技能.
<br>The 生物 `Example生物` create the 护盾 from the previous example once it gets damaged with a 20% chance, but unlike the previous example this time the orbital also has an auraName attribute. When the 生物 receives a REMOVESHIELD signal, he will both remove the orbital via the auraremove 技能 and the orbital's auraName while also sending a SHIELDREMOVED signal back to the 触发 of the metaskill

```yaml
# Mob File
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=IceShield} @self ~onDamaged 0.2
  - skill{s=IceShield-Remove} @self ~onSignal:REMOVESHIELD
```

```yaml
# Skills File
IceShield:
  Skills:
  - orbital{
    auraName=IceShield;
    onTick=IceShield-Tick;onHit=IceShield-Hit;points=20;interval=1;duration=200;charges=1}

IceShield-Remove:
  Skills:
  - auraremove{aura=IceShield}
  - signal{s=SHIELDREMOVED} @trigger
```


## 别名
- [x] o


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:Projectile-->
