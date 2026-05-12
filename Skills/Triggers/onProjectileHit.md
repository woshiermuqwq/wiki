## 描述
生物的特殊弹射物类型（三叉戟、雪球、凋零骷髅头、羊驼口水等）命中实体时执行技能。

> 关联的 [@trigger](/Skills/Targeters/Trigger) 为被命中的实体

| [已实现的占位符](/Skills/Placeholders#variable-placeholders)     |
|--------------------------------|
| `<skill.var.damage-amount>`    |
| `<skill.var.damage-type>`      |
| `<skill.var.damage-cause>`     |

### 兼容的弹射物
| 施法实体类型 | 弹射物 |
|---------------------|------------|
| BLAZE               | SMALL_FIREBALL |
| ENDER_DRAGON        | DRAGON_FIREBALL |
| GHAST               | FIREBALL |
| LLAMA               | LLAMA_SPIT |
| WITHER              | WITHER_SKULL |
| DROWNED             | TRIDENT |
| SNOW_GOLEM          | SNOWBALL |


## 示例
```yaml
NotYourAverageDrowned:
  Type: DROWNED
  Equipment:
    - TRIDENT HAND
  Skills:
  - modifyDamage{a=3;modifier=MULTIPLY;sync=true} ~onProjectileHit
```


## 别名
- [x] onProjectile_Hit
- [x] onTrident_Hit
- [x] onTridentHit
