## 描述
Sets the gamemode of the target player. Does nothing if the target is
not a player. Requires the `sync=true` attribute.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| mode      | m         | The gamemode to change the target to.                                | SURVIVAL<!--type:Gamemode-->|


## 示例
```yaml
  Skills:
  - setgamemode{m=CREATIVE;sync=true} @PlayersInRadius{r=10} ~onSpawn
  - ...
```
