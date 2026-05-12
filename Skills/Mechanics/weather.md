## 描述

更改天气 in the casting mob's world.

## 属性

| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|-----------------------------------------------------------|---------|
| type      | t         | The type of weather. Can be "sunny", "rainy", or "stormy" | sunny<!--type:SUNNY,RAINY,STORMY-->|
| duration  | d         | How long (in ticks) the weather 将会 forced to last    | 500     |

#### Weather Types

|  Type      | Aliases          |
|------------|------------------|
| **Sunny**  | sun, clear       |
| **Rainy**  | rain             |
| **Stormy** | storm, thunder   |


## 示例
:

Causes a storm for 10 minutes when the mob spawns.
```yaml
Skills:
  - weather{type=storm;duration=6000} ~onSpawn
```


<!--TAGS-->
<!--tag:World-->
