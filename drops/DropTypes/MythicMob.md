## 描述
掉落时，生成一些指定的 MythicMobs


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, mob, m| 要生成的生物类型。可以是 Mythic 生物类型或常规实体类型                                                                 | SKELETON|
| amount    | a         | 要生成的生物数量。                                        | 1       |
| level     | lvl, l    | 要生成生物的等级                                  | 0       |
| radius    | r, noise, n| 生物将在目标周围生成的半径 | 0       |
| yRadius   | yr, ynoise, yn| 覆盖半径的 Y 分量。                             | radius  |
| yRadiusUpOnly | yradiusonlyup, yruo, yu| Y 轴散布是否仅向上，不向下。                                                                                      | false   |
| velocity | v, force, f| 生物生成后的最大初始速度向量，使生物沿随机方向推进                                                                | 0       |
| yvelocity| yv, yforce, yf | 与 velocity 相同，但仅应用于 Y 轴                 | velocity|
| onSurface | os, s     |(true/false) 生物是否仅应在固体方块上生成 | false   |


## 示例
```yaml
  Drops:
  - mythicmob{type=IncredibleLootchest;velocity=1;os=true} 1 1
```


## 别名
- [x] mythicmobs
- [x] mm
