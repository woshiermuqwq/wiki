## 描述
Causes the casting 生物 to summon a specified Mythic生物 and mount it. The 施法者 将被设为 as both the [owner](/Skills/Targeters/Owner) and the [parent](/Skills/Targeters/Parent) of the summoned 生物.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, 生物, m | The type of Mythic生物 to summon                                      |<!--type:生物-->|
| stack     | s         | If the summoned 生物 should stack atop existing mounted entities      | false   |

### Type Attribute
The Mythic生物 defines in type must be a valid Mythic生物 type (and is
case-sensitive). If an invalid type is specified the skill may throw an
error.


## 示例
此示例将 summon a Mythic 生物 of the type "UndeadMount" and
make the 施法者 mount it.
```yaml
CallSkeletalHorse:
  Skills:
  - mount{type=UndeadMount}
```


## 别名
- [x] vehicle


<!--TAGS-->
<!--tag:Mount-->
