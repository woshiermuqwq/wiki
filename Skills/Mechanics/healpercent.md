## 描述
治疗目标实体 for a percentage of its max-health. Like the
heal skill, can also overheal mobs by a percentage.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| multiplier | m, amount, a | The percentage to heal, refers to the targets max-health.<br>0.1 = 10%, 1 = 100% and so on                                                                                      | 0.1     |
| overheal   | oh       | Whether or not to apply overhealing as additional MaxHealth          | false   |
| maxoverheal | maxabsorb, maxshield, mo, ma, ms | The maximum amount of overhealing that 可以 applied | 0 |


## 示例
This will make the casting mob heal for 20% of its health each time it
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
