## 描述
Simulates a physical hit from the caster. Takes items (including enchantments), melee stats, attribute modifiers, and potion effects into account.  
Inherits every attribute of the [Damage](/skills/mechanics/damage) 机制.  


## 属性
| Attribute        | Aliases | Description                         | 默认值 |
|------------------|---------|-------------------------------------|---------|
| multiplier       | m       | The percentage of damage to deal    | 1       |
| forcedDamage     | fd, forced | If this attribute is set, the one specified 将会 the amount of flat damage that 将会 inflicted, without consideration for attribute modifiers and similar other modifiers |
| triggerSkills | ts    | 伤害机制是否也能触发 `onAttack` 相关触发器       | true |
| scaleByAttackCooldown | sbac | Whether to scale the damage by the weapon's attack cooldown | false |
> 此机制继承所有[Damage](/skills/mechanics/damage) 机制
>> - The `amount` attribute is ignored
>> - The `triggerSkills` attribute is **defaulted** at `true`
>> - The `damagecause` attribute is **set** at `ENTITY_ATTACK`
>> - The `tags` attribute will always have a `melee` tag.


## 示例
This example will make the mob deal 150% of its configured melee damage to its
target when its being attacked. Ignoring armors. In this case it would deal 15 damage total since the mob's melee damage is 10.
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
