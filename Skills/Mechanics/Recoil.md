## 描述
Kicks the target's screen to simulate recoil.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| recoil    | r         | The amount of recoil.                                                | 1       |
| pitch     | p         | The range of pitch the screen will get kicked by                     | -10to10 |
| yaw       | y         | The range of yaw the screen will get kicked by                   | -0.25to0.25 |
| sneaking  | sn        | The value of the pitch's and yaw's multiplier if the player is sneaking | 0.75 |
| sprinting | sp        | The value of the pitch's and yaw's multiplier if the player is sprinting| 1.25 |

### Recoil Attribute
Negative numbers on pitch will recoil upwards, whilst positive will recoil downwards. If you set the values to the same number it will always go the same distance: `pitch=-1to-1`


## 示例
```yaml
  Skills:
  - recoil{r=1;pitch=-1to1} @self
```


## 别名
- [x] effect:recoil
- [x] e:recoil


<!--TAGS-->
<!--tag:Movement:Rotation-->
