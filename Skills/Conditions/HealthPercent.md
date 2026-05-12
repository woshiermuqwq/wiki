## 描述
匹配目标的生命值百分比或倍数。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| percent   | p, healthpercent, hp | 要检查的生命值百分比或倍数（例如 50% 或 0.5）  | 0       |
| includeabsorption | ia | 是否将吸收生命值纳入计算 | false |

## 示例

```yaml
# 恰好 50% 生命值
Conditions:
- healthpercent{p=50%} true
```

```yaml
# 低于 50% 生命值
Conditions:
- healthpercent{p=<50%} true
```

```yaml
# 高于 10% 生命值
Conditions:
- healthpercent{p=>0.1} true
```

## 别名
- [x] hppercent