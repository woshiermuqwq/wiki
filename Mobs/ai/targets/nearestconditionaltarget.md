## 描述
使生物目标 基于 条件。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 间隔 | int,i | Determines the 概率 对于 AI 目标 to be ran | 0 |
| mustsee | ms | Whether the 生物 必须 be able to see the 目标 | true |
| mustreach | mr | Whether the 生物 必须 be able to reach the 目标 | false |
| 条件 | c, cond, targetconditions | The 条件 to use | |


## 示例
Would cause the 生物 to 目标 实体 holding Iron Ingots.
```yaml
ExampleMob:
  Type: ZOMBIE
  AITargetSelectors:
    - clear
    - nearestconditionaltarget{mr=true;ms=true;conditions=[ - holding{m=IRON_INGOT} true ]}
```


## 别名
- [x] nearestconditional
- [x] nearestif