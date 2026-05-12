## 描述
Displays an advancement-like "toast" message to all targeted players. Can only affect targeted players, has no effect on non-player targets.

The header of the toast is set by the frame type, such as `challenge` being titled `Challenge Complete!`.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| icon      | i         | The icon to send. Accepts any valid MATERIAL or Mythic Item          | diamond_sword<!--type:Item-->|
| iconnbt   | nbt       | The NBT of the icon.                                                 | NONE    |
| message   | msg,m   | 要发送的消息. Must be in double-quotes.                         | NONE    |
| frame     | f       | The type of toast to send. MUST BE LOWERCASE. Options are: `challenge`, `task` or `goal`.                                                                                       | challenge<!--type:AdvancementDisplayFrame-->|


## 示例
```yaml
  Skills:
  - sendtoast{icon=MyCustomDiamond;message="This is a Toast!";frame=challenge} @PlayersInRadius{r=10}
  - ...
```


## 别名
- [x] toastmessage
- [x] toastmsg
- [x] advmessage
- [x] advancementmessage


<!--TAGS-->
<!--tag:Message-->
