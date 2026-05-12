## 描述
Changes the target color, can only be applied to colorable mobs such as
shulkers or sheeps.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| color     | c         | The color name                                                       |<!--type:DyeColor-->|


## 示例
Sets the color of colorable mobs to blue when it spawns.
```yaml
  Skills:
  - setcolor{color=blue} @self ~onSpawn
  - ...
```


## 别名
- [x] setcolor
