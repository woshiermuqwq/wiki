## 描述
Unsets a [variable](/skills/variables).


## 属性
> This 技能 inherits every *inheritable* attribute of the [SetVariable](skills/mechanics/setvariable) 技能


## 示例
This will unset the testing caster scope variable from the caster.

```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=caster.testing} @self
```

This will unset the testing caster scope variable from the caster as well.
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
