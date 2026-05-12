## 描述
匹配目标的生命值百分比或倍率。

## 属性

| 属性               | 别名                      | 描述                                         | 默认值 |
| ------------------ | ------------------------- | -------------------------------------------- | ------ |
| percent            | p, healthpercent, hp      | 要检测的生命值百分比或倍率（如 50% 或 0.5）   | 0      |
| includeabsorption  | ia                        | 是否将伤害吸收提供的生命值纳入计算             | false  |

## 示例

```yaml
# 生命值恰好 50%
Conditions:
- healthpercent{p=50%} true
```

```yaml
# 生命值低于 50%
Conditions:
- healthpercent{p=<50%} true
```

```yaml
# 生命值高于 10%
Conditions:
- healthpercent{p=>0.1} true
```

## 别名
- [x] hppercent
