## 描述
Applies an 光环 to the 目标 that 触发 a skill when they swing (left click)


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onSwing   | onswingskill, osw | Skill to 执行 if the 目标 swings / left clicks          |<!--type:Metaskill-->|

> This 技能 继承 [光环] 技能


## 示例
Simple:

Apply an onSwing 光环 to yourself and catch any entities in front and within 10 blocks of you on fire.
```yaml
ApplyAura:
  Skills:
  - onSwing{osw=CatchOnFire;auraname=Ignite;d=300;i=1} @self
CatchOnFire:
  Skills:
  - ignite{t=60} @EntitiesInCone{angle=90;range=10;rotation=0}
```

##

Intermediate:

Apple on onSwing 光环 to yourself that shoots out a 弹射物 whenever you swing. It will play the skeleton shoot sound when the 弹射物 spawns, have flame 粒子 and a firecharge while it travels, and will deal between 2-4 MAGIC damage. 

```yaml
ApplyAura:
  Skills:
  - onSwing{osw=ShootProjectile;auraname=Fireballs;d=300;i=1} @self
ShootProjectile:
  Skills:
  - projectile{bulletType=ITEM;material=FIRE_CHARGE;bulletSpin=29;i=1;v=24;mr=100;d=100;hnp=true;oS=Fireball_oS;oT=Fireball_oT;oH=Fireball_oH} @forward{f=300;y=0}
Fireball_oS:
  Skills:
  - sound{s=entity.skeleton.shoot;v=1;p=1} @origin
Fireball_oT:
  Skills:
  - particles{particle=flame;a=4;hs=0.2;vs=0.2;y=0;s=0.1} @origin
Fireball_oH:
  Skills:
  - damage{a=2-4;cause=magic}
```


## 别名
- [x] onleftclick


<!-- LINKS -->
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
