## 描述
Executes the specified metaskill *once and separately* for each target of the 机制. Each metaskill that 将会 called will have a single entity/location (from among the original targets) as its inherited target.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| targettype | targett, tt | Which type of targets this 机制 should iterate on. Can be `ALL`, `ENTITY` or `LOCATION`| ALL<!--type:ALL,ENTITY,LOCATION-->|

> 此机制继承所有[Skill](/skills/mechanics/skill) 机制


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
