## 描述
村民与玩家交易时执行技能。  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为与村民交易的玩家


## 示例
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # 生物切换目标时向世界中所有玩家发送消息
    - message{m=已交易} @World ~onTrade
```
