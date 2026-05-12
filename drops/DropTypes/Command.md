## 描述
掉落时，一条指令仅由控制台执行一次，无论指定的数量是多少。
你可以使用施法者范围和触发器范围的占位符，分别从掉落指令的生物和击杀它的实体获取信息。
`<drop.amount>` [占位符](/Skills/Placeholders#misc-placeholders)可用于获取原始数量。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| command   | cmd, c    | 要执行的指令                                               |         |
| ascaster  | caster, ac, sudo, asmob | 是否以掉落该物品的生物身份执行指令，而非控制台 | false |
| astrigger | trigger, at | 是否以触发掉落者的身份执行指令，而非控制台 | false |
| asop      | op, operator | 是否以完整权限执行指令      | false   |


## 示例
```yaml
  Drops:
  - command{c="say 你好世界！我被掉落了 <drop.amount> 次！"} 1-10 1
```


## 别名
- [x] cmd
