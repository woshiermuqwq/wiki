## 描述
Ex执行 the 技能 when the 生物 is loaded 之后 a 服务器 restart.


## 示例
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob is loaded after a server restart
    - message{m=LOADED} @World ~onLoad
```