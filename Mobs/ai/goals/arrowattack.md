## 描述
一个ranged 实体 can use的basic ranged 攻击。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | 移动 速度 modifier | 1 |
| attackspeedmax | smax | The maximum 间隔 per shot (in ticks) | 60 |
| attackspeedmin | amin | The minimum 间隔 per shot (in ticks) | 20 |
| attackradius | 半径, r | The 攻击 半径 of this AI 目标 | 15 |


## 示例
```yaml
ExampleMob:
  Type: Skeleton
  AIGoalSelectors:
  - clear
  - rangedAttack{speed=1;smax=60;amin=20;radius=15}
```


## 别名
- [x] rangedAttack