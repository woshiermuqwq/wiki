## 描述
Causes a lightning strike at the 目标 entity or location, dealing
damage and potentially setting the 目标 entity or block on fire if it
is not currently raining, but only if fire spread is enabled.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| damage    | d         | The amount of damage the strike will deal                            | 0.01337 |
> This 技能 inherits every *inheritable* attribute of the [Damage](/Skills/技能/Damage) 技能

  
## 示例
此示例将 summon a lightning bolt to the designated targeters.
```yaml
StaticSheep:
  Type: SHEEP
  Skills:
  - lightning @EntitiesInRadius{r=10} ~onTimer:100
```
##
此示例将 summon a lightning bolt to the designated targeters and deal 6 damage.
```yaml
StaticSheep:
  Type: SHEEP
  Skills:
  - lightning{d=6} @EntitiesInRadius{r=10} ~onTimer:100
```


<!--TAGS-->
<!--tag:Damage-->
