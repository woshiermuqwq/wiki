## 描述
Causes a geyser of liquid to shoot out of the ground 在targeted entity or location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | The type of liquid. Can be “WATER” or “LAVA”                         | WATER<!--type:Fluid-->|
| height    | h         | How high the geyser will go. Will be set to *at least* 1 even if specified otherwise. | 3       |
| interval  | i, speed, s | The interval (in ticks) between each iteration of the geyser animation | 10  |
| audience  |           | The [audience] of the effect                                         | nearby<!--type:Audience--> |


## 示例
```yaml
GeyserSkill:
  Skills:
  - geyser{type=LAVA;height=3;speed=10} @selflocation
```


## 别名
- [x] effect:geyser
- [x] e:geyser


<!-- LINKS -->
[audience]: /Skills/Audience


<!--TAGS-->
<!--tag:Effect-->
