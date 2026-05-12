## 描述
Causes the player's screen to black out.  


## 属性
> 此机制继承所有[Aura](/Skills/Mechanics/Aura) 机制
>> - The `auraname` attribute is **set** at `#blackScreen`
>> - The `maxStacks` attribute is **set** at `1`  
>> - The `refreshDuration` attribute is **set** at `true`  
>> - The `interval` attribute is **set** at `10`  


## 示例
Blinds players when the mob teleports
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
