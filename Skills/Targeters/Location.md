## 描述
以specified coordinates in a 世界为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 位置 | loc, l, c | The full 位置, in the `x,y,z,yaw,pitch` 格式 | |
| x | | If `location` 不是 set, 它是 the x coordinate of the 目标 位置 | 0 |
| y | | If `location` 不是 set, 它是 the y coordinate of the 目标 位置 | 0 |
| z | | If `location` 不是 set, 它是 the z coordinate of the 目标 位置 | 0 |
| yaw | | If `location` 不是 set, 它是 the yaw of the 目标 位置 | 0 |
| pitch | | If `location` 不是 set, 它是 the pitch of the 目标 位置 | 0 |
| 世界 | w | The 世界 to 目标. If not set, 它将 目标 the 施法者 世界 | |


## 示例
```yaml
ExampleSkill:
  Skills:
  - setblock{m=DIAMOND_BLOCK} @Location{location=100,70,-120,0,0}
  - setblock{m=EMERALD_BLOCK} @Location{x=100;y=71;z=-120}
```


## 别名
- [x] l
- [x] loc