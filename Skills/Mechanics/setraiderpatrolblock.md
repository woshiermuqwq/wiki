## 描述
Sets the target raider to patrol the given location


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| location  |block, l, b| A [Location Targeter], whose targeted location 将会 the specified one |<!--type:Targeter-->|                                       


## 示例
```yaml
  Skills:
  - setRaiderPatrolBlock{l=@TrackedLocation} @self
```

## 别名
- [x] setRaiderBlock

[Location Targeter]: /Skills/Targeters#single-location-targeters
