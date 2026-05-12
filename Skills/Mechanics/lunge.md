## 描述
Applies forward directional velocity to the target.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| velocity  | v, magnitude | The horizontal velocity at which the entity is moved forward      | 1       |
| velocityY | vy, yv, yvelocity | The vertical velocity at which the entity is moved forward   | 1       |
| oldmath   | old, o    | If the lunge 技能 should use the old math formula                | false   |

  
## 示例
```yaml
  Skills:    
  - lunge{velocity=15;velocityY=5} @Self
```


<!--TAGS-->
<!--tag:Movement-->
