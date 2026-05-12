## 描述
检查[变量](/Skills/Variables)的值的条件。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| variable  | name, n, var, key, k | 变量的名称。可选地可以加上作用域前缀|    |
| value| val, v | 变量必须等于的值才会返回 true。必须适用于变量类型，否则机制将失败。如果使用空格，应使用双引号包围。值也可以包含占位符，甚至来自 PlaceholderAPI。                                                        |         |
| scope| s| 变量的[作用域](/Skills/Variables#variable-scopes)，即变量所在位置                                                                                        |<!--type:VariableScope-->|


## 示例
在此示例中，目标玩家每 10 分钟才能听到附近任何熊的咆哮声。

```yaml
BearMob:
  Skills:
  - skill:BearGrowl @PlayersInRadius{r=40} ~onTimer:60
```
```yaml
BearGrowl:
  TargetConditions:
  - variableEquals{var=target.heardbear;value="yes"} cancel
  Skills:
  - message{m="&7你听到一声低沉的咆哮……"}
  - setvariable{var=target.heardbear;value="yes";duration=6000}
```
在此示例中，只有当全局变量 "poison_storm" 被设置为 true 时技能才会触发。
```yaml
PoisonStormDamage:
  Conditions:
  - varEquals{var=global.poison_storm;value="yes"}
  Skills:
  - potion{type=POISON;duration=100}
  - damage{amount=1;ignorearmor=true}
```


## 别名
- [x] variableeq
- [x] varequals
- [x] vareq