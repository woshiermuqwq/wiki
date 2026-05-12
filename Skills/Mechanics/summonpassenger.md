## 描述
生成一个生物 to mount the caster. Will knock the current rider off if there is one.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| passenger | p, rider, r, type, t | The type of the mob to set as the passenger               |         |
| stack | s | Sets whether to mount the summoned entity to the current passenger of the caster | false   |


## 示例
```yaml
  Skills:
  - summonPassenger{type=MyZombie}
```
Will summon the mob "MyZombie" to ride the caster of the 技能.


## 别名
- [x] passenger
- [x] summonRider
- [x] rider


<!--TAGS-->
<!--tag:Mount-->
<!--tag:Summon-->
