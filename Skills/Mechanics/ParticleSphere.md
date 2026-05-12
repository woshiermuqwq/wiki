## 描述
Creates a sphere of 粒子 at 目标实体 or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径    | r         | The 半径 of the sphere to draw                                     | 0       |
> This 技能 继承 [粒子](/skills/技能/粒子) 技能


## 示例
```yaml
FlameSphere:
  Skills:
  - particlesphere{particle=flame;amount=200;radius=5} @self
```


## 别名
- [x] effect:particlesphere
- [x] e:ps
- [x] ps



<!--TAGS-->
<!--tag:Effect:Particle-->
