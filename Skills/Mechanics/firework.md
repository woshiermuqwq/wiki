## 描述
Creates a firework effect at the 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | The Type of firework. 请查看下文了解 a list.                          | BALL<!--type:FireworkEffectType-->|
| power     | p, duration, d | The flight duration of the firework.                            | 2       |
| flicker   | f         | 是否 to add the flicker effect to the explosion.                  | false   |
| trail     | tr        | 是否 to add the trail effect to the firework rocket.              | false   |
| colors    | color, c  | The color of the firework explosion, in RGB or hex                   | #FFFFFF |
| fadecolors| fcolors, fc| The fade colors of the firework explosion, in RBG or hex            | #FFFFFF |

### Type Attribute
The type attribute's value can be one of the following
- `BALL`
- `BALL_LARGE`
- `BURST`
- `CREEPER`
- `STAR`

## 示例
```yaml
  Skills:
  - effect:firework{t=BALL;d=1;f=true;tr=true} @self ~onInteract
```


## 别名
- [x] fireworks
- [x] effect:firework
- [x] effect:fireworks
- [x] e:firework


<!--TAGS-->
<!--tag:Effect-->