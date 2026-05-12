## 描述
检查目标玩家的附魔经验点数。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| level     | l, amount, a | 检查距离达到下一级还差的经验值，范围 0 到 1。0 表示「无进度」，1 表示「下一级」。接受范围值。                   | 0       |


## 示例
```yaml
  TargetConditions:
  - enchantingExperience{l=>0.2} true
```

## 别名
- [x] enchantingExp
- [x] enchantExperience
- [x] enchantExp