## 描述
测试目标物品实体的材质。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | mat, m, type, types, t | 要匹配的材料列表                            |<!--type:Material--><!--list--> |


## 示例
```yaml
  TargetConditions:
  - entityMaterialType{mat=STONE,DIRT} true
```