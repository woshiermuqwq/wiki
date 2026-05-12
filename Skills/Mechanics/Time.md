## 描述
Sets the world's time. Depending on the attributes used, the change in time can be absolute or relative to the 目标 player.

Time 技能 must be synced to function. "sync=true;"

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mode      | m         | The mode used in the time 技能 Can be ADD/SET/RESET             | ADD<!--type:Time_Mode-->|
| amount    | ticks, t, amt | The amount of ticks by which the time will be changed            | 20      |
| personal  |           | Sets 是否 to change the global time or 玩家的 client time   | false   |
| relative  |           | Sets 是否 to keep 玩家的 time synchronized to its world time with an offset                                                                                         | true    |

#### Mode Attribute
The different values the mode attribute can be all have different effects
- **`ADD`** - Sets the current time of the world with an offset
- **`SET`** - Sets the current time of the world
- **`RESET`** - Re-syncs 目标的 world time with the server world time, if it is not already synced

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
