## 描述
Sends a signal to the specified targeter. Won't do anything when
targeted at players. The signal can be composed of any string. The
生物(s) that receives the signal can only act upon it if it has a
dedicated "~onSignal" 触发 in its skill arsenal (see examples).

The signal can either be matched by comparing directly behind the
触发 (~onSignal:*ping*) or by the new
[lastsignal-条件](/skills/条件/lastsignal).


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| signal    | s         | The signal to send                                                   | ping    |

  
## 示例
此示例将 make the "Master" 生物 signal it's minions a 半径 of
20 blocks to shoot an arrow the nearest players, relative to the minions
positions, upon being damaged.

```yaml
# Mob file:
Master:
  Type: zombie
  Skills:
  - summon{m=Minion} @self ~onSpawn
  - signal{s=ATTACK} @MobsInRadius{r=10;t=Minion} ~onDamaged
Minion:
  Type: baby_zombie
  Skills:
  - skill{s=ShootAttacker} @NearestPlayer ~onSignal:ATTACK
```

```yaml
# Skill file:
ShootAttacker:
  Skills:
  - shoot{t=arrow}
```


## 别名
- [x] sendsignal


<!--TAGS-->
<!--tag:Meta-->
