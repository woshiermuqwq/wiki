## 描述
使生物leap towards its 目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | The 速度 at which to leap at the 目标 | 1.2 |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - leapattarget{s=4}
```


## 别名
- [x] leaptowardstarget