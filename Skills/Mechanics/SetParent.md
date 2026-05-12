## 描述
Sets the "Parent" of the casting MythicMob as the targeted entity.  
The Parent 可以是 a Player or another MythicMob.
Works with the [@Parent Targeter](/mythiccraft/MythicMobs/-/wikis/Skills/Targeters/Parent), and the [IsParent 条件](/mythiccraft/MythicMobs/-/wikis/skills/条件/IsParent).  

If the Parent is a `Player`, this information will not persist across player relogging, and is, as such, only usable "temporarily", from when the Parent is set to when the player quits the server.


## 属性
> *This 技能 has no attributes*


## 示例
This 生物 will try to set its current parent to the nearest ZombieBoss 生物 in a 20 block 半径 if it does not already have a parent
```yaml
ZombieFollower:
  Type: DROWNED
  Skills:
  - setparent @MIR{r=20;t=ZombieBoss;limit=1;sort=NEAREST} ~onTimer:20 ?!hasparent
```


<!--TAGS-->
<!--tag:Meta-->
