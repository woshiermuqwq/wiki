## 描述
生物的弹射物命中实体时执行技能。

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为被命中的实体

| [已实现的占位符](/Skills/Placeholders#variable-placeholders)     |
|--------------------------------|
| `<skill.var.damage-amount>`    |
| `<skill.var.damage-type>`      |
| `<skill.var.damage-cause>`     |


## 实现
- [MythicCrucible](/../../../mythiccrucible/-/wikis/Skills/Triggers/onBowHit)


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
