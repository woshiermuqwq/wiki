## 描述
Sets the world's time. Depending on the attributes used, the change in time 可以 absolute or relative to the target player.

Time 机制s 必须 synced to function. "sync=true;"

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mode      | m         | The mode used in the time 机制. Can be ADD/SET/RESET             | ADD<!--type:Time_Mode-->|
| amount    | ticks, t, amt | The amount of ticks by which the time 将会 changed            | 20      |
| personal  |           | Sets whether to change the global time or the player's client time   | false   |
| relative  |           | Sets whether to keep the player's time synchronized to its world time with an offset                                                                                         | true    |

#### Mode Attribute
The different values the mode attribute 可以 all have different effects
- **`ADD`** - Sets the current time of the world with an offset
- **`SET`** - Sets the current time of the world
- **`RESET`** - Re-syncs the target's world time with the server world time, if it is not already synced

## 示例
```yaml
# Mob File
ExampleMob:
  Type: ZOMBIE
  Skills:
  - sudoskill{s=MidnightAura} @PIR{r=30} ~onTimer:20
```
```yaml
# Skills File
MidnightAura:
  Skills:
  - aura{auraName=midnight;i=1;ms=1;rd=true;
    onTick=[
      - time{mode=SET;amount=18000;personal=true;relative=false;sync=true} @self
    ];
    onEnd=[
      - time{mode=RESET;sync=true} @self
    ]} @self
```

## 别名
- [x] setTime


<!--TAGS-->
<!--tag:World-->
<!--tag:Effect-->
