## 描述
Clears all potion effects from the 目标 entity


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| types     | type, t   | The type or list of types of potion effects to clear. Not providing a type will clear all effects.                                                                             |<!--type:PotionEffectType-->|


## 示例
```yaml
  Skills:
  - potionclear{type=FIRE_RESISTANCE} @target
  - potionclear{type=FIRE_RESISTANCE,SPEED} @self
  - potionclear @self
```


## 别名
- [x] clearpotion
- [x] clearpotions