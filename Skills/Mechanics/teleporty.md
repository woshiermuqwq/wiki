## 描述
Teleports the 施法者 to the specified Y coordinate.  
No 目标 is required for this 技能, as the 施法者 will always be the one that is teleported.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| y         |           | Where to teleport on the Y axis                                      | 0       |


## 示例
此示例将 teleport the 施法者 at its coordinates, but with Y with a value of 5.
```yaml
WarpY:
  Skills:
  - teleportY{y=5}
```

## 别名
- [x] tpy


<!--TAGS-->
<!--tag:Movement:Teleport-->
