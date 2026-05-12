## 描述
匹配目标玩家的游戏模式。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mode      | m         | 要匹配的游戏模式                                                | SURVIVAL<!--type:Gamemode--> |

### Mode 属性
可用的游戏模式有：
- `SURVIVAL`（生存模式）
- `CREATIVE`（创造模式）
- `ADVENTURE`（冒险模式）
- `SPECTATOR`（旁观模式）


## 示例
```yaml
ExampleSkill:
  Conditions:
  - gamemode{m=ADVENTURE} true
```


## 别名
- [x] gm