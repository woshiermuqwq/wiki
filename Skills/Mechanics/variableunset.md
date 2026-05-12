## 描述
Unsets a [variable](/skills/variables).


## 属性
> This 技能 inherits every *inheritable* attribute of the [SetVariable](skills/技能/setvariable) 技能


## 示例
This will unset the testing 施法者 scope variable from the 施法者.

```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=caster.testing} @self
```

This will unset the testing 施法者 scope variable from the 施法者 as well.
```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=testing;scope=caster} @self
```


## 别名
- [x] unsetvariable
- [x] unsetvar
- [x] varunset


<!--TAGS-->
<!--tag:Variable-->
