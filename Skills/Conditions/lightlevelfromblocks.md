## 描述
测试目标位置发光方块产生的光照等级。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| level     | l         | 要匹配的光照等级范围                                       | 0       |


## 示例
```yaml
  Conditions:
  - lightlevelfromblocks{l=10} true
```

```yaml
  Conditions:
  - lightlevelfromblocks{l=>10} true
```

```yaml
  Conditions:
  - lightlevelfromblocks{l=1to10} true
```

## 别名
- [x] blocklightlevel