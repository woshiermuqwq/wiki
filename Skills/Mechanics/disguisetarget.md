## 描述
Runs a disguise string on the target mob. This skill requires Libs'
Disguises be installed to enable Disguise functionality.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| disguise  | d, type   | The disguise to apply to the target.                          | player Ashijin |
| audience  |           | The [audience] of the disguise                           |<!--type:Audience--> |


## 示例
```yaml
Skills:
  - disguisetarget{d=SHEEP} @target
```
> This example would cause the target to turn into a sheep.

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
