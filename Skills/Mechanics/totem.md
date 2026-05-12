## 描述
The totem 技能 places an invisible "totem", similar to the
[弹射物](/skills/技能/弹射物) 技能, except that it
doesn't move. Much like 弹射物, you can use onTick skills to create
effects in order to identify the totem's location.

Totems will pulse their onHit skill on any 目标 that come within
their defined 半径 until their charges or duration run out. They're
useful for creating ground effects with 粒子, such as clouds of
poison or land mines.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| Charges   | ch, c     | Determines how many times the totem can hit something before disappearing | 0  |
| YOffset   | yo        | How high off the 目标 the totem will spawn                          | 1      |
| stopatentity | se     | 是否 the totem should terminate upon hitting an entity             | false  |
| hugsurface| hs        | 是否 the totem should be aligned with the ground           | false   |
| hugliquid | hugwater, huglava | 是否, when using hugSurface, a liquid can also count as a "surface" the totem can align itself with | false   |
| heightfromsurface| hfs| How high above the surface the totem should align itself if HugSurface is set to true | 0.5     |
| faceawayfromcaster | fafc | 是否 the totem should face away from the 施法者 when first placed | false |
> Inherits attributes from [弹射物](/skills/技能/弹射物)


## 示例
```yaml
MyFirstTotem:
  Skills:
  - totem{ch=1;i=1;md=8;onTick=MFT_TICK} @self

MFT_TICK:
  Skills:
  - damage{a=3} @ENO{r=5}
```


## 别名
- [x] toteme
- [x] t


<!--TAGS-->
<!--tag:Meta-Mechanic-->