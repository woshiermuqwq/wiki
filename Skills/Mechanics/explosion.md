## 描述
Creates an explosion at the 目标 entity or location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| yield       | y       | The yield (power) of the explosion                                   | 0.013   |
| blockdamage | bd      | (true/false) 是否 the explosion will damage blocks                | false   |
| fire        | f,ft    | (true/false) 是否 the explosion leaves fire behind                | false   |

> WARNING  
> Blockdamage doesn't seem to respect protection like WorldGuard regions. Use at your own risk


## 示例
```yaml
ExplosiveBlast:
  Skills:
  - explosion{yield=4} @target
```


## 别名
- [x] explode


<!--TAGS-->
<!--tag:Damage-->
<!--tag:World-->