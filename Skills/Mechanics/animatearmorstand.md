## 描述
Makes an armor stand assume a pose over a specified time


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d         | The duration of the animation in ticks                               | 1       |
| smart     |           | Whether to apply smart angle conversion                              | true    |
| ignoreempty | ie      | Whether to ignore empty pose values                                  | true    |
| usedegrees  | ud      | Interprets the input' values as degrees (0-360) 如果设置 to true and as radians (0-6.28) 如果设置 to false                                                                       | true    |
| head      | h         | The pose 对于armorstand's head                                   |         |
| body      | b         | The pose 对于armorstand's body                                   |         |
| leftarm   | la        | The pose 对于armorstand's left arm                               |         |
| rightarm  | ra        | The pose 对于armorstand's right arm                              |         |
| leftleg   | ll        | The pose 对于armorstand's left leg                               |         |
| rightleg  | rl        | The pose 对于armorstand's right leg                              |         |

  

## 示例
```yaml
  Skills:
  - animatearmorstand{d=10;leftarm=90,0,0;rightarm=270,0,0;ignoreempty=false}
```


## 别名
- [x] animateas
- [x] animas
