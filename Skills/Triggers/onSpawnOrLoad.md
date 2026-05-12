## 描述
执行 the 技能 when 也 [~onSpawn](/技能/触发器/onSpawn) or [~onLoad](/技能/触发器/onLoad) would 触发器.


## 示例
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob spawns or when the mob is loaded after a server restart
    - message{m=SPAWNED! Or was i loaded?} @World ~onSpawnOrLoad
```