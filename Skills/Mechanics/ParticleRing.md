## 描述
创建一个粒子环 around the targeted entity or location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| points    | pts       | The number of points to draw representing the ring                   | 8       |
| radius    | r         | The radius of the ring around the target                             | 10      |
> 此技能继承所有[Particle](/skills/mechanics/particle) 技能
>> The particles are generated “per point” in this 技能, so keeping `amount` low is recommended.


## 示例
```yaml
FlameRing:
  Skills:
  - particlering{particle=flame;radius=20;points=32;amount=1;hS=1;vS=0} @target
```


## 别名
- [x] effect:particlering
- [x] e:pr
- [x] pr


<!--TAGS-->
<!--tag:Effect:Particle-->
