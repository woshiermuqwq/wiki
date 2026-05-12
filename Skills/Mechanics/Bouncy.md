## 描述
Applies an 光环 to the 目标 that 使 it bouncy


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onBounceSkill | onbounce, ob | The metaskill to execute on bounce                            |<!--type:Metaskill-->|
| cancelevent | ce, canceldamage, cd | Whether to cancel fall damage for the duration of the 光环| false |
> 此技能继承[光环](Skills/技能/光环) 技能


## 示例
```yaml
ExampleSkill:
  Skills:
  - bouncy{auraName=bouce;onBounceSkill=ExampleSkill2;ce=true} @target

ExampleSkill2:
  Skills:
  - ignite
```


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->