## 描述
ThThis 触发器 has a special syntax: `~onSignal:<signal>`

Ex执行 the 技能 when the 生物 receives a 信号 从 [信号](/技能/机制/信号) 机制.
A A 信号 必须为 alphanumeric.

> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that sent the 信号


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a signal to all mythicmob entity in a radius of 64 blocks
    # when a player right-clicks the mob
    - signal{s=MOO_FOR_ME} @EIR{r=64} ~onInteract
```
##
```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # sends a message to all the players in the world
    # when the mob receives a "MOO_FOR_ME" signal
    - message{m=MOO} @World ~onSignal:MOO_FOR_ME
```
##
You may 也 choose to not specify a 信号 for this 触发器, in which case the associated 机制 将 triggered every time the 生物 receives a generic 信号.
```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # sends a message to all the players in the world
    # when the mob receives a signal
    - message{m=MOO...?} @World ~onSignal
```