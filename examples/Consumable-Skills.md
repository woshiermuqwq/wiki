这些技能通常由玩家使用物品时触发，并利用 [Mythic Crucible](https://git.lumine.io/mythiccraft/mythiccrucible)。
### 进食技能
----------
* 一个食物消耗示例技能，使用时恢复饱腹感并短暂提供饱和药水效果，同时带有轻微延迟播放三种音效和粒子。

```yaml
eatmeal:
  Skills:
  - feed{amount=10;overfeed=true} @self
  - effect:particles{p=happy_villager;amount=5;speed=.5;y=1} @self
  - effect:sound{s=minecraft:entity.experience_orb.pickup;v=0.8;p=0.6} @self
  - Delay 2
  - effect:sound{s=minecraft:entity.experience_orb.pickup;v=0.8;p=0.7} @self
  - Delay 2
  - effect:sound{s=minecraft:entity.experience_orb.pickup;v=0.8;p=0.8} @self
  - potion{t=SATURATION;d=100;l=2;force=true} @self
```

---

### 飞行药水技能
----------
* 一个药水消耗法术，使用后给予使用者在 1 分钟内飞行的能力，带有一个倒计时剩余时间的 Boss 血条和显示效果激活中的粒子。

```yaml
basicflypot:
  Conditions:
  Skills:
  - effect:sound{s=entity.generic.drink;v=1;p=1} @self
  - effect:particles{p=fireworks_spark;amount=20;speed=.5;y=1} @self
  - effect:sound{s=block.end_portal_frame.fill;v=0.3;p=2} @self
  - effect:sound{s=item.bottle.fill_dragonbreath;v=0.3;p=0.8} @self
  - effect:sound{s=minecraft:block.beacon.power_select;v=1;p=1.4} @self
  - effect:particles{p=ELECTRIC_SPARK;amount=10;speed=.8;y=1} @self
  - fly{duration=1200;ot=flightaura;i=20;bt=true;auraName=Flight Remaining:} @self
flightaura:
  Skills:
  - effect:particles{p=fireworks_spark;amount=5;speed=.1;y=1} @self
```
