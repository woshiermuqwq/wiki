## 描述
此触发器具有特殊语法：`~onSignal:<signal>`  

生物收到 [signal](/Skills/Mechanics/Signal) 技能发送的信号时执行技能。  
信号必须是字母数字字符串。  

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为发送信号的实体


## 示例
```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # 玩家右键点击生物时向半径 64 格内的所有 MythicMob 实体发送信号
    - signal{s=MOO_FOR_ME} @EIR{r=64} ~onInteract
```
##
```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # 生物收到 "MOO_FOR_ME" 信号时向世界中所有玩家发送消息
    - message{m=哞} @World ~onSignal:MOO_FOR_ME
```
##
你也可以选择不为此触发器指定信号，此时生物每收到一个通用信号就会触发关联技能。
```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # 生物收到信号时向世界中所有玩家发送消息
    - message{m=哞……？} @World ~onSignal
```
