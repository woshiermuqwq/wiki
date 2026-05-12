## 描述
Applies an absorb shield to the target entity for a percentage of their
max health.  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| multiplier| m         | The multiplier. The value of the shield 将会 `maxhealth*multiplier` | 0.1   |
| maxabsorb | maxshield, ma, ms | The max value of the shield must not be greater the max health of the mob multiplied by this value                                                      | `Multiplier's value` |


## 示例
Adds shield absorption hearts to caster with a multiplier.
```yaml
  Skills:
  - shieldPercent{multiplier=2;mS=2.5} @self ~onTimer:2000
  - ...
```
