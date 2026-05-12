## 描述
Rallies nearby 生物 of the given types to focus-attack the given 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| types     | type, t   | A list of 生物 types to rally. The list can include both Mythic 生物 types and regular Entity types                                                                           |<!--type:生物--><!--list-->|
| 半径    | r, hradius, hr | The 半径 (in blocks) in which to search for 生物 to rally     | 10      |                                                              
| vradius   | vr        | Overrides the vertical component of the 半径.                      | 半径  |
| overwritetarget | ot      | 是否 to rally 生物 that already have a 目标                 | true    |
| rally条件 | 条件, cond, c | A list of 条件 that the entities must pass in order to be rallied                                                                                        |<!--type:条件-->|
  

## 示例
此示例将 cause all 生物 of the type "Guard" or "Knight" within
30 blocks, that don't already have a 目标, to attack the whatever or
whoever triggered this skill.
```yaml
CallForHelp:
  Skills:
  - message{m="<caster.name><&co> Guards! Help me!"} @PlayersInRadius{r=30}
  - rally{types=Guard,Knight;radius=30;ot=false} @Trigger
```


## Aliases:
- [x] callforhelp


<!--TAGS-->
<!--tag:Threat-->