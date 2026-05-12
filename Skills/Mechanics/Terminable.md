## 描述
Creates an [aura] that, each tick, checks if a set of conditions is met: If so, the execution of the onStart skill is immediately cancelled. 


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| terminateconditions | conditions, cond, c | The conditions to check against                  |<!--type:Conditions-->|
| deep      |           | Whether the terminable aura, once its conditions have been met, should also stop the execution of the [metaskill] it has been called from                                       | false   |
| onterminate | ox      | 要执行的[元技能] once the onStart is terminated            |<!--type:Metaskill-->|
> 此技能继承所有[aura] 技能

### Deep Attribute
The deep attribute is quite peculiar: when enabled, other than the onStart metaskill, it makes the terminate aura also affect the metaskill it was originally called from. So, if we had a situation like the following
```yaml
ExampleSkill:
  Skills:
  - terminable{deep=true;...}
  - skill:test1
  - delay 100
  - 技能2

SecondarySkill:
  Skills:
  - 技能1
  - delay 200
  - 技能3
```
Then the `ExampleSkill` and the subsequently called `SecondarySkill` metaskill would be stopped if the terminable aura had its conditions met: so, for example, if the terminable aura stopped the execution after 10 ticks, neither `技能2` or `技能3` could be triggered  

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
