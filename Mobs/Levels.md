生物等级是一项实用功能，可以为你的生物添加等级系统，从而支持多种有用的特性。

例如，你可以让生物的伤害和生命值随等级提升而增长，或者让它们根据等级掉落更多物品（参见[掉落表选项](/drops/DropTables#droptable-options)中的 _BonusLevelItems_）。

更进一步的话，你可以根据等级完全改变生物的掉落物，根据等级赋予不同的技能，甚至根据等级改变它们的生成位置/方式（利用刷怪点和随机生成）。

生物等级还会受到世界缩放（见下文）、[随机生成](/Random%20Spawns)或[设置等级技能](/skills/mechanics/setlevel)的影响。

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

# 等级修正

这些选项放在 `LevelModifiers` 区块下，每提升一级，生物的对应属性就会增加给定的数值。这些加成会叠加在基础属性之上。

如果在生物配置中未指定受影响的属性的基础值，等级修正可能不会生效。
```yaml
  LevelModifiers:
    Health: [数值]
    Damage: [数值]
    KnockbackResistance: [数值]
    Power: [数值]
    Armor: [数值]
    MovementSpeed: [数值]
```

# 世界缩放

通过设置 `/MythicMobs/config/config-mobs.yml` 中的世界缩放选项，插件可以自动为随机生成的生物赋予等级。配置非常简单。默认情况下，`config-mobs.yml` 中的缩放部分大致如下：
```yaml
  MobLeveling:
    # 用于随着生物升级缩放其属性
    ScalingEquations:
      Health: V * ((1.05)^(L-1))
      Damage: V * ((1.05)^(L-1))
      Scale: V
    # 备用的传统生物属性缩放方式
    DefaultLevelModifiers:
      Health: 0.1
      Armor: 0
      Damage: 0
      KnockbackResistance: 0
      Power: 0
    # 按世界分别缩放
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
以上示例展示了不同世界使用不同缩放级别的配置。以 `world2` 为例，随机生成生物的等级如下：

-   白色区域（距出生点 0-249 格）：等级 0。
-   浅棕色区域（距离 250-499 格）：等级 1。
-   黄色区域（距离 500-749 格）：等级 2。
-   橙色区域（距离 750-999 格）：等级 3。
-   红色区域（距离 1000-1249 格）：等级 4。
-   以此类推。

![](http://fs5.directupload.net/images/160317/ebnd74rs.jpg)

这些选项会自动应用于所有通过 MythicMobs [随机生成](Random-Spawns)召唤到游戏中的生物。你可以在随机生成配置中使用 **UseWorldScaling: \[true/false\]** 选项来控制生物是否受世界缩放的影响。

> 注意：世界缩放选项永远不会影响[原版覆盖](Vanilla-Overrides)，除非该世界的 `ScaleVanillaMobs` 选项被设为 `true`。
