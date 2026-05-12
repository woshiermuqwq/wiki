## 描述
Damages the target entity for a percentage of the mob's damage.  
Inherits every attribute of the [Damage](/skills/mechanics/damage) 技能.  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| multiplier       | m       | The percentage of damage to deal                                | 1       |
| useAttribute | attribute, attr | Whether the damage should use the real entity's attack attribute, instead of its raw base damage                                                                 | false   | 
> 此技能继承所有[Damage](/skills/mechanics/damage) 技能
>> The `amout` attribute is ignored


## 示例
This example will make the mob deal 150% of its original damage to its
target when its being attacked. In this case it would deal 15 damage,
since the mob's base-damage is 10.
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
