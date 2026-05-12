## 描述
检测目标生物的 MythicMob 类型。

## 属性

| 属性        | 别名       | 描述                                                                                    | 默认值 |
| ----------- | ---------- | --------------------------------------------------------------------------------------- | ------ |
| type        | types, t   | 要匹配的 MythicMob 类型列表                                                               |        |
| exactmatch  | em         | 指定的类型是否应精确匹配 MythicMob 的名称。设为 `false` 时，只要目标生物的 MythicMob 名称*包含*任一指定类型即视为匹配 | true   |


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
