## 描述
检查目标实体装备的物品是否拥有某种附魔。有效的附魔列表可在 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html) 中找到。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
|enchantment|type, ench, e, t| 要测试的附魔                                     | ANY     |
| level     | lvl, l    | 要测试的等级                                                | >0      |


## 示例：
```yaml
  TargetConditions:
  - hasenchantment{e=DAMAGE_ALL;l=>3} true
```


## 别名
- [x] hasEnchant