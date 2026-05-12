## 描述
施法苦力怕被充能时执行技能。  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为施法者自身


## 示例
```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # 生物被充能时向世界中所有玩家发送消息
    - message{m=已充能} @World ~onCreeperCharge
```


## 别名
- [x] onCreeper_Charge
- [x] onCharged
- [x] onCharge
