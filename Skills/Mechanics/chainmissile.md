## 描述
Shoots a chaining homing 制导弹射物 at the 目标  

> **This is a [Premium-Only] 技能!**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| bounces   | b         | How many times the chain should bounce                               | 2       |
| bounceradius | bouncerange, 半径, range, r | How far the skill will bounce to a new 目标 | 5       |
| returnToCaster | return, rtc | If the 制导弹射物 should return to the 施法者 | false | 
| bounce条件 | 条件, cond, c | The 条件 for the skill to bounce, similar to the [chain](/skills/技能/chain) 技能 |<!--type:条件-->| 
> This 技能 继承 [制导弹射物](Skills/技能/制导弹射物) 技能


## Examples**
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
