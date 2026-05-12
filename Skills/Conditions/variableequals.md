## 描述
检测[变量](/Skills/Variables)的值是否等于指定值。

## 属性
| 属性       | 别名                      | 描述                                                      | 默认值          |
| ---------- | ------------------------- | --------------------------------------------------------- | --------------- |
| variable   | name, n, var, key, k      | 变量名称。可选地加上作用域前缀                              |                 |
| value      | val, v                    | 变量必须等于的值才会返回 true。类型必须匹配，否则条件失败。如果包含空格应使用双引号包裹。值也可以包含占位符，包括 PlaceholderAPI |                 |
| scope      | s                         | 变量的[作用域](/Skills/Variables#variable-scopes)           |<!--type:VariableScope--> |


## 示例
在此例中，目标玩家每 10 分钟最多只会听到一次附近熊的咆哮声。

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
  - message{m="&7你听到了一阵低吼声……"}
  - setvariable{var=target.heardbear;value="yes";duration=6000}
```
在此例中，只有当全局变量 `poison_storm` 设置为 true 时技能才会触发。
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
