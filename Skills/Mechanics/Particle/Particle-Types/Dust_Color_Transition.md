## Particle
![img](/Skills/Mechanics/Particle/Particle-Types/images/DUST_COLOR_TRANSITION.gif)


## Attributes
| Attribute | Aliases   | Description                                                          | Default |
|-----------|-----------|----------------------------------------------------------------------|---------|
| color | c, color1, c1, fromcolor, fc | 粒子的起始颜色 | #FF0000 |
| color2 | c2, tocolor, tc | 粒子过渡到的颜色 | #0000FF |
| size |  | 粒子的大小 | 1 |
> 此粒子具有 [Dusttransition](/Skills/Mechanics/Particle/Particle-Types#dusttransition) 数据类型，并继承其所有属性



## Examples
```yaml
  Skills:
  - particle{p=dust_color_transition;color=#FF0000;color2=#0000FF;size=1}
```


## Aliases
- [x] dustcolortransition
- [x] dustcolor


