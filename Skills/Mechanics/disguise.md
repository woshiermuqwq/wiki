## 描述
Runs a 伪装 string on the casting 生物. This skill requires Libs'
伪装 to be installed to enable 伪装 functionality.

See [Add-On: 伪装](/生物/伪装) for a list of available
伪装.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 伪装  | d, type   | The 伪装 to apply to the 生物.                             | player Ashijin |
| audience  |           | The [audience] of the 伪装                           |<!--type:Audience--> |


## 示例
> You can test 施放 both of these 伪装 with ``/mm test 施放 TestingDisguise技能``

##

```yml
TestingDisguiseMechanic:
  Skills:
  - disguise{d="Sheep SetBurning SetSpinning"} @self
```
> This will 伪装 you as a sheep that is on fire and spinning.

##

```yml
TestingDisguiseMechanic:
  Skills:
  - disguise{d="Zombie setYModifier -1.5 setPitchLocked setInvisible setHelmet PLAYER_HEAD"} @self
```
> 此示例将 turn you into a steve head that glides across the floor. No good way to describe it. It is pretty funny. I recommend you try it out!


<!-- LINKS -->
[audience]: /Skills/Audience


<!--TAGS-->
<!--tag:Disguise-->