## 描述
Spawns a hologram at a target location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
|    text   | t         | The text to show                                       | Hologram Text Missing |
|    stay   | time, staytime  | The duration of the hologram in ticks                          | 100     |


## 示例
Creates a hologram above the mob when the mob gets right clicked, which displays for 100 ticks.
```yaml
  Skills:
  - holo{text="Example Text";time=100} @selflocation{y=1.6} ~onInteract
```

## 别名
- [x] summonhologram
- [x] holo
