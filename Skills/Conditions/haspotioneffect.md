## 描述
检测目标生物是否拥有药水效果。

## 属性

| 属性       | 别名      | 描述                     | 默认值  |
| ---------- | --------- | ------------------------ | ------- |
| type       | t         | 药水效果类型              | ANY<!--type:PotionEffectType--> |
| level      | lvl, l    | 可选的要匹配的等级范围     |         |
| duration   | d         | 可选的要匹配的持续时间范围 |         |


## 示例
```yaml
  Conditions:
  - haspotioneffect{t=SLOW;l=0-2;d=0-9999} true
```

```yaml
  TargetConditions:
  - haspotioneffect{t=Speed;l=0-9} true
```

## 别名
- [x] hasPotion
