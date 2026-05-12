## 描述
检测目标实体的指定技能是否处于冷却中。

## 属性

| 属性       | 别名   | 描述               | 默认值             |
| ---------- | ------ | ------------------ | ------------------ |
| skill      | s      | 要检测的技能         |<!--type:MetaSkill--> |


## 示例
```yaml
  TargetConditions:
  - skillOnCooldown{skill=TestSkill}
```
