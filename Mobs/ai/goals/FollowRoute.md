## 描述
使生物follow a specific path, one time 仅。


## 属性

| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| points | p | The points of the path, in a x1,y1,z1;x2,y2,z2;x3,y3,z3; syntax | |
| 速度 | s | The 速度 of the 移动 | |
| tolerance | t | The minimum 距离 the 生物 必须为 from a point 之前 moving to the next one| 3 |



## 示例
```yaml
  AIGoalSelectors:
  - clear
  - followRoute{p=1,0,0;12,0,10}
```


## 别名
- [x] followPath