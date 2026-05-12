## 描述
Shoots a fireball from the 生物 towards the 目标 entity or location.

> Caution!  
> The large version of this fireball can grief blocks.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| yield     | strength, y, s | The yield (power) of the fireball's explosion                   | 1       |
| 速度  | v         | The 速度 of the fireball                                         | 1       |
| fireTicks | ft        | How long (in ticks) fire left behind by the fireball will persist    | 0       |
| incendiary| i         | (true/false) 是否 the fireball will leave behind fire             | false   |
| charged   | c         | 是否 the fireball is charged                                      | false   |
| fromorigin| fo        | 是否 the fireball should be shot from the [原点]                | false   |
| playsound | ps        | 是否 to play the fireball launching sound when it is created | false |
| smallfireball | small,sml | 是否 to use the smaller blaze fireball instead of the ghast fireball                                                                                       | false   |
| type      | t         | The type of the fireball                                             | SMALL<!--type:ShootFireball_Type--> |
| item      | material  | The [material] of the fireball, if ITEM type was used           | BLAZE_POWDER<!--type:Material-->|


### Type Attribute
| Available Types |
|-----------------|
| NORMAL
| SMALL
| LARGE
| WITHER
| DRAGON
| ITEM


## 示例
此示例将 shoot a barrage of 3 fast-moving fireballs at the
目标.
```yaml
FireballBarrage:
  Skills:
  - shootfireball{y=1;v=4} @target
  - delay 10
  - shootfireball{y=1;v=4} @target
  - delay 10
  - shootfireball{y=1;v=4} @target
```


## 别名
- [x] fireball


<!-- LINKS -->
[origin]: /Skills/Targeters/Origin
[material]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html


<!--TAGS-->
<!--tag:Projectile-->
