## 描述
设置显示名称 of the caster. This 将不会 work with players.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| name      | n         | 要设置的名称                                                      |         |


## 示例
Sets the name of the mob to "newmobname" when the mob is damaged.
```yaml
Skills:
  - setname{name=newmobname} @self ~onDamaged 1
```
##
This will set the name of the mob to the name it has in its Display: option when it is damaged and every 10 ticks when it is in combat. This is an example of how to make your mob update any placeholders in its name. In this example we are doing it to update the <caster.hp> placeholder.
```yaml
MySkeleton:
  Type: Skeleton
  Display: 'Skeleton <caster.hp>/<caster.mhp><&heart>'
  Skills:
  - setname{name=<caster.name>;delay=2} @self ~onDamaged
  - setname{name=<caster.name>;delay=2} @self ~onTimer:10 ?incombat
```
