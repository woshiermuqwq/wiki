## 描述
Sets the calling projectile's movement direction to the given target


## 属性
## Attributes
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| magnitude | m         | The magnitude of the change. A value of 1 will make the projectile change direction perfectly. Lower values will interpolate the changed direction position between 0 and 100% | 1 |


## 示例
Once called by a projectile, this 机制 will change the projectile's direction based on its current direction
```yaml
  Skills:
  - setprojectiledirection @ProjectileForward{f=10;rot=45}
```


<!--TAGS-->
<!--tag:Meta-->
