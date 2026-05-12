## 描述
Ex执行 the 技能 when the 生物, 必须为 a creeper, is primed (i.e. via the use of a flint and steel).
  
> The associated [@触发器](/技能/目标选择器/触发器) is the 施法者 自身


## 示例
```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob is primed
    - message{m=OOO I'M GONNA EXPLODE} @World ~onPrime
```