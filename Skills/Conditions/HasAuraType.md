## 描述
检查目标实体是否拥有给定类型的光环。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auragroup | auratype, group, type, t, g | 要检查的光环类型                         |         |


## 示例
此示例将为自身应用一个 `Example` 类型的光环。第二个示例将检查其是否存在。
```yaml
  Skills:
  - aura{auraName=NotMeThisTime;auratype=Example;d=100} @self
```
```yaml
  Conditions:
  - hasAuraType{type=Example} true
```

## 别名
- [x] hasbufftype
- [x] hasdebufftype