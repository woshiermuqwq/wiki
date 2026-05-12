## 描述
Summons an Ender Crystal which shoots a beam towards the target.

**Warning: This effect creates an Ender Crystal which 可以 exploded and cause block damage.**


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d      | The time (in ticks) that the effect is active     | 60            |
| yoffset   | y, yo  | 	The default vertical offset from the casting mob | 0             |


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
