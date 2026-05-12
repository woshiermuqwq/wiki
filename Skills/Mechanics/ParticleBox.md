## 描述
创建一个粒子方框 在targeted entity or location. 


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | The radius of the box to draw                                        | 5       |
> 此技能继承所有[Particle](/skills/mechanics/particle) 技能


## 示例
```yaml
ParticleCube:
  Skills:
  - particlebox{particle=flame;amount=200;radius=5} @self
```


## 别名
- [x] effect:particlebox
- [x] e:pb
- [x] pb


<!--TAGS-->
<!--tag:Effect:Particle-->
