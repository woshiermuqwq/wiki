## 描述
以a specific 玩家 by their 名称. Can be a 占位符为目标。

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 名称 | n | The 名称 of the 玩家 | CarsonJF|


## 示例
玩家 that first hit it 之后 it spawned, and will continue to ignite them every 10 seconds 之后 that的following 生物 will remeber the名称。
```yaml
VengefulMob:
  Type: ZOMBIE
  Skills:
  - setvariable{var=caster.targetedplayer;type=STRING;val=<trigger.name>} @self ~onDamaged =100% ?~isPlayer
  - ignite @PlayerByName{name=<caster.var.targetedplayer>} ~onTimer:200 ?variableisset{var=caster.targetedplayer}
```


## 别名
- [x] specificplayer