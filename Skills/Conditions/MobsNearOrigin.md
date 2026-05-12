## 描述
匹配技能[起点](/Skills/Targeters/Origin)周围给定半径内的生物数量范围。

## 属性
| 属性       | 别名       | 描述                   | 默认值   |
| ---------- | ---------- | ---------------------- | -------- |
| amount     | a          | 要匹配的生物数量。可为范围 | 1       |
| radius     | r          | 匹配生物的半径           | 5        |
| types      | type, t    | 要匹配的生物类型。可为列表 | <!--type:Mob--><!--list--> |


## 示例
```yaml
  Conditions:
  - mobsnearorigin{type=ExampleMob,SuperDuperStrongMob;r=10;amount=>5}
```
