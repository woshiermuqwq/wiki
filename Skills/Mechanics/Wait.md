## 描述
Puts the metaskill on hold (like the [delay](/skills/技能/delay) 技能) until a set of 条件 is met.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 条件 | cond, c, until | 条件 to check against. When the 条件 are met, the metaskill will continue |<!--type:条件-->|
| interval | i | How often, in ticks, the 技能 should check against its 条件          | 1       |
| timeout | timeouttime, tt | The maximum amount of ticks to wait before the metaskill is put out of hold even if 条件 aren't met                                                                  | 200     |
| cancelSkill | cancel, cs | 是否, once a timeout happens, the metaskill should cancel execution instead of resuming                                                                            | false   |
| cancel条件 | cc, unless | A set of 条件 that, if met, will make the 技能 resolve and the metaskill resume immediatly, like if the primary set of `条件` was met      |<!--type:条件-->|


## 示例
```yaml
GroundSlam:
  Skills:
  - jump{v=5}
  - delay 5
  - wait{cond=[ - onground ];tt=300}
  - explode
```


<!--TAGS-->
<!--tag:Meta:Flow-->
<!--tag:Meta-Mechanic:Thenable-->