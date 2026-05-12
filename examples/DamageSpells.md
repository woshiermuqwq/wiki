单体目标火焰
---------------------
* 基础版
```yaml
SingleTargetFire:
  Cooldown: 1
  Skills:
  - effect:particles{p=flame;hs=1;vs=1;a=50;s=0.01;} @target  
  - damage{a=6;ignorearmor=true;}
  - ignite{d=60;}
```
* 进阶版：施法时间，生物停下施法
```yaml
SingleTargetFire:
  Cooldown: 1
  Skills:
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=40;level=7;} @self
  - delay 40
  - message{m="<target.name> &e燃烧起来。"} @PIR{r=20}
  - effect:particles{p=largesmoke;vs=1;hs=1;a=50;s=0.01;}
  - effect:particles{p=flame;hs=1;vs=1;a=50;s=0.01;} @target
  - effect:particles{p=explode;vs=1;hs=1;a=50;s=0.01;}
  - effect:sound{s=entity.ghast.fireball;v=1;p=1;}
  - damage{a=6;ignorearmor=true;}
  - ignite{d=60;}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
SingleTargetFire:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD{t=40}
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=40;level=7;} @self
  - delay 40
  - message{m="<target.name> &e燃烧起来。"} @PIR{r=20}
  - effect:particles{p=largesmoke;vs=1;hs=1;a=50;s=0.01;}
  - effect:particles{p=flame;hs=1;vs=1;a=50;s=0.01;} @target
  - effect:particles{p=explode;vs=1;hs=1;a=50;s=0.01;}
  - effect:sound{s=entity.ghast.fireball;v=1;p=1;}
  - damage{a=6;ignorearmor=true;}
  - ignite{d=60;}
```
AOE 火焰
------------------------
* 基础版
```yaml
AOEFire:
  Cooldown: 1
  Skills:
  - effect:particles{p=flame;hs=10;vs=1;a=1000;s=0.01;} 
  - damage{a=6;ignorearmor=true;} @PIR{r=10}
  - ignite{d=60;} @PIR{r=10}
```
* 进阶版：施法时间，生物停下施法
```yaml
AOEFire:
  Cooldown: 1
  Skills:
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=80;level=7;}
  - delay 80
  - message{m="<target.name>&e 燃烧起来。"} @PIR{r=20}
  - effect:particles{p=reddust;hs=10;vs=1;a=1000;s=0.01;}
  - effect:particles{p=flame;hs=10;vs=1;a=1000;s=0.01;}
  - effect:sound{s=entity.ghast.fireball;v=1;p=1;}
  - damage{a=6;ignorearmor=true;} @PIR{r=10}
  - ignite{d=60;} @PIR{r=10}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
AOEFire:
  Cooldown: 1
  Conditions:
  - targetwithin 20
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=80;level=7;}
  - delay 80
  - message{m="<target.name>&e 燃烧起来。"} @PIR{r=20}
  - effect:particles{p=reddust;hs=10;vs=1;a=1000;s=0.01;}
  - effect:particles{p=flame;hs=10;vs=1;a=1000;s=0.01;} @self
  - effect:sound{s=entity.ghast.fireball;v=1;p=1;}
  - damage{a=6;ignorearmor=true;} @PIR{r=10}
  - ignite{d=60;} @PIR{r=10}
```
单体目标冰霜
---------------------
* 基础版
```yaml
SingleTargetFrost:
  Cooldown: 1
  Skills:
  - effect:particles{p=splash;vs=1;hs=1;a=100;s=0.01}
  - effect:sound{s=block.fire.extinguish;v=2;p=1;}
  - damage{a=3;i=true;}
  - potion{type=SLOW;d=60;level=3;} 
```
* 进阶版：施法时间，生物停下施法
```yaml
SingleTargetFrost:
  Cooldown: 1
  Skills:
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=40;level=7;} @self
  - delay 40
  - message{m="<target.name>&e 被冻结了。"} @PIR{r=20}
  - effect:particles{p=splash;vs=1;hs=1;a=100;s=0.01}
  - effect:sound{s=block.fire.extinguish;v=1;p=1;}
  - damage{a=3;i=true;}
  - potion{type=SLOW;d=60;level=3;} 
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
SingleTargetFrost:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD{t=40}
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=40;level=7;} @self
  - delay 40
  - message{m="<target.name>&e 被冻结了"} @PIR{r=20}
  - effect:particles{p=splash;vs=1;hs=1;a=100;s=0.01}
  - effect:sound{s=block.fire.extinguish;v=1;p=1;}
  - damage{a=3;i=true;}
  - potion{type=SLOW;d=60;level=3;} 
```
AOE 冰霜
--------------
* 基础版
```yaml
AOEFrost:
  Cooldown: 1
  Skills:
  - effect:particles{p=splash;hs=5;vs=1;a=5000;s=0.01;y=1}
  - effect:sound{s=block.fire.extinguish;v=2;p=1;}
  - damage{a=6;ignorearmor=true;} @PIR{r=10}
  - potion{type=SLOW;d=60;level=3;} @PIR{r=10}
```
* 进阶版：施法时间，生物停下施法
```yaml
AOEFrost:
  Cooldown: 1
  Skills:
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 被冻结了"} @PIR{r=20}
  - effect:particles{p=splash;hs=5;vs=1;a=5000;s=0.01;y=1}
  - effect:sound{s=block.fire.extinguish;v=2;p=1;}
  - damage{a=6;ignorearmor=true;} @PIR{r=10}
  - potion{type=SLOW;d=60;level=3;} @PIR{r=10}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
AOEFrost:
  Cooldown: 1
  Conditions:
  - targetwithin 20
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 被冻结了"} @PIR{r=20}
  - effect:particles{p=splash;hs=5;vs=1;a=5000;s=0.01;y=1}
  - effect:sound{s=block.fire.extinguish;v=2;p=1;}
  - damage{a=6;ignorearmor=true;} @PIR{r=10}
  - potion{type=SLOW;d=60;level=3;} @PIR{r=10}
```
单体目标闪电
----------------------
* 基础版
```yaml
SingleTargetLightning:
  Cooldown: 1
  Skills: 
  - lightning{d=5;}
  - delay 5
  - effect:particles{p=fireworksSpark;vs=1;hs=1;a=100;s=1;}
```
* 进阶版：施法时间，生物停下施法
```yaml
SingleTargetLightning:
  Cooldown: 1
  Skills: 
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=60;level=7;} @self
  - delay 60
  - lightning{d=5;}
  - message{m="<target.name>&e 被电击了。"} @PIR{r=20}
  - delay 5
  - effect:smoke @target
  - effect:particles{p=fireworksSpark;vs=1;hs=1;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=1;a=500;s=0.01;}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
SingleTargetLightning:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD{t=60}
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=60;level=7;} @self
  - delay 60
  - lightning{d=5;}
  - message{m="<target.name>&e 被电击了。"} @PIR{r=20}
  - delay 5
  - effect:smoke @target
  - effect:particles{p=fireworksSpark;vs=1;hs=1;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=1;a=500;s=0.01;}
```
AOE 闪电
----------------
* 基础版
```yaml
AOELightning:
  Cooldown: 1
  Skills: 
  - lightning{d=18;} @PIR{r=10}
  - delay 5
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
```
* 进阶版：施法时间，生物停下施法
```yaml
AOELightning:
  Cooldown: 1
  Skills: 
  Cooldown: 1
  Skills: 
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 被电击了。"} @PIR{r=20}
  - lightning{d=18;} @PIR{r=10}
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
AOELightning:
  Cooldown: 1
  Conditions:
  - targetwithin 20
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 被电击了。"} @PIR{r=20}
  - lightning{d=18;} @PIR{r=10}
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
```
AOE 雷暴
--------------------
* 进阶版：施法时间，生物停下施法，带条件和 GCD，多段打击
```yaml
AOELightningStorm:
  Cooldown: 1
  Conditions:
  - targetwithin 20
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{m="$boss &e开始施展法术。"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 被闪电吞噬了。"} @PIR{r=20}
  - lightning 10:3
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
  - delay 10
  - lightning 10:3
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
  - delay 10
  - lightning 10:3
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
  - delay 10
  - lightning 10:3
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
  - delay 10
  - lightning 10:3
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
  - delay 10
  - lightning 10:3
  - delay 5
  - effect:smoke
  - effect:particles{p=fireworksSpark;vs=1;hs=5;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=5;a=100;s=0.01;}
```
单体目标 DOT
--------------------
* 基础版
```yaml
SingleTargetDOT:
  Cooldown: 1
  Skills:
  - effect:particles{p=happyVillager;hs=1;vs=1;a=250;s=0.5;}
  - effect:sound{s=entity.spider.ambient;v=2;p=1;}
  - potion{type=POISON;d=200;level=1;}
  - potion{type=SLOW;d=80;level=7;} @self
```
* 进阶版：施法时间，生物停下施法
```yaml
SingleTargetDOT:
  Cooldown: 1
  Skills:
  - message{m="$boss&e 开始施展法术"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 中毒了。"} @PIR{r=20}
  - effect:particles{p=happyVillager;hs=1;vs=1;a=250;s=0.5;}
  - effect:sound{s=entity.spider.ambient;v=2;p=1;}
  - potion{type=POISON;d=200;level=1;}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
SingleTargetDOT:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{m="$boss&e 开始施展法术"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 中毒了。"} @PIR{r=20}
  - effect:particles{p=happyVillager;hs=1;vs=1;a=250;s=0.5;}
  - effect:sound{s=entity.spider.ambient;v=2;p=1;}
  - potion{type=POISON;d=200;level=1;}
```
AOE DOT
----------------
* 基础版
```yaml
AOEDOT:
  Cooldown: 1
  Skills:
  - effect:particles{p=happyVillager;hs=1;vs=1;a=250;s=0.5;}
  - effect:sound{s=entity.spider.ambient;v=2;p=1;}
  - potion{type=POISON;d=200;level=1;} @PIR{r=10}
```
* 进阶版：施法时间，生物停下施法
```yaml
AOEDOT:
  Cooldown: 1
  Skills:
  - message{m="$boss&e 开始施展法术"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 中毒了。"} @PIR{r=20}
  - effect:particles{p=happyVillager;hs=1;vs=1;a=250;s=0.5;}
  - effect:sound{s=entity.spider.ambient;v=2;p=1;}
  - potion{type=POISON;d=200;level=1;} @PIR{r=10}
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
AOEDOT:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{m="$boss&e 开始施展法术"} @PIR{r=20}
  - potion{type=SLOW;d=80;level=7;} @self
  - delay 80
  - message{m="<target.name>&e 中毒了。"} @PIR{r=20}
  - effect:particles{p=happyVillager;hs=1;vs=1;a=250;s=0.5;}
  - effect:sound{s=entity.spider.ambient;v=2;p=1;}
  - potion{type=POISON;d=200;level=1;} @PIR{r=10}
```
单体目标生命榨取
-------------------
* 基础版
```yaml
LifeTap:
  Cooldown: 1
  Skills:
  - effect:particles{p=dripLava;hs=1;vs=1;a=250;s=0.5;}
  - consume{d=12;h=12}
  - effect:particles{p=dripLava;hs=1;vs=1;a=250;s=0.1;} @self
```
* 进阶版：施法时间，生物停下施法
```yaml
LifeTap:
  Cooldown: 1
  Skills:
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=30;level=7;} @self
  - delay 30
  - message{m="<target.name>&e 感到自己的生命正在流逝。"} @PIR{r=20}
  - effect:particles{p=dripLava;hs=1;vs=1;a=250;s=0.5;}
  - consume{d=12;h=12}
  - effect:particles{p=dripLava;hs=1;vs=1;a=250;s=0.1;} @self
```
* 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
LifeTap:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD 30
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=30;level=7;} @self
  - delay 30
  - message{m="<target.name>&e 感到自己的生命正在流逝。"} @PIR{r=20}
  - effect:particles{p=dripLava;hs=1;vs=1;a=250;s=0.5;}
  - consume{d=12;h=12}
  - effect:particles{p=dripLava;hs=1;vs=1;a=250;s=0.1;} @self
```
重力波动
--------------
* 将玩家抛向空中。 * 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
GravityFlux:
  Cooldown: 30
  Conditions:
  - targetwithin 15
  - offgcd true
  Skills:
  - GCD{t=80}
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=40;level=7;} @self
  - delay 40
  - message{m="<target.name>&e 混乱地升向空中。"} @PIR{r=20}
  - effect:sound{s=entity.wither.death;v=2;p=1;} @self
  - effect:particles{p=cloud:1:10:a=1000;s=0.01;}
  - throw{velocity=0;velocityY=10}
```
陨石
----------
* 陨石 v1（CPU 占用较低） * 进阶版：施法时间，生物停下施法，带条件和 GCD * 请记住指定为 @target 技能，例如 - skill{s=Meteor} @target
```yaml
Meteor:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD{t=60}
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=60;level=7;} @self
  - delay 60
  - message{m="&e一颗陨石砸向 &f<target.name>。"} @PIR{r=20}
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=20;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=20;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=18;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=18;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=16;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=16;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=14;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=14;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=12;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=12;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=10;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=10;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=8;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=8;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=6;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=6;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=4;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=4;}
  - delay 1
  - effect:particles{p=cloud;vs=1;hs=1;a=50;s=0.01;y=2;}
  - effect:particles{p=reddust;vs=1;hs=1;a=100;s=0.01;y=2}
  - delay 1
  - effect:particles{p=flame;vs=1;hs=3;a=1000;s=0.01;}
  - effect:particles{p=lava;vs=2;hs=1;a=100;s=1;}
  - effect:particles{p=lava;vs=1;hs=1;a=100;s=1;}
  - effect:particles{p=reddust;vs=1;hs=3;a=500;s=0.01;}
  - effect:sound{s=entity.ghast.fireball;v=1;p=1;}
  - throw{velocity=3;velocityY=3}
  - potion{type=slow,duration=20;level=7;}
  - damage{a=6;ignorearmor=true;}
```
* 陨石 v2（CPU 占用较高） * 进阶版：施法时间，生物停下施法，带条件和 GCD
```yaml
Meteor:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - offgcd true
  Skills:
  - GCD{t=60}
  - message{msg="<mob.name>&e 开始施展法术。"} @PIR{r=15}
  - potion{type=SLOW;d=60;level=7;} @self
  - delay 60
  - message{m="&e一颗陨石砸向 &f<target.name>。"} @PIR{r=20}
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=20;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=18;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=16;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=14;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=12;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=10;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=8;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=6;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=4;}
  - delay 1
  - effect:particles{p=lava;vs=1;hs=1;a=300;s=1;y=2;}
  - delay 1
  - effect:particles{p=flame;vs=1;hs=3;a=1000;s=0.01;}
  - effect:particles{p=lava;vs=1;hs=1;a=1000;s=1;}
  - effect:particles{p=cloud;vs=1;hs=3;a=1000;s=0.01;}
  - effect:sound{s=entity.ghast.fireball;v=2;p=1;}
  - throw{velocity=3;velocityY=3}
  - potion{type=slow,duration=20;level=7;}
  - damage{a=6;ignorearmor=true;}
```
