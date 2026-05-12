## 描述
生物的特殊弹射物类型（三叉戟、雪球、凋零骷髅头、羊驼口水等）未命中实体而落地时执行技能。

### 兼容的弹射物
[> 参考 onProjectileHit 的兼容列表 <](/Skills/Triggers/onProjectileHit#compatible-projectiles)


## 示例
```yaml
YourAverageDrowned:
  Type: DROWNED
  Equipment:
  - TRIDENT HAND
  Skills:
  - message{m="哎呀……"} @target ~onProjectileLand
```


## 别名
- [x] onProjectile_Land
- [x] onTridentLand
