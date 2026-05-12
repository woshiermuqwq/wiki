## 描述
攻击 with a crossbow. Only Piglins and Pillagers can use crossbowAttack AI 目标 只要y're holding a crossbow.


### 属性
> *This aigoal has no 属性*

### 示例

```yaml
ExampleMob:
  Type: Piglins
  Equipment:
    - crossbow HAND
  AIGoalSelectors:
    - clear
    - crossbowAttack
```