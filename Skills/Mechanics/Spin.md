## 描述
Causes the 目标 entity to spin around for the given duration.  
When a 生物 casts the spin 技能 repeatedly it will move upwards while spinning.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v         | The 速度 the 目标 spins at                                     | 18      |

> 此技能继承[光环](/Skills/技能/光环) 技能

### 速度 Attribute
When you set 速度 to 0, this 生物's direction will be locked.


## 示例
```yaml
SpinningSpider:
  Type: SPIDER
  Skills:
  - spin{duration=100;velocity=20} @self ~onTimer:100
```


## 别名
- [x] effect:spin
- [x] e:spin


<!--TAGS-->
<!--tag:Movement:Rotation-->
