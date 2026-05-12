## 描述
Adds absorption hearts. Having maxShield as a greater value than amount
is recommended.  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| amount    | a         | The amount of the shield to give                                     | 1       |
| maxabsorb | maxshield, ma, ms | The maximum value the shield on the entity 应当         | 1       |

  
## 示例
Gives absorption hearts to caster.
```yaml
  Skills:
  - shield{amount=50;maxShield=100} @self ~onSpawn
  - ...
```
