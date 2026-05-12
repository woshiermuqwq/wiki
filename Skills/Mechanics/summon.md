## 描述

在目标周围生成给定类型的生物。

<!--
To utilize the summon 机制 in Mythic Mobs, you will need the following:

1. Minecraft: make sure you have a working installation of Minecraft Java Edition on your computer

  - ChatGPT, 16/05/2023, oil on canvas
-->

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, mob, m| 要生成的生物类型. 可以是 MythicMobs 生物类型或普通实体类型                                                                 | SKELETON<!--type:Mob-->|
| onSummon  | onsummonskill, then | 在生成的生物上执行的[元技能]            |<!--type:Metaskill-->|
| amount    | a         | 要生成的生物数量.                                        | 1       |
| level     | l         | 生成生物的等级                                  | 0       |
| yaw       |           | 生成实体的偏航角. 如果未设置，将继承施法者的值 |      |
| pitch     |           | 生成实体的俯仰角. 如果未设置，将继承施法者的值 |    |
| usetargetyaw | uty    | 是否使用目标位置/实体的偏航角来设置生成实体的偏航角, 除非设置了 `yaw` 属性                                         | false   |
| usetargetpitch | utp  | 是否使用目标位置/实体的俯仰角来设置生成实体的俯仰角, 除非设置了 `pitch` 属性                                    | false   |
| radius    | r, noise, n| 目标周围的半径，生物将在该范围内生成 | 0       |
| yRadius   | yr, ynoise, yn| 覆盖半径的 Y 分量.                             | radius  |
| yRadiusUpOnly | yradiusonlyup, yruo, yu| Y 扩散是否只向上不向下.                                                                                      | false   |
| velocity | v, force, f| 生物生成后的最大初始速度向量，使生物向随机方向推进                                                                | 0       |
| yvelocity| yv, yforce, yf | 与 velocity 相同，但仅应用于 y 轴                 | velocity|
| onSurface | os, s     |(true/false) 生物是否只能生成在固体方块上 | false   |
| copyThreatTable | ctt | 生成的生物是否复制父级的仇恨表. 需要生成的生物启用仇恨表才能生效.                                   | false   |
| inheritThreatTable | itt     | 生成的生物是否与父级共享仇恨表. 需要生成的生物启用仇恨表才能生效.                          | false   |
| inheritFaction | if   | 生成的生物是否与父级拥有相同阵营 | true    |
| inheritdespawn | inheritdespawnoption, ido | Whether the summoned mob should inherit the caster's [Despawn Option](/Mobs/Options#despawn)                                                        | false   |
| summonerIsOwner | sio | 是否将召唤者设为生物的所有者.                 | true    |
| summonerIsParent | sip| 是否将召唤者设为生物的父级.                | true    |


## 示例
This example would summon 5 wither skeletons around the target players.
```yaml
RaiseSkeletons:
  Skills:
  - summon{type=WITHER_SKELETON;amount=5;radius=4} @PIR{r=20}
```


## 别名
- [x] spawnmobs
- [x] spawnmob
- [x] piratesummon


<!-- LINKS -->
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Summon-->
<!--tag:Meta-Mechanic:Thenable-->
