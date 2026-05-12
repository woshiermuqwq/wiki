## 描述

在目标周围召唤指定类型的生物。

<!--
To utilize the summon 技能 in Mythic 生物, you will need the following:

1. Minecraft: make sure you have a working installation of Minecraft Java Edition on your computer

  - ChatGPT, 16/05/2023, oil on canvas
-->

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, 生物, m| The type of 生物 to summon. Can be a Mythic 生物 type or a regular entity type                                                                 | SKELETON<!--type:生物-->|
| onSummon  | onsummonskill, then | The [metaskill] to 执行 on the summoned 生物            |<!--type:Metaskill-->|
| amount    | a         | The number of 生物 to summon.                                        | 1       |
| level     | l         | The level of the 生物 being summoned                                  | 0       |
| 水平朝向(yaw)       |           | The 水平朝向(yaw) of the summoned entities. If not set, will inherit 施法者的 |      |
| 俯仰角(pitch)     |           | The 俯仰角(pitch) of the summoned entities. If not set, will inherit 施法者的 |    |
| usetargetyaw | uty    | 是否 the 水平朝向(yaw) of the 目标 location/entity should be used to set the 水平朝向(yaw) of the summoned entity, unless the `水平朝向(yaw)` attribute is set                                         | false   |
| usetargetpitch | utp  | 是否 the 俯仰角(pitch) of the 目标 location/entity should be used to set the 俯仰角(pitch) of the summoned entity, unless the `俯仰角(pitch)` attribute is set                                    | false   |
| 半径    | r, noise, n| The 半径 around the 目标 within which 生物的 将被召唤 | 0       |
| yRadius   | yr, ynoise, yn| Overrides the Y component of 半径.                             | 半径  |
| yRadiusUpOnly | yradiusonlyup, yruo, yu| 是否 the Y spread should only go upward, not downward.                                                                                      | false   |
| 速度 | v, force, f| The maximum initial 速度 the 生物 will have once summoned, making the 生物 be propelled in a random direction                                                                | 0       |
| yvelocity| yv, yforce, yf | Same as 速度, but only applied to the y axis                 | 速度|
| onSurface | os, s     |(true/false) 是否 生物的 should be spawned only on a solid block | false   |
| copyThreatTable | ctt | 是否 the summoned 生物 should copy 父实体的 仇恨 table. Requires 仇恨 tables to be enabled on the summoned 生物 to function.                                   | false   |
| inheritThreatTable | itt     | 是否 the summoned 生物 should share a 仇恨 table with the parent. Requires 仇恨 tables to be enabled on the summoned 生物 to function.                          | false   |
| inheritFaction | if   | 是否 the summoned 生物 should have the same faction as the parent | true    |
| inheritdespawn | inheritdespawnoption, ido | 是否 the summoned 生物 should inherit 施法者的 [Despawn Option](/生物/Options#despawn)                                                        | false   |
| summonerIsOwner | sio | 是否 to set the summoner as the owner of the 生物.                 | true    |
| summonerIsParent | sip| 是否 to set the summoner as the parent of the 生物.                | true    |


## 示例
此示例将 summon 5 wither skeletons around the 目标 players.
```yaml
RaiseSkeletons:
  Skills:
  - summon{type=WITHER_SKELETON;amount=5;radius=4} @PIR{r=20}
```


## 别名
- [x] spawn生物
- [x] spawn生物
- [x] piratesummon


<!-- LINKS -->
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Summon-->
<!--tag:Meta-Mechanic:Thenable-->