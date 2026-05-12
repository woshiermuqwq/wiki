## 伤害修正

伤害修正器是一种属性，可以添加到你的 MythicMob 上，用于增减其从各种来源受到的伤害。

举例来说，假设一个实体受到了类型为 `ENTITY_ATTACK`、数值为 `10` 的伤害。根据其对应伤害修正器的值，会发生不同的情况：

- **值 > 0**：伤害量将乘以该值。如果值为 `2`，伤害翻倍；如果值为 `0.5`，伤害减半。
- **值 = 0**：伤害事件不会造成伤害，但仍会播放受伤动画。
- **值 < 0**：伤害事件将被取消，并且施法者会恢复生命值，回复量等于原始伤害乘以该修正器绝对值的数值。如果值为 `-2`，施法者将回复 `20` 点生命值；如果值为 `-0.1`，则回复 `1` 点生命值。

在正常情况下，部分伤害类型不会发生在某些生物身上（例如 SUICIDE，因为没有生物会自然自杀）。
伤害修正器完全是可选的，你只需要添加你想用的那些即可。

完整的可用伤害类型列表请参见 [Spigot 官方文档](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。

## 选项

| 修正器               | 说明                                                               |
| ------------------- | ------------------------------------------------------------------ |
| BLOCK_EXPLOSION     | 方块爆炸时，处于爆炸范围内的实体受到的伤害                               |
| CAMPFIRE            | 实体踩到营火或灵魂营火时受到的伤害                                     |
| CONTACT             | 实体接触仙人掌、滴水石锥（石笋）或甜浆果丛等方块时受到的伤害                |
| CRAMMING            | 由于游戏规则 maxEntityCramming 导致实体与过多实体碰撞时受到的伤害           |
| CUSTOM              | 自定义伤害                                                          |
| DRAGON_BREATH       | 末影龙吐息造成的伤害                                                   |
| DROWNING            | 在水中氧气耗尽时受到的伤害                                              |
| DRYOUT              | 应该在水中的实体离开水后受到的伤害                                       |
| ENTITY_ATTACK       | 一个实体攻击另一个实体时造成的伤害                                        |
| ENTITY_EXPLOSION    | 实体（如苦力怕）爆炸时，处于爆炸范围内的实体受到的伤害                       |
| ENTITY_SWEEP_ATTACK | 实体使用横扫攻击另一个实体时造成的伤害                                     |
| FALL                | 实体从超过 3 格的高度坠落时受到的伤害                                     |
| FALLING_BLOCK       | 被会造成伤害的掉落方块击中时受到的伤害                                     |
| FIRE                | 直接暴露在火焰中受到的伤害                                               |
| FIRE_TICK           | 因火焰燃烧效果受到的伤害                                                 |
| FLY_INTO_WALL       | 实体撞墙时受到的伤害                                                    |
| FREEZE              | 冰冻造成的伤害                                                         |
| HOT_FLOOR           | 实体踩到岩浆块时受到的伤害                                               |
| KILL                | /kill 命令造成的伤害                                                   |
| LAVA                | 直接暴露在熔岩中受到的伤害                                               |
| LIGHTNING           | 被闪电击中时受到的伤害                                                   |
| MAGIC               | 被伤害药水或法术击中时受到的伤害                                           |
| MELTING             | 雪傀儡融化造成的伤害                                                    |
| POISON              | 持续中毒效果造成的伤害                                                   |
| PROJECTILE          | 被弹射物攻击时受到的伤害                                                 |
| SONIC_BOOM          | 监守者的音爆攻擊造成的伤害                                               |
| STARVATION          | 饥饿值耗尽导致的饥饿伤害                                                 |
| SUFFOCATION         | 被卡在方块中受到的窒息伤害                                               |
| SUICIDE             | 自杀造成的伤害                                                         |
| THORNS              | 荆棘附魔在受到攻击时造成的反伤                                            |
| VOID                | 掉入虚空时受到的伤害                                                    |
| WITHER              | 凋零药水效果造成的伤害                                                   |
| WORLD_BORDER        | 世界边界造成的伤害                                                      |

<!--
这些选项由脚本自动生成，请勿直接编辑。
-->

## 示例

注意：修正值为 1 表示生物从该来源受到正常伤害。大于 1 的数值会按比例放大受到的伤害。小于 1 的数值会按比例减少受到的伤害。0 表示生物对该伤害来源免疫。
负值会使生物从该伤害类型中恢复生命值。但请注意，如果生物天生对该伤害免疫，则此法无效。例如：铁傀儡免疫坠落伤害、烈焰人免疫火焰/燃烧/熔岩伤害等。

在第一个示例中，我们的装甲僵尸只是一个普通的基础 MythicMob，没有添加任何特殊配置。

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
```

但是，如果我们给它添加伤害修正器属性，就可以开始调整它的弱点和抗性。在这个示例中，我们让近战和弹射物攻击对这只装甲僵尸只造成正常伤害的 75%。

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
  DamageModifiers:
  - ENTITY_ATTACK 0.75
  - PROJECTILE 0.75
```

好了，现在我们有了一个具有伤害抗性的僵尸。它受到的任何近战和弹射物伤害都将减少 25%（包括来自玩家和其他生物的伤害）。但它现在看起来有点太强了，所以我们也给它添加一个弱点来平衡。

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
  DamageModifiers:
  - ENTITY_ATTACK 0.75
  - PROJECTILE 0.75
  - MAGIC 1.25
```

我们的小装甲僵尸仍然对弹射物和近战攻击有很好的防护，但我们给它加了一个对魔法（喷溅型治疗药水）的弱点来作为平衡。

第二个示例是一个火元素生物。它不仅不会受到燃烧伤害，站在火中反而会回复生命值，而在熔岩中回复得更多。注意：这对下界生物无效，因为它们根本不会受到火焰伤害，因此无法对其火焰和熔岩伤害进行修正。

```yaml
FireElemental:
  Mobtype: zombie
  Display: '&cFire Elemental'
  Health: 20
  DamageModifiers:
  - FIRE -1
  - LAVA -4
  - FIRE_TICK 0
```
