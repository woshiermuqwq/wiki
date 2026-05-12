## 描述
M使生物move 朝向 specified 方块 类型。


## 属性
| 属性 | 别名 | Description | 默认 |
|----------------|----------|-----------------------------------------------|---------|
| material | m, mat | The 方块 类型 to 目标 | IRON_ORE<!--类型:方块--> |
| 半径 | r, search, searchrange | The 半径 in which to search 对于 方块 | 8 |
| radiusy | ry, verticalsearchrange, vsearch, yr, yradius | The y 半径 in which to search 对于 方块 | 2 |
| 速度 | s | The 速度 of 移动 | 0.9 |


### 示例
```yaml
ExampleMob:
  Type: Pig
  AIGoalSelectors:
    - clear
    - moveToBlock{material=STONE;radius=8;radiusY=2;speed=0.9}
```


## 别名
- [x] gotoblock