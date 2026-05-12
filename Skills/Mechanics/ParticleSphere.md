## 描述
创建一个粒子球 在targeted entity or location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | The radius of the sphere to draw                                     | 0       |
> 此机制继承所有[Particle](/skills/mechanics/particle) 机制


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
