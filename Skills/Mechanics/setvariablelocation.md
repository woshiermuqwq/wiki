## 描述
Sets a value of type string. The value will depend on the location passed to the "value" parameter, and will include informations regarding coordinates and world of the target location



## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| value     | val, v, a, amount | The target location                                          | @self   |
> This 技能 inherits every *inheritable* attribute of the [SetVariable](skills/mechanics/setvariable) 技能


## 示例
```yaml
TestSkill:
 Skills:
 - setvarloc{var=caster.1;v=@self} @self
 - m{m=<caster.var.1>} @self
```


## 别名
- [x] variableSetLocation
- [x] setVarLoc


<!--TAGS-->
<!--tag:Variable-->
