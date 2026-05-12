## 描述
执行 the 技能 when the 生物 is ready to 生成 from a [生成器](/生成器)


## 别名
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob is about to spawn from a spawner
    - message{m=READY TO SPAWN FROM A SPAWNER} @World ~onReady
    - message{m=READY TO SPAWN FROM A SPAWNER} @World ~onFirstSpawn
```


## 别名
- [x] onFirstSpawn