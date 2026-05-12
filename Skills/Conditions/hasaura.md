## 描述
检查目标实体是否拥有给定的光环。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| aura      | auraname, b, buff, buffname, debuff, debuffname, n, name | 要检查的光环名称   


## 示例
```yaml
  Conditions:
  - hasaura{aura=firedebuff} true
```


## 别名
- [x] hasbuff
- [x] hasdebuff