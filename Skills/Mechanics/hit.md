## 描述
Simulates a physical hit from the 施法者. Takes items (including enchantments), melee stats, attribute modifiers, and potion effects into account.  
继承 [Damage](/skills/技能/damage) 技能.  


## 属性
| 属性        | 缩写 | 描述                         | 默认值 |
|------------------|---------|-------------------------------------|---------|
| multiplier       | m       | The percentage of damage to deal    | 1       |
| forcedDamage     | fd, forced | If this attribute is set, the one specified will be the amount of flat damage that will be inflicted, without consideration for attribute modifiers and similar other modifiers |
| triggerSkills | ts    | 是否 the damage 技能 should also be able to 触发 `onAttack` related 触发       | true |
| scaleByAttackCooldown | sbac | 是否 to scale the damage by the weapon's attack 冷却 | false |
> This 技能 继承 [Damage](/skills/技能/damage) 技能
>> - `amount` 属性会被忽略
>> - The `triggerSkills` attribute is **defaulted** at `true`
>> - The `damagecause` attribute is **set** at `ENTITY_ATTACK`
>> - The `tags` attribute will always have a `melee` tag.


## 示例
此示例将 make the 生物 deal 150% of its configured melee damage to its
目标 when its being attacked. Ignoring armors. In this case it would deal 15 damage total since 生物的 melee damage is 10.
```yaml
HitMob:
  Type: Zombie
  Damage: 10
  Skills:
    - hit{m=1.5;ia=true} @target ~onDamaged
```


## 别名
- [x] physicalDamage
- [x] meleeHit


<!--TAGS-->
<!--tag:Damage-->