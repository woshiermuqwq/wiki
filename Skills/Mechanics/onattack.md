## 描述
Applies an 光环 to the 目标 that 触发 a skill when they damage
something. Can use any 光环 attribute

| [Implemented Placeholders]     |
|--------------------------------|
| `<skill.var.damage-amount>`    |
| `<skill.var.damage-type>`      |
| `<skill.var.damage-cause>`     |


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onattackskill | onattack, oa, onmelee, onhitskill, onhit, oh | [metaskill] to 执行 if the 目标 hits something   |<!--type:Metaskill-->|
| cancelEvent | cE, canceldamage, cd | 是否 to cancel the event that triggered the 光环  | false   |
| damageAdd | add, a    | An optional static increase to the original hit's damage             | 0       |
| damageMultiplier | multiplier, m | An optional multiplier to the original hit's damage       | 1       |
| modDamageType | damagetype | The [type](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html) of the damage inflicted                                |<!--type:DamageCause--> |

> This 技能 继承 [光环] 技能


## 示例
```yaml
  Skills:
  - onAttack{oH=SuperPunch;cE=true;auraname=MyAura}
```


## 别名
- [x] onhit


<!-- LINKS -->
[metaskill]: /Skills/Metaskills
[aura]: /skills/mechanics/aura
[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
