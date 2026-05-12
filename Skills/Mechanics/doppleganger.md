## 描述 
复制目标玩家的外观。如果目标不是玩家则无效。此技能需要安装 Libs' 伪装 才能启用伪装功能。


## 属性 
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| hasnameplate | nameplate | 是否 the 伪装 should have a nameplate                      | true    |
| usePlayerName | upn |  Uses the player name as the nameplate                                 |         |


## 示例
```yaml
TotallyNotDitto:
  Type: SKELETON
  Skills:
  - doppleganger @NearestPlayer ~onSpawn
```


## 别名
- [x] copyplayer


<!--TAGS-->
<!--tag:Disguise-->