## 描述
执行 a 技能 when the 生物 special 弹射物 类型 (trident, snowball, wither skull, llama spit etc) hits an 实体.

> The associated [@触发器](/技能/目标选择器/触发器) is the 实体 that 已被 hit

| [Implemented 占位符](/技能/占位符#变量-占位符) |
|--------------------------------|
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

### Compatible 弹射物
| Casting 实体 类型 | 弹射物 |
|---------------------|------------|
| BLAZE | SMALL_FIREBALL |
| ENDER_DRAGON | DRAGON_FIREBALL |
| GHAST | FIREBALL |
| LLAMA | LLAMA_SPIT |
| WITHER | WITHER_SKULL |
| DROWNED | TRIDENT |
| SNOW_GOLEM | SNOWBALL |


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