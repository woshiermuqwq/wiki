## 描述
将所有目标实体以基础速度拉向施法者，拉力随目标与施法者的距离增加而增强。
increasing based on the distance of 目标 from the 施法者.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度  | v         | The base 速度 of the 拉                                        | 1       |
| toOrigin  | to        | Wether or not the 目标 should pulled towards the 原点 of the skill  | false|

### 速度 Attribute

目标 are pulled much faster based on their distance from the 施法者.
The defined 速度 is a "base" 速度, and the skill scales the
速度 based on distance to attempt to 拉 the entity directly to the
生物 if it is possible based on the base 速度.


## 示例
拉 the 目标 and then all players within 10 blocks to the casting 生物.
```yaml
DeathGrip:
  Skills:
  - pull{velocity=10} @target
  - delay 60
  - pull{v=6;to=true} @PIR{r=10}
```


<!--TAGS-->
<!--tag:Movement-->