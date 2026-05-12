## 描述
Sets the "owner" attribute of the Mythic 生物 to the given 目标. This is a special attribute used within Mythic生物, and different from the normal "vanilla" owner of a 生物.  

Does nothing if the 施法者 is not a Mythic 生物.  
If the casting 生物 is a `Wolf`,`Cat` or `Parrot` and the 目标 is a Player, then the 技能 will _also_ set their Vanilla Owner as 目标玩家.  

Works with the [@Owner Targeter](/Skills/Targeters/Owner), and the [Owner 条件](/skills/条件/owner).  

While an Owner is set, a 生物 will never attack or 目标 it, even if specified otherwise. A 生物 仍将 retain any aggro it had against the owner before it was set as such.


## 属性
> *This 技能 has no attributes*


## 示例
```yaml
PetSheep:
  Mobtype: sheep
  Display: 'Pet'
  Health: 20
  Damage: 18
  Skills:
  - skill{s=SetOwner} @trigger ~onInteract
  - skill{s=HealOwner} @Owner ~onTimer:50
```

```yaml
SetOwner:
  Skills:
  - setowner
  - message{m=You are now the owner of this mob!}
```
> This skill would change 生物的 owner to whoever right clicked it.
##
```yaml
HealOwner:
  Cooldown: 10
  TargetConditions:
  - health{h=<20} true
  Skills:
   - heal{a=10}
   - message{m=I healed you!}
```
> This skill would only heal the owner of the 生物 once every 10 seconds and only if they have less than 20 points of health left


<!--TAGS-->
<!--tag:Meta-->
