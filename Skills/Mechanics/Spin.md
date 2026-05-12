## 描述
Causes the target entity to spin around 对于given duration.  
When a mob casts the spin 技能 repeatedly it will move upwards while spinning.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| velocity  | v         | The velocity the target spins at                                     | 18      |

> 此技能继承所有[Aura](/Skills/Mechanics/Aura) 技能

### Velocity Attribute
When you set velocity to 0, this mob's direction 将会 locked.


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
