**难度：初学者**

你可能想向正在与生物战斗的玩家显示其生命值，有几种不同的方式可以实现，本指南将逐一介绍！

# Boss 血条
你可以为生物创建 Boss 血条，用于显示其生命值，就像末影龙或凋零那样。操作很简单。
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  BossBar:
    Enabled: true
    Title: '&cSkeleton King!'
    Range: 50
    Color: GREEN
    Style: SEGMENTED_12
```

# 铭牌
你可以在生物头顶的铭牌中显示其生命值，可用多种方式实现。以下是两个示例：一个以数字形式显示生命值（15/20），另一个带有一个随生物血量减少而变化的进度条。

### 数字方式
需要结合 [SetName](/skills/mechanics/setname) 机制和 [~onDamaged](/Skills/Triggers/onDamaged) 触发器。我们利用生物的 display 选项来设置信息，使用 caster.hp 和 caster.mhp 占位符来获取当前生命值和最大生命值。
```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King &7(<caster.hp>/<caster.mhp>)'
  Skills:
  - setname{n=<caster.name>;delay=2} @self ~onDamaged
```
