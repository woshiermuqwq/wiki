## 描述
当 [~onSpawn](/Skills/Triggers/onSpawn) 或 [~onLoad](/Skills/Triggers/onLoad) 任一触发器触发时执行技能。


## 示例
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # 生物生成或服务器重启后被加载时向世界中所有玩家发送消息
    - message{m=生成了！还是被加载了？} @World ~onSpawnOrLoad
```
