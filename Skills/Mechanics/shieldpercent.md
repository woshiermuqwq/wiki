## 描述
Applies an absorb 护盾 to the 目标 entity for a percentage of their
max health.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| multiplier| m         | The multiplier. The value of the 护盾 will be `maxhealth*multiplier` | 0.1   |
| maxabsorb | maxshield, ma, ms | The max value of the 护盾 must not be greater the max health of the 生物 multiplied by this value                                                      | `Multiplier's value` |


## 示例
Adds 护盾 absorption hearts to 施法者 with a multiplier.
```yaml
  Skills:
  - shieldPercent{multiplier=2;mS=2.5} @self ~onTimer:2000
  - ...
```