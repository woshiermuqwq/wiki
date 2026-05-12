## 描述
Sends a chat message to the 目标, if the 目标 is a player. [Color
codes](/Skills/Placeholders#color-codes) and
[variables](/Skills/Variables) are useable in this 技能

* Allows hex colors 格式为 **`<#FFFFFF>`**
* Supports gradients 格式为 **`<gradient:#color1:#color2>text</gradient>`**
* Supports **`<rainbow>text</rainbow>`**
* Supports hover text 格式为 **`<hover:show_text:'hover text??'>hover over me!</hover>`**
* Supports clickable text 格式为 **`<click:run_command:/say hello>click me!</click>`**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| message   | msg,m     | The message to send                                                  | None    |
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