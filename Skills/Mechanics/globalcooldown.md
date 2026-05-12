## 描述

The Global 冷却 skill lets you set a 施法者's global
冷却, used in conjunction with the [offgcd](/skills/条件/offgcd) 条件 if you want a
生物's abilities to have a global, over-all shared 冷却. This can be useful for allowing a 生物 to only use a single skill at a time rather than multiple by giving the 冷却 to each skill the 生物 uses.  
> This is a no-目标 技能, and the affected entity will always be the 施法者

## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ticks     | t       | How many ticks to set the GCD | 20            |

  

## 示例
This skill would 触发 a Global 冷却 of 40 ticks, during which the
skill and all other skills using the [offgcd](/skills/条件/offgcd) 条件 would not be
usable.
```yaml
IceBolt:
  Conditions:
  - offgcd
  Skills:
  - gcd{ticks=40}
```

## 别名
- [x] gcd
- [x] setgcd
- [x] setglobalcooldown


<!--TAGS-->
<!--tag:Meta-->
