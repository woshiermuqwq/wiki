## 描述 
Creates a 粒子 effect at the targeted entity or location.

A list of 粒子 types can be found **[here](/Skills/技能/粒子/粒子-Types)**. 

[All of the spigot 粒子 effects listed in the javadocs should be acceptable as well.](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/粒子.html)


## 属性
### General Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 粒子  | p         | The [粒子 type] to use.                                          | reddust<!--type:粒子-->|
| 生物       | m, t      | The entity to spawn as the 粒子. Cannot be the original entity. **Premium Only**.                                                                                  |<!--type:生物-->|
| amount    | count, a  | The number of 粒子 to create                                    | 10      |
| spread    | offset    | 粒子的垂直扩散范围                                 | 0       |
| hSpread   | hs        | 粒子的水平扩散范围                               | `spread`|
| vSpread   | vs, yspread, ys| The spread of the 粒子 on the y axis. Overwrites `spread`  | `spread`|
| xSpread   | xs        | The spread of the 粒子 on the x axis. Overwrites `hSpread` on that axis       | hSpread |
| zSpread   | zs        | The spread of the 粒子 on the z axis. Overwrites `hSpread` on that axis                            | hSpread |
| speed     | s         | The “speed” of the 粒子. If a 粒子 has a [DataType](/Skills/技能/粒子/粒子-Types#datatypes), this attribute will behave inconsistently. | 0    |
| yOffset   | y         | Y轴偏移 of the 粒子 from the 目标                        | 0       |
| viewDistance | vd     | The distance the 粒子 are rendered                              | 128     |
| fromorigin| fo        | Should the 粒子 be generated from the 原点 of the 技能    | false   |
| directional| d        | Does the 粒子 use directional travel. The [粒子 type] used must not have additional data (extra attributes)                                                             | false   | 
| directionReversed| dr | Reverses the direction of the 粒子.                             | false   | 
| direction | dir       | Specifies a vector for the 粒子 to move towards.          | 0,0,0 (x,y,z) | 
| fixedyaw  | 水平朝向(yaw)       | Sets the 水平朝向(yaw) of the location 目标(s) of the 技能的所有属性。 This is ignored if it remains -1111 | -1111   |
| fixedpitch| 俯仰角(pitch)     | Sets the 俯仰角(pitch) of the location 目标(s) of the 技能的所有属性。 This is ignored if it remains -1111 | -1111   |
| audience  |           | The [audience] of the 粒子 effect                                | nearby<!--type:Audience--> |
| color     | c         | 粒子的颜色, if supported                              |<!--type:Color-->|
| exactoffsets | eo     | Changes the formula with which random spawn locations for the 粒子 are computed | false |


#### Extra Attributes
Depending on the specific [粒子 type] used, extra attributes 将变为 available to use inside 粒子-related 技能s too. you can find more by accessing the specific 粒子's page from the [粒子 types wiki page]

#### 生物-Type 粒子 \[**Premium Only**\]
This 粒子 type will replace the spawned 粒子 with the selected entity. The entity will act as a normal one, being able to attack, be hit, activate skills and so on. The entity will have no parent/owner relationship with the 施法者.

### Entity-Only Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| useEyeLocation | uel  | (true/false) Whether to base the 粒子 on 实体的 eyes      | false   |
| forwardOffset | startfoffset, sfo | The forward-offset from the targeted entity, does not work when `directional` is set to true | 0       |
| sideOffset| soffset, sso | The side-offset from the targeted entity, does not work when `directional` is set to true | 0 |

## 示例
```yaml
  Skills:
  - effect:particles{particle=flame;amount=200;hS=1;vS=1;speed=5} @self
  - ...
```
```yaml
  Skills:
  - effect:particles{particle=block;m=dirt;amount=100;hS=1;vS=1} @self
  - ...
```
```yaml
  Skills:
  - particles{particle=flame;a=10;hs=0.3;vs=0.3;y=0.3;s=0.1125} @self
  - ...
```

## 别名
- [x] effect:粒子
- [x] effect:粒子
- [x] 粒子
- [x] 粒子
- [x] e:粒子
- [x] e:粒子
- [x] e:p


<!-- LINKS -->
[particle type]: /Skills/Mechanics/Particle/Particle-Types
[particle types wiki page]: /Skills/Mechanics/Particle/Particle-Types


<!--TAGS-->
<!--tag:Effect:Particle-->