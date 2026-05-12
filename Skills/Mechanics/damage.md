## 描述

对目标实体造成伤害。  


## 属性

### 不可继承属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | 要造成的伤害量                                         | 1       |

### 可继承属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ignoreArmor | ia, i   | 是否忽略护甲，但在计算总伤害时仍会使用附魔修饰符                                                                       | false   |
| preventknockback | pkb, pk | 是否防止击退                             | false   |
| preventimmunity  | pi      | 是否在造成伤害后将目标的[伤害免疫刻]设为 0 来防止伤害免疫                                                | false   |
| damagecause | dc, cause | 设置此伤害机制的伤害原因.<br/> (此选项仅适用于 1.17+)                                                                     | entity_attack<!--type:DamageCause--> |
| ignoreenchantments |ignoreenchants, ie  | 是否在计算总伤害时忽略附魔.<br>(此选项仅适用于 1.19+) | false         |
| noanger   | na        | 是否在伤害实体时产生愤怒            | false   |
| ignoreinvulnerability | ignoreinvulnerable, ii | 是否在造成伤害前将目标的[伤害免疫刻]设为 0 来忽略伤害免疫                                 | false   |
| ignoreshield | is     | 是否忽略目标的盾牌格挡           | false   |
| damageshelmet| dh     | 是否损坏头盔                          | false   |
| ignoreeffects| ieff   | 是否忽略效果                             | false   |
| ignoreresistance | ir | 是否忽略抗性                          | false   |
| poweraffectsdamage | pad | 技能强度是否影响造成的伤害              | true    |
| tags         | tag    | 允许你为伤害机制指定任意数量的标签 使用 `tags=THIS,THAT` 语法. 所有插入的标签将被转为大写，因此在检查标签时请始终使用大写名称 |         |
| rawtags      | rtag   | 与 tags 相同，放在这里的内容也会被当作标签，但不会像 tags 那样转为大写 |  |
| damagetype| element, e| *成为 Tags 之一*                                            |         |
| triggerSkills | ts    | 伤害机制是否也能触发 `onAttack` 相关触发器       | false  |

[damage immunity ticks]: /skills/mechanics/setnodamageticks


### DamageCause 属性
此属性仅在较新的 MM 5.0 版本中可用。
所有可用的伤害原因可在 [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)

Note: Only `entity_attack`, `entity_sweep_attack`, `thorns`, `sonic_boom`, `entity_explosion`, and `projectile` 会返回一个实体伤害源, 
这意味着 `<trigger.name>` 不会返回 "Unknown".

### Element 属性
As seen above, the damage 机制 offers the ability to set an "element" 对于damage, like so:

```yaml
- damage{amount=10;element=FIRE} @target ~onUse
- damage{amount=10;element=ICE} @target ~onUse
```

This element 可以 named anything, and 可以 used in a mob's DamageModifiers to alter resistance to the damage type 按需调整:
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
这些选项也可以在 "onDamaged" 光环中使用, using the `damageMods="FIRE 0.5"` attribute.

### Tags 属性
```yaml
- damage{amount=5;tags=WITCHCURSE,FIRE}
```
这允许你为这种伤害类型设置任意标签，配合 [DamageTag](/skills/conditions/damagetag) condition.  

标签是任意的，因此可以有任意名称，只要不包含无效字符即可.  
You can set an indefinite number of tags for each damage 机制. 

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
A more complex use of the **damage** 机制 can give illusions of say
Ice attacks like the example above. Which uses effects to make the
targets of the mob appear as if they were frozen by using particles (On
a repeating interval to create a sort of lingering frost effect as well)
and inflicting Slowness level 7 (which is -105% movement speed.) slowing
the mob to a halt. Additionally, the 机制 inflicts 120 damage (60
hearts) to players within 6 blocks.

##

**Premium Example**
```yaml
  Skills:
  - damage{amount=<caster.var.somevariable> * 0.5 + 1} @target ~onTimer:20
```
This skill above does "<caster.var.somevariable> * 0.5 + 1" damage
if the varibute: <caster.var.somevariable>'s value is 5,this mechaine will does 3.5 damage


## 别名
- [x] d


<!--TAGS-->
<!--tag:Damage-->
