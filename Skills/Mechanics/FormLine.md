## 描述
Makes the casting 生物 follow a linear path to a location


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| path      | p         | A list of either coordinates in the format `(x,y,z)` or [targeters]  |         |
| onGoalSkill| onGoal, og, then | The [metaskill] to execute when the last point is reached    |<!--type:Metaskill-->|
| tolerance |           | The minimum distance the 生物 must be from each point in order to have "reached" it                                                                                   | 2       |
| speed     | s         | The speed multiplier of the movement                                 | 1       |
| duration  | ticks, t, d, time, t | The maximum duration of the 技能的所有属性。 Unless set, it's the maximum possible value for an integer                                                                  |         |

> 此技能继承[光环](/Skills/技能/光环) 技能


## 示例
```yaml
  Skills:
  - formline{
    speed=2;
    tolerance=2;
    path=(200,5,520),(200,5,500),@forward{a=5};
    onGoal=[
      - message{m="I DID IT"} @world
    ]} @self ~onInteract
```


## 别名
- [x] lineup


<!--TAGS-->
<!--tag:Movement-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:AI-->