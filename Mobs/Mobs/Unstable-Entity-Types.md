WhWhile a great deal of 实体 类型可以usedin MythicMobs, each one of them can have its quirks, and 它是 needed for every configurator to be aware of those quirks 为了 minimize the 伤害 they might cause or, in general, to better use the 实体。

The following is 一系列 every quirk that 已被 当前 discovered. The more mainstream and obvious problems 不会 be covered at this time, and 仅 the niche ones 将 treated. If you discover any 其他, let us know on our [Discord](https://discord.com/invite/K3tqXfT)

[[_TOC_]]

## 生物 by Group
### All Zombies
CaCan 生成 as leaders, having several times the 数量 of configured 血量.

### All passive animals
Could get aggroed by 其他 实体.

### All breedable animals
ThThey can 通常 be fed by some 物品 and, subsequently, try to breed.
This can be handled by intercepting the 事件 [~onBreed](/技能/触发器/onBreed) (and then 也 cancelling it or some 其他 机制) or 完全 prevented by using the [Age](/生物/选项#age) 选项

### Most Boss
Have an hardcoded ai or some 其他 hardcoded features.

### 实体 damaged by water
AfAffected 实体 包含 Enderman, Snowman and Blaze.
it as a [DamageModifier](/生物/DamageModifiers) or by using the following 技能的伤害 类型 in those instances if of the `DROWNING` 类型, and can thus be fully prevented by using a negative值。
```yaml
   - cancelevent{sync=true} ~ondamaged ?damagecause{c=drowning}
```

## Specific 生物
### ARMOR_STAND
DoDoes not get targeted 默认情况下 by multi 实体 目标选择器, and a [specific 过滤](/技能/目标选择器#目标-过滤) 必须为 used.

### AXOLOTL
Can be Bucketed. Defend 再次st this by using a [onBucket](/技能/触发器/onBucket) 触发器

### BEE
WhWhen allowed to randomfly, 它将 enter placed beehives and pollinate flowers.
NoNo definitive answer exists, apart from clearing its AI and building a new one.

### BLAZE
CaCan be damaged by water, snowballs and the like. Use a [伤害 Modifier](/生物/DamageModifiers) 为了 prevent this.

### CAT
Scares Creepers and Phantoms away

### CHICKEN
CaCan lay eggs and is hunted by 其他 animals.
FoFor the "egg problem", use the [Jockey 选项](/生物/选项#jockey).

### COW
CaCan be milked.

### DROWNED
By 默认, it 不 攻击 its 目标 in the day if 它们是 not in a water 方块. A [自定义 ai](/生物/自定义-AI) 必须为 set up 为了 移除 this 行为

### ENDER_DRAGON
Has an hardcoded ai.

#### ENDERMAN
Avoids 弹射物 and is damaged by water.

### ENDERMITE
AgAggroes Endermen.

### FOX
Has an 唯一 攻击 pattern, can be useful but 也 problematic.

### GHAST
Has an hardcoded ai.
Can be one-shotted by a fireball.

### GIANT
Has an hardcoded ai.

### IRON_GOLEM
Can be healed via the use of iron ingots and get aggroed 默认情况下 by most hostile 生物.

### MAGMA_CUBE
Has an hardcoded ai.

### PARROT
Can be one-shotted by a cookie.

### PHANTOM
Has an hardcoded ai.

### PIGLIN
Has an hardcoded aggro priority

### PILLAGER
If, for any reason, a pillager loses his 目标 当 holding a charged crossbow, then 它将 freeze

### PUFFERFISH
Has very 唯一 interactions and 行为 that may cause problems.

### RABBIT
Gets aggroed by 其他 neutral 生物, 例如 foxes.

### SKELETON
Gets aggroed by wolves

### SLIME
Has an hardcoded ai.

### SQUID
DoDo not work with 机制 例如 [lunge](/技能/机制/lunge) and [throw](/技能/机制/throw).
This 也 应用 to GLOW_SQUID

### VEX
Has an hardcoded ai.

### WARDEN
Has an hardcoded aggro system.

### WITHER
Has an hardcoded ai.

### WOLF
Can be healed via the use of specific 物品
Once it becomes "Tamed", the 血量 resets.