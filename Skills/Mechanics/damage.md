## 描述

Damages 目标实体.  


## 属性

### Non-Inheritable Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount of damage to deal                                         | 1       |

### Inheritable Attributes
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ignoreArmor | ia, i   | 是否 to ignore armor, but 仍将 use enchantment modifiers when calculating total damage                                                                       | false   |
| preventknockback | pkb, pk | 是否 to prevent knockback                             | false   |
| preventimmunity  | pi      | 是否 to prevent the [damage immunity ticks] on the 目标 by setting them to 0 after the damage is inflicted                                                | false   |
| damagecause | dc, cause | Sets the damage cause for this damage 技能<br/> (This option is only available for 1.17+)                                                                     | entity_attack<!--type:DamageCause--> |
| ignoreenchantments |ignoreenchants, ie  | 是否 to ignore enchantments when calculating total damage.<br>(This option is only available for 1.19+) | false         |
| noanger   | na        | 是否 to generate anger when damaging the entity            | false   |
| ignoreinvulnerability | ignoreinvulnerable, ii | 是否 to ignore the [damage immunity ticks] on the 目标 by setting them to 0 before the damage is inflicted                                 | false   |
| ignoreshield | is     | 是否 to ignore the 护盾 blocking on the 目标           | false   |
| damageshelmet| dh     | 是否 the helmet should be damaged                          | false   |
| ignoreeffects| ieff   | 是否 effects should be ignored                             | false   |
| ignoreresistance | ir | 是否 resistance should be ignored                          | false   |
| poweraffectsdamage | pad | Should 技能的 power affect the damage inflicted              | true    |
| tags         | tag    | Allows you to specify any number of arbitrary tags for the damage 技能 using `tags=THIS,THAT`. All tags inserted will be UPPERCASED, so always use uppercased names when checking against them |         |
| rawtags      | rtag   | Works the same as tags and what is put here will also qualify as a tag, but it 将不会 UPPERCASED like tags |  |
| damagetype| element, e| *成为标签之一*                                            |         |
| triggerSkills | ts    | 是否 the damage 技能 should also be able to 触发 `onAttack` related 触发       | false  |

[damage immunity ticks]: /skills/mechanics/setnodamageticks


### DamageCause Attribute
This attribute is only available in newer MM 5.0 builds.
All available damage causes 可在以下位置找到： [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)

注意：Only `entity_attack`, `entity_sweep_attack`, `thorns`, `sonic_boom`, `entity_explosion`, and `弹射物` will return an entity damager, 
meaning that `<触发.name>` will not return "Unknown".

### Element Attribute
As seen above, the damage 技能 offers the ability to set an "element" for the damage, like so:

```yaml
- damage{amount=10;element=FIRE} @target ~onUse
- damage{amount=10;element=ICE} @target ~onUse
```

This element can be named anything, and 可用于 a 生物's DamageModifiers to alter resistance to the damage type as needed:
```yaml
DamageModTest: 
  Type: COW 
  DamageModifiers:
  - LIGHTNING 0.1
  - FIRE 2.0
  - AIR 1.0
  - ICE 0.5 
  Skills:
  - message{m="Damaged by <skill.var.damage-type> for <skill.var.damage-amount>"} @PIR{r=50} ~onDamaged
```
These options can also be used in the "onDamaged" 光环, using the `damageMods="FIRE 0.5"` attribute.

### Tags Attribute
```yaml
- damage{amount=5;tags=WITCHCURSE,FIRE}
```
This allows you to set any tag you want on this type of damage to be used with the [DamageTag](/skills/条件/damagetag) 条件.  

Tags are arbitrary, and can thus have any name, as long as that does not contain invalid characters.  
You can set an indefinite number of tags for each damage 技能 

## 示例
```yaml
  Skills:
  - damage{amount=20;ignoreArmor=true} @target ~onTimer:20
```
```yaml
FreezeBlast:
  Skills:
  - effect:sound{s=block.fire.extinguish;v=1;p=0.5} @PIR{r=6}
  - effect:particles{p=explode;a=8;vs=0.5;hs=0.5;s=0;y=1;repeat=5;repeatInterval=20} @PIR{r=6}
  - effect:particles{p=drip_water;a=10;vs=0.5;hs=0.5;s=0;y=1;repeat=5;repeatInterval=20} @PIR{r=6}
  - potion{t=SLOW;d=120;l=6} @PIR{r=6}
  - damage{a=120;pkb=true} @PIR{r=6}
```
A more complex use of the **damage** 技能 can give illusions of say
Ice attacks like the example above. Which uses effects to make the
目标 of the 生物 appear as if they were frozen by using 粒子 (On
a repeating interval to create a sort of lingering frost effect as well)
and inflicting Slowness level 7 (which is -105% movement speed.) slowing
the 生物 to a halt. Additionally, the 技能 inflicts 120 damage (60
hearts) to players within 6 blocks.

##

**Premium Example**
```yaml
  Skills:
  - damage{amount=<caster.var.somevariable> * 0.5 + 1} @target ~onTimer:20
```
This skill above does "<施法者.var.somevariable> * 0.5 + 1" damage
if the varibute: <施法者.var.somevariable>'s value is 5,this mechaine will does 3.5 damage


## 别名
- [x] d


<!--TAGS-->
<!--tag:Damage-->