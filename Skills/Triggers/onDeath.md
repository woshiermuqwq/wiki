## 描述
生物死亡时执行技能。  
如果是 Paper 服务端，可以通过同步执行 cancelevent 技能来取消死亡事件。生物在此之后的血量由 `ReviveHealth` 选项决定。  
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为杀死施法者的实体


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onDeath)
- [MythicRPG](/../../../mythicrpg/-/wikis/Skills/Triggers/onDeath)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 生物死亡时向世界中所有玩家发送消息
    - message{m=死亡} @World ~onDeath
```
```yaml
ImmortalCow:
  Type: COW
  Display: '&e不死牛'
  Health: 20
  Options:
    ReviveHealth: -1
  Skills:
  - skill{s=[
    - cancelevent
    - particle{p=HEART;hs=0.5;vs=0.5;y=1.5}
    - speak{m=叫救护车，但不是给我叫！}
    ];sync=true} @self ~onDeath
```
