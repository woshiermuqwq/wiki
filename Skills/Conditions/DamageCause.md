## 描述
检查实体所受伤害的原因，前提是技能树源自 [onDamaged 触发器](/Skills/Triggers/onDamaged) 或 [onDamaged 光环](/skills/mechanics/ondamaged)。  
有效的伤害原因列表可在 [Spigot DamageCause javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html) 中找到。


## 属性

| 属性 | 别名   | 描述                                                    | 默认值       |
|-----------|-----------|----------------------------------------------------------------|---------------|
| damagecause | cause, c | 要匹配的伤害原因                                     | ENTITY_ATTACK<!--type:DamageCause--> |


## 示例
```yaml
  Conditions:
  - damagecause{cause=ENTITY_ATTACK} true
```