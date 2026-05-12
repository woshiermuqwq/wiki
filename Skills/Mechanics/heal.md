## 描述
Heals 目标实体 for the 指定的value. Can also "overheal"
the 生物 to more than its maximum health.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount     | a        | The amount to heal the 目标                                        | 1       |
| overheal  | oh        | 是否 to apply overhealing as additional MaxHealth          | false   |
| maxoverheal | maxabsorb, maxshield, mo, ma, ms | The maximum amount of overhealing that can be applied | 1 |


## 示例
Heals the casting 生物 for 20 health (10 hearts) when it is damaged. (20%
chance)
```yaml
  Skills:
  - heal{amount=20} @self ~onDamaged 0.2
```
##
Heals the casting 生物 for 20 health (10 hearts) when it is damaged. (20%
chance)
```yaml
  Skills:
  - heal{amount=20;overheal=true} @self ~onDamaged 0.2
```
If the 生物 is near or at full health, it will add those 20 health points
onto its existing health. Eg. 生物 with 20 health using this move will
now have 40 health. 20/20 + 20 = 40/20

The same 生物 with 17 health will gain 17 health on top of its maximum of
20. 17/20 + 20 = 37/20


## 别名
- [x] h


<!--TAGS-->
<!--tag:Health-->
