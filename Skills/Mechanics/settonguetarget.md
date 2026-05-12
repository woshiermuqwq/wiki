## 描述
Sets the tongue target for a frog caster to the target entity.


## 属性
> *This 技能 has no attribute*


## 示例
Sets the frog's tongue target to the nearest entity when right clicked.
```yaml
MyLovingFrog:
  Type: FROG
  Skills:
  - setTongueTarget @EIR{r=5;limit=1;sort=NEAREST} ~onInteract
```


## 别名
- [x] tonguetarget

<!--TAGS-->
<!--tag:AI-->
