## 描述
Executes the specified metaskill *once and separately* for each value of the specified list/map formatted value. Each metaskill that 将会 called will have special skill parameters set depending on the iterated value:
- For list-formatted inputs
  - `<skill.value>` 对于iterated value
  - `<skill.index>` 对于index of the value
- For map-formatted inputs
  - `<skill.key>` 对于iterated key
  - `<skill.value>` 对于iterated value
  - `<skill.index>` 对于index of the key-value pair


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| values    | val, v    | The list or map formatted string to iterate on                       |         |

> 此机制继承所有[Skill](/skills/mechanics/skill) 机制


## 示例
```yaml
# Skills file
ExampleForEachValue:
  Skills:
  - setvariable{var=skill.listnames;type=LIST;val="Steve,Alex"} @self
  - foreachvalue{skill=ExampleSkill;values=<skill.var.listnames>} @self # Can also directly use the entry1,entry2,entry3... syntax

ExampleSkill:
  Skills:
  - message{m="Found you :D"} @PlayerByName{name=<skill.value>}
```

```yaml
# Skills file
ExampleForEachValueForMap:
  Skills:
  - setvariable{var=skill.mapnames;type=MAP;val="Steve=hello;Alex=1,2,3"} @self
  - foreachvalue{skill=ExampleSkill;values=<skill.var.mapnames>} @self # Can also directly use the key=value;key2=value2... syntax

ExampleSkill:
  Skills:
  - message{m="You have a value of <skill.value>"} @PlayerByName{name=<skill.key>}
```


<!--TAGS-->
<!--tag:Meta-Mechanic-->
