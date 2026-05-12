## 描述
检查玩家是否在看向某个方块或实体。  
仅对玩家可用。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t, block, b, entity, e | 要检查的对象                             |         |
| distance  | d         | 射线追踪的距离。如果生物查找行为异常，可以尝试调整此值  | 5 |

## 示例
```yaml
  Conditions:
  - lookingat{b=DIRT} true
```
```yaml
  TargetConditions:
  - isPlayer orElseCast fallbackmechanic
  - lookingat{e=COW} true
```