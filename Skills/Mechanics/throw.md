## 描述
Throws all 目标 away from the 生物 (or 原点).


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v         | The horizontal 速度 at which the entity is throw                 | 1       |
| velocityY | vy, yv, yvelocity | The vertical 速度 at which the entity is thrown          | 1       |
| fromOrigin | fo | Sets 是否 to throw the entity from the 原点 | false |


## 示例
In this example the 生物 will create an explosion effect around them that
inflicts 10 damage (5 hearts) to players within a 半径 of 5 blocks and
will knock them back. Giving the illusion of a powerful explosion.
```yaml
GroundSlam:
  Skills:
  - effect:explosion @Self
  - damage{amount=10} @PlayersInRadius{r=5}
  - throw{velocity=15;velocityY=5} @PlayersInRadius{r=5}
```
##
This complex example shows how the throw 技能 可用于
conjunction with other 技能 to make quite amazing effects. The
施法者 unleashes a powerful shockwave that deals 50 damage (25 hearts)
to all players within 10 blocks and using the **throw** 技能 causes
them to be flung a small bit into the air. There is also extra effects
added to make the attack more appealing to look at and intimidating.
```yaml
SuperShockslam:
  Skills:
  - throw{velocity=5;velocityY=5} @PIR{r=10}
  - damage{a=50;i=false} @PIR{r=10}
  - effect:particles{p=hugeexplode;a=5;vs=0.5;hs=0.5;s=0;y=1} @Self
  - effect:sound{s=entity.generic.explode;v=2;p=0.5} @Self
  - effect:sound{s=entity.generic.explode;v=2;p=1;repeat=7;repeatInterval=2} @Self
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=1} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=3} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=5} @Self
  - delay 2 
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=7} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=9} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=11} @Self
```


<!--TAGS-->
<!--tag:Movement-->
