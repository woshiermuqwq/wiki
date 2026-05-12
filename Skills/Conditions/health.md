## 描述
匹配目标的生命值。

## 属性

| 属性               | 别名            | 描述                                 | 默认值 |
| ------------------ | --------------- | ------------------------------------ | ------ |
| health             | h, amount, a    | 要检测的生命值范围                     | 0      |
| includeabsorption  | ia              | 是否将伤害吸收提供的生命值纳入计算     | false  |

## 示例

```yaml
Conditions:
- health{h=50} true
```

```yaml
# 生命值低于 50
Conditions:
- health{h=<50} true
```

```yaml
# 生命值高于 10
Conditions:
- health{h=>10} true
```

## 别名
- [x] hp
