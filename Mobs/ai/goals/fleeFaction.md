## 描述
使生物flee from a specific 阵营。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 距离 | d | The 距离 for targets to be 从 生物 自身 | 4 |
| 速度 | s | The 速度 at which to flee | 1.2 |
| safespeed | ss | The 速度 at which to flee 一旦 a safe 距离 (50 方块) away | 1 |
| 阵营 | f | The 阵营 to flee from | |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleefaction{distance=5;speed=2;safespeed=2;faction=somefaction}
```


## 别名
- [x] runfromfaction