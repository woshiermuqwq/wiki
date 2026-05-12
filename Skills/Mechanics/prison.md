## 描述
困住 the 目标 entity inside a temporary prison of blocks. The
created blocks will disappear automatically after the specified
duration.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m, t, type | The Material (block type) the prison is made out of.                | ICE<!--type:Material--> |
| duration  | d         | How long (in ticks) the prison will last                             | 100     |
| 可破坏 | b         | (true/false) 是否 the prison blocks 可被破坏.         | false   |
| materialdata | md     | Deprecated. The data of the material, which existed in older versions of the game. If present, the plugin will try to convert the material to its new equivalent            | 0       |


## 示例
此技能创建一个 iron block prison around the 目标 of the casting
生物, for 200 ticks (10 seconds), and the prison can be mined.
```yaml
IronPrison:
  Skills:
  - prison{material=IRON_BLOCK;duration=200;breakable=true} @target
```


<!--TAGS-->
<!--tag:World-->
