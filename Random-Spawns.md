随机生成让你能够完全控制生物在世界中的生成方式。你可以自定义生物生成的位置、频率和数量，从而精确掌控生物的生成。

这是你第一次制作随机生成吗？建议先阅读[新手随机生成指南](/Guides/Your-First-Random-Spawn)

## 重要区别

有几个重要的随机生成选项需要区分：

-   **Action: REPLACE**
    -   REPLACE 操作用于将 Minecraft 自身随机生成系统生成的生物替换为你的自定义生物。
    -   这使你能完全控制 Minecraft 的生成系统。
    -   如果服务器上 Minecraft 的随机生成器被关闭（例如设置游戏规则 doMobSpawning 为 false），则此操作不会产生任何效果。

-   **Action: ADD**
    -   ADD 操作利用 MythicMobs 自身的生成算法，以类似 Minecraft 生成系统的方式在玩家周围生成随机生成点。
    -   但与 Minecraft 不同的是，这些生成点会在没有任何条件的情况下生成，允许你在任何光照等级和任何位置生成生物。
    -   关于这些生成点的详细配置可在 MythicMobs 的配置文件 "config.yml" 中找到。
    -   **请注意**，Action: ADD 只在生存和冒险模式玩家周围生成点，且仅在有位置存在时才生成。
    -   如果使用了需要实体的条件，会抛出异常。对于生物群系条件，可以使用 Biomes: 选项！
    -   要让 Action: ADD 生效，需要前往 `plugins/MythicMobs/config/config-spawning.yml` 并将 GenerateSpawnPoints 设置为 true！

-   **Action: DENY**
    -   Deny 操作用于阻止生物生成。
    -   任何匹配配置为 DENY 的随机生成条件的生物将不会生成。

-   **Action: SCALE**
    -   *即将推出的功能*

## 选项

所有可用随机生成选项的完整列表。

### 全局随机生成选项

#### 示例
```yaml
    my_favorite_randomspawn:
      Action: ADD
      Type: cute_zombie
      Level: 2
      Chance: 0.01
      Priority: 10
      UseWorldScaling: false
      Worlds: my_overworld,my_overworld_nether
      Biomes: JUNGLE,PLAINS
      Conditions:
      - day true
```
-   **Action: [操作]**
    -   使用的生成方法，默认为 "ADD"
    -   Action: ADD
    -   Action: REPLACE

-   **Type: [生物类型]**
    -   定义要生成的生物类型。可以是数组或多种生物类型
    -   Type: SuperZombie
    -   Type: SkeletalMage,WitchBoss
    -   也可以使用原版生物类型。
    -   可选地，还可以用以下语法让单个随机生成以不同的权重生成多种生物

```yaml
Deeps:
  Types:
  - RegularZombie 100
  - BigZombie 50
  - GiantZombie 5
  - HugeZombie 1
  Worlds: world
  Chance: 0.1
  Priority: 1
  Action: ADD
  PositionType: LAND
```

-   **Level: [数字]**
    -   指定生物生成的等级。
    -   必须为固定数字，不会解析数字范围。
    -   可能被世界缩放设置覆盖（见下方选项）
    -   默认为 1
    -   Level: 7

-   **Chance: [数字]**
    -   生物生成的概率。
    -   默认为 1
    -   **Chance: 0.025**

-   **Priority: [数字]**
    -   当多个生物被选中在同一生成点生成时，用于确定优先使用哪个随机生成的优先级。
    -   经验法则：*优先级数字越大 = 多个生物被选中时的选中概率越高*
    -   默认为 1
    -   **Priority: 128**

-   **UseWorldScaling: [true/false]**
    -   生成的生物等级是否受世界缩放设置影响
    -   默认为 true

-   **Conditions: [列表]**
    -   用于进一步约束随机生成的条件列表。
    -   若任一条件不满足，该随机生成将失败。
    -   完整可用条件列表见：[条件手册页面](/Skills/conditions#conditions)
    -   **Conditions:**
    -   **- condition 1**
    -   **- condition 2**
    -   **...**

-   **Worlds: [世界名]**
    -   应用随机生成的世界名称。
    -   可以是数组或多个世界
    -   这些名称对应你 Minecraft 世界在游戏文件中的命名
    -   **Worlds: world**
    -   **Worlds: world,world\_the\_end,world\_nether**
    -   **Worlds: jays\_overworld**

-   **Biomes: [生物群系]**
    -   指定生物类型可生成的生物群系。
    -   可以是数组或多个生物群系
    -   **Biomes: SNOWY\_TUNDRA,ICE\_SPIKES,SNOWY\_TAIGA,...**

-   **Reason: [原因]**
    -   要匹配的 Minecraft 随机生成原因
    -   可以是数组或多个原因
    -   如果设置了此选项，随机生成仅在匹配指定原因之一时生效
    -   可以是以下列表中的任一项：[CreatureSpawnEvent.SpawnReason](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/CreatureSpawnEvent.SpawnReason.html)
    -   **Reason: NATURAL**

-   **PositionType: [LAND/SEA]**
    -   此随机生成应使用陆地还是海洋的生成点
    -   仅对 Action: ADD 有效
    -   **PositionType: LAND**

-   **Cooldown: [数字]**
    -   同一随机生成两次生成之间必须经过的间隔（秒）
    -   于 MythicMobs 5.2.0 添加
    -   **Cooldown: 60**

- **Structures: [列表]**
  - 生物可在其中生成的结构列表。如果设置，生物将仅能在这些位置生成。

```yaml
Nether_Fortress:
  Types:
  - blaze_wisp 100
  - blazer 60
  - blaze_soldier 60
  - blaze_skeleton 50
  Worlds: world_nether
  Chance: 0.02
  Priority: 1
  Action: ADD
  PositionType: LAND
  Structures:
  - 'minecraft:fortress'
  - 'incendium:forbidden_castle'
  - 'incendium:infernal_altar'
```


### config.yml 中的额外选项
你可以在 `MythicMobs/config/config-spawning.yml` 文件中找到通用随机生成选项，最新版本可[在此处](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Config/config-spawning)找到
