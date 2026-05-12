## 描述
Replaces blocks in a region using WorldEdit. Needs a [@region](/Skills/Targeters/Region) or similar targeter

> **This is a [Premium-Only] 技能!**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| from      | f | The material to replace                                      | AIR<!--type:MATERIAL--> |
| to        | t | The material to set in place of the replaced one             | AIR<!--type:MATERIAL--> |


## 示例
```yaml
  Skills:
  - worldEditReplace{from=STONE;to=AIR} @Region{min=0,0,0;max=100,100,100;world=resources}
```


## 别名
- [x] weReplace


<!-- LINKS -->
[Premium-Only]: Premium-Features


<!--TAGS-->
<!--tag:Premium-Only-->