```yaml
#
# 通用配置选项
#
# Mythic 的通用配置选项。更多信息请参阅 Wiki：
#
# 手册 - https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/home
# Discord - https://www.discord.gg/MythicCraft
#
Configuration:
  Version: 5.6

  #================================================================================
  # 通用选项
  #================================================================================

  General:
    AllowMetrics: true              # 允许发送指标数据
    CheckForUpdates: true           # 检查更新
    DebugLevel: 0                   # 调试级别
    DebugMode: false                # 调试模式
    DebugSpawners: false            # 调试生成器
    ErrorLogging: true              # 错误日志记录

    ThreadPoolSize: -1              # 线程池大小
    UseVirtualThreads: false        # 使用虚拟线程

    AnnounceOpReload: false         # 向 OP 公告重载

    # 尝试通过生物的显示名称匹配并将其转换为 Mythic 生物，
    # 用于不支持 Mythic API 但生成实体的其他插件
    CompatibilityMode: false

  #================================================================================
  # 功能 - 设为 false 可完全禁用某项功能
  #================================================================================
  Features:
    PlayerFactions: true            # 玩家阵营
    RandomSpawning: true            # 随机生成
    Spawners: true                  # 生成器

  #================================================================================
  # 指令 - 与指令相关的选项
  #================================================================================
  Commands:
    SendGiveItemFeedback: true      # 发送给予物品反馈

  #================================================================================
  # 时钟 - 影响时钟的选项。通常不建议更改。
  # 所有值以 tick 为单位
  #================================================================================
  Clock:
    Main: 1                         # 主时钟
    Saving: 300                     # 保存间隔
    Spawners: 2                     # 生成器时钟
    RandomSpawning: 1               # 随机生成时钟
    Scanner: 10                     # 扫描器时钟
    Cleanup: 600                    # 清理时钟

  #================================================================================
  # 与其他插件的内置兼容性
  #================================================================================
  Compatibility:
    ProtocolLib:
      Enabled: true
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
      MoneyMessageFormat: '&7你因击杀 <dropper.name> 获得了 <drop.amount> 货币'```
