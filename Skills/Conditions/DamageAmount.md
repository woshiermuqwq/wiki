## 描述
检查实体所受伤害的范围，前提是技能树源自 [onDamaged 触发器](/Skills/Triggers/onDamaged) 或 [onDamaged 光环](/skills/mechanics/ondamaged)。


## 属性

| 属性 | 别名      | 描述                                                       | 默认值 |
|-----------|--------------|-------------------------------------------------------------------|---------|
| damageAmount | amount, a | 要检查的伤害范围                                      | >0      |


## 示例
```yaml
  Conditions:
  - damageamount{amount=>10} true
```