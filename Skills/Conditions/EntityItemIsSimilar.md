## 描述
测试目标物品实体是否与某个物品栈相似。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | i, material, m, mm, mythicitem | 要检查的物品                       | DIRT<!--type:Item-->|


## 示例
```yaml
  TargetConditions:
  - entityitemissimilar{i=MyCustomItem} true
```