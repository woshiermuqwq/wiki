## 描述
执行 a 技能 when the 生物 弹射物 hits an 实体.

> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that 已被 hit

| [Implemented 占位符](/技能/占位符#变量-占位符) |
|--------------------------------|
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/技能/触发器/onBowHit)


## 示例
```yaml
NotYourAverageSkeleton:
  Type: SKELETON
  Equipment:
    - BOW HAND
  Skills:
  - modifyDamage{a=3;modifier=MULTIPLY;sync=true} ~onBowHit
```


## 别名
- [x] onBow_Hit
- [x] onArrowHit