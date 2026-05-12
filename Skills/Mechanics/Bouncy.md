## 描述
Applies an aura to the target that makes it bouncy


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onBounceSkill | onbounce, ob | 要执行的元技能 on bounce                            |<!--type:Metaskill-->|
| cancelevent | ce, canceldamage, cd | Whether to cancel fall damage 对于duration of the aura| false |
> 此机制继承所有[Aura](Skills/Mechanics/Aura) 机制


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
