## 描述
Deals damage equal to a percent of 玩家的 max health, where 1 is
100%. 继承 [Damage](/skills/技能/damage) 技能.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| percent   | p         | The percentage to damage the 目标                                  | 0.1     |
| currentHealth | current, c, ch |是否 it calculates the percent from your original or current health| false   |
> This 技能 继承 [damage](/skills/技能/damage) 技能
>> `amount` 属性会被忽略 


## 示例
Hurts the 目标 for half (50%) of its max health.
```yaml
  Skills:
  - damagepercent{percent=0.5}
```


## 别名
- [x] damagepercent
- [x] percentdamage



<!--TAGS-->
<!--tag:Damage-->
