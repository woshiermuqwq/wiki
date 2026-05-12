## 描述 
Creates a 粒子 line helix effect at 目标实体 or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| distanceBetween | db  | The distance between each point                                      | 1       |
| startYOffset    | syo, ystartoffset, ys| Offset Y location of the starting point             | 0       |
| targetYOffset   | tyo, ytargetoffset, yt | Offset Y location of the 目标 point             | 0       |
| fromOrigin      | fo  | 是否 to draw the line from the [@原点] instead                  | false   |
| helixlength     | hl  | The length of the helix effect                                       | 2       |
| helixradius     | hr  | The 半径 of the helix effect                                       | 1       |
| helixrotation   | rot | The rotation of the helix effect                                     | 0       |
| maxdistance     | md  | The maximum distance the line can reach                              | 256     |
> This 技能 继承 [粒子](/skills/技能/粒子) 技能
>> The 粒子 are generated “per point” in this 技能, so keeping `amount` low is recommended.


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
