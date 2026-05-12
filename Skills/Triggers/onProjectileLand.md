## 描述
执行 a 技能 when the 生物 special 弹射物 类型 (trident, snowball, wither skull, llama spit etc) lands on the ground 没有 hitting an 实体.

### Compatible 弹射物
[> Reference onProjectileH它是 <](/技能/触发器/onProjectileHit#compatible-弹射物)


## 示例
```yaml
YourAverageDrowned:
  Type: DROWNED
  Equipment:
  - TRIDENT HAND
  Skills:
  - message{m="Awww..."} @target ~onProjectileLand
```


## 别名
- [x] onProjectile_Land
- [x] onTridentLand