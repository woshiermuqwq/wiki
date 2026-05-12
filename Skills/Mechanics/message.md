## 描述
向目标发送聊天消息，前提是目标为玩家。 [Color
codes](/Skills/Placeholders#color-codes) and
[variables](/Skills/Variables) are useable in this 技能.

* Allows hex colors in the format **`<#FFFFFF>`**
* Supports gradients in the format **`<gradient:#color1:#color2>text</gradient>`**
* Supports **`<rainbow>text</rainbow>`**
* Supports hover text in the format **`<hover:show_text:'hover text??'>hover over me!</hover>`**
* Supports clickable text in the format **`<click:run_command:/say hello>click me!</click>`**


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| message   | msg,m     | 要发送的消息                                                  | None    |
| audience  |           | the [audience] of the message                                        | <!--type:Audience-->|


## 示例
```yaml
   Skills:
   - message{m="<caster.name>&f<&co> Hahaha! You will all die!"} @PlayersInRadius{r=30}
```


## 别名
- [x] m
- [x] msg


<!-- LINKS -->
[audience]:/Skills/Audience


<!--TAGS-->
<!--tag:Message-->
