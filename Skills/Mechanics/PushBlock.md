## 描述
Pushes the block at the 目标 location in the given direction using piston logic.  
Direction 可以是 cardinal direction or a location targeter. If given a targeter, the block will be pushed once towards that location.
技能 follows piston rules and will push other connected slime blocks as well, but only if they're adjacent or in front of the block - it cannot push connected blocks behind the pushed block.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| direction | dir, d    | The direction of the movement. Can also be a Targeter                | NORTH<!--type:NORTH,SOUTH,EAST,WEST,UP,DOWN-->|
| onPush    | then      | The metaskill to execute once the block has been successfully pushed |<!--type:Metaskill-->|
| onFail    |           | The metaskill to execute if the block failed to be pushed            |<!--type:Metaskill-->|

### Direction Attribute
The direction attribute can either be a `named direction` or a `targeter`

### Named Direction
The possible named directions are
- `NORTH`
- `SOUTH`
- `EAST`
- `WEST`
- `UP`
- `DOWN`
and you can use them like the following
```yaml
  - pushblock{dir=UP} @SelfLocation{y=-0.1}
```

### Targeters
You can also use a targeter in as the attribute value's, like the following
```yaml
  - pushblock{dir=@Forward{f=1}} @SelfLocation{y=-0.1}
```


## 示例
```yaml
  Skills:
  - pushblock{dir=@Forward{f=1}} @ForwardWall{f=5;y=1;h=2;w=2}
```


<!--TAGS-->
<!--tag:World-->
<!--tag:Meta-Mechanic:Thenable-->