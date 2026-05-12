## 描述
Ta以all 玩家 in a ring 在...周围 施法者为目标。
The targeted 玩家 将 the ones at a 距离 从 施法者 在...之间 minimum and the maximum 范围.


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| minrange | min | The minimum 范围 of the ring | 5 |
| maxrange | max | The maximum 范围 of the ring | 10 |


## 示例
```yaml
  Skills:
  - ignite @PlayersInRing{min=2;max=10}
```


## 别名
- [x] pring