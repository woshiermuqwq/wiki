## 描述
Applies an 光环 to the 目标 that 触发 a skill when they die


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onDeathSkill | od     | Skill to 执行 if the 目标 dies                                  |<!--type:Metaskill-->|

> This 技能 继承 [光环] 技能


## 示例
Force an onDeath 光环 through sudoskill on all entities around you. When you kill them they will all 掉落 diamonds. This could be useful for quests where killing enemies makes them 掉落 a quest item, but you dont want to have to add the 掉落 生物. 
```yaml
ForceApplyAura:
  Skills:
  - sudoskill{s=ApplyAura} @EIR{r=50}
ApplyAura:
  Skills:
  - onDeath{od=DropDiamonds;auraname=Gonners;d=1200;i=1} @self
DropDiamonds:
  Skills:
  - dropitem{i=DIAMOND 3-5} @self
```


<!-- LINKS -->
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
