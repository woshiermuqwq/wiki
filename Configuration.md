```yaml
# 更多信息请查阅插件手册或加入我们的 Discord：
# http://www.mythiccraft.io
#  
Configuration:
  Version: 5.2
  General:
    AllowMetrics: true
    CheckForUpdates: true
    CompatibilityMode: false
    DebugLevel: 0
    ErrorLogging: true
    Language: enUS
    SendGiveItemFeedback: true
  Clock:
    ClockInterval: 1 # 时钟间隔
    SaveInterval: 5 # 保存间隔
    SpawnsInterval: 2 # 生成间隔
    RandomSpawningInterval: 1 # 随机生成间隔
    ScannerInterval: 10 # 扫描器间隔
    CleanupInterval: 600 # 清理间隔
  Components:
    CustomSpawners: true # 自定义生成器
    RandomSpawning: true # 随机生成
  ItemUpdating:
    Enabled: true # 物品更新
  Targeters:
    Filters:
      Default:
        TargetSelf: false
        TargetPlayers: true
        TargetArmorStands: false
        TargetMarkers: false
        TargetCreativeMode: true
        TargetSpectatorMode: true
        TargetCitizensNPCs: false
        TargetAnimals: true
        TargetCreatures: true
        TargetMonsters: true
        TargetWaterMobs: true
        TargetFlyingMobs: true
        TargetSameFaction: true
        TargetOwner: true
        TargetNonMythic: true
        TargetVillagers: true
  Mobs:
    DespawnByDefault: true # 默认消失
    EnableAIModifiers: true # 启用 AI 修正
    EnableTimerSkills: true # 启用定时器技能
    EnableThreatTables: true # 启用仇恨表
    EnablePlayerFactions: true # 启用玩家阵营
    EnableLegacySkills: false # 启用旧版技能
    KillMessagePrefix: '' # 击杀信息前缀
    PreventOtherDropsByDefault: false # 默认阻止其他掉落
    Scaling:
      Default:
        Enabled: true
        ScaleVanillaMobs: true # 缩放原版生物
        PerBlocksFromSpawn: 250 # 每距离生成点多少方块
      world2:
        Enabled: true
        PerBlocksFromSpawn: 250
      world2_nether:
        Enabled: false
        PerBlocksFromSpawn: 100
    BossBar:
      UpdateInterval: 20 # Boss血条更新间隔
    ScalingEquations:
      Health: V * ((1.05)^(L-1)) # 生命值缩放方程
      Damage: V * ((1.05)^(L-1)) # 伤害缩放方程
    DefaultLevelModifiers: # 默认等级修正
      Health: 0.1
      Armor: 0
      Damage: 0
      KnockbackResistance: 0
      Power: 0
  RandomSpawning:
    DisableVanillaSpawns: false
    GenerateSpawnPoints: false
    MaxMobsMultiplier: 1.0
    SpawnRadiusPerPlayerY: 32
    DespawnLazyRandomMobs: true
    MaxGenerationTime: 20
    PointsPerSecond:
      Land: 5
      Air: 0
      Sea: 2
      Lava: 0
      Ground: 0
  Compatibility:
    Heroes:
      Enabled: true
    McMMO:
      Enabled: true
      ShowXPMessage: true
      XPMessageFormat: '&7你因击杀 <dropper.name> 获得了 <drop.amount> 经验'
    SkillAPI:
      Enabled: true
      ShowXPMessage: true
      XPMessageFormat: '&7你因击杀 <dropper.name> 获得了 <drop.amount> 经验'
    Vault:
      Enabled: true
      ShowMoneyMessage: true
      MoneyMessageFormat: '&7你因击杀 <dropper.name> 获得了 <drop.amount> 货币'

```
