## 描述
匹配目标的生命值。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| health    | h, amount, a | 要检查的生命值范围                                     | 0       |
| includeabsorption | ia | 是否将吸收生命值纳入计算 | false |

## 示例

```yaml
Conditions:
- health{h=50} true
```

```yaml
# 低于 50 生命值
Conditions:
- health{h=<50} true
```

```yaml
# 高于 10 生命值
Conditions:
- health{h=>10} true
```

## 别名
- [x] hp