## 描述
Sets the display name of the 施法者. This will not work with players.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| name      | n         | The name to set                                                      |         |


## 示例
Sets the name of the 生物 to "newmobname" when the 生物 is damaged.
```yaml
Skills:
  - setname{name=newmobname} @self ~onDamaged 1
```
##
This will set the name of the 生物 to the name it has in its Display: option when it is damaged and every 10 ticks when it is in combat. 这是一个示例：how to make your 生物 update any placeholders in its name. In this example we are doing it to update the <施法者.hp> placeholder.
```yaml
MySkeleton:
  Type: Skeleton
  Display: 'Skeleton <caster.hp>/<caster.mhp><&heart>'
  Skills:
  - setname{name=<caster.name>;delay=2} @self ~onDamaged
  - setname{name=<caster.name>;delay=2} @self ~onTimer:10 ?incombat
```