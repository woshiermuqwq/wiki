## 描述
Applies an [光环] to the 目标 that applies a specific [stat] to them.  
The buff received is multiplied by the amount of stacks the 光环 has


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| stat      | s         | The [stat] to apply                                           |<!--type:Stat-->|
| type      | t, modifier, mod, m | The [stat modifier] to use         | ADDITIVE<!--type:StatModifier-->|
| value     | val, v    | The value to use for the stat                                        | 0.0     |

> This 技能 继承 [光环] 技能


## 示例
The following 光环 will double the critical strike chance of the 施法者 for 5 seconds
```yaml
  Skills:
  - stataura{auraName=exampleaura;d=100;stat=CRITICAL_STRIKE_CHANCE;type=COMPOUND_MULTIPLIER;val=2} @self
```


## 别名
- [x] statbuff
- [x] statdebuff


<!-- LINKS -->
[aura]: /skills/mechanics/aura
[stat]: Stats
[stat modifier]: Stats#modifiers


<!--TAGS-->
<!--tag:Stat-->
<!--tag:Meta-Mechanic:Aura-->
