## 描述
Executes the specified metaskill *once and separately* for each 目标 of the 技能的所有属性。 Each metaskill that will be called will have a single entity/location (from among the original 目标) as its inherited 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| targettype | targett, tt | Which type of 目标 this 技能 should iterate on. Can be `ALL`, `ENTITY` or `LOCATION`| ALL<!--type:ALL,ENTITY,LOCATION-->|

> 此技能继承[Skill](/skills/技能/skill) 技能


## 示例
```yaml
# Skills file
ExampleForEach:
  Skills:
  - setvariable{var=skill.listuuid;type=LIST;val=""} @self
  - foreach{skill=ExampleSkill} @PIR{r=10;sort=NEAREST}
  - message{m=<skill.var.listuuid>}

ExampleSkill:
  Skills:
  - variableadd{var=skill.listuuid;value=<target.uuid>}
```


<!--TAGS-->
<!--tag:Meta-Mechanic-->