## 描述
生物（必须是苦力怕）被点燃时执行技能（例如通过打火石点燃）。  
  
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为施法者自身


## 示例
```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # 生物被点燃时向世界中所有玩家发送消息
    - message{m=哦哦我要炸了} @World ~onPrime
```
