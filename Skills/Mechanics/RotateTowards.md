## 描述
Rotates the caster towards the target location, up to a maximum yaw/pitch increment from the current rotation. 


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| rotateyaw | yaw       | Whether yaw 应当 rotated                                        | true    |
| rotatepitch | pitch   | Whether pitch 应当 rotated                                      | false   |
| useEyeLocation | uel  | Whether the caster's eye location 应当 used as the base to calculate the new yaw/pitch                                                                                  | false   |
| maxyaw    | my, y     | The maximum increment the yaw can have                               | 0       |
| maxpitch  | mp, p     | The maximum increment the pitch can have                             | 0       |


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
