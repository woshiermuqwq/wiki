## 描述
Modifies the 计分板-objective value of a fake player name. Works
like the [Modify Score](/skills/技能/modifyscore) 技能, but is
only capable of performing the **set**-action.


## 属性
> This 技能 inherits every *inheritable* attribute of the [ModifyScore](/Skills/技能/modifyscore) 技能
>> - The `action` attribute is **set** at `SET` and cannot be modified

  
## 示例
此示例将 set the score of a player named
"Bob" for the objective "TestScore", even if that player doesn't exist
on the server.  
It will create the objective if it does not currently exist.
```yaml
  Skills:
  - setscore{o=TestScore;e=Bob;v=1} ~onInteract 
```
![](https://i.imgur.com/0HKvAUM.png)


<!--TAGS-->
<!--tag:Scoreboard-->
