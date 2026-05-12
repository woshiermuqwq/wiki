## 描述
检测目标物品实体的类型。

## 属性
| 属性       | 别名                    | 描述               | 默认值               |
| ---------- | ----------------------- | ------------------ | -------------------- |
| material   | mat, m, type, types, t  | 要匹配的物品列表    |<!--type:Item--><!--list--> |


## 示例
```yaml
  TargetConditions:
  - entityItemType{m=STONE} true
```
