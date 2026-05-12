## 描述
检测给定半径内的玩家数量。

## 属性

| 属性             | 别名              | 描述                     | 默认值 |
| ---------------- | ----------------- | ------------------------ | ------ |
| amount           | a                 | 要检测的数量范围           | >0     |
| radius           | r, distance, d    | 检测半径                  | 32     |
| ignorespectator  | is                | 是否忽略旁观模式玩家       | true   |


## 示例
```yaml
  Conditions:
  - playersinradius{a=>3;r=16}
```

## 别名
- [x] pir
- [x] playerInRadius
