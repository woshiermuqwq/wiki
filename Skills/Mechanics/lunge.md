## 描述
Applies forward directional 速度 to the 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v, magnitude | The horizontal 速度 at which the entity is moved forward      | 1       |
| velocityY | vy, yv, yvelocity | The vertical 速度 at which the entity is moved forward   | 1       |
| oldmath   | old, o    | If the lunge 技能 should use the old math formula                | false   |

  
## 示例
```yaml
  Skills:    
  - lunge{velocity=15;velocityY=5} @Self
```


<!--TAGS-->
<!--tag:Movement-->
