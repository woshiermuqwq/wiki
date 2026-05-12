```yaml
#
# 生成器配置选项
#
# 关于 Mythic 生成功能的更多信息可在此找到：
#
# 随机生成 -> https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Random-Spawns
# 生成器 -> https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Spawners
#
Configuration:

  #================================================================================
  # 生成器
  #================================================================================

  Spawners:

    # 如果你想手动创建和编辑生成器文件而不是使用指令，请启用此选项
    DisableCommandSaving: false

  #================================================================================
  # 随机生成
  #================================================================================
  RandomSpawning:

    # ADD 方法使用的生成器。可选 NONE、CLUSTER 或 LEGACY
    Generator: NONE

    # 生物生成会尝试在玩家周围生成的区域
    SpawnRadiusPerPlayer: 64
    SpawnRadiusPerPlayerMin: 12
    SpawnRadiusPerPlayerY: 16

    # 玩家被视为一个分组的距离
    PlayerClusterDistance: 24

    # 允许 Mythic 生物以此倍数超过原版上限生成
    LimitMultiplier: 1.2

    # 如果为 true，原版生物不计入上限
    IgnoreVanillaMobs: false

    # 如果为 true，仅通过生成器生成的 Mythic 生物才计入上限
    IgnoreUnnaturalMobs: false

    # 服务器生物上限。设为 -1 则遵循服务器限制，设为 0 则无限制
    SpawningLimit: -1

    # 生成器的默认本地生物上限。设为 -1 则遵循服务器限制。
    LocalSpawningLimit: -1

    # 每增加一个玩家，本地生物上限乘以此数
    LocalGroupMultiplier: 1.33

    # Action: REPLACE 生成器是否遵循 Spigot 生物上限
    ReplaceObeysCap: false

    # 每 tick 用于生成的最大毫秒数
    MaxGenerationTime: 5

    # 每组每 tick 搜索生成点的最大尝试次数
    MaxGenerationAttempts: 10
```
