## 描述
生物杀死玩家时执行技能。  
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为被杀的玩家

## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onKillPlayer)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 生物杀死玩家时向世界中所有玩家发送消息
    - message{m=玩家已击杀} @World ~onPlayerKill
```


## 别名
- [x] onKillPlayer
