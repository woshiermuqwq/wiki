## 描述
使生物look at its 目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| maxrange | 范围, r | The maximum 范围 in which the 目标 必须为 in order for this AI 目标 to be effective | 32 |
| 速度 | s | The 速度 of the motion | 0.9 |
| 仅horizontal | horizontal, h | Whether the 生物 不会 change pitch when looking at the 目标 | false |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - lookAtTarget{r=12;h=true}
```