## 描述
Causes the casting mob to summon a specified MythicMob and mount it. The caster 将会 set as both the [owner](/Skills/Targeters/Owner) and the [parent](/Skills/Targeters/Parent) of the summoned mob.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, mob, m | The type of MythicMob to summon                                      |<!--type:Mob-->|
| stack     | s         | If the summoned mob should stack atop existing mounted entities      | false   |

### Type Attribute
The MythicMob defines in type 必须 a valid MythicMob type (and is
case-sensitive). If an invalid type is specified the skill may throw an
error.


## 示例
This example would summon a Mythic Mob of the type "UndeadMount" and
make the caster mount it.
```yaml
CallSkeletalHorse:
  Skills:
  - mount{type=UndeadMount}
```


## 别名
- [x] vehicle


<!--TAGS-->
<!--tag:Mount-->
