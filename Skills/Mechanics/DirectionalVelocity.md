## 描述
Changes the velocity on the target entity on a specific vector


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| yaw       |           | The yaw of the vector 对于velocity change                        |         |
| pitch     |           | The pitch of the vector 对于velocity change                      |         |
| velocity  | v         | The magnitude of the velocity change                                 |         |
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
