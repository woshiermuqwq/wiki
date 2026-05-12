## 描述
使生物move towards water。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | The 速度 at which to move | 0.9 |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - movetowater{s=2}
```


## 别名
- [x] gotowater