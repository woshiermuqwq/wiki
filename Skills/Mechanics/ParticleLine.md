## 描述
创建一条粒子线 from the caster to the targeted entity or location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| distanceBetween | db  | The distance between each point in the line                          | 0.25    |
| startYOffset    | syo, ystartoffset, ys| Offset Y location of the starting point of the line | 0       |
| targetYOffset   | tyo, ytargetoffset, yt | Offset Y location of the target point of the line | 0       |
| fromOrigin      | fo  | Whether to draw the line from the [@origin] instead                  | false   |
| zigzag          | zz  | Whether to draw the line to the target as a zigzag                   | false   |
| zigzags         | zzs | Amount of zigzags when using the zigzag option                       | 10      |
| zigzagOffset    | zzo | Offset of each zigzag                                                | 0.2     |
| maxdistance     | md  | The maximum distance the line can reach                             | 256      |
> 此机制继承所有[Particle](/skills/mechanics/particle) 机制
>> The particles are generated “per point” in this 机制, so keeping `amount` low is recommended.


## 示例
```yaml
FlameParticleLine:
  Skills:
  - particleline{particle=flame;amount=1;fromOrigin=true} @target
```


## 别名
- [x] effect:particleline
- [x] e:pl
- [x] pl


<!-- LINKS -->
[@origin]: /skills/targeters/origin



<!--TAGS-->
<!--tag:Effect:Particle-->
