## 描述
Gives the 目标 player an amount of oxygen.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | the amount of oxygen to give the player                              | 1       |


## 示例
```yaml
  Skills:
  - oxygen{amount=10} @trigger ~onInteract
```