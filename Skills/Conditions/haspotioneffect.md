## 描述
测试目标实体是否拥有某种药水效果。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | 药水效果类型                                               | ANY<!--type:PotionEffectType--> |
| level     | lvl, l    | 可选的药水等级范围，用于匹配                                     |         |
| duration  | d         | 可选的持续时间范围，用于匹配                                  |         |


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