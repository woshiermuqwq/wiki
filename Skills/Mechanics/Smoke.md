## 描述
Creates a puff of smoke 在location of the targeter.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| direction | dir, d    | The direction the effect should play towards. Can be an integer from 1 to 4| 4 |


## 示例
```yaml
SmokeMonster:
  Type: ZOMBIE
  Skills:
  - smoke @target ~onTimer:10
  - smoke{direction=2} @self ~onAttack
```


## 别名
- [x] effect:smoke
- [x] e:smoke


<!--TAGS-->
<!--tag:Effect-->
