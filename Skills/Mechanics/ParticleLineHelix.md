## 描述
 
Creates a particle line helix effect 在targeted entity or location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| distanceBetween | db  | The distance between each point                                      | 1       |
| startYOffset    | syo, ystartoffset, ys| Offset Y location of the starting point             | 0       |
| targetYOffset   | tyo, ytargetoffset, yt | Offset Y location of the target point             | 0       |
| fromOrigin      | fo  | Whether to draw the line from the [@origin] instead                  | false   |
| helixlength     | hl  | The length of the helix effect                                       | 2       |
| helixradius     | hr  | The radius of the helix effect                                       | 1       |
| helixrotation   | rot | The rotation of the helix effect                                     | 0       |
| maxdistance     | md  | The maximum distance the line can reach                              | 256     |
> 此机制继承所有[Particle](/skills/mechanics/particle) 机制
>> The particles are generated “per point” in this 机制, so keeping `amount` low is recommended.


## 示例
```yaml
  Skills:
  - particlelinehelix{Fo=true;db=0.4;hl=4;syo=1.8;p=scrape;hr=0.5;md=40} @targetlocation
```
<details><summary>Resulting effect</summary>
![Image](https://i.imgur.com/b812UFl.png)
</details>


## 别名
- [x] effect:particlelinehelix
- [x] particlehelixline


<!-- LINKS -->
[@origin]: /skills/targeters/origin



<!--TAGS-->
<!--tag:Effect:Particle-->
