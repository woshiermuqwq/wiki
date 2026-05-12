## 描述
生物被清除时执行技能。
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为施法者自身


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 生物被清除时向世界中所有玩家发送消息
    - message{m=已被清除} @World ~onDespawn
```


## 别名
- [x] onDespawned
