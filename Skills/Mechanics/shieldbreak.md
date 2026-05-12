## 描述
Breaks the target player's shield block if they are blocking. Only works when targeting players.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d         | The duration in ticks that the shield 将会 disabled for after the block is broken                                                                                         | 100     |


## 示例
If the player is blocking, this would break the block and put the shield on cooldown for 200 ticks (or 10 seconds.)
```yaml
  Skills:
  - shieldbreak{duration=200} @target
```


## 别名
- [x] disableshield
