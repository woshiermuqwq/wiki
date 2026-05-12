## 描述

Changes the weather in the casting 生物's world.

## 属性

| 属性 | 缩写   | 描述                                               | 默认值 |
|-----------|-----------|-----------------------------------------------------------|---------|
| type      | t         | The type of weather. Can be "sunny", "rainy", or "stormy" | sunny<!--type:SUNNY,RAINY,STORMY-->|
| duration  | d         | How long (in ticks) the weather will be forced to last    | 500     |

#### Weather Types

|  Type      | 缩写          |
|------------|------------------|
| **Sunny**  | sun, clear       |
| **Rainy**  | rain             |
| **Stormy** | storm, thunder   |


## Examples:

Causes a storm for 10 minutes when the 生物 spawns.
```yaml
Skills:
  - weather{type=storm;duration=6000} ~onSpawn
```


<!--TAGS-->
<!--tag:World-->
