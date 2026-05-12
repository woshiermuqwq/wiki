## 描述
向目标发送消息 player's action bar.

[Color codes](/Skills/Placeholders#color-codes) and
[Variables](/Skills/Variables) are compatible with the action
message bar. Some targeters might not work properly with this 技能.
If you happen to find a targeter that doesn't work, please be sure to
post it in the bugs/suggestion-subforum!

![](http://fs5.directupload.net/images/160306/zswobuo8.jpg)


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| message   | m, msg    | 要发送的消息. Must be surrounded by quotes                    |         |


## 示例
```yaml
  Skills:
  - actionmessage{m="<caster.name>&f is casting a spell!"} @PlayersInRadius{r=30}
  - actionmessage{m="&lHello! &cI'm &athe &9&lactionmessage-bar&r! &e:)"} @trigger
  - am{m="<caster.name>&f is using the *skill alias!*"} @PlayersInRadius{r=30}
```


## 别名
- [x] am
- [x] actionmessage


<!--TAGS-->
<!--tag:Message-->
