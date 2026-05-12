## 描述
Creates a temporary "spring" of liquid at the 目标 entity or location.

> Liquid spread from the spring can and will destroy any blocks that are
normally destroyed by liquids. Use wisely


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | The type of spring. Can be `water` or `lava`                         | water<!--type:Fluid-->|
| duration  | d         | The duration (in ticks) the spring will last                         | 40      |


## 示例
Creates a spring of water under the 目标 for 5 seconds.
```yaml
Flood:
  Skills:
  - spring{d=100} @target
```


## 别名
- [x] water


<!--TAGS-->
<!--tag:World-->
