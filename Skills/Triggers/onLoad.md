## 描述
服务器重启后生物被加载时执行技能。  


## 示例
```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # 生物在服务器重启后被加载时向世界中所有玩家发送消息
    - message{m=已加载} @World ~onLoad
```
