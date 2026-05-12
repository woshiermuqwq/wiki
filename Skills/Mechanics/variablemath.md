## 描述
设置变量 to the result of a math equation, where 'x' is the
[variable](/skills/variables)'s current value.  

Basically a setvariable 机制 with some extra spices


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| equation  | eq, e     | The operation to be done, 必须 inside quotes                      | x       |
> This 机制 inherits every *inheritable* attribute of the [SetVariable](skills/mechanics/setvariable) 机制

  
## 示例
Storing a placeholder in a variable
```yaml
    MMOVar:
      Skills:
      - variableMath{var=target.exp;equation="%mmocore_level%"}
```
Doing math
```yaml
    Math1:
      Skills:
      - variableMath{var=caster.damage;equation="<caster.hp>*5"}
    Math2:
      Skills:
      - variableMath{var=caster.speed;equation="(<caster.var.age>/5)+1"}
```

## 别名
- [x] mathvariable
- [x] varmath
- [x] mathvar


<!--TAGS-->
<!--tag:Variable-->
