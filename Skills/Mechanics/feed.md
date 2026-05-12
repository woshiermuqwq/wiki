## 描述
喂食目标ed player.  
Doesn't work for other mobs.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount     | a        | 要恢复的饥饿值                                      | 1       |
| saturation | s        | The amount of saturation to restore                                  | 0       |
| overfeed   | o,of     | Whether or not to overfeed                                           | false   |

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
