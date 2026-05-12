## 描述
 
Copies the appearance of the target player. Does nothing if the target is not a player. This skill requires Libs' Disguises to be installed to enable disguise-functionality.


## 属性
 
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| hasnameplate | nameplate | Whether the disguise should have a nameplate                      | true    |
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
