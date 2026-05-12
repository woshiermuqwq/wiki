## 描述
Causes the 生物 to pathfind to a location.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| speed     | s     | The movement speed modifier                                              | 1       |
| spreadH   | sh    | Amount of horizontal spread it can be away from the 目标 its moving towards | 0  |
| spreadV   | sv    | Amount of vertical spread it can be away from the 目标 its moving towards| 0     |


## 示例
```yml
  Skills:
  - goto{speedModifier=1;sh=5;sv=5} @owner
  - goto{speedModifier=1;sh=5;sv=5} @location{c=100,65,100}
```


## 别名
- [x] pathto
- [x] navigateto


<!--TAGS-->
<!--tag:Movement-->
<!--tag:AI-->
