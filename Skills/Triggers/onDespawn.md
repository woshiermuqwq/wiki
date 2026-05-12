## 描述
执行 the 技能 when the 生物 despawns.
> The associated [@触发器](/技能/目标选择器/触发器) is the 施法者 自身


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob despawns
    - message{m=DESPAWNED} @World ~onDespawn
```


## 别名
- [x] onDespawned