## 描述
使生物look at nearby 玩家。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 范围 | 半径,r | The 范围 to look for 玩家 | 5 |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - lookatplayers{r=12}
```


## 别名
- [x] lookatplayer