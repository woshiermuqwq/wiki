## 描述
Causes the entity to look at its target. Can be used to make cool effects or creepy ones depending on how creative you get with it.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| headOnly  | ho        | Only the mob's head is facing the target                             | false   |
| force     | f         | Forces the mob to look 在target (even works with no AI)         | false   |
| forcepaper | fp       | Whether to use Paper's method to force the mob to look 在target | false   |
| immediately | immediate, i | Immediately causes the mob to turn towards the target with no turning animation. | true   |


## 示例
The skill below causes the mob to immediately force it's head to face
the target immediately. Giving it a creepy effect as only the head will
stare for a short bit before the body catches up and turns around as
well.
```yaml
CreepyStare:
  Skills:
  - look{headOnly=true;immediately=true} @Target
```


<!--TAGS-->
<!--tag:Movement:Rotation-->
