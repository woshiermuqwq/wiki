## 描述
Ex执行 the 技能 when the casting creeper is charged.

> The associated [@触发器](/技能/目标选择器/触发器) is the 施法者 自身


## 示例
```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob gets charge
    - message{m=CHARGED} @World ~onCreeperCharge
```


## 别名
- [x] onCreeper_Charge
- [x] onCharged
- [x] onCharge