## 描述
An advanced ranged 攻击 that can 经常 cause the shooter to strafe backwards or clockwise.


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | 移动 速度 modifier | 1 |
| attackradius | 半径,r | The 半径 of the 攻击 | 15 |
| attackspeedmax | smax | The maximum 攻击 速度 | 20 |


## 示例
```yaml
ExampleMob:
  Type: Skeleton
  AIGoalSelectors:
    - clear
    - bowattack{speed=1;radius=15}
```


## 别名
- [x] skeletonbowattack
- [x] bowshoot
- [x] bowmaster