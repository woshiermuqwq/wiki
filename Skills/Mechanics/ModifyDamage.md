## 描述
Modifies the damage event that triggered the skill.  
This 机制 必须 synced, meaning that either the 机制 or the initial skill calling it 必须 run with the `sync=true` attribute.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount of the operation                                          | 1       |
| damagetype| type, dt, t | The type of the damage to evaluate                                 | ALL     |
| action    | mod, m    | The [modifier](/Stats#modifiers) to use                  | ADD<!--type:SpigotAttributeOperation-->|


## 示例
```yaml
  Skills:
  - modifyDamage{a=2;modifier=ADDITIVE_MULTIPLIER;sync=true} @self ~onAttack 0.2
```


## 别名
- [x] modDamage


<!--TAGS-->
<!--tag:Damage-->
<!--tag:Meta-->
