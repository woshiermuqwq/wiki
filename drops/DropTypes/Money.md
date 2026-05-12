## 描述
掉落时，如果触发者是玩家，则通过 `Vault` 插件给予货币。
`<drop.amount>` [占位符](/Skills/Placeholders#misc-placeholders)可在奖励消息中使用，以获取正在给予的货币数量。此消息可在 `config-general.yml` 文件中配置。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| sendmessage | sm      | 是否应向玩家发送预配置的消息       | true    |


## 示例
```yaml
  Drops:
  - money 20
```


## 别名
- [x] vault
- [x] currency
