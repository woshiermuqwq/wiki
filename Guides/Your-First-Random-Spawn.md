**难度：初学者**

[随机生成](/Random-Spawns) 系统允许你让自定义 MythicMobs 在世界中随机生成！你可以使用许多选项和条件来微调这些生成，让它们完全按你想要的方式生成！

创建生成时有两种操作可用：ADD 和 REPLACE。使用 REPLACE 会让 MythicMobs 覆盖原版生物生成，意味着生成的原版生物会减少，你对它的控制也更少。而 ADD 则在原版生成点之外额外生成额外的生成点，不影响原版生成，你拥有更多控制权。

使用 ADD 时，你必须启用 `/plugins/MythicMobs/config/config-spawning.yml` 中的 `GenerateSpawnPoints` 设置，且必须处于生存模式或冒险模式生物才会生成。

在本指南中，我们将使用 ADD 操作，因为它通常是更好的选择。

你的随机生成文件放在 `/plugins/MythicMobs/RandomSpawns` 文件夹中，也可以放入子文件夹以便更好地组织。你也可以在[包](/Packs)中创建 `RandomSpawns` 文件夹。


# 基础设置
随机生成的基础设置包含几个选项。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
```

在这个基础示例中，我们让生物 `SkeletonKing` 以 10% 的概率在我们的世界 `world` 和 `world_nether` 中生成。

- `Action: ADD` 我们使用 [ADD](/wikis/Random-Spawns#important-differences) 操作来生成生成点。
- `Type: SkeletonKing` 要生成的 MythicMob 的[内部名称](/Mobs/Mobs#internal_name)。
- `Chance: 0.1` 概率是基于 1 的百分比，所以 0.1 是 10%
- `Priority: 10` 如果我们有多个随机生成，且两个被选中在同一位置生成时，优先级更高的将生成。
- `Worlds: world,world_nether` 生物仅在这些世界中生成，基础服务器设置中这通常对应主世界和地狱。

### 生物群系

我们可以进一步指定生物能够生成的生物群系！可使用 Biomes 选项。可以只添加一个，也可以添加多个生物群系的列表。

Biomes 使用 [Spigot 生物群系名称](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)
```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
```
在此示例中，我们的生物可以在 `world` 和 `nether` 世界中生成，且仅在 `JUNGLE`、`FOREST` 和 `SOUL_SAND_VALLEY` 生物群系中生成。

### 位置类型
使用 ADD 操作时，你可以设置位置类型，告诉 Mythic 生物应该生成在陆地还是水中。
```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
  PositionType: LAND
```
现在我们的骷髅王只会在陆地上生成，而不会在海洋和河流中生成。

### 等级
如果你使用[等级](/Mobs/Levels)系统并希望生物以特定等级生成，也可以设置。
```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Level: 4
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
```
这将生成一个 4 级的生物。

# 添加条件
我们可以向随机生成添加几乎任何[条件](/Skills/conditions)，来进一步决定生物如何生成。通常我们只能使用实体类型和位置类型的条件，REPLACE 操作会检查实体条件。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
  Conditions:
  - night true
  - raining true
```
在这个示例中，我们添加了条件，使生物仅在夜间且下雨时生成。列表中的所有条件都必须满足生物才能生成。

**进阶提示**

使用[复合条件](/Skills/conditions#composite-conditions)，你可以设置满足其中之一但不一定非要全部满足的条件。

# 限制数量
你可以使用条件来限制生物生成，只允许特定数量的生物生成。最常见的两种方式是使用 [MobsInRadius](/skills/conditions/mobsinradius) 和 [MobsInChunk](/skills/conditions/mobsinchunk) 条件。
```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
  Conditions:
  - night true
  - raining true
  - mobsinchunk{a=<10} true
  - mobsinradius{t=SkeletonKing;a=<3;r=64} true
```
在这个示例中，我们只允许在区块内*任何*生物少于 10 只，且 64 方块半径内骷髅王少于 3 只时生成骷髅王。

# 缩放
本节仅适用于已设置[等级修正](/Mobs/Levels)的生物。

我们可以使用 [WorldScaling](/Mobs/Levels#world-scaling) 来决定生物的等级是否根据距离增加。默认情况下这是启用的，所以如果你的生物有等级修正，而你*不*希望它们基于世界缩放增加等级，请将其设置为 false。
```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  UseWorldScaling: false
```
