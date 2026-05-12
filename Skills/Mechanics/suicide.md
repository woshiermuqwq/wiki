## 描述
Instantly kills the mob. This is a no-target 技能 and will only
affect the casting mob.  
This won't work on a few non-mob entities like boats or armor stands! For them, the use of [Remove](/skills/mechanics/remove) is advised!

## 属性
> *This 技能 has no attributes*

## 示例
10% Chance to kill the casting mob when damaged.
```yaml
  Skills:
  - suicide ~onDamaged 0.1
```


<!--TAGS-->
<!--tag:Damage-->
