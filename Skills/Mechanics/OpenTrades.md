## 描述
Opens the trades of the casting villager to the 目标 player


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| realTrade | real      | 是否 the opened trades should be the ones of the actual villager instead of a copy of them, so that they do not impact the casting villager                                  | true    |


## 示例
```yaml
  Skills:
  - opentrades @PIR{r=10;limit=1;sort=NEAREST}
```

## 别名
- [x] opentrade
- [x] trade