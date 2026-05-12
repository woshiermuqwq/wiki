## 描述
Causes 玩家的 screen to black out.  


## 属性
> This 技能 继承 [光环](/Skills/技能/光环) 技能
>> - The `auraname` attribute is **set** at `#blackScreen`
>> - The `maxStacks` attribute is **set** at `1`  
>> - The `refreshDuration` attribute is **set** at `true`  
>> - The `interval` attribute is **set** at `10`  


## 示例
Blinds players when the 生物 teleports
```yaml
BlackScreen:
  Skills:
  - blackscreen{d=2} @PlayersInRadius{r=100} ~onTeleport
```


## 别名
- [x] effect:blackScreen
- [x] e:blackScreen


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->