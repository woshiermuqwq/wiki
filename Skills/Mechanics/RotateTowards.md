## 描述
Rotates the 施法者 towards the 目标 location, up to a maximum 水平朝向(yaw)/俯仰角(pitch) increment from the current rotation. 


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| rotateyaw | 水平朝向(yaw)       | 是否 水平朝向(yaw) should be rotated                                        | true    |
| rotatepitch | 俯仰角(pitch)   | 是否 俯仰角(pitch) should be rotated                                      | false   |
| useEyeLocation | uel  | 是否 施法者的 eye location should be used as the base to calculate the new 水平朝向(yaw)/俯仰角(pitch)                                                                                  | false   |
| maxyaw    | my, y     | The maximum increment the 水平朝向(yaw) can have                               | 0       |
| maxpitch  | mp, p     | The maximum increment the 俯仰角(pitch) can have                             | 0       |


## 示例
```yaml
SlowTurn:
  Skills:
  - rotatetowards{pitch=true;uel=true;maxyaw=1;maxpitch=0.5;repeat=199;repeatInterval=2} @Trigger ~onInteract
```


## 别名
- [x] rotateto


<!--TAGS-->
<!--tag:Movement:Rotation-->
