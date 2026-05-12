## 描述
Sets the pathfinding malus of a 生物, influencing how a particular entity evaluates different types of blocks when calculating its path


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| malus     | type, malustype | The type of block or terrain the entity can encounter        | OPEN    |
| value     | amount    | A weight that represents how "undesirable" the associated block or terrain is for pathfinding. Can be negative                                                                                       | 0.0     |

### Malus Attribute
The valid malus types are
|  |  |  |  |
|------------------------|------------------------|------------------------|------------------------|
| `BLOCKED`              | `OPEN`                 | `WALKABLE`             | `WALKABLE_DOOR`        |
| `TRAPDOOR`             | `POWDER_SNOW`          | `DANGER_POWDER_SNOW`   | `FENCE`                |
| `LAVA`                 | `WATER`                | `WATER_BORDER`         | `RAIL`                 |
| `UNPASSABLE_RAIL`      | `DANGER_FIRE`          | `DAMAGE_FIRE`          | `DANGER_OTHER`         |
| `DAMAGE_OTHER`         | `DOOR_OPEN`            | `DOOR_WOOD_CLOSED`     | `DOOR_IRON_CLOSED`     |
| `BREACH`               | `LEAVES`               | `STICKY_HONEY`         | `COCOA`                |
| `DAMAGE_CAUTIOUS`      |                        |                        |                        |
 

### Value Attribute
When 实体的 AI calculates a path, it checks the block types along the potential path. By setting a malus using this function, you can make the entity more or less likely to walk over, around, or avoid certain blocks. For example:

- A positive value (例如, 1.0) means the entity will consider this block type harder to walk over or less favorable, causing the entity to try to avoid it.
- A negative or zero value (例如, -1.0 or 0.0) means the entity will consider this block type neutral or easier to walk over, making it more likely to choose paths with these blocks


## 示例
```yaml
  Skills:
  - setpathfindingmalus{malus=BLOCKED;value=2} @self
```


## 别名
- [x] setmalus
- [x] malus


<!--TAGS-->
<!--tag:AI-->
