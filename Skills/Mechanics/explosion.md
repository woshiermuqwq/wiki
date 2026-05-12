## 描述
创建爆炸 在target entity or location.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| yield       | y       | The yield (power) of the explosion                                   | 0.013   |
| blockdamage | bd      | (true/false) Whether the explosion will damage blocks                | false   |
| fire        | f,ft    | (true/false) Whether the explosion leaves fire behind                | false   |

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
