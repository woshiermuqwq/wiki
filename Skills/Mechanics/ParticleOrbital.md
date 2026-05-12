## 描述
Creates a 粒子 orbital effect, where the 粒子 将环绕 around the targeted entity or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径    | r         | The 半径 at which the 粒子 orbits                              | 4       |
| points    | p         | How many points make up the circle                                   | 20      |
| ticks     | t         | For how many ticks this effect 将持续                             | 100     |
| interval  | in, i     | Tick speed at which the 粒子 moves (faster tick rate=slower movement) | 10 |
| rotationX | rotX, rX  | Rotates the orbit around the X axis                                  | 0       |
| rotationY | rotY, rY  | Rotates the orbit around the Y axis                                  | 0       |
| rotationZ | rotZ, rZ  | Rotates the orbit around the Z axis                                  | 0       |
| offsetX   | offx, ox  | X轴偏移 of the orbit's center                                   | 0       |
| offsetY   | offy, oy  | Y轴偏移 of the orbit's center                                   | 0       |
| offsetZ   | offz, oz  | Z轴偏移 of the orbit's center                                   | 0       |
| angularVelocityX | avx, vx | Modifies the angular 速度 around the X axis                 | 0       |
| angularVelocityY | avy, vy | Modifies the angular 速度 around the Y axis                 | 0       |
| angularVelocityZ | avz, vz | Modifies the angular 速度 around the Z axis                 | 0       |
| rotate    |           | Whether the 粒子 should rotate. Defaults to true if one of the angularvelocity attributes is greater than 0                                                   |         |
| reversed  | reverse   | Whether the 粒子 should orbit in the opposite direction         | false   |
> 此技能继承[粒子](/skills/技能/粒子) 技能


## 示例
```yaml
OrbitalParticleSkill:
  Skills:
  - particleorbital{r=2;points=16;t=100;i=1;vy=20;particle=flame} @self ~onSpawn
```


## 别名
- [x] effect:particleorbital
- [x] e:particleorbital
- [x] effect:particlecircle
- [x] particlecircle
- [x] e:particlecricle


<!--TAGS-->
<!--tag:Effect:Particle-->
