## 描述
使生物move to and melee 攻击 its 目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| speedmodifier | 速度, s | The 速度 modifier 对于 生物 当 this 动作 is being taken | 1 |
| followUnseen | fu | Should the 目标 被跟踪 即使它不可见 | false |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - meleeattack{s=1;fu=false}
```