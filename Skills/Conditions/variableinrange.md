## 描述
检测给定的数值型变量是否在某个范围内。

## 属性
| 属性       | 别名                    | 描述                                            | 默认值          |
| ---------- | ----------------------- | ----------------------------------------------- | --------------- |
| variable   | name, n, var, key, k    | 要匹配的变量，可选地加上作用域前缀                |                 |
| value      | val, v, range, r        | 要匹配的数值范围                                  |                 |
| scope      | s                       | 变量的[作用域](/Skills/Variables#variable-scopes) |<!--type:VariableScope--> |


## 示例

```yaml
ShootCheck:
  Cooldown: 0
  Conditions:
  - variableInRange{var=caster.shootsLeft;value=>0} castInstead ShootThemUp
  Skills:
  - message{m="&7正在装弹……"} @self
  - delay 0
  - setskillcooldown{skill=ShootCheck;seconds=2} @self
  - delay 20
  - setvariable{var=caster.shootsLeft;value=10} @self
  - message{m="&7装弹完毕！"} @self
```

## 别名
- [x] varinrange
- [x] varrange
