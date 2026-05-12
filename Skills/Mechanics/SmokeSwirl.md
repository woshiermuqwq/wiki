## 描述
Creates a swirling vortex of smoke at the targeted entity or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d     | How many intervals the swirl 将持续                                   | 5       |
| interval  | i     | How many ticks there are between each pulse of smoke                     | 1       |


## 示例
```yaml
SmokeSwirlSkill:
  Skills:
  - smokeswirl{duration=10;interval=10} @TargetLocation
```


## 别名
- [x] effect:smokeswirl
- [x] e:smokeswirl


<!--TAGS-->
<!--tag:Effect-->
