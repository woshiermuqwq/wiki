## 描述
Hides the caster from the targeted players for a set duration.  

> The hidden entity can then be shown via the used of the [showentity] 机制.  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraname  | buffname, debuffname | The name of the aura                                      | #hiding |
| ignoreAuraOptions| iao, permanent, perma | This will make the 机制 ignore any [aura]-related option and the `duration` attribute      | false   | 

> 此机制继承所有[Aura] 机制  
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
