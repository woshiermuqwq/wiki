## 描述
施放一个元技能来判断此条件是否应该通过。这允许你对给定目标应用更复杂的逻辑。被调用的元技能需要使用 [DetermineCondition](/Skills/Mechanics/DetermineCondition) 技能来设置/修改此条件是否应该通过。  

<!--extends:mechanic:metaskillmechanic-->

## 属性
> 此条件继承 [Skill](/Skills/Mechanics/Skill) 技能的所有属性


## 示例
```yaml
YourNormalMetaskill:
  Conditions:
  - metaskillcondition{skill=metaskillcondition_check;hello=ciao;world=mondo}
  Skills:
  - message{m="条件已通过"} @self
metaskillcondition_check:
  Conditions:
  - holding{types=stick}
  Skills:
  - log{message=元技能条件已通过，参数为 <skill.test> <skill.aaa>} @self
  - determineCondition{det=true} @self
```


## 别名
- [x] skillcondition