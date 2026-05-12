## 描述
Causes the target to change its speed attribute

> The [MovementSpeed](/Mobs/Options#movementspeed) option 必须 explicitly set for this to work!

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| speed     | a, amount, m, multiplier, s, v, value | Speed multiplier to apply to the base speed of the entity | 1       |
| type      | t         | Type of speed, 可以 `FLY` or any other string. If not exactly `FLY`, this will change walk speed                                                                              | WALK    |

<!--
This value will then be multiplied by the default speed value of the respective speed type:
- `0.1` for `WALK`
- `0.2` for `FLY`
-->

## 示例
This will set the mob's walking speed to 2 when it spawns
```yaml
  Skills:
  - setspeed{speed=2;type=walking} ~onSpawn
```
