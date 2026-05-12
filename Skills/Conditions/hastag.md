## 描述
测试目标是否拥有计分板标签。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tag       | t         | 要检查的标签                                                 |         |


## 示例
```yaml
  Conditions:
  - hastag{t=KilledBoss1} true
```

```yaml
  TargetConditions:
  - hastag{t=PuzzleRoom1Solved} true
```


## 别名
- [x] hasScoreboardTag