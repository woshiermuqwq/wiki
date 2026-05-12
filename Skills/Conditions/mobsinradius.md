## 描述
检查给定半径内的生物数量。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| types     | type, t   | 要检查的生物类型                                       |         |
| amount    | a         | 要检查的生物数量范围。不计入施法者            | 1       |
| radius    | r         | 要检查的半径                                                  | 5       |


## 示例

### 单一类型
```yaml
  Conditions:
  - mobsInRadius{types=NewZombie;amount=5to10;radius=15}
```

### 多种类型
```yaml
  Conditions:
  - mobsInRadius{types=NewZombie,NewSkeleton,NewSpider;amount=5to10;radius=15}
```