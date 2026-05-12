## 描述
Ma使生物move towards its [主人](/技能/目标选择器/主人) when beyond a certain 距离。
[Followrange](/生物/选项#followrange) 必须为 多于 the 距离 在...之间 主人 and the 生物)


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| followrange | fr, r, maxrange | 距离 之后 which the 生物 will start to follow the 主人 | 4 |
| minrange | mr | 距离 in which the 生物 will stop following the 主人 | 4 |
| 速度 | s | 速度 of the 移动 | 1.0 |
| droptarget | dt | Whether the current 目标 应为 dropped when the 生物 starts following the 主人 | true |
| teleportToWorld | ttw, tow | Whether the 生物 will teleport if the 主人 is in a different 世界 | true |

## 示例
```yaml
  AIGoalSelectors:
  - clear
  - gotoowner{fr=10;mr=3}
```