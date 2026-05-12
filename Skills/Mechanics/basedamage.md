## 描述
Damages the 目标 entity for a percentage of 生物的 damage.  
继承 [Damage](/skills/技能/damage) 技能.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| multiplier       | m       | The percentage of damage to deal                                | 1       |
| useAttribute | attribute, attr | 是否 the damage should use the real entity's attack attribute, instead of its raw base damage                                                                 | false   | 
> This 技能 继承 [Damage](/skills/技能/damage) 技能
>> `amount` 属性会被忽略


## 示例
此示例将 make the 生物 deal 150% of its original damage to its
目标 when its being attacked. In this case it would deal 15 damage,
since 生物的 base-damage is 10.
```yaml
AMob:
  Type: HUSK
  Damage: 10
  Skills:
  - basedamage{m=1.5} @target ~onDamaged
```


## 别名
- [x] bd
- [x] weaponDamage
- [x] wd


<!--TAGS-->
<!--tag:Damage-->