## 描述
Terminates the 弹射物 this 技能 has been called from, activating its onEnd skill in the process.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 条件| 条件, cond, con | The 条件 to check before terminating the 弹射物 |<!--type:条件-->|

##Examples

**生物 file**
```yaml
Mob:
  Type: HUSK
  Skills:
  - skill{s=ExplodingProjectile} @target ~onTimer:20
  - aura{auraName=explode;d=2} @self ~onTimer:200
```

**Skill file**
```yaml
ExplodingProjectile:
  Skills:
  - projectile{onTick=ExplodingProjectile_Tick;onEnd=ExplodingProjectile_End;v=4;i=1;hp=false;sb=false;se=false;d=200}
ExplodingProjectile_Tick:
  Skills:
  - effect:particles{p=flame;amount=20;speed=0;hS=0.2;vS=0.2} @origin
  - sound{s=entity.blaze.burn;v=0.5} @origin
  - damage{a=2} @EntitiesNearOrigin{r=2}
  - endprojectile ?hasaura{auraName=explode}
ExplodingProjectile_End:
  Skills:
  - damage{a=20} @EntitiesNearOrigin{r=5}
  - throw{fromorigin=true} @EntitiesNearOrigin{r=5}
  - effect:explosion @origin
```


## 别名
- [x] terminateProjectile
- [x] terminateproj
- [x] endproj
- [x] stopprojectile
- [x] stopproj


<!--TAGS-->
<!--tag:Meta-->
