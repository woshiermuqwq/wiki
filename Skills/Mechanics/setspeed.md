## 描述
Causes the 目标 to change its speed attribute

> The [MovementSpeed](/生物/Options#movementspeed) option must be explicitly set for this to work!

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| speed     | a, amount, m, multiplier, s, v, value | Speed multiplier to apply to the base speed of the entity | 1       |
| type      | t         | Type of speed, can be `FLY` or any other string. If not exactly `FLY`, this will change walk speed                                                                              | WALK    |

<!--
This value will then be multiplied by the 默认值： speed value of the respective speed type:
- `0.1` for `WALK`
- `0.2` for `FLY`
-->

## 示例
This will set 生物的 walking speed to 2 when it spawns
```yaml
  Skills:
  - setspeed{speed=2;type=walking} ~onSpawn
```