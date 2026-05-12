## 描述
Hides the 施法者 from 目标玩家 for a set duration.  

> The hidden entity can then be shown via the used of the [showentity] 技能.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraname  | buffname, debuffname | The name of the 光环                                      | #hiding |
| ignoreAuraOptions| iao, permanent, perma | This will make the 技能 ignore any [光环]-related option and the `duration` attribute      | false   | 

> This 技能 继承 [光环] 技能  
>> - The `auraname` attribute is **defaulted** at `#hiding`
>> - The `charges` attribute is **set** at `1`  
>> - The `maxStacks` attribute is **set** at `1`  
>> - The `mergeAll` attribute is **set** at `true`  


## 示例
```yml
DUMMY:
  Type: ZOMBIE
  Skills:
  - hide{d=100} @Server ~onInteract
```
##
```yml
CUSTOM_ITEM:
  Id: STICK
  Skills:
  - hide{d=100} @Server ~onUse #User is now invisible from all online players, no armor is shown
```


## 别名
- [x] hideFromPlayers
- [x] hideFromPlayer


<!-- LINKS -->
[aura]: /skills/mechanics/aura
[showentity]: /skills/mechanics/showentity



<!--TAGS-->
<!--tag:Effect-->
<!--tag:Meta-Mechanic:Aura-->

