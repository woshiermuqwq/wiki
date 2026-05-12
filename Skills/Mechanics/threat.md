## 描述
Modifies 生物的 仇恨 value towards the 目标. Requires the casting 生物
have [仇恨 Tables](/生物/ThreatTables) enabled in order to have any effect.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount of 仇恨 to give the 目标. Can be negative.            | 1       |
| mode      | m         | The [mode](#mode-attribute) of the operation                         | add<!--type:ThreatMode-->|


### Mode Attribute
| Mode      | 缩写   | 描述                                                                    |
|-----------|-----------|--------------------------------------------------------------------------------|
| add       |           | Adds `amount` 仇恨 to the 目标 entity                                      |
| remove    |           | Removes `amount` 仇恨 from the 目标 entity                                 |
| multiply  |           | Multiplies the 仇恨 against the 目标 entity by `amount`                    |
| divide    |           | Divides the 仇恨 against the 目标 entity by `amount`                       |
| set       |           | Sets the 仇恨 against the 目标 entity to `amount`                          |
| reset     | delete    | Remove all 仇恨 from the 目标 entity                                       |
| forcetop  | force, top, topthreat, taunt | Gives the 目标 enough 仇恨 to be moved to the top of the 仇恨 list |


## 示例
此示例将 set the nearest player's 仇恨 level to a very high
amount.
```yaml
Fixate:
  Skills:
  - threat{amount=10000} @NearestPlayer ~onSpawn
```


## 别名
- [x] threatchange
- [x] threatmod


<!--TAGS-->
<!--tag:Threat-->
