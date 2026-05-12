## 描述
Teleports the caster to the specified Y coordinate.  
No target is required for this 机制, as the caster will always be the one that is teleported.  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| y         |           | Where to teleport on the Y axis                                      | 0       |


## 示例
This example would teleport the caster at its coordinates, but with Y with a value of 5.
```yaml
WarpY:
  Skills:
  - teleportY{y=5}
```

## 别名
- [x] tpy


<!--TAGS-->
<!--tag:Movement:Teleport-->
