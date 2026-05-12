## 描述
The 制导弹射物 技能 is similar to the 弹射物 技能 and can use any of the [弹射物's Inheritable Attributes](/skills/技能/弹射物#inheritable-attributes).  
制导弹射物 however are homing and will track down their 目标.
制导弹射物 can 目标 both a location and an entity.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| Inertia   | in, intertia | Sets the "turning-rate" of the 制导弹射物. Lower values make the 制导弹射物 turn around faster. Use big numbers (10-100) when trying to make your 制导弹射物 turn slowly.         | 1.5     |
| Bounces   | bounce    | Should the 弹射物 bounce. Bounce 半径 depends on 弹射物的 hitbox. **Premium Only**.                                                                              | false   |
| BounceVelocity | bv   | Every time the 弹射物 bounces, its 速度 will be multiplied by this value. **Premium Only** .                                                                      | 0.9     |
| startWithParentVelocity | swpv, spv | 是否 the 制导弹射物, if called from another 弹射物, should start with the same 速度 as the parent 弹射物                                          | false   |
| HugSurface| hs        | 是否 the 弹射物 should move along the ground.          | false   |
| HugLiquid | hugwater, huglava | when using hugSurface will also move on top of liquids       | false   |
| HeightFromSurface| hfs| For NORMAL 弹射物, how high above the surface the 弹射物 should glide if HugSurface is set to TRUE. For METEOR 弹射物, how high above the surface the 弹射物 starts above the 目标.                                                                              | 0.5     |
| MaxClimbHeight | mch  | The number of attempts the 弹射物 will make to **increase** its y-location before terminating itself, when 弹射物的 is "hugging" either a block or a liquid        | 3       |
| MaxDropHeight  | mdh  | The number of attempts the 弹射物 will make to **decrease** its y-location before terminating itself, when 弹射物的 is "hugging" either a block or a liquid        | 10      |
| highAccuracyMode | ham| 是否 to use high-accuracy mode, which raytraces every tick to ensure the 弹射物 cannot ever go through anything. Values can be `true`, `false`, `PLAYERS_ONLY`         | PLAYERS_ONLY<!--type:Projectile_HighAccuracyMode-->|
| hitnonplayers | hnp   | 是否 the 制导弹射物 should hit non player entities                   | true    |

> This 技能 继承 [弹射物](/skills/技能/弹射物#inheritable-attributes) 技能
>> - The `hitnonplayers ` attribute is **defaulted** at `true`


## 示例
This example shoots a 制导弹射物 that looks like a thin trail of flames
with a high turning rate. It bursts into a powerful explosion upon
hitting its 目标.
```yaml
# Mob File
Mob:
  Type: ZOMBIE
  Skills:
  - skill{s=Homer} @target ~onTimer:100
```
```yaml
# Skills File
Homer:
  Skills:
  - missile{ot=Homer_TICK;oh=Homer_HIT;v=4;i=1;hR=1;vR=1;in=0.75}

Homer_TICK:
  Skills:
  - effect:particles{p=flame;a=1} @origin

Homer_HIT:
  Skills:
  - effect:particles{p=lava;a=50;hS=1;vS=1}
  - effect:sound{s=entity.generic.explode;v=1;p=0}
  - damage{a=1337;i=false}
```


## 别名
- [x] mi


<!--TAGS-->
<!--tag:Projectile-->