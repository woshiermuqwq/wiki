## 描述
Moves 朝向 目标 to be 在...内 a certain 范围


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | The 速度 modifier | 1 |
| minrange | minrange, 范围, r, 距离, d | The minimum 范围 to 从 目标 实体 | 10.0 |
| maxrange | maxrange, maxr | The maximum 范围 to 从 目标 实体 | 32.0 |


## 示例
```yaml
  AIGoalSelectors:
  - clear
  - moveTowardsDistanceOfTarget{s=2;minr=3;maxrange=6}
```


## 别名
- [x] moveWithin