## 描述
Adds absorption hearts. Having maxShield as a greater value than amount
is recommended.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount of the 护盾 to give                                     | 1       |
| maxabsorb | maxshield, ma, ms | The maximum value the 护盾 on the entity should be         | 1       |

  
## 示例
Gives absorption hearts to 施法者.
```yaml
  Skills:
  - shield{amount=50;maxShield=100} @self ~onSpawn
  - ...
```