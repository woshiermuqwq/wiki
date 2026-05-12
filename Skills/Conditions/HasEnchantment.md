## 描述
检测目标生物手持的物品是否拥有某个附魔。有效附魔列表可在 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html) 中找到。

## 属性
| 属性        | 别名            | 描述               | 默认值 |
| ----------- | --------------- | ------------------ | ------ |
| enchantment | type, ench, e, t| 要检测的附魔        | ANY    |
| level       | lvl, l          | 要检测的附魔等级    | >0     |


## 示例：
```yaml
  TargetConditions:
  - hasenchantment{e=DAMAGE_ALL;l=>3} true
```

## 别名
- [x] hasEnchant
