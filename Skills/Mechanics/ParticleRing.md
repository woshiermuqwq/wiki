## 描述
Creates a ring of 粒子 around the targeted entity or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| points    | pts       | The number of points to draw representing the ring                   | 8       |
| 半径    | r         | The 半径 of the ring around the 目标                             | 10      |
> 此技能继承[粒子](/skills/技能/粒子) 技能
>> The 粒子 are generated “per point” in this 技能, so keeping `amount` low is recommended.


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
