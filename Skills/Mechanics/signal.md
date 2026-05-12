## 描述
发送信号 to the specified targeter. Won't do anything when
targeted at players. The signal 可以 composed of any string. The
mob(s) that receives the signal can only act upon it if it has a
dedicated "~onSignal" trigger in its skill arsenal (see examples).

The signal can either be matched by comparing directly behind the
trigger (~onSignal:*ping*) or by the new
[lastsignal-condition](/skills/conditions/lastsignal).


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| signal    | s         | 要发送的信号                                                   | ping    |

  
## 示例
This example would make the "Master" mob signal it's minions a radius of
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
