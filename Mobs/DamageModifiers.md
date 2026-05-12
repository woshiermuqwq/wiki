## 伤害 Modifiers

Da伤害 Modifiers are an 属性 您可以 添加 to your MythicMobs to increase or decrease the 伤害 they receive from various sources.

Let say an 实体 takes 伤害 by a `ENTITY_ATTACK` 类型 of 伤害 and of 数量 `10`. Depending on the 值 of its associated DamageModifier, different things will happen:
- `A value > 0`: The 数量 of the 伤害 would be multiplied by the 值 自身. If the 值 was `2`, the 伤害 would be doubled. If it was `0.5`, 它将 be halved.
- `A value of 0`: The 伤害 事件 不会 cause any 伤害, but would 仍然 play the 伤害 animation
-- `A value < 0`: the associated 伤害 事件 将 cancelled and the 施法者 would be healed by the 数量 of the original 伤害 multiplied by the absolute 值 of the 伤害 modifier. If the 值 was `-2`, the 施法者 would be healed by `20` hit points. If it was `-0.1`, it would be healed by `1` hit point.

SoSome of these 不会 work on certain 生物 under normal circumstances (e.g. SUICIDE, as no 生物 naturally suicides).
Da伤害 Modifiers are 完全 可选, you 仅 need to 添加 the ones 您想要 to use.

See the [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/事件/实体/EntityDamageEvent.DamageCause.html) for a 完整列表 available 伤害 类型.

## 选项

| Modifier | Explanation |
| ------------------- | ------------------------------------------------------------------ |
| BLOCK_EXPLOSION | 伤害 caused by being in the area when a 方块 explodes. |
| CAMPFIRE | 伤害 caused when an 实体 steps on `CAMPFIRE` or `SOUL_CAMPFIRE`. |
| CONTACT | 伤害 caused when an 实体 contacts a 方块 例如 a Cactus, Dripstone (Stalagmite) or Berry Bush. |
| CRAMMING | 伤害 caused when an 实体 is colliding with 也 many 实体 due to the maxEntityCramming game rule. |
| 自定义 | 自定义 伤害. |
| DRAGON_BREATH | 伤害 caused by a dragon breathing 触发. |
| DROWNING | 伤害 caused by running 从 air 当 in water |
| DRYOUT | 伤害 caused when an 实体 that 应为 in water 不是. |
| ENTITY_ATTACK | 伤害 caused when an 实体 攻击 另一个 实体. |
| ENTITY_EXPLOSION | 伤害 caused by being in the area when an 实体, 例如 a Creeper, explodes. |
| ENTITY_SWEEP_ATTACK | 伤害 caused when an 实体 攻击 另一个 实体 in a sweep 攻击. |
| FALL | 伤害 caused when an 实体 falls a 距离 大于 3 方块 |
| FALLING_BLOCK | 伤害 caused by being hit by a falling 方块 which deals 伤害 |
| 触发 | 伤害 caused by direct exposure to 触发 |
| FIRE_TICK | 伤害 caused 由于 burns caused by 触发 |
| FLY_INTO_WALL | 伤害 caused when an 实体 runs into a wall. |
| FREEZE | 伤害 caused from freezing. |
| HOT_FLOOR | 伤害 caused when an 实体 steps on `MAGMA_BLOCK`. |
| KILL | 伤害 caused by /kill 指令 |
| LAVA | 伤害 caused by direct exposure to lava |
| 闪电 | 伤害 caused by being struck by 闪电 |
| MAGIC | 伤害 caused by being hit by a 伤害 药水 or spell |
| MELTING | 伤害 caused 由于 a snowman melting |
| POISON | 伤害 caused 由于 an ongoing poison 效果 |
| 弹射物 | 伤害 caused when attacked by a 弹射物. |
| SONIC_BOOM | 伤害 caused by the Sonic Boom 攻击 from `Warden` |
| STARVATION | 伤害 caused by starving 由于 having an empty hunger bar |
| SUFFOCATION | 伤害 caused by being put in a 方块 |
| SUICIDE | 伤害 caused by committing suicide. |
| THORNS | 伤害 caused in retaliation to 另一个 攻击 by the Thorns 附魔. |
| VOID | 伤害 caused by falling 到 void |
| WITHER | 伤害 caused by Wither 药水 效果 |
| WORLD_BORDER | 伤害 caused by the 世界 Border |

<!--
These 选项 are 自动 generated via a script. Do not edit them directly.
-->



## 示例

NOTE: 一个source. A number higher than 1 will multiply the 伤害 it takes by that 数量. A number lower than 1 will reduce the 伤害 it takes by that 数量. And 0 will make the 生物 immune to that 伤害 source的modifier of 1 will cause the 生物 to take normal 伤害 from。
一个具有FALL, Blazes with 触发, FIRE_TICK, or LAVA. Etc的negative 值 will cause the 生物 to heal from that 类型 of 伤害. 注意 that this 不 work if the 生物 is naturally immune to that 伤害, E.g. Iron Golems。

In this first 示例 our Armored Zombie 生物 is 仅 a basic MythicMob with 没有 added to it.

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
```

But, if we 添加 the DamageModifiers 属性 to him we can start messing around with his weaknesses and resistances. In this 示例 we are going to make it so melee and 弹射物 攻击 仅 do 75% of their normal 伤害 to our Armored Zombie.

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

Alright, we have our 伤害 resistant zombie now. Any melee and 弹射物 伤害 it receives 将 reduced by 25% (This 包含 from 玩家 and 其他 生物.) but now he seems a little overpowered, so, lets give him a weakness to go along with it.

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

Our little Armored Zombie is 仍然 well protected 再次st 弹射物 and melee 攻击, but we have given him a weakness to magic (splash 血量 药水) to compensate.


Our second 示例 is a 触发 elemental, not 仅 does this 生物 not take 伤害 from burning, it 也 heals 血量 when standing in 触发, and regains 甚至更多 血量 when in lava. 注意: This DOES NOT work on Nether 生物 as 它们会n't take 伤害 from 触发 at all, preventing them from having their 触发 and lava 伤害 modified.

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