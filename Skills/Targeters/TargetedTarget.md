## 描述
选取继承的目标实体。配合[目标选择器选项](/Skills/Targeters#targeter-options)用于[目标过滤](/Skills/Metaskills#targets-filtering)。


## 属性
> *此目标选择器没有属性*


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @PIR{r=10}
```
##
```yaml
ExampleSkill2:
  Skills:
  - lightning @TargetedTarget
```


## 别名
- [x] targeted
