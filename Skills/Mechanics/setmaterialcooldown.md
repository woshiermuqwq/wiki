## 描述
Sets a 冷却 on items of a specified material on the 目标 player


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
|  material | mat, m    | The material to set the 冷却 to                              | ENDER_PEARL<!--type:Material--> |
| duration  | d         | The duration of the 冷却 in ticks                                | 100     |


## 示例
```yaml
  Skills:
  - setmaterialcooldown{m=CHORUS_FRUIT;d=150} @PIR{r=10}
```