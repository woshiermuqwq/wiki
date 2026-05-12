## 描述
Moves the extremities of an armorstand, the value is in radians.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| head      | h         | The rotation of the head                                             | 0,0,0   |
| body      | b         | The rotation of the body                                             | 0,0,0   |
| leftarm   | la        | The rotation of the left arm                                         | 0,0,0   |
| rightarm  | ra        | The rotation of the right arm                                        | 0,0,0   |
| leftleg   | ll        | The rotation of the left leg                                         | 0,0,0   |
| rightleg  | rl        | The rotation of the right leg                                        | 0,0,0   |


## 示例
```yaml
  Skills:
  - posearmorstand{head=0.78,0,0} @self ~onSpawn
  - ...
```


## 别名
- [x] armorstandpose