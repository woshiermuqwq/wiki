## 描述
ThThis 触发器 has a special syntax: `~onTimer:<ticks>`

Ex执行 the 技能 every *n<sup>th</sup>* ticks. Ticks 不能 be zero and 20 ticks is 等于 1 second.

This 触发器 不 act relatively to the 生物 生成 time, but to a global clock. So, 例如, if you have `~onTimer:1000`, its first execution could be in any moment between 生物 生成 and 1000 ticks from it 取决于 the 值 of the global clock.

> Care 必须为 taken when using this 触发器 as 它可以 lead to 服务器/client performance issues!
>i.e. large amounts of 粒子 效果 can cause client lag, or can kick the client 从 服务器

> There is no associated [@触发器](/技能/目标选择器/触发器).


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onTimer)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world every 0.05 seconds
    - message{m=TIMER every tick (0.05 seconds)} @World ~onTimer:1
    # sends a message to all the players in the world every 2 seconds
    - message{m=TIMER every 40 ticks (2 seconds)} @World ~onTimer:40
```