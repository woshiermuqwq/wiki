## 描述
Summons an Ender Crystal which shoots a beam towards the 目标.

**Warning: This effect creates an Ender Crystal which can be exploded and cause block damage.**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d      | The time (in ticks) that the effect is active     | 60            |
| yoffset   | y, yo  | 	The 默认值： vertical offset from the casting 生物 | 0             |


## 示例
```yaml
EnderBeamSkill:
  Skills:
  - effect:enderbeam{d=100;y=2} @target
```


## 别名
- [x] effect:enderbeam


<!--TAGS-->
<!--tag:Effect-->