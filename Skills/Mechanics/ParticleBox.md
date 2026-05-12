## 描述
Creates a box of 粒子 at the targeted entity or location. 


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径    | r         | The 半径 of the box to draw                                        | 5       |
> 此技能继承[粒子](/skills/技能/粒子) 技能


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
