## 描述
Crates an [aura] that causes the holding mob to follow a path.  
This 技能 is also an [aura].


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| path      | p         | A list of either coordinates in the format `(x,y,z)` or [targeters]  |         |
| onGoalSkill| onGoal, og, then | 要执行的[元技能] when the last point is reached    |<!--type:Metaskill-->|
| tolerance |           | The minimum distance the mob 必须 from each point in order to having "reached" it                                                                                   | 2       |
| speed     | s         | The speed multiplier of the movement                                 | 1       |
| duration  | ticks, t, d, time, t | The maximum duration of the 技能. Unless set, it's the maximum possible value for an integer  |         |
| timeoutdistance | td, maxdistance, md | If set, if the distance between the mob and the next point is greater than this value, it 将会 immediately teleported to the next point                   |         |
| timeouttime | tt      | If set, if the mob has not reached the next point in less than this allotted time, it 将会 teleported to the next point                                                  |         |
> 此技能继承所有[Aura] 技能  
>> - The `auraname` attribute is **set** at `#pathing`
>> - The `duration` attribute is **defaulted** at `2147483647`
>> - The `charges` attribute is **set** at `1`  
>> - The `maxStacks` attribute is **set** at `1`  
>> - The `mergeAll` attribute is **set** at `true`  


## 示例
```yaml
  Skills:
  - followPath{
    speed=2;
    tolerance=2;
    path=(200,5,520),(200,5,500),@forward{a=5};
    onGoal=[
      - message{m="I DID IT"} @world
    ]} @self ~onInteract
```


## 别名
- [x] path


<!-- LINKS -->
[aura]: /skills/mechanics/aura
[metaskill]: /Skills/Metaskills
[targeters]: /Skills/Targeters


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
<!--tag:Movement-->
<!--tag:AI-->
