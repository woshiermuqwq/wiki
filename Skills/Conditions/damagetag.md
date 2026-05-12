## 描述
检测触发当前技能树的伤害是否带有特定标签。

## 属性
| 属性      | 别名                    | 描述                                               | 默认值 |
| --------- | ----------------------- | -------------------------------------------------- | ------ |
| tag       | t                       | 要检测的标签                                        |        |
| value     | val, v, b, bool, boolean | 设为 true 则检查存在该标签<br>设为 false 则检查不存在 | true   |


## 示例
```yaml
Conditions:
- damageTag{tag=WITCHCURSES}
```
用于检测 [Damage](/skills/mechanics/damage) 技能或继承其属性的技能所指定的伤害标签。

## 别名
- [x] damagehastag
