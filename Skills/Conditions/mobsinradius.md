## 描述
检测给定半径内的生物数量。

## 属性
| 属性       | 别名       | 描述                           | 默认值 |
| ---------- | ---------- | ------------------------------ | ------ |
| types      | type, t    | 要检测的生物类型                 |        |
| amount     | a          | 要检测的生物数量范围。不计施法者  | 1      |
| radius     | r          | 检测半径                        | 5      |


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
