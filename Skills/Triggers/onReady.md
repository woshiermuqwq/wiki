## 描述
生物准备从[刷怪器](/Spawners)生成时执行技能


## 别名
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # 生物即将从刷怪器生成时向世界中所有玩家发送消息
    - message{m=准备从刷怪器生成} @World ~onReady
    - message{m=准备从刷怪器生成} @World ~onFirstSpawn
```


## 别名
- [x] onFirstSpawn
