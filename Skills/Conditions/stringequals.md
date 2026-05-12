## 描述
检查 value1 是否等于 value2。两个值都可以使用[变量](/Skills/Variables)和[占位符](/Skills/Placeholders)。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| value1    | val1, v1, string, s                     | 第一个值                        |         |
| value2    | val2, v2, value, val, v, equals, eq, e  | 第二个值                       |         |


## 示例
```yaml
  Conditions:
  - stringequals{val1="yes!";val2="yes!"} true
```
```yaml
  Conditions:
  - stringequals{val1="%denizen_<player[<trigger.uuid>].item_in_hand.has_nbt[special_item]>%";val2="true"} true
```
使用 Denizen、PlaceholderAPI 和 MythicMobs 检查玩家手持的物品是否具有 Denizen 的 "special_item" NBT 键。<trigger.uuid> 是 MythicMobs 的占位符，在 PlaceholderAPI 解析 Denizen 标签之前会被先解析。
```yaml
  Conditions:
  - stringequals{val1="%denizen_<player[<trigger.uuid>].item_in_hand.raw_nbt.get[mythic_type].after[string:]>%";val2="SomeMythicItem"} true
```


## 别名
- [x] stringEq