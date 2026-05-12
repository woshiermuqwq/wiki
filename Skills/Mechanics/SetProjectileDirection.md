## 描述
Sets the calling 弹射物's movement direction to the given 目标


## 属性
## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| magnitude | m         | The magnitude of the change. A value of 1 will make the 弹射物 change direction perfectly. Lower values will interpolate the changed direction position between 0 and 100% | 1 |


## 示例
Once called by a 弹射物, this 技能 will change 弹射物的 direction based on its current direction
```yaml
  Skills:
  - setprojectiledirection @ProjectileForward{f=10;rot=45}
```


<!--TAGS-->
<!--tag:Meta-->
