## 描述
Sets the immunity ticks on the 目标. This should be delayed if used immediately during an attack since the ticks are applied after an event completes.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ticks     | d, duration, t | The NoDamageTicks to set (for how many ticks 生物的 will be invulnerable under normal circumstances) | 0 |


## 示例
Gives the 施法者 invincibility after it attacks.
```yaml
  Skills:
  - setNoDamageTicks{ticks=0;delay=1} @self ~onAttack
```


## 别名
- [x] setimmunityticks