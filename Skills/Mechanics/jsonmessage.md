## 描述
Sends a json-format chat message to the target player(s). JSON-messages
are capable of hover-events, click events and some other perks that are
unavailable in the other message 机制s. They also support [color
codes](https://htmlcolorcodes.com/bukkit-color-codes/) and [message
variables](/skills/stringvariables).

The format of JSON-messages is a little more advanced than your everyday
message. The syntax requires some extra symbols. If you don't know
anything about writing JSONs, you can visit [this
page](https://www.minecraftjson.com/) or [this
one](http://minecraft.tools/en/tellraw.php) for help.

> Note that double quotes 必须 replaced with single quotes in
JSON-message 机制s

Please do not post issues relating to this 机制 in the bug-report
subforums unless you're certain that your syntax is correct.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| message   | m, msg    | The json-message to send. Must be surrounded by double-quotes        |         |

  
## 示例
You can use both bukkit color codes or json color formatting:  
  
![](http://fs5.directupload.net/images/160309/u3fdf5cx.jpg)  
```yaml
Skills:
  - jsonmessage{m="[{'text':'&aHey, i am a JSON message!'}]"} @trigger ~onInteract
  - jsonmessage{m="[{'text':'Hey, i am a red JSON message!','color':'red'}]"} @trigger ~onInteract
```

##

Here's an example of how to make use of hover-events:  
  
<img src="http://fs5.directupload.net/images/160309/7irfoune.jpg" width="500" height="30" alt="http://fs5.directupload.net/images/160309/7irfoune.jpg" />

```yaml
Skills:
  - jsonmessage{m="[{'text':'&7With me, you can create hover events','hoverEvent':{'action':'show_text','value':{'text':'&aI am a hover event :)'}}}]"} @trigger ~onInteract

```

##

And click events 可以 created like this. This is especially useful for
the /mm signal command to create interactive quest mobs. This example
would send the signal &lt;signal&gt; to the mob casting the json-message
机制, if the player clicks on the click-event.  
  
![](http://fs5.directupload.net/images/160309/gjxvhpd8.jpg)
```yaml
Skills:
  - jsonmessage{m="[{'text':'&7&nAlso click events! :)','clickEvent':{'action':'run_command','value':'/mm signal <mob.uuid> <signal>'}}]"} @trigger ~onInteract
```


## 别名
- [x] messagejson
- [x] jmsg
- [x] jm


<!--TAGS-->
<!--tag:Message-->
