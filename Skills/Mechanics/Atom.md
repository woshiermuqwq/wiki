## 描述 
Creates an orbiting Atom effect at the location.            


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| particleorbital | particleo, po | The [粒子] that 将显示 at the orbitals     |`粒子`<!--type:粒子-->|
| particlenucleus | particlen, pn | The [粒子] that 将显示 at the nucleus       | reddust<!--type:粒子-->|
| amountnucleus | amountn, apn, an | The amount of 粒子 for the nucleus                   | 50      |
| orbitals  | o         | The amount of orbitals around the nucleus                            | 2       |
| amountorbital | amounto, apo, ao | The amount of 粒子 for each orbital                  | 1       |
| 半径    | r         | The 半径 of the orbitals                                           | 4       |
| radiusnucleus | rn    | The 半径 of the nucleus                                            | 1       |
| rotation  | ro        | The rotation of the atom                                             | 0       |
| ticks     | t         | The amount of ticks during which the atom will persist               | 1       |
| interval  | in        | The interval of the updates of the atom                              | 10      |
| 速度  | v         | The 速度 of the atom                                             | 80      |
> This 技能 继承 [粒子](/skills/技能/粒子) 技能


## 示例
```yaml
  Skills:
  - Atom{p=reddust;r=2;d=true;dr=true;dir=1,0,0;ticks=20} @selflocation{y=2} ~onSwing
```


## 别名
- [x] effect:atom
- [x] e:atom


<!-- LINKS -->
[particle]: /Skills/Mechanics/Particle/Particle-Types


<!--TAGS-->
<!--tag:Effect:Particle-->