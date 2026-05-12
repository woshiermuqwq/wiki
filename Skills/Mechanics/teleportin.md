## 描述
Will teleport the 目标 relative to 施法者的 水平朝向(yaw). The direction attribute must be in this format: direction=x,y,z

`x` is forward or backward, `y` is up or down, and `z` is left or right

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| vector    | direction,dir,d,v | The direction to where the 生物 will be teleported            |         |
| 水平朝向(yaw)       | y         | 水平朝向(yaw) modifier                                                         | 0       | 
| targetasorigin | tao  | Will use 目标的 location as the 原点 instead of 施法者的 | false   |
            
    
## 示例
Will teleport the player that triggered the skill to the right of the 施法者.
```yaml
  Skills:
  - teleportin{vector=0,0,1} @trigger ~onInteract
```

## 别名
- [x] tpin 
- [x] tpdir 
- [x] tpi


<!--TAGS-->
<!--tag:Movement:Teleport-->
