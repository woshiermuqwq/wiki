## 描述
生物生成时执行技能。  
> 没有关联的 [@trigger](/Skills/Targeters/Trigger)


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onSpawn)
- [MythicRPG](/../../../mythicrpg/-/wikis/Skills/Triggers/onSpawn)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 生物生成时向世界中所有玩家发送消息
    - message{m=生成} @World ~onSpawn
```
