## 描述
使生物flee from wolves。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 距离 | d | The 距离 for wolves to be 从 生物 自身 | 6 |
| 速度 | s | The 速度 at which to flee | 1.2 |
| safespeed | ss | The 速度 at which to flee 一旦 a safe 距离 (50 方块) away | 1 |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleewolf{d=10;s=2;ss=1}
```


## 别名
- [x] runfromwolves