## 描述
玩家驯服生物时执行技能。  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为驯服该生物的玩家


## 示例
```yml
EXAMPLE_MOB:
  Type: WOLF
  Skills:
    # 玩家驯服生物时向世界中所有玩家发送消息
    - message{m=我被驯服了} @World ~onTame
```
