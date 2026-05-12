```yaml
#
# 生物配置选项
#
# 关于 Mythic 生物功能的更多信息可在此找到：
# https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Mobs/Mobs
#
Configuration:

  #================================================================================
  # 通用生物选项
  #================================================================================
  Mobs:
    CancelDamageIfZero: false           # 伤害为零时取消伤害事件
    KillMessagePrefix: ''               # 击杀信息前缀

  #================================================================================
  # 生物默认值 - 选择生物选项的默认值
  #================================================================================
  DefaultMobOptions:
    Despawn: true                       # 默认消失

    PreventOtherDrops: false            # 默认阻止其他掉落
    PreventVanillaDamage: false         # 默认阻止原版伤害

  #================================================================================
  # 掉落 - 影响生物掉落战利品的选项
  #================================================================================
  MobDrops:
    DefaultDropMethod: VANILLA                  # 默认掉落方式
    DoLootsplosionByDefault: false              # 默认进行战利品爆炸效果
    DoHologramNameByDefault: false              # 默认显示全息名称
    DoItemGlowByDefault: false                  # 默认物品发光
    DoItemBeamByDefault: false                  # 默认物品光束
    DoItemVFXByDefault: false                   # 默认物品视觉特效

    # 覆盖在掉落物品上的特殊 VFX 物品。
    # 可用于制作超华丽的掉落效果
    DefaultItemVFX:
      Material: POTION
      Model: 1
      #Generation: item/vfx_item            # Generation 需要 Crucible

    DoPerPlayerDropsByDefault: false           # 默认为每个参战者分别计算掉落
    MinimumDamagePercentForDrops: 0.00         # 获得每人掉落所需的最低伤害百分比
    DoClientsideDropsByDefault: false          # 每人掉落仅对该玩家可见

    DefaultDeathHologram:                      # 默认死亡全息图
      - '<rainbow>--------------------------------'
      - '<red><bold>已击败 <mob.name>'
      - '<gold>排名：<white>#<player.rank>'
      - '<gold>伤害：<white><player.damage>'
      - ''
      - '<green>#1. <1.name> - <1.damage>'
      - '<yellow>#2. <2.name> - <2.damage>'
      - '<yellow>#3. <3.name> - <3.damage>'
      - '<rainbow>--------------------------------'
    DefaultDeathChatMessage:                   # 默认死亡聊天消息
      - '<rainbow>--------------------------------'
      - '<red><bold>已击败 <mob.name>'
      - '<gold>排名：<white>#<player.rank>'
      - '<gold>伤害：<white><player.damage>'
      - ''
      - '<green>#1. <1.name> - <1.damage>'
      - '<yellow>#2. <2.name> - <2.damage>'
      - '<yellow>#3. <3.name> - <3.damage>'
      - '<rainbow>--------------------------------'

  #================================================================================
  # 生物蛋 - 与生物蛋相关的选项
  #================================================================================
  MobEggs:
    Material: PIG_SPAWN_EGG
    Model: 0
    DefaultDisplay: "<mob.name> 生成蛋"
    DefaultLore:
    - '<dark_gray>一个神话蛋，可以'
    - '<dark_gray>用来复活一只'
    - '<dark_gray><mob.name</dark_gray>'

  #================================================================================
  # 全息图 - 与全息相关功能的选项
  #================================================================================
  Holograms:
    GlobalOffset: 0.15                        # 全局偏移

    CastBar:                                   # 施法条
      InfoBackground: 0,0,0,0
      InfoBillboarding: VERTICAL
      CastBackground: 0,0,0,0
      CastBillboarding: VERTICAL
      Offset: 1

    HealthBar:                                 # 生命条
      Background: 0,0,0,0
      Billboarding: VERTICAL
      Offset: -0.05
      Length: 50
      Scale: 0.4,0.4,0.4

    Nameplate:                                 # 铭牌
      Background: 0,0,0,60
      Billboarding: VERTICAL
      Offset: 0

    Speech:                                    # 对话
      Background: 100,100,100,60
      Billboarding: VERTICAL
      LinePrefix: "<white>"
      Offset: 0.4

  #================================================================================
  # 等级缩放 - 允许生物升级并变强
  #================================================================================
  MobLeveling:

    # 用于随生物等级缩放其属性的公式
    ScalingEquations:
      Health: 'V * ((1.05)^(L-1))'
      Damage: 'V * ((1.05)^(L-1))'

    # 另一种旧版缩放生物属性的方法
    DefaultLevelModifiers:
      Health: 0.1
      Armor: 0
      Damage: 0
      KnockbackResistance: 0
      Power: 0

    # 每个世界的缩放选项
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
