## 描述
Makes the caster speak using chat and speech bubbles. Supports
Holograms.  
You can force a new line in the hologram by using `\n`


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| offset    | o, yo, yoffset | The y offset 对于hologram.                                  | 1       |
| radius    | r         | The radius of entities which will see the chat message               | 12      |
| maxlinelength | ll, mll, ml, linelength | The maximum length of the hologram                 | 22      |
| lineprefix| lp        | The prefix 对于hologram.                                         | &f      |
| message   | m, msg    | The message to be displayed (affects both hologram and chat)         |         |
| chatprefix| cp        | The prefix 对于chat message            | &lt;caster.name&gt;&f&lt;&co&gt;  |
| duration  | d, ticks, time, t | The amount of time the hologram 将会 displayed for.               | MESSAGE LENGTH * 4  |
| sendchatmessage | chatmessage, chat | Whether the message shows up in chat                   | true    |
| audience  |           | The [Audience] of the 机制                                       | tracked<!--type:Audience--> |

> 此机制继承所有[Aura] 机制  
>> - The `auraname` attribute is **set** at `#speaking`
>> - The `charges` attribute is **set** at `1`  
>> - The `maxStacks` attribute is **set** at `1`  
>> - The `mergeSameCaster` attribute is **set** at `false`  
>> - The `overwriteCaster` attribute is **set** at `true`  
>> - The `refreshDuration` attribute is **set** at `false`  

## 示例
```yaml
  Skills:
  - speak{
    offset=0.6f;
    radius=30;
    maxlinelength=22;
    lineprefix="&5";
    message=" I just spawned!";
    chatprefix=<caster.name>&f<&co>;
    duration=200} @self ~onSpawn
```


## 别名
- [x] speech


<!-- LINKS -->
[audience]: /Skills/Audience
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Message-->
