## 描述
Feeds 目标玩家.  
Doesn't work for other 生物.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount     | a        | The amount of hunger to restore                                      | 1       |
| saturation | s        | The amount of saturation to restore                                  | 0       |
| overfeed   | o,of     | 是否 to overfeed                                           | false   |

## Amount Attribute
1 amount is half a food unit.  
Overfeeding means excess food is converted into saturation.  
Allows for negative values to decrease food!


## 示例
This skill feeds the player 10 hunger (or 5 drumsticks).
```yaml
  Skills:
  - feed{amount=10} @trigger ~onInteract
```