## 描述
检测目标最近一次受到的伤害原因。
有效伤害原因列表可在 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html) 中找到。

## 属性

| 属性         | 别名      | 描述               | 默认值          |
| ------------ | --------- | ------------------ | --------------- |
| damagecause  | cause, c  | 要匹配的伤害原因    | ENTITY_ATTACK<!--type:DamageCause--> |


## 示例
```yaml
  Conditions:
  - lastdamagecause{c=ENTITY_ATTACK} true
```
