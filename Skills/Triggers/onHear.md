## 描述
生物[启用了听觉功能](/Mobs/Mobs#hearing)后，听到声音时执行技能。  
触发技能中可使用 `<skill.var.volume>` [占位符](/Skills/Placeholders#variable-placeholders) 获取表示声源距离的浮点值（1-15）

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为发出声音的实体  

> 关联的 [@origin](/Skills/Targeters/Origin) 为声音产生的位置  

| [已实现的占位符](/Skills/Placeholders#variable-placeholders)     |
|--------------------------------|
| `<skill.var.volume>`           |
| `<skill.var.sound-type>`       |


## 示例
```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="我能听到你，<trigger.name>！<skill.var.volume>？太吵了！"} @trigger ~onHear
```


## 别名
- [x] onVibration
