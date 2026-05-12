## 描述
Deals damage equal to a percent of the player's max health, where 1 is
100%. Inherits every attribute of the [Damage](/skills/mechanics/damage) 技能.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| percent   | p         | The percentage to damage the target                                  | 0.1     |
| currentHealth | current, c, ch |Whether it calculates the percent from your original or current health| false   |
> 此技能继承所有[damage](/skills/mechanics/damage) 技能
>> The `amount` attribute is ignored 


## 示例
Hurts the target for half (50%) of its max health.
```yaml
  Skills:
  - damagepercent{percent=0.5}
```


## 别名
- [x] damagepercent
- [x] percentdamage



<!--TAGS-->
<!--tag:Damage-->
