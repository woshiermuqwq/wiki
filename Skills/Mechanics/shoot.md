## 描述

向目标实体或位置发射一支箭或物品弹射物，造成伤害。Shoot 技能在 2.4 版本中进行了重大更改。请参见下方了解更改前后的工作方式。

MM 4.11 中为 Shoot 和 Volley 添加了弹射物技能的大部分选项。


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | 要发射的弹射物类型                                         | arrow<!--type:Shoot_Type-->|
| damage    | d, amount | 弹射物造成的伤害量                            | 5       |
| velocity  | v         | 弹射物的速度向量                                       | 1       |
| maxDistance | md      | 弹射物行进的最大距离                      | 64      |
| poweraffectsvelocity | pav | 生物强度等级是否影响弹射物的速度向量                 | true    |
| interval  | int, i    | 弹射物每秒产生刻事件的频率             | 4       |
| item      |           | 被发射的物品。仅适用于某些弹射物类型        |<!--type:Material-->|
| ontickskill | ontick, ot, m, meta, s, skill | 弹射物每个刻/间隔执行的元技能 |<!--type:Metaskill-->|
| onhitskill | onhit, oh| 弹射物击中目标时执行的元技能        |<!--type:Metaskill-->|
| onendskill | onend, oe| 弹射物未命中并结束时执行的元技能        |<!--type:Metaskill-->|
| bounce    |           | 弹射物击中某物时是否弹跳            | false   |
| pickup    |           | 是否可以捡起物品                                                 | false   |
| expiration | duration, expire, e | 弹射物落地后在移除前应存在的刻数                                                                         | 100     |
| accuracy  | ac, a     | 弹射物的准确度                                           | 1       |
| knockback | kb        | 弹射物的击退强度                                 | 0       |
| piercelevel | pl      | 箭可以穿透实体的次数           | 0       | 
| verticaloffset       | vo         | 发射弹射物的垂直偏移量               | 0       |
| horizontaloffset     | ho         | 发射弹射物的水平偏移量             | 0       |
| forwardoffset | startfoffset, sfo | 发射弹射物的前方偏移量 | 1 |
| sideoffset | soffset, so | 发射弹射物的侧面偏移量 | 0 |
| startsideoffset | ssoffset, sso | 发射弹射物的侧面偏移量。是的，与上面相同，但*此*属性支持占位符 | `sideOffset 的值`|
| gravity   | g         | 弹射物是否受重力影响                 | true    |
| startyoffset | syo    | 弹射物的起始 y 偏移量                              | 0       |
| adjustvelocity | av   | 如果施法者是玩家，调整速度向量和方向，就像玩家自己射击一样 | true  |
| calculatefiringangle | cfa        | 如果设置且弹射物有 `gravity`，弹射物将在空中划出弧线后落在目标位置                                  | false   | 
| verticalnoise  | vn  | 发射弹射物的垂直噪声（随机性） | ((1-`accuracy`)*45)/10 |
| horizontalnoise | hn  | 发射弹射物的水平噪声（随机性）   | (1-`accuracy`)*45 |         
| fromorigin| fo        | 弹射物是否应从技能的原点发射| false   |  
> 此技能继承[伤害](/Skills/Mechanics/Damage)技能的所有*可继承*属性

### Type 属性
弹射物的类型可以为：
| 类型            | 别名        |
|-----------------|----------------|
| `ARROW`         |                |
| `SNOWBALL`      |                |
| `EGG`           |                |
| `ENDERPEARL`    |                |
| `POTION`        | `SPLASH_POTION`|
| `LINGERING_POTION` |             |
| `ITEM`          |                |
| `BLOCK`         | `FALLING_BLOCK`|
| `TRIDENT`       |                |

#### 药水类型属性
如果弹射物 `type` 为 `POTION`，则适用以下属性：
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| potiontype     | ptype, effect, pt, pe | 应用于弹射物的药水类型，如果类型为 POTION | SLOW<!--type:PotionEffectType-->|
| potionduration | pduration, pd | 药水效果的持续时间                           | 100     |
| potionlevel    | plevel, lvl, pl | 药水效果的等级                            | 1       |
| force          | overwrite, ow, override, or | 如果已应用，是否覆盖目标上的效果    | false  |
| potioncolor | pc      | 药水的颜色                                              | #FFFFFF<!--type:Color--> |
| hasParticles | particles | 是否不显示状态效果粒子                  | true    |
| hasIcon   | icon  | 是否不显示状态效果图标                              | true    |
| ambientparticles | ambient  | 是否显示环境粒子                             | false   |


#### 三叉戟类型属性
如果弹射物 `type` 为 `TRIDENT`，则适用以下属性：
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tridentitem | titem, ti | 三叉戟物品                                                   |         |

## 示例
```yaml
ArrowBarrage:
  Skills:
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
```


## 别名
- [x] shootprojetile


<!--TAGS-->
<!--tag:Projectile-->
<!--tag:Meta-Mechanic-->