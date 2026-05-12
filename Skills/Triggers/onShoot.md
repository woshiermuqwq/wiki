## 描述
生物发射弹射物时执行技能。  
例如，持弓的骷髅会射箭；恶魂、烈焰人或末影龙会发射某种火球。  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为施法者

| [已实现的占位符](/Skills/Placeholders#variable-placeholders)     |
|--------------------------------|
| `<skill.var.bow-tension>`      |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onShoot)
- [MythicRPG](/../../../mythicrpg/-/wikis/Skills/Triggers/onShoot)


## 示例
```yml
EXAMPLE_MOB:
  Type: SKELETON
  Skills:
    # 骷髅射箭时向世界中所有玩家发送消息
    - message{m=我射了一支箭} @World ~onShoot
```


## 别名
- [x] onBowShoot
- [x] onShootBow
