## 描述
检测生物受到的伤害范围，前提是技能树来自于 [onDamaged 触发器](/Skills/Triggers/onDamaged) 或 [onDamaged 光环](/skills/mechanics/ondamaged)。

## 属性

| 属性          | 别名        | 描述                 | 默认值 |
| ------------- | ----------- | -------------------- | ------ |
| damageAmount  | amount, a   | 要检测的伤害数值范围  | >0     |


## 示例
```yaml
  Conditions:
  - damageamount{amount=>10} true
```
