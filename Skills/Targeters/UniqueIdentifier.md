## 描述
Ta以a specific 实体 by their UUID. Can be a 占位符为目标。
This 目标选择器 will 目标 任何事物, 无论 目标选择器 过滤


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| uuid | u | The uuid of the 实体 | 0 |


## 示例
The following 生物 will remember the uuid of the 实体 that first hit it 之后 it spawned, and will continue to ignite them every 10 seconds 之后 that
```yaml
VengefulMob:
  Type: ZOMBIE
  Skills:
  - setvariable{var=caster.targetedentity;type=STRING;val=<trigger.uuid>} @self ~onDamaged =100% ?~isLiving
  - ignite @UniqueIdentifier{uuid=<caster.var.targetedentity>} ~onTimer:200 ?variableisset{var=caster.targetedentity}
```


## 别名
- [x] uuid