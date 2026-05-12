## 描述
Summons a 生物 to mount the 施法者. Will knock the current rider off if there is one.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 乘客 | p, rider, r, type, t | The type of the 生物 to set as the 乘客               |         |
| stack | s | Sets 是否 to mount the summoned entity to the current 乘客 of the 施法者 | false   |


## 示例
```yaml
  Skills:
  - summonPassenger{type=MyZombie}
```
Will summon the 生物 "MyZombie" to ride the 施法者 of the 技能


## 别名
- [x] 乘客
- [x] summonRider
- [x] rider


<!--TAGS-->
<!--tag:Mount-->
<!--tag:Summon-->

