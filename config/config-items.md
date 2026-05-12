```yaml
#
# 物品配置选项
#
# 关于 Mythic 物品功能的更多信息可在此找到：
# https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Items/Items
#
Configuration:

  #================================================================================
  # 物品更新器
  #================================================================================
  ItemUpdating:
    Enabled: false
    OnLogin: true                   # 登录时更新
    OnScroll: true                  # 滚动时更新
    OnInvClose: true                # 背包关闭时更新

  #================================================================================
  # 全局华丽掉落（实验性功能）
  #================================================================================
  EnableFancyDropEffectsEverywhere: false

  #================================================================================
  # 物品默认值 - 选择物品选项的默认值
  #================================================================================
  DefaultItemOptions:
    Material: STONE
    PreventEnchanting: false            # 可设为 true 或 false（阻止附魔）
    PreventCrafting: modeled            # 可设为 true、false、modeled 或 default（阻止合成）
    PreventAnviling: default            # 可设为 true、false、modeled 或 default（阻止铁砧操作）
    PreventSmithing: default            # 可设为 true、false、modeled 或 default（阻止锻造）

  #================================================================================
  # 物品技能（需要 Crucible）
  #================================================================================
  ItemSkills:
    JoinDelay: 20                       # 加入时的延迟时间，在此之后才开始扫描物品

  #================================================================================
  # 物品属性（需要 Crucible）
  #================================================================================
  ItemStats:
    Rounding: 2                         # 属性生成时的默认小数位数
    SaveRatios: false                   # 为物品更新器保存生成的属性比率

  #================================================================================
  # 物品描述模板（需要 Crucible）
  #================================================================================
  LoreTemplates:
    EnableDefaultTemplate: false        # 是否对所有物品应用默认模板
    DefaultTemplateName: DEFAULT        # 默认模板名称
    DefaultTemplate:                    # 默认物品描述模板
    - Line:
        - '{stats}'
        - '{stats}<gray>额外属性：'
        - '{stats-each}<green> <stat.display>'
    - Filler: ''
    - Line:
        - '{augments:GEM}<gray>宝石：'
        - '{augments-each:GEM}<yellow><augment.display>'
    - Filler: ''
    - Line:
        - '{lore}'

  #================================================================================
  # 自定义方块（需要 Crucible）
  #================================================================================
  CustomBlocks:
    SwapIsPickBlock: true               # 可设为 true 或 false（替换拾取方块）

  #================================================================================
  # 自定义家具（需要 Crucible）
  #================================================================================
  Furniture:
    DefaultType: DISPLAY                # 可设为 DISPLAY、ARMOR_STAND 或 ITEM_FRAME
```
