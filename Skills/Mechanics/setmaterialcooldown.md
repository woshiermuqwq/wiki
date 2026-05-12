## 描述
Sets a cooldown on items of a specified material on the target player


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
|  material | mat, m    | The material to set the cooldown to                              | ENDER_PEARL<!--type:Material--> |
| duration  | d         | 冷却的持续时间 in ticks                                | 100     |


## 示例
```yaml
  Skills:
  - setmaterialcooldown{m=CHORUS_FRUIT;d=150} @PIR{r=10}
```
