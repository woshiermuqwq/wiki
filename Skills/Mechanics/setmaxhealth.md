## 描述
设置最大生命值 of the target entity.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount to set max health by                                      | 1.0     |
| mode      | m         | The method of setting max health. `STATIC` will set the max health directly to amount value. `SCALE` will set the new max health but also scale the current health of the entity accordingly                                                                                    | STATIC<!--type:SetMaxHealth_Mode-->|


## 示例
This example would simply set the new max health of the entity to 5. If
the new max health is lower than the entity's current health, the
current health 将会 set to the new max health.
```yaml
  Skills:
  - setmaxhealth{amount=5;mode=STATIC} @self ~onInteract
  - ...
```
##
This example would increase the new max health of the mob to 5 and scale
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
