## 描述
Breaks the 目标 player's 护盾 block if they are blocking. Only works when targeting players.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d         | The duration in ticks that the 护盾 will be disabled for after the block is broken                                                                                         | 100     |


## 示例
If the player is blocking, this would break the block and put the 护盾 on 冷却 for 200 ticks (or 10 seconds.)
```yaml
  Skills:
  - shieldbreak{duration=200} @target
```


## 别名
- [x] disableshield