## 描述 
Creates a particleline ring.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| distanceBetween | db  | The distance between each point                                      | 1       |
| startYOffset    | syo, ystartoffset, ys| Offset Y location of the starting point             | 0       |
| targetYOffset   | tyo, ytargetoffset, yt | Offset Y location of the 目标 point             | 0       |
| fromOrigin      | fo  | 是否 to draw the line from the [@原点] instead                  | false   |
| ringpoints | rp       | The number of points in the line ring                                | 16      |
| ringradius | rr       | The 半径 of the line ring                                          | 0.5     |
| maxdistance     | md  | The maximum distance the line can reach                              | 256     |
> This 技能 继承 [粒子](/skills/技能/粒子) 技能


## 示例
```yaml
  Skills:
  - particlelinering{p=flame;r=3;rr=1} @PIR{r=20;limit=1;sort=RANDOM}
```


## 别名
- [x] effect:particlelinering
- [x] particleringline


<!-- LINKS -->
[@origin]: /skills/targeters/origin



<!--TAGS-->
<!--tag:Effect:Particle-->
