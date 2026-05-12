## 描述
玩家与生物交互（即右键点击）时执行技能。  
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为与施法者交互的玩家


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onInteract)
- [MythicRPG](/../../../mythicrpg/-/wikis/Skills/Triggers/onInteract)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 玩家右键点击生物时向世界中所有玩家发送消息
    - message{m=已交互} @World ~onInteract
```
