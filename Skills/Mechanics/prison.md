## 描述
Encases the target entity inside a temporary prison of blocks. The
created blocks will disappear automatically after the specified
duration.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m, t, type | The Material (block type) the prison is made out of.                | ICE<!--type:Material--> |
| duration  | d         | How long (in ticks) the prison will last                             | 100     |
| breakable | b         | (true/false) Whether or not the prison blocks 可以 broken.         | false   |
| materialdata | md     | Deprecated. The data of the material, which existed in older versions of the game. If present, the plugin will try to convert the material to its new equivalent            | 0       |


## 示例
This skill creates a iron block prison around the target of the casting
mob, for 200 ticks (10 seconds), and the prison 可以 mined.
```yaml
IronPrison:
  Skills:
  - prison{material=IRON_BLOCK;duration=200;breakable=true} @target
```


<!--TAGS-->
<!--tag:World-->
