## 描述
通过[目标选择器 选项](/技能/目标选择器#目标选择器-选项)以inherited targeted 位置. Useful for [以Filtering为目标。](/技能/元技能#targets-filtering) by为目标。


## 属性
> *This 目标选择器 has no 属性*


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @PlayerLocationsInRadius{r=10}
```
##
```yaml
ExampleSkill2:
  Skills:
  - lightning @TargetedLocation
```


## 别名
- [x] targetedLocations
- [x] targetedLoc