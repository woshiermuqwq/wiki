## 描述
Modifies the scoreboard-objective value of a fake player name. Works
like the [Modify Score](/skills/mechanics/modifyscore) 机制, but is
only capable of performing the **set**-action.


## 属性
> This 机制 inherits every *inheritable* attribute of the [ModifyScore](/Skills/Mechanics/modifyscore) 机制
>> - The `action` attribute is **set** at `SET` and cannot be modified

  
## 示例
This example will set the score of a player named
"Bob" 对于objective "TestScore", even if that player doesn't exist
on the server.  
It will create the objective if it does not currently exist.
```yaml
  Skills:
  - setscore{o=TestScore;e=Bob;v=1} ~onInteract 
```
![](https://i.imgur.com/0HKvAUM.png)


<!--TAGS-->
<!--tag:Scoreboard-->
