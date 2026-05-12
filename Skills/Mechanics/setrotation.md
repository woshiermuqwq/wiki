## 描述
Changes the rotation of the 目标 (only works on non-player entities).


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| relative  | r, rel    | If the change is relative to the 目标, boolean                     | false   |
| 水平朝向(yaw)       | y         | The new 水平朝向(yaw)                                                          | 0       |
| 俯仰角(pitch)     | p         | The new 俯仰角(pitch)                                                        | 0       |


## 示例
```yaml
  Skills:
  - setrotation{relative=true;pitch=-45}
  - ...
```


## 别名
- [x] setrot


<!--TAGS-->
<!--tag:Movement:Rotation-->
