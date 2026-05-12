## 描述
检测目标生物是否拥有指定类型的光环。

## 属性
| 属性       | 别名                        | 描述                 | 默认值 |
| ---------- | --------------------------- | -------------------- | ------ |
| auragroup  | auratype, group, type, t, g | 要检测的光环类型      |        |


## 示例
此例先施加一个 `Example` 类型的光环，然后用条件检测其是否存在。
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
