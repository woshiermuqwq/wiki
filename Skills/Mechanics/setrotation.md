## 描述
Changes the rotation of the target (only works on non-player entities).


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| relative  | r, rel    | If the change is relative to the target, boolean                     | false   |
| yaw       | y         | The new yaw                                                          | 0       |
| pitch     | p         | The new pitch                                                        | 0       |


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
