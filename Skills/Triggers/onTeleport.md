## 描述
生物传送时执行技能。  
> 没有关联的 [@trigger](/Skills/Targeters/Trigger)


## 示例
```yml
EXAMPLE_MOB:
  Type: ENDERMAN
  Skills:
    # 生物传送时向世界中所有玩家发送消息
    - message{m=传送} @World ~onTeleport
```
