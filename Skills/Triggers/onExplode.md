## 描述
生物爆炸时执行技能。  
`mobGriefing` 游戏规则必须设为 true 才能生效。  
通常此触发器仅对苦力怕和 TNT 有效，因为它们是仅有的会爆炸的实体  
> 没有关联的 [@trigger](/Skills/Targeters/Trigger)


## 示例
```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # 生物爆炸时向世界中所有玩家发送消息
    - message{m=爆炸} @World ~onExplode
```
