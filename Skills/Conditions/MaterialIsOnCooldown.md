## 描述
检测目标玩家的指定材料是否处于冷却中。

## 属性
| 属性       | 别名      | 描述               | 默认值       |
| ---------- | --------- | ------------------ | ------------ |
| material   | mat, m    | 要检测的材料        | enderpearl<!--type:Material--> |


## 示例
```yaml
  TargetConditions:
  - materialIsOnCooldown{mat=STONE} true
```

## 别名
- [x] materialCooldown
- [x] matCooldown
