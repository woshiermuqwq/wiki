## 描述
Shoots a chaining homing missile 在target  

> **This is a [Premium-Only] 技能!**


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bounces   | b         | How many times the chain should bounce                               | 2       |
| bounceradius | bouncerange, radius, range, r | How far the skill will bounce to a new target | 5       |
| returnToCaster | return, rtc | If the missile should return to the caster | false | 
| bounceConditions | conditions, cond, c | The conditions 对于skill to bounce, similar to the [chain](/skills/mechanics/chain) 技能 |<!--type:Conditions-->| 
> 此技能继承所有[Missile](Skills/Mechanics/Missile) 技能


## 示例
**
```yaml
## Mob.yml ##
Skills:
- skill{s=ChainMissile} @target ~onTimer:200
```
```yaml
## Skills.yml ##
ChainMissile:
  Skills:
  - ChainMissile{bounces=10;r=10;in=1.25;oT=CM_oT;oH=CM_oH;i=1;md=200;mr=30;v=5;hnp=true;hp=true;hR=1;vR=1;sB=False;sE=false;tyo=1;hs=true;hfs=1}
CM_oT:
  Skills:
  - effect:particles{particle=flame;a=1;hs=0;vs=0;s=0;y=0} @origin
CM_oH:
  Skills:
  - damage{a=1;pkb=true}
```


## 别名
- [x] cmi


<!-- LINKS -->
[Premium-Only]: Premium-Features


<!--TAGS-->
<!--tag:Meta-Mechanic-->
<!--tag:Projectile-->
<!--tag:Premium-Only-->
