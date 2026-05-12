## 描述
检查目标 MythicMob 的等级。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| level     | l         | 要匹配的等级范围                                             |         |


## 示例
```yaml
  Conditions:
  - level{l=10} true
```

```yaml
  Conditions:
  - level{l=>10} true
```

```yaml
  Conditions:
  - level{l=1to10} true
```

```yaml
  Conditions:
  - level{l=<10} true
```