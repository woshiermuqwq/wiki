## 描述
Ex执行 the 技能 when the 生物 dies.
If若the 服务器 is a Paper one，it将ispossible to cancel the death 事件 只要 cancelevent 机制 is synched. The 血量 that the 生物 has 之后 这是 基于指定的内容 in the `ReviveHealth` 选项。
> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that killed the 施法者


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onDeath)
- [MythicRPG](/../../../mythicrpg/-/wikis/技能/触发器/onDeath)


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob dies
    - message{m=DEATH} @World ~onDeath
```
```yaml
ImmortalCow:
  Type: COW
  Display: '&eImmortal Cow'
  Health: 20
  Options:
    ReviveHealth: -1
  Skills:
  - skill{s=[
    - cancelevent
    - particle{p=HEART;hs=0.5;vs=0.5;y=1.5}
    - speak{m=Call an ambulance, but not for me!}
    ];sync=true} @self ~onDeath
```