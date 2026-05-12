## 描述
使生物目标 monsters of a specific 阵营。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 阵营 | f | The 阵营 to 目标 | |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AITargetSelectors:
    - clear
    - specificfactionmonsters{f=somefaction}
```


## 别名
- [x] nearestspecificfactionmonsters