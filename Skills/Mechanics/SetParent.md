## 描述
Sets the "Parent" of the casting Mythic生物 as 目标实体.  
The Parent can be either a Player or another Mythic生物.
Works with the [@Parent Targeter](/mythiccraft/Mythic生物/-/wikis/Skills/Targeters/Parent), and the [IsParent 条件](/mythiccraft/Mythic生物/-/wikis/skills/条件/IsParent).  

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
