## 描述
Shoots a wither skull from the 生物 towards the 目标 entity or
location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| yield     | strength, y, s | The yield (power) of the skull's explosion.                     | 1       |
| playsound | ps        | 是否 to play the skull launching sound when it is created  | false   |


## 示例
此示例将 shoot a barrage of 3 fast-moving Wither Skulls at the
目标.
```yaml
SkullBarrage:
  Skills:
  - shootskull{y=1;v=4} @target
  - delay 10
  - shootskull{y=1;v=4} @target
  - delay 10
  - shootskull{y=1;v=4} @target
```


## 别名
- [x] shootwitherskull
- [x] skull
- [x] witherskull


<!--TAGS-->
<!--tag:Projectile-->
