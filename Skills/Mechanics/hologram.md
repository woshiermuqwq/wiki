## 描述
Spawns a hologram at a 目标 location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
|    text   | t         | The text to show                                       | Hologram Text Missing |
|    stay   | time, staytime  | The duration of the hologram in ticks                          | 100     |


## 示例
Creates a hologram above the 生物 when the 生物 gets right clicked, which displays for 100 ticks.
```yaml
  Skills:
  - holo{text="Example Text";time=100} @selflocation{y=1.6} ~onInteract
```

## 别名
- [x] summonhologram
- [x] holo