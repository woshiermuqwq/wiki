## 描述
通过玩家名称选取特定玩家。支持占位符。

## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| name      | n         | 玩家名称                                               | CarsonJF|


## 示例
以下生物会记住生成后第一个攻击它的玩家的名字，之后每 10 秒点燃该玩家一次
```yaml
VengefulMob:
  Type: ZOMBIE
  Skills:
  - setvariable{var=caster.targetedplayer;type=STRING;val=<trigger.name>} @self ~onDamaged =100% ?~isPlayer
  - ignite @PlayerByName{name=<caster.var.targetedplayer>} ~onTimer:200 ?variableisset{var=caster.targetedplayer}
```


## 别名
- [x] specificplayer
