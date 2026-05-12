## 描述
Will strike a “fake” lightning bolt 在specified target. 

The effect purely cosmetic and it plays the lightning sound effect, but 将不会 cause any kind of damage to the target.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| localized | l         | Whether the lightning should only be seen/heard by players in radius | false   |
| localizedradius | lr, r     | The radius of the localized effect<br>Only works if localized is set to true!             | 128           |


## 示例
```yaml
SuperLightningSkill:
  Skills:
  - fakelightning @target
  - fakelightning @self
  - fakelightning{repeat=20;repeatInterval=1} @PIR{r=100}
```


## 别名
- [x] effect:lightning
- [x] e:lightning


<!--TAGS-->
<!--tag:Effect-->
