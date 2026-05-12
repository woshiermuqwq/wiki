## 描述
Applies an 光环 to the 目标 that 触发 a skill when they take
damage. Can use any 光环 attribute

| [Implemented Placeholders]     |
|--------------------------------|
| `<skill.var.damage-amount>`    |
| `<skill.var.damage-type>`      |
| `<skill.var.damage-cause>`     |


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onHit     | ondamagedskill, ondamaged, od, onhitskill, oh | [Metaskill] to 执行 if the 目标 is damaged     |<!--type:Metaskill-->|
| cancelEvent | cE, canceldamage | 是否 to cancel the event that triggered the 光环  | false   |
| damageSub | sub, s    | An optional static decrease (or increase if negative) to the original hit's damage | 0  |
| damageMultiplier | multiplier, m | An optional multiplier on the original hit's damage        | 1      |
| damagemodifiers | damagemods, damagemod | Allows the 光环 to apply damage modifiers. Also accepts a list, as shown in the example. Placeholders can be used as the modifier's amount (**Premium only**). |   |
| deflectProjectiles | deflect, reflect | 是否 弹射物 should be deflected               | false  |
| deflect条件 | d条件 | If `deflectProjectiles` is enabled, it will have to follow the specified set of 条件 to work |<!--type:条件-->|
| modDamageType | damagetype | The [type](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html) of the damage that must be received in order to 触发 the onHit metaskill |<!--type:DamageCause--> |

> This 技能 继承 [光环] 技能


## 示例
```yaml
  Skills:
  - onDamaged{
      auraName=damageResist;d=200;
      onTick=[
        - particles{p=flame;amount=10;hS=0.4}
      ];
      damageMods="FIRE 0.5, MAGIC 0.3, CUSTOM <caster.var.customresistance>"} @self ~onInteract
```


<!-- LINKS -->
[aura]: /skills/mechanics/aura
[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
