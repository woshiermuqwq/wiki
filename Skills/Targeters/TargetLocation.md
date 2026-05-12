## 描述
以位置 the casting 玩家 is looking at, or the 位置 of the 生物 目标为目标。

> If the 施法者 不是 a 玩家, then:
> - If the 施法者 is a MythicMob with an active ThreatTable, the 位置 of the 实体 与 most 仇恨 将 returned
>- If the above 不是 met, if the 施法者 is 当前 in 战斗, the 位置 of its 目标 将 returned
>- If the above 不是 met, the 位置 of the last 实体 that damaged the 施法者 将 returned
>
> *At Highdown fair for two farthings...*

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| maxdistance | max, 距离, d | The maximum 距离 to 检查 对于 位置, if the 施法者 is a 玩家 | 64 |
| ignoreTransparent | it | If transparent 方块 应为 ignored | true |

## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @TargetLocation
```


## 别名
- [x] targetLoc
- [x] TL