## 描述
以位置 of the inherited targets为目标。


## 属性
>*This 目标选择器 has no 属性*


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @EIR{r=10}

ExampleSkill2:
  Skills:
  - lightning @LocationsOfTargets
```


## 别名
- [x] locationOfTarget
- [x] LOT