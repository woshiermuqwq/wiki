## 描述
Causes the 生物 to leap through the air at the 目标. Leap calculates a
弹射物-like trajectory so that the 生物 will land directly on top of
the 目标 if the 速度 is great enough, otherwise the 生物 will leap
at far as possible towards the 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v         | The max 速度 of the leap                                         | 100     |
| noise     | n         | Added variance to where the 生物 will land                            | 0       |

### 速度 Attribute
Because of the way this skill works, using very high 速度 values is
recommended (usually values exceeding 100 work best). 速度 is
calculated differently with this skill than most others.


## 示例
This skill would cause the 生物 to leap towards the 目标 at high
speeds, then slam into the ground and cause an explosion.
```yaml
CrushingLeap:
  Cooldown: 10
  Skills:
  - leap{velocity=200} @target
  - delay 20
  - jump{velocity=-100}
  - effect:explosion @self
  - damage{amount=20} @EntitiesInRadius{r=5}
```


<!--TAGS-->
<!--tag:Movement-->