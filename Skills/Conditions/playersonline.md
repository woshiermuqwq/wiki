## 描述
匹配当前在线玩家数量。

## 属性

| 属性       | 别名   | 描述                   | 默认值 |
| ---------- | ------ | ---------------------- | ------ |
| amount     | a      | 要检测的玩家数量。可为范围 | 0      |


## 示例
```yaml
  Conditions:
  - playersOnline{amount=>5}
```

## 别名
- [x] onlineplayercount
- [x] onlineplayers
