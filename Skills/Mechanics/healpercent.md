## 描述
Heals the 目标 entity for a percentage of its max-health. Like the
heal skill, can also overheal 生物 by a percentage.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| multiplier | m, amount, a | The percentage to heal, refers to 目标的 max-health.<br>0.1 = 10%, 1 = 100% and so on                                                                                      | 0.1     |
| overheal   | oh       | 是否 to apply overhealing as additional MaxHealth          | false   |
| maxoverheal | maxabsorb, maxshield, mo, ma, ms | The maximum amount of overhealing that can be applied | 0 |


## 示例
This will make the casting 生物 heal for 20% of its health each time it
gets to attack.
```yaml
  Skills:
  - healpercent{m=0.2} @self ~onAttack
```


## 别名
- [x] percentheal
- [x] hp


<!--TAGS-->
<!--tag:Health-->
