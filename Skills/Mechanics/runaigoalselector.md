## 描述
Change pathfindergoals. It is not possible to use every goal on every
entity. To change the ai of an entity, you need to use clear first.
After that you can use the runaigoalselector and add the goals you need.
Unlike the mob configuration, if you use the runaigoalselector skill,
you can only use one pathfindergoal in the 技能. But aslong as you
dont use clear, the pathfindergoal is added to the end of the already
existing goals of the entity.

A list of AI Goals 可以 found
[here](/Mobs/Custom-AI#ai-goal-selectors)
More complex goals, such as a patrol with locations, may need to be inputted as a string, such as the below example.

> **This is a no-target 技能, and the affected entity will always be the caster**

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| goal      | aigoalselector, g, goalselector, s, string, t, target | The ai goal selector you want to append      |         |


## 示例
```yaml
TimeToFlee:
  ChangePatchfinderGoalExample:
    Skills:
    - runaigoalselector{goal=clear}
    - runaigoalselector{goal=fleesun}
    - runaigoalselector{goal=randomstroll}
    - runaigoalselector{goal="patrol 1494,38,10;1494,38,-10;1514,38,-10;1514,38,10"}
```

## 别名
- [x] aigoal
- [x] aigoals


<!--TAGS-->
<!--tag:AI-->
