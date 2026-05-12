## 描述
Makes an armor stand assume a pose over a specified time


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d         | The duration of the animation in ticks                               | 1       |
| smart     |           | 是否 to apply smart angle conversion                              | true    |
| ignoreempty | ie      | 是否 to ignore empty pose values                                  | true    |
| usedegrees  | ud      | Interprets the input' values as degrees (0-360) if set to true and as radians (0-6.28) if set to false                                                                       | true    |
| head      | h         | The pose for the armorstand's head                                   |         |
| body      | b         | The pose for the armorstand's body                                   |         |
| leftarm   | la        | The pose for the armorstand's left arm                               |         |
| rightarm  | ra        | The pose for the armorstand's right arm                              |         |
| leftleg   | ll        | The pose for the armorstand's left leg                               |         |
| rightleg  | rl        | The pose for the armorstand's right leg                              |         |

  

## 示例
```yaml
  Skills:
  - animatearmorstand{d=10;leftarm=90,0,0;rightarm=270,0,0;ignoreempty=false}
```


## 别名
- [x] animateas
- [x] animas