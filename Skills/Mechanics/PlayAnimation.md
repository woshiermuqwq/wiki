## 描述
Forces the entity to play an animation


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| animation | a, effect, e | The animation to play                                             | 1       |
| audience  |           | The [audience] of the effect                                         | world<!--type:Audience--> |

### Animation Attribute
| ID    | Animation               |
|-------|-------------------------|
| 0     | Swing main arm          |
| 1     | Take damage             |
| 2     | Leave bed               |
| 3     | Swing offhand           |
| 4     | Critical effect         |
| 5     | Magic critical effect   |


## 示例
Causes the caster to swing their arm.
```yaml
SwingSkill:
  Skills:
  - playanimation{a=0;audience=World} @Self
```


## 别名
- [x] effect:playanimation
- [x] e:playanimation
- [x] playarmanimation


<!--TAGS-->
<!--tag:Effect-->
