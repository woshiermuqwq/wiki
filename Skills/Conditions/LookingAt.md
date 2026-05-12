## 描述
检测玩家是否正在看向某个方块或生物。
仅限玩家使用。

## 属性
| 属性       | 别名                  | 描述                                                              | 默认值 |
| ---------- | --------------------- | ----------------------------------------------------------------- | ------ |
| type       | t, block, b, entity, e| 要检测的目标对象                                                   |        |
| distance   | d                     | 射线检测的距离。如果生物的视线检测行为异常，可以尝试调整此值          | 5      |

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
