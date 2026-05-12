## 描述
通过实体的 UUID 选取特定实体。支持占位符。  
此目标选择器会选取任何实体，不受目标选择器过滤器的影响


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| uuid      | u         | 实体的 UUID                                               | 0       |


## 示例
以下生物会记住生成后第一个攻击它的实体的 UUID，之后每 10 秒点燃该实体一次
```yaml
VengefulMob:
  Type: ZOMBIE
  Skills:
  - setvariable{var=caster.targetedentity;type=STRING;val=<trigger.uuid>} @self ~onDamaged =100% ?~isLiving
  - ignite @UniqueIdentifier{uuid=<caster.var.targetedentity>} ~onTimer:200 ?variableisset{var=caster.targetedentity}
```


## 别名
- [x] uuid
