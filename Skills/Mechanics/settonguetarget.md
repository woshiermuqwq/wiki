## 描述
Sets the tongue 目标 for a frog 施法者 to the 目标 entity.


## 属性
> *This 技能 has no attribute*


## 示例
Sets the frog's tongue 目标 to the nearest entity when right clicked.
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