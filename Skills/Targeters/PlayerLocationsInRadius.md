## 描述
选取施法者周围指定半径内所有玩家的位置


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |
| yoffset   | y         | 目标位置的 Y 轴偏移                               | 0       |


## 示例
```yaml
  Skills:
  - effect:particles @PlayerLocationsInRadius{r=10}
```


## 别名
- [x] LocationRadius
- [x] PLIR
- [x] PLR
