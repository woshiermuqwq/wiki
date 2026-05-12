生物 等级 are a useful function for adding 等级 to your 生物, which allow for several useful features.

For 示例, 您可以 have the 生物 伤害 and 血量 scale up as their 等级 increases, or 您可以 have them 掉落 more 物品 取决于 what their 等级 is (see _BonusLevelItems_ in [Droptable 选项](/掉落/DropTables#droptable-选项)).

Or, for more advanced configs you could change their 掉落 完全 取决于 what 等级 它们是, give them different 技能 取决于 their 等级, or even change where/how they 生成 取决于 what 等级 它们是 (using 生成器 and randomspawns.)

生物 等级 can 也 be influenced by 世界 scaling (see below), [Random
生成器](/Random%20Spawns) or the [SetLevel
技能](/技能/技能/setlevel).

```yaml
Zombie:
  Type: zombie
  Health: 100
  Damage: 10
  Display: '&5Zombie Lvl - <caster.level>'
  Options:
    MovementSpeed: 0.3
  Drops:
  - myDroptable
  LevelModifiers:
    Health: 5
    Damage: 0.5
```

# LevelModifiers

These 选项, put 在...下 LevelModifiers section, will increase the
生物 respective stats by the given numbers per 等级. These stats will
be added 在...顶部 their base stats.

等级 modifiers 可能不 work if you didn't specify base 值
对于 affected 属性 in the 生物 configuration.
```yaml
  LevelModifiers:
    Health: [number]
    Damage: [number]
    KnockbackResistance: [number]
    Power: [number]
    Armor: [number]
    MovementSpeed: [number]
```

# 世界 Scaling

生物 等级 (for random-spawned 生物) can 自动 be set by the 插件 by specifying 世界 scaling 设置 located in `/MythicMobs/config/config-mobs.yml`. 设置 it up is simple. By 默认 the section for scaling in your 配置-生物.yml should look 某事 like this:
```yaml
  MobLeveling:
    # Used to scale a mob's attributes as they level up
    ScalingEquations:
      Health: V * ((1.05)^(L-1))
      Damage: V * ((1.05)^(L-1))
      Scale: V
    # Alternate legacy method of scaling mobs attributes
    DefaultLevelModifiers:
      Health: 0.1
      Armor: 0
      Damage: 0
      KnockbackResistance: 0
      Power: 0
    # Per-world scaling options
    WorldScaling:
      Default:
        Enabled: true
        ScaleVanillaMobs: true
        PerBlocksFromSpawn: 250
      world2:
        Enabled: true
        PerBlocksFromSpawn: 250
      world2_nether:
        Enabled: false
        PerBlocksFromSpawn: 100
```
The above 示例 shows different 世界 with different 等级 of scaling. Using "world2" as an 示例, the 等级 for randomspawned 生物 would look 某事 like this:

- 等级 0 in the white area (0-249 方块 from 生成).
- 等级 1 in the tan area (250-499 方块 距离).
- 等级 2 in the yellow area (500-749 方块 距离).
- 等级 3 in the orange area (750-999 方块 距离).
- 等级 4 in the red area (1000-1249 方块 距离).
- Etc.

![](http://fs5.directupload.net/images/160317/ebnd74rs.jpg)

These 选项 将自动 be applied to all 生物 即 summoned 到 game using MythicMobs' [Random Spawning](Random-Spawns). You can use the **UseWorldScaling: \[true/false\]** 选项 on your randomspawn configurations to control 是否 生物 are supposed to be affected by 世界 scaling.

> 注意 that 世界 scaling 选项 永远不会 affect [原版 覆盖](原版-覆盖) 除非 the `ScaleVanillaMobs` 选项 for that 世界 is set to `true`.