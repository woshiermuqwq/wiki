## 描述
Sends a random message to the 目标 player. Does nothing if the 目标
is not a player. No limit to how much messages can be added to the list.
The special character # will cause this skill to fail.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| messages  | m, message, msg, msgs | A list of message strings to send to the player, separated by commas. Each string must be in quotes. These strings can use variables.                        |         |


## 示例
This will each player n a 20 blocks 半径 one random message when the 施法者 is interacted with.
```yaml
  Skills:
  - randommessage{
      m=
      "message 1",
      "message 2",
      "message 3";
      } @PIR{r=20} ~onInteract
```
##
This will do the same as above, but this time sending 2 random messages per each player
```yaml
  Skills:
  - randommessage{m="one test","not a test","test";repeat=1} @PIR{r=20} ~onInteract
```


## 别名
- [x] randommsg
- [x] rm
- [x] rmsg


<!--TAGS-->
<!--tag:Random-->
<!--tag:Message-->