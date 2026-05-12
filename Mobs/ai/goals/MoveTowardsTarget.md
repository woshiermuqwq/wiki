## 描述
使生物move towards its 目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | The 速度 of the 移动 | 0.9 |
| maxrange | 范围, r | The max 范围 in which to engage this 行为 | 32.0 |


## 示例
```yaml
  AIGoalSelectors:
  - clear
  - moveTowardsTarget
```