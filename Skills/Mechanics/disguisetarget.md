## 描述
Runs a 伪装 string on the 目标 生物. This skill requires Libs'
伪装 be installed to enable 伪装 functionality.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 伪装  | d, type   | The 伪装 to apply to the 目标.                          | player Ashijin |
| audience  |           | The [audience] of the 伪装                           |<!--type:Audience--> |


## 示例
```yaml
Skills:
  - disguisetarget{d=SHEEP} @target
```
> 此示例将 cause the 目标 to turn into a sheep.

##

```yaml
Skills:
  - disguisetarget{d="player libraryaddict setCustomName '&7Jeb' setSkin Notch.png"} @target
```
> This one would turn it into a player using the skin of Notch and giving it the display name *Jeb*. Color codes are useable in the nametag field.


<!-- LINKS -->
[audience]: /Skills/Audience


<!--TAGS-->
<!--tag:Disguise-->