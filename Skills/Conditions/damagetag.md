## 描述
检查引发当前技能树的伤害是否具有特定标签。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tag       | t         | 要检查的标签                                             |         |
| value     | val, v, b, bool, boolean | 如果为 true，检查标签的存在<br>如果为 false，检查标签的不存在 | true  |


## 示例
```yaml
Conditions:
- damageTag{tag=WITCHCURSES}
```
用于检查 [Damage](/skills/mechanics/damage) 技能或继承其属性的技能中指定的伤害标签。


## 别名
- [x] damagehastag