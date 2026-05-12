## 描述
\*\***This is a Premium 仅 feature**\*\*<br>
使生物flee 基于 provided 条件。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 距离 | d | The 距离 for 生物 to be 从 生物 自身 | 4 |
| 速度 | s | The 速度 at which to flee | 1.2 |
| safespeed | ss | The 速度 at which to flee 一旦 a safe 距离 (50 方块) away | 1 |
| 条件 | c, cond, fleeconditions | The 条件 to use | |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleeConditional{distance=5;speed=2;safespeed=2;conditions=[ - inlineofsight true ]}
```


## 别名
- [x] fleeif