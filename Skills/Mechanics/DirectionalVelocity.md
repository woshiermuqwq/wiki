## 描述
Changes the 速度 on the 目标 entity on a specific vector


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 水平朝向(yaw)       |           | The 水平朝向(yaw) of the vector for the 速度 change                        |         |
| 俯仰角(pitch)     |           | The 俯仰角(pitch) of the vector for the 速度 change                      |         |
| 速度  | v         | The magnitude of the 速度 change                                 |         |
| mode      | m         | The mode to use                      | SET<!--type:SET,ADD,REMOVE,MULTIPLY,DIVIDE,MINIMUM--> |

### Mode Attribute
Accepted values are
- `SET`
- `ADD`
- `MULTIPLY`
- `REMOVE`
- `DIVIDE`
- `MINIMUM`


## 示例
```yaml
  Skills:
  - directionalvelocity{yaw=180;v=1;mode=MINIMUM} @self
```


## 别名
- [x] dvelocity


<!--TAGS-->
<!--tag:Movement-->