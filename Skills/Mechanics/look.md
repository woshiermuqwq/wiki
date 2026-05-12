## 描述
使实体看向其目标。可根据创意制作酷炫或诡异的效果。


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| headOnly  | ho        | Only 生物的 head is facing the 目标                             | false   |
| force     | f         | Forces the 生物 to look at the 目标 (even works with no AI)         | false   |
| forcepaper | fp       | 是否 to use Paper's method to force the 生物 to look at the 目标 | false   |
| immediately | immediate, i | Immediately causes the 生物 to turn towards the 目标 with no turning animation. | true   |


## 示例
下面的技能使生物immediately force it's head to face
the 目标 immediately. Giving it a creepy effect as only the head will
stare for a short bit before the body catches up and turns around as
well.
```yaml
CreepyStare:
  Skills:
  - look{headOnly=true;immediately=true} @Target
```


<!--TAGS-->
<!--tag:Movement:Rotation-->
