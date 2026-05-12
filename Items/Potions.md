This 属性 用于 应用 药水 效果 to 药水 based 物品.
注意 that 药水 效果 can be added to any kind of 物品, but 只会
have an actual function on 药水. Here is an 示例:

### 格式
```yml
internal_itemname:
  Id: potion
  Options:
    Color: 0,0,0 #rgb(red,green,blue) format
  PotionEffects:
    - <type> <duration> <level>
```
#### **\<类型>**
The 类型 of 药水 效果 that 应为 applied. See below for 一系列 all 类型.

##### **\<持续时间>**
The 持续时间 of the 药水 效果 measured in ticks <sup>(*20 ticks is 1 second*)</sup>.

##### **\<等级>**
药水 效果. 0 = 等级 I, 1 = 等级 II, Etc的等级modifier。

药水 效果
--------------

all 支持 药水 效果 are listed on the [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/药水/PotionEffectType.html)的complete 列表。

<!--
This is a 完整列表 all 药水 效果 当前 usable by MythicMobs. These can be utilized by 也 药水 based 物品 or the [药水 机制](/技能/机制/药水).

| **药水 类型** | **Description** |
|------------------------|---------------------------------------------------------------------------------------------------------------------|
| **ABSORPTION** | Increases the maximum 血量 of an 实体 with 血量 that 不能 be regenerated, but is refilled every 30 seconds. |
| **BLINDNESS** | Blinds an 实体. |
| **BAD_OMEN** | oof. |
| **CONDUIT\_POWER** | Increases underwater visibility and mining 速度, 阻止 drowning. |
| **CONFUSION** | Warps vision on the client. |
| **伤害\_RESISTANCE** | Decreases 伤害 dealt to an 实体. |
| **DOLPHINS\_GRACE** | Increases swimming 速度. |
| **FAST\_DIGGING** | Increases dig 速度. |
| **触发\_RESISTANCE** | Stops 触发 伤害. |
| **GLOWING** | Makes the 目标 实体 glow. |
| **HARM** | Hurts an 实体. |
| **HEAL** | Heals an 实体. |
| **血量\_BOOST** | Increases the maximum 血量 of an 实体. |
| **HUNGER** | Increases hunger. |
| **INCREASE\_DAMAGE** | Increases 伤害 dealt. |
| **INVISIBILITY** | Makes the 目标 invisible. |
| **JUMP** | Increases jump 高度. |
| **LEVITATION** | Makes the 目标 实体 levitate. |
| **LUCK** | Grants the 目标 实体 luck. |
| **NIGHT\_VISION** | Allows an 实体 to see in the dark. |
| **POISON** | Deals 伤害 to an 实体 随时间. |
| **REGENERATION** | Regenerates 血量. |
| **SATURATION** | Increases the food 等级 of an 实体 each tick. |
| **SLOW** | Decreases 移动 速度. |
| **SLOW\_DIGGING** | Decreases dig 速度. |
| **SLOW\_FALLING** | Decreases falling 速度 and negates all fall 伤害. Eliminates all 伤害 from thrown ender pearls. |
| **速度** | Increases 移动 速度. |
| **UNLUCK** | Grants the 目标 实体 bad luck. |
| **WATER\_BREATHING** | Allows breathing underwater. |
| **WEAKNESS** | Decreases 伤害 dealt by an 实体. |
| **WITHER** | Deals 伤害 to an 实体 随时间 and gives the 血量 to the shooter. |

-->
<!--
Pre-Made 药水 类型 and 效果
---------------------------------

If you'd rather use one of the 默认 Minecraft 药水 类型, here are
some common Data 值 您可以 use 与 药水 物品 类型 to make
them!

| **DATA - Regular** | **DATA - Splash** | **DATA - Lingering** | **药水** | **效果** |
|--------------------|-------------------|----------------------|-------------------------------|-----------------------------------------------------------------------|
| 8193 | 16385 | | Regeneration 药水 (0:45) | Heals 18 over 45 seconds |
| 8194 | 16386 | | Swiftness 药水 (3:00) | Increase 移动 速度 by 20% for 3 mins |
| 8195 | 16387 | | 触发 Resistance 药水 (3:00) | Immunity to 触发 for 3 minutes |
| 8196 | 16388 | | Poison 药水 (0:45) | 36 伤害 over 45 seconds |
| 8197 | 16389 | | Healing 药水 | Heals 4 instantly |
| 8198 | 16390 | | Night Vision 药水 (3:00) | Night vision for 3 minutes |
| 8200 | 16392 | | Weakness 药水 (1:30) | Reduced melee 伤害 by 50% for 1 minute 30 seconds |
| 8201 | 16393 | | Strength 药水 (3:00) | Increase melee 伤害 by 130% for 3 minutes |
| 8202 | 16394 | | Slowness 药水 (1:30) | Slows by 15% + 15% per 层级 for 1 minute 30 seconds |
| 8204 | 16396 | | Harming 药水 | Does 6 伤害 |
| 8205 | 16397 | | Water Breathing 药水 (3:00) | Water breathing for 3 minutes |
| 8206 | 16398 | | Invisibility 药水 (3:00) | Invisibility for 3 minutes |
| 8225 | 16417 | | Regeneration 药水 II (0:22) | Heals 18 over 22.5 seconds |
| 8226 | 16418 | | Swiftness 药水 II (1:30) | Increase 移动 速度 by 40% for 1 minute 30 seconds |
| 8228 | 16420 | | Poison 药水 II (0:22) | Does 38 伤害 over 22.5 seconds |
| 8229 | 16421 | | Healing 药水 II | Heals 8 instantly plus 4 per 层级 |
| 8233 | 16425 | | Strength 药水 II (1:30) | Increase melee 伤害 by 260% + 130% per 层级 for 1 minute 30 seconds |
| 8236 | 16428 | | Harming 药水 II | Does 12 伤害 plus 6 伤害 per 层级 |
| 8257 | 16449 | | Regeneration 药水 (2:00) | Heals 48 over 2 minutes |
| 8258 | 16450 | | Swiftness 药水 (8:00) | Increase 移动 速度 by 20% for 8 minutes |
| 8259 | 16451 | | 触发 Resistance 药水 (8:00) | Immunity to 触发 for 8 minutes |
| 8260 | 16452 | | Poison 药水 (2:00) | Does 96 伤害 over 2 minutes |
| 8262 | 16454 | | Night Vision 药水 (8:00) | Night vision for 8 minutes |
| 8264 | 16456 | | Weakness 药水 (4:00) | Reduces melee 伤害 by 50% for 4 minutes |
| 8265 | 16457 | | Strength 药水 (8:00) | Increase melee 伤害 by 130% for 8 minutes |
| 8266 | 16458 | | Slowness 药水 (4:00) | Slows by 15% + 15% per 层级 for 4 minutes |
| 8269 | 16461 | | Water Breathing 药水 (8:00) | Water breathing for 8 minutes |
| 8270 | 16462 | | Invisibility 药水 (8:00) | Invisibility for 8 minutes |
| 8289 | 16481 | | Regeneration 药水 II (1:00) | Heals 48 over 1 minute |
| 8290 | 16482 | | Swiftness 药水 II (4:00) | Increased 移动 速度 by 40% for 4 minutes |
| 8292 | 16484 | | Poison 药水 II (1:00) | Does \~101 伤害 over a minute |
| 8297 | 16489 | | Strength 药水 II (4:00) | Increase melee 伤害 by 260% + 130% per 层级 for 4 minutes |
-->
示例
--------
```yml
SupremeHealingPotion:
      Id: potion
      Display: '&6Supreme Healing Potion'
      Options:
        Color: 239,103,216
        HideFlags: true
      PotionEffects:
      - HEAL 60 1
      - CONFUSION 20 0
      Lore:
      - '&8An incredibly potent healing potion'
      - '&8able to cure even tremendous wounds.'
      - '&cNotice: May cause liver failure.'
```