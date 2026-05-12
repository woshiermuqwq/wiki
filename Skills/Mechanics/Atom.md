## 描述
 
Creates an orbiting Atom effect 在location.            


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| particleorbital | particleo, po | The [particle] that 将会 displayed 在orbitals     |`particle`<!--type:Particle-->|
| particlenucleus | particlen, pn | The [particle] that 将会 displayed 在nucleus       | reddust<!--type:Particle-->|
| amountnucleus | amountn, apn, an | The amount of particles 对于nucleus                   | 50      |
| orbitals  | o         | The amount of orbitals around the nucleus                            | 2       |
| amountorbital | amounto, apo, ao | The amount of particles for each orbital                  | 1       |
| radius    | r         | The radius of the orbitals                                           | 4       |
| radiusnucleus | rn    | The radius of the nucleus                                            | 1       |
| rotation  | ro        | The rotation of the atom                                             | 0       |
| ticks     | t         | The amount of ticks during which the atom will persist               | 1       |
| interval  | in        | The interval of the updates of the atom                              | 10      |
| velocity  | v         | The velocity of the atom                                             | 80      |
> 此机制继承所有[particle](/skills/mechanics/Particle) 机制


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
