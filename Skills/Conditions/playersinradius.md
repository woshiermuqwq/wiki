## 描述
检查半径内的玩家数量。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | 要检查的范围值                                       | >0      |
| radius    | r, distance, d  | 要检查的给定半径                                      | 32      |
| ignorespectator | is  | 是否忽略旁观模式玩家                  | true    |


## 示例
```yaml
  Conditions:
  - playersinradius{a=>3;r=16}
```


## 别名
- [x] pir
- [x] playerInRadius