## 描述
Creates a line of 粒子 from the 施法者 to 目标实体 or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| distanceBetween | db  | The distance between each point in the line                          | 0.25    |
| startYOffset    | syo, ystartoffset, ys| Offset Y location of the starting point of the line | 0       |
| targetYOffset   | tyo, ytargetoffset, yt | Offset Y location of the 目标 point of the line | 0       |
| fromOrigin      | fo  | 是否 to draw the line from the [@原点] instead                  | false   |
| zigzag          | zz  | 是否 to draw the line to the 目标 as a zigzag                   | false   |
| zigzags         | zzs | Amount of zigzags when using the zigzag option                       | 10      |
| zigzagOffset    | zzo | Offset of each zigzag                                                | 0.2     |
| maxdistance     | md  | The maximum distance the line can reach                             | 256      |
> This 技能 继承 [粒子](/skills/技能/粒子) 技能
>> The 粒子 are generated “per point” in this 技能, so keeping `amount` low is recommended.


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
