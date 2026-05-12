## 描述
Creates an [光环] that, each tick, checks if a set of 条件 is met: If so, the execution of the onStart skill is immediately cancelled. 


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| terminate条件 | 条件, cond, c | The 条件 to check against                  |<!--type:条件-->|
| deep      |           | 是否 the terminable 光环, once its 条件 have been met, should also stop the execution of the [metaskill] it has been called from                                       | false   |
| onterminate | ox      | The [metaskill] to 执行 once the onStart is terminated            |<!--type:Metaskill-->|
> This 技能 继承 [光环] 技能

### Deep Attribute
The deep attribute is quite peculiar: when enabled, other than the onStart metaskill, it makes the terminate 光环 also affect the metaskill it was originally called from. So, if we had a situation like the following
```yaml
ExampleSkill:
  Skills:
  - terminable{deep=true;...}
  - skill:test1
  - delay 100
  - mechanic2

SecondarySkill:
  Skills:
  - mechanic1
  - delay 200
  - mechanic3
```
Then the `ExampleSkill` and the subsequently called `SecondarySkill` metaskill would be stopped if the terminable 光环 had its 条件 met: so, for example, if the terminable 光环 stopped the execution after 10 ticks, neither `技能2` or `技能3` could be triggered  

## 示例
```yaml
  Skills:
  - terminable{
    auraName=exampleAura;
    d=2000;
    conditions=[
      - health{h=<50} true
    ];
    onStart=[
    - state{s=charged_attack}
    - delay 20
    - skill{s=ChargedAttackDamage}
    ];
    onTerminate=[
    - state{s=charged_attack;remove=true}
    - state{s=stunned}
    ]} @self
```


## 别名
- [x] stoppable
- [x] cancelable
- [x] exit
- [x] terminatable


<!-- LINKS -->
[aura]: /Skills/Mechanics/aura
[metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->