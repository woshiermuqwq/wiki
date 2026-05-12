## 描述
Sets the max health of the 目标 entity.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount to set max health by                                      | 1.0     |
| mode      | m         | The method of setting max health. `STATIC` will set the max health directly to amount value. `SCALE` will set the new max health but also scale the current health of the entity accordingly                                                                                    | STATIC<!--type:SetMaxHealth_Mode-->|


## 示例
此示例将 simply set the new max health of the entity to 5. If
the new max health is lower than 实体的 current health, the
current health 将被设为 to the new max health.
```yaml
  Skills:
  - setmaxhealth{amount=5;mode=STATIC} @self ~onInteract
  - ...
```
##
此示例将 increase the new max health of the 生物 to 5 and scale
it's remaining HP up as well. If the entity has 15/20 health and is then
interacted with, instead of the new health being 5/5 it would become
3/5.
```yaml
  Skills:
  - setmaxhealth{amount=5;mode=SCALE} @self ~onInteract
  - ...
```


## 别名
- [x] setmaxhp


<!--TAGS-->
<!--tag:Health-->
