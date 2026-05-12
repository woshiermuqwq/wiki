## 描述
Causes a lightning strike 在target entity or location, dealing
damage and potentially setting the target entity or block on fire if it
is not currently raining, but only if fire spread is enabled.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| damage    | d         | The amount of damage the strike will deal                            | 0.01337 |
> This 机制 inherits every *inheritable* attribute of the [Damage](/Skills/Mechanics/Damage) 机制

  
## 示例
This example will summon a lightning bolt to the designated targeters.
```yaml
StaticSheep:
  Type: SHEEP
  Skills:
  - lightning @EntitiesInRadius{r=10} ~onTimer:100
```
##
This example will summon a lightning bolt to the designated targeters and deal 6 damage.
```yaml
StaticSheep:
  Type: SHEEP
  Skills:
  - lightning{d=6} @EntitiesInRadius{r=10} ~onTimer:100
```


<!--TAGS-->
<!--tag:Damage-->
