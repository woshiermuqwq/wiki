## 描述
Applies a potion effect to the 目标 entity, which is usually
frequently used on custom 生物 creations and a quite powerful tool; as it
allows for countless interesting applications. See the [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html) for a complete list of available potion
effects.

Potion effects are currently the only way to make 生物 invisible, with
the exception of the armorstand mobtype which has it's own attribute for
indefinite invisibility. Extremely high modifier-levels may have obscure
effects.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, effect | The type of [potion effect](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html) to apply.   | SLOW<!--type:PotionEffectType--> |
| duration  | d         | The duration of the effect in ticks [1].                             | 100     |
| level     | lvl, l    | The modifier-level of the potion effect. The real level is level's value +1.| 0|
| force     | overwrite, ow, override, or | 是否 not to override the current potion effect or not. | false |
| hasParticles | 粒子, p | 是否 not to show the status effect 粒子.               | true    |
| hasIcon   | icon,  i  | 是否 not to show the status effect icon.                          | true    |
| ambientparticles | ambient, a | 是否 to show ambient 粒子.                           | false   |


## 示例
This example skill-configuration will strongly slow down the 目标 for
10 seconds (200 ticks) and deal 5 hearts of damage to it.
```yaml
Cripple:
  Skills:
  - potion{type=SLOW;duration=200;level=4}
  - damage{amount=10}
```
> 20 ticks = 1 second