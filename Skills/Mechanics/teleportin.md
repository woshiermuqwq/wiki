## 描述
Will teleport the target relative to the caster's yaw. The direction attribute 必须 in this format: direction=x,y,z

`x` is forward or backward, `y` is up or down, and `z` is left or right

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| vector    | direction,dir,d,v | The direction to where the mob 将会 teleported            |         |
| yaw       | y         | Yaw modifier                                                         | 0       | 
| targetasorigin | tao  | Will use the target's location as the origin instead of the caster's | false   |
            
    
## 示例
Will teleport the player that triggered the skill to the right of the caster.
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
