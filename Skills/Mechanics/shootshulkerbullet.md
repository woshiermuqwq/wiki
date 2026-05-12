## 描述
Shoots a shulker bullet at the 目标 entity, giving them levitation on hit.

> Requires a 目标 entity. Does not work well with location targeters


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | The type of the bullet                                               | arrow   |
| damage    | d         | The damage of the bullet                                             | 5       |
| bounce    |           | 是否 the bullet should bounce                                     | false   |
| interval  | int, i    | how often in ticks this 技能 updates                             | 4       |
| onTick    | oT, m, meta, ontickskill, s, skill | the skill this 技能 calls each interval |<!--type:Metaskill-->|
| onHit     | oH, onhitskill | the skill this 技能 calls when it hits the 目标           |<!--type:Metaskill-->|
| onEnd     | oE, onendskill | the skill this 技能 calls when it ends                      |<!--type:Metaskill-->|
| startyoffset | syo    | The starting y offset of the bullet                                  | 0       |
| forwardoffset | startfoffset, sfo | The forward offset of the bullet                         | 0       |
| fromorigin | fo | 是否 to shoot the shulker bullet from the 原点                        | false   |


## 示例
此示例将 shoot a shulker bullet with some smaller white reddust 粒子 in the onTick and onEnd. It would also damage the 目标 for 5 damage when it hits them.

```yaml
TestingShootShulkerBullet:
  Skills:
  - ShootShulkerBullet{oT=TSSB_oT;oH=TSSB_oH;oE=TSSB_oE;i=1} @target
  
TSSB_oT:
  Skills:
  - particles{particle=reddust;color=#ffffff;size=0.66;a=2;hs=0;vs=0;s=0;y=0} @origin
TSSB_oH:
  Skills:
  - damage{a=5}
TSSB_oE:
  Skills:
  - particlesphere{particle=reddust;color=#ffffff;size=0.66;a=30;r=1;hs=0;vs=0;s=0;y=0} @origin
```


## 别名
- [x] shootshulker


<!--TAGS-->
<!--tag:Projectile-->
<!--tag:Meta-Mechanic-->