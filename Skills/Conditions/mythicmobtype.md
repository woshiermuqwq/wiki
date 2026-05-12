## 描述
检查目标生物的 MythicMob 类型。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | types, t  | 要匹配的 MythicMob 类型列表                                   |         |
| exactmatch | em       | 指定类型是否应精确匹配 MythicMob 的名称。如果此属性设为 `false`，当被评估实体的 MythicMob 名称仅*包含*指定类型中的任意一个时，条件也会通过 | true |


## 示例
```yaml
  Conditions:
  - mythicmobtype{t=CoolZombie,IceZombie,SnowZombie} true
```

```yaml
  TargetConditions:
  - mythicmobtype{t=HotZombie,LavaZombie,FireZombie} true
```


## 别名
- [x] mmType