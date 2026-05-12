## 描述
Change 目标 pathfindergoals. It is not possible to use every goal on
every entity. To change the ai of an entity, you need to use clear
first. After that you can use the runaitargetselector and add the goals
you need. Unlike the 生物 configuration, if you use the
runaitargetselector skill, you can only use one pathfindergoal in the
技能. But aslong as you dont use clear, the pathfindergoal is added
to the end of the already existing goals of the entity.

A list of available 目标 can be found [here](/生物/Custom-AI#ai-目标-selectors)

> **This is a no-目标 技能, and the affected entity will always be the 施法者**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 目标    | aitargetselector, s, string, targetselector, goal, g | The 目标 selector you want to append                               |         |


## 示例
```yaml
TargetPossibleThreats:
  Skills:
  - runaitargetselector{target=clear}
  - runaitargetselector{target=players}
  - runaitargetselector{target=monsters}
```


## 别名
- [x] aitarget


<!--TAGS-->
<!--tag:AI-->