## 描述
\*\***This is a Premium 仅 feature**\*\*<br>
使生物stop doing 任何事物 基于 provided 条件。

**It seems 条件 are reversed when using this, 例如 `day true` will make the 生物 doNothing if 它是 night time, and `day false` will make the 生物 doNothing if its day time.**

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 条件 | c, cond, fleeconditions | The 条件 to use | |


## 示例
This would cause the 生物 to stop 它是 AI if the [day](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/技能/条件/day) 条件 is met.
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - doNothing{conditions=[ - day true ]}
```


## 别名
- [x] 没有