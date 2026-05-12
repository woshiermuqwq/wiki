## 描述
此触发器具有特殊语法：`~onTimer:<ticks>`  

每 *n* 刻执行一次技能。刻数不能为零，20 刻等于 1 秒。  

此触发器的计时不基于生物的生成时间，而是基于全局时钟。因此，例如你设置了 `~onTimer:1000`，它的首次执行可能发生在生物生成后到 1000 刻之间的任意时刻，取决于全局时钟的值。

> 使用此触发器时需谨慎，可能导致服务端/客户端性能问题！
> 例如：大量粒子效果会造成客户端卡顿，甚至将客户端踢出服务器

> 没有关联的 [@trigger](/Skills/Targeters/Trigger)。


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onTimer)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 每刻（0.05 秒）向世界中所有玩家发送消息
    - message{m=TIMER 每刻（0.05 秒）} @World ~onTimer:1
    # 每 40 刻（2 秒）向世界中所有玩家发送消息
    - message{m=TIMER 每 40 刻（2 秒）} @World ~onTimer:40
```
